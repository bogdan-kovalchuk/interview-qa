---
id: py-fileio-0010
title: "Чому string-prefix check не визначає path containment за наявності `..` і як `Path.resolve()` змінює lexical path перед порівнянням?"
track: python
section: files-and-io
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
  - source_id: py314-library-pathlib-path-resolve
    title: "Python 3.14: Library/pathlib (Path.resolve)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.resolve
  - source_id: py314-library-pathlib-purepath-is-relative-to
    title: "Python 3.14: Library/pathlib (PurePath.is_relative_to)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_relative_to
---

## Short answer

**Рядковий `startswith()` не враховує `..` та symlinks: шлях `/data/public/../secret` лексично починається з `/data/public`, але фактично вказує на `/data/secret`.**[^py314-library-pathlib-path-resolve] `Path.resolve()` перетворює шлях на абсолютний, розгортає symlinks і усуває `..` за реальною структурою файлової системи.[^py314-library-pathlib-path-resolve] Після цього належність варто перевіряти через `is_relative_to()` для обох шляхів, базового каталогу і кандидата, бо сам `is_relative_to()` працює з рядками і `..` не розуміє.[^py314-library-pathlib-purepath-is-relative-to]

## Detailed explanation

Рядкове порівняння бачить лише символи, а файлова система розв’язує шлях покроково: `..` означає батьківський каталог за фактичною структурою, а symlink змінює, який каталог є батьківським. `Path.is_relative_to()` теж рядковий і `..` не розуміє, тож сам по собі не замінює розв’язання шляху.[^py314-library-pathlib-purepath-is-relative-to] Приклад (`#` коментарі показують результат):

```python
import tempfile
from pathlib import Path

root = Path(tempfile.mkdtemp()).resolve()
(root / 'data' / 'public').mkdir(parents=True)
(root / 'data' / 'secret').mkdir()
(root / 'data' / 'secret' / 'key.txt').write_text('top secret')
(root / 'data' / 'public' / 'ok.txt').write_text('hello')
(root / 'data' / 'public' / 'link').symlink_to(root / 'data' / 'secret')

base = root / 'data' / 'public'
for user in ('ok.txt', '../secret/key.txt', 'link/key.txt'):
    candidate = base / user
    prefix_ok = str(candidate).startswith(str(base))
    resolved_ok = candidate.resolve().is_relative_to(base.resolve())
    print(user, prefix_ok, resolved_ok)
# ok.txt True True
# ../secret/key.txt True False
# link/key.txt True False
```

Перший шлях лежить усередині base за обома перевірками. Другий і третій проходять `startswith()`, але після розв’язання лежать поза `public`. `Path.resolve()` перетворює шлях на абсолютний, розгортає symlinks і усуває `..`; документація каже, що це єдиний метод `Path`, який прибирає `..`.[^py314-library-pathlib-path-resolve]

Щоб перевірка була правильною, розв’язуємо обидва шляхи: і базовий каталог, і кандидата. Якщо сам base містить symlink, нерозв’язаний base не є префіксом розв’язаного кандидата, і коректний шлях відхиляється помилково (перевірено на 3.13 і 3.14). Порівняння `is_relative_to()` іде за частинами шляху: `Path('/data/public2/x').is_relative_to('/data/public')` дає `False`, тоді як `startswith()` дає `True`. Функція нижче поєднує ці кроки і повертає шлях лише тоді, коли він лежить усередині base:

```python
from pathlib import Path

def safe_join(base: Path, user_part: str) -> Path:
    base_resolved = base.resolve()     # resolve the base too, not only the user part
    candidate = (base_resolved / user_part).resolve()
    if not candidate.is_relative_to(base_resolved):   # compares whole components
        raise ValueError(f'path escapes base: {user_part}')
    return candidate
```

Це не повний захист: між `resolve()` і відкриттям файлу symlink можна створити в уже перевіреному компоненті (гонка TOCTOU). Для недовіреного введення файл слід відкривати відносно дескриптора каталогу без переходу за symlink; це окрема тема.

**Типові помилки:**
- перевіряти `str(path).startswith(str(base))`: `/data/public2/x` проходить для `/data/public`;
- викликати `is_relative_to()` без `resolve()`: `(base / '../../x').is_relative_to(base)` дає `True`, хоча шлях виходить за base;
- розв’язувати лише шлях користувача, а base залишати нерозв’язаним, коли base сам містить symlink.

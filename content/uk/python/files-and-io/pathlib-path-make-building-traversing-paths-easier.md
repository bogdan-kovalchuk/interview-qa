---
id: py-fileio-0009
title: "Чим `pathlib.Path` полегшує побудову та обхід шляхів порівняно з ручною конкатенацією strings?"
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
  - source_id: py314-library-pathlib-path
    title: "Python 3.14: Library/pathlib (Path)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.Path
  - source_id: py314-library-pathlib-pure-paths
    title: "Python 3.14: Library/pathlib (Pure paths)"
    url: https://docs.python.org/3.14/library/pathlib.html#pure-paths
  - source_id: py314-library-pathlib-purepath-joinpath
    title: "Python 3.14: Library/pathlib (PurePath.joinpath)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.joinpath
  - source_id: py314-library-pathlib-path-rglob
    title: "Python 3.14: Library/pathlib (Path.rglob)"
    url: https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob
---

## Short answer

**`pathlib.Path` надає об’єктно-орієнтований API: оператор `/` для з’єднання частин шляху, методи `iterdir()`, `glob()`, `rglob()`, властивості `.suffix`, `.stem`, `.parent`.**[^py314-library-pathlib-path] На відміну від ручної конкатенації рядків, `Path` сам ставить один роздільник, а його шляхи незмінні й хешовані (їх можна використовувати як ключ у dict); `PurePosixPath` і `PureWindowsPath` дозволяють обробляти шляхи іншого синтаксису без звернень до ОС.[^py314-library-pathlib-pure-paths]

## Detailed explanation

Рядковий шлях – це просто текст. При ручній конкатенації треба самому вставити роздільник, а його вигляд залежить від ОС, і легко пропустити його або поставити два. `Path` складає шлях з об’єктів: оператор `/` додає роздільник рівно один раз, а синтаксис визначає поточна ОС.[^py314-library-pathlib-path] Порівняння на POSIX (`#` коментарі показують результат):

```python
from pathlib import Path

base = '/srv/app'
name = 'logs/app.log'
print(base + name)                  # /srv/applogs/app.log: the separator is lost
print(base + '/' + name)            # /srv/app/logs/app.log: correct only if written by hand every time
print(Path(base) / name)            # /srv/app/logs/app.log: one separator, inserted by pathlib
print(Path(base) / '/etc/passwd')   # /etc/passwd: an absolute right side replaces the left one
```

Правило з абсолютним операндом варто знати заздалегідь. `Path(base) / '/etc/passwd'` дає `/etc/passwd`: якщо сегмент є абсолютним шляхом, попередні сегменти відкидаються.[^py314-library-pathlib-purepath-joinpath] Так само поводиться `os.path.join(base, '/etc/passwd')` (перевірено на 3.13 і 3.14). На Windows є умова: правий операнд, який має лише корінь без диска, не є абсолютним, тож диск лівого операнда зберігається. `PureWindowsPath('c:/a') / '/b'` дає `c:\b` (перевірено на 3.13 і 3.14). Тому шлях, який прийшов ззовні, не можна просто приєднувати до каталогу; див. qid:py-fileio-0010.

Обхід дерева теж робить `Path`: `iterdir()` повертає прямий вміст каталогу, `glob()` шукає за шаблоном в одному каталозі, а `rglob()` шукає рекурсивно.[^py314-library-pathlib-path-rglob] Результати знову є `Path`-об’єктами, тож `.suffix`, `.stem` і `.parent` доступні без ручних `split()` і `rfind()`. Приклад (`#` коментарі показують результат):

```python
import tempfile
from pathlib import Path

root = Path(tempfile.mkdtemp())
(root / 'logs').mkdir()
(root / 'logs' / 'app.log').write_text('x')
(root / 'app.txt').write_text('y')

for p in sorted(root.rglob('*.*')):   # recursive search, yields Path objects
    print(p.relative_to(root), p.suffix, p.stem)
# app.txt .txt app
# logs/app.log .log app
```

`Path` незмінний і хешується, тому його можна використовувати як ключ у dict або як елемент set. Порівняння нормалізує запис: `Path('a/b') == Path('a//b/')` дає `True`.[^py314-library-pathlib-pure-paths] Сам `Path` при створенні не перевіряє, що шлях існує; до файлової системи він звертається лише в методах на кшталт `exists()`. Чисті класи (`PurePath`, `PurePosixPath`, `PureWindowsPath`) не звертаються до ОС взагалі, тому їх зручно використовувати для шляхів іншої ОС.

**Типові помилки:**
- складати шлях через `+`: `Path('a') + 'b'` дає `TypeError`, бо `Path` не підтримує конкатенацію з рядком;
- вважати, що створення `Path(...)` перевіряє наявність файлу чи каталогу;
- вважати, що абсолютний правий операнд просто дописується до лівого.

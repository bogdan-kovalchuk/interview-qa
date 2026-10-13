---
id: py-fileio-0007
title: "Як в межах однієї filesystem оновити файл через temporary file та `os.replace()`, щоб reader не побачив partial content?"
description: "Записати нові дані у тимчасовий файл у тому самому каталозі, потім викликати os.replace(tmp_path, target_path): на POSIX це атомарна заміна, тож читач бачить стару або нову версію."
track: python
section: files-and-io
level: middle
type: practical
tags: [os-replace]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-tempfile-mkstemp
    title: "Python 3.14: Library/tempfile (mkstemp)"
    url: https://docs.python.org/3.14/library/tempfile.html#tempfile.mkstemp
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: mkstemp() створює файл, доступний для читання й запису лише користувачеві, що його створив; параметр dir задає каталог."
  - source_id: py314-library-functions-open
    title: "Python 3.14: Built-in Functions (open)"
    url: https://docs.python.org/3.14/library/functions.html#open
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: режим 'w' відкриває файл для запису, спочатку обрізаючи його."
---

## Short answer

**Записати нові дані у тимчасовий файл у тому самому каталозі, тобто на тій самій filesystem, потім викликати `os.replace(tmp_path, target_path)`.**[^py314-library-os-os-replace] На POSIX успішна заміна є атомарною операцією, тож читач, що відкриває `target_path` у будь-який момент, бачить стару або нову версію, але не проміжний стан. <span class="warn">Якщо тимчасовий файл на іншій filesystem, `os.replace()` може не вдатися; у CPython на Linux це `OSError` з `errno.EXDEV`.</span> Перед заміною варто викликати `flush()` і `os.fsync()` для тимчасового файлу.[^py314-library-os-os-fsync]

## Detailed explanation

Проблема в тому, що `open(path, 'w')` спочатку обрізає файл до нуля.[^py314-library-functions-open] Читач, який відкриє файл у цей момент або під час запису, побачить частковий вміст, наприклад неповний JSON. Тому замінювати файл на місці небезпечно: нові дані записують в окремий тимчасовий файл, а потім перейменовують його на місце старого.

`os.replace(src, dst)` замінює `dst` на `src`. Документація каже, що успішна заміна є атомарною і що це вимога POSIX.[^py314-library-os-os-replace] Читач, який відкрив `dst` після заміни, бачить новий вміст. Читач, який відкрив старий файл раніше, продовжує читати старі дані через уже відкритий дескриптор. Тож атомарність стосується самого перейменування, а не всього оновлення.

Тимчасовий файл має бути на тій самій filesystem, що й ціль. Перейменування між різними filesystem може не вдатися (у CPython на Linux це `OSError` з `errno.EXDEV`).[^py314-library-os-os-replace] Тому файл створюють у тому самому каталозі, як у функції нижче:

```python
import os
import tempfile
from pathlib import Path

def write_atomic(target: Path, data: str) -> None:
    # The temp file must be in the same directory, so the rename stays on one filesystem.
    fd, tmp_name = tempfile.mkstemp(dir=target.parent, prefix=target.name, suffix='.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        # mkstemp() creates the file with mode 0600; set the mode the target needs before this line.
        os.replace(tmp_name, target)   # atomic on POSIX: readers see the old or the new content
    except BaseException:
        os.unlink(tmp_name)            # the replace did not happen: remove the temp file
        raise
```

`flush()` переносить буфер Python у буфер ОС, а `os.fsync()` просить ОС записати дані на диск.[^py314-library-os-os-fsync] Без `fsync` після збою на деяких файлових системах перейменування може опинитися на диску раніше за дані. `mkstemp()` створює файл, доступний лише його власникові,[^py314-library-tempfile-mkstemp] тож на практиці це режим 0600, і після заміни файл матиме ці права. Функція цього не відновлює; якщо іншим потрібне читання, режим треба встановити явно.

**Типові помилки:**
- створювати тимчасовий файл у `/tmp` або в іншому каталозі: `os.replace()` може не вдатися з `EXDEV`;
- пропускати `flush()` і `os.fsync()` і вважати, що після перейменування дані вже на диску;
- не перевіряти права файлу після заміни;
- вважати атомарність гарантованою на всіх платформах: документація описує її як вимогу POSIX.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

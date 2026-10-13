---
id: py-stdlib-0010
title: "Коли для filesystem operation варто лишитися на `os`, а коли обрати `pathlib`?"
description: "pathlib зручніший для маніпуляцій зі шляхами та побудови нових шляхів; os потрібен для низькорівневих операцій з файловими дескрипторами, яких pathlib не має."
track: python
section: standard-library
level: middle
type: comparison
tags: [os, pathlib]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-os-open
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.open
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, os.open: повертає файловий дескриптор відкритого файлу; прапорці відкриття."
  - source_id: py314-library-os-scandir
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.scandir
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, os.scandir: функція приймає path-like об’єкт."
  - source_id: py314-library-os-fspath
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fspath
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, os.fspath: повертає str або bytes; для path-like об’єкта викликає __fspath__()."
---

## Short answer

**`pathlib` зручніший для маніпуляцій зі шляхами та побудови нових шляхів, а `os` потрібен для низькорівневих операцій з файловими дескрипторами, як-от `os.open()` і `os.fstat()`.**[^py314-library-os-open] `os.scandir()` приймає path-like об’єкти, тож `Path` можна передати без перетворення.[^py314-library-os-scandir] Якщо API очікує саме str, використовуйте `os.fspath(path)`, яка повертає рядок.[^py314-library-os-fspath]

## Detailed explanation

Обидва модулі працюють з тими самими файлами, тож вибір залежить від того, що саме ви робите. `pathlib` моделює шлях як об’єкт: `Path` має методи для побудови, перевірки й читання, і код читається як опис наміру. `os` ближчий до системних викликів: `os.open()` повертає цілочисельний файловий дескриптор, а `os.fstat()` читає метадані за цим дескриптором.[^py314-library-os-open] У `Path` немає ні `fstat()`, ні `fileno()`, тож для таких операцій `os` лишається потрібним.

Приклад поєднує обидва підходи: `os.open()` приймає `Path`, а для `os.environ` потрібен рядок:

```python
import os
from pathlib import Path

script = Path(__file__)
fd = os.open(script, os.O_RDONLY)        # os.open accepts a Path and returns an int descriptor
print(os.fstat(fd).st_size > 0)          # True; pathlib has no fstat()
os.close(fd)
os.environ["SCRIPT"] = os.fspath(script) # env values must be str; a bare Path raises TypeError
```

Перехід між ними здебільшого простий. `os.scandir()` приймає path-like об’єкт, тож `Path` можна передати напряму.[^py314-library-os-scandir] У зворотному напрямі явний крок потрібен там, де API очікує str: `os.fspath()` повертає рядок для path-like об’єкта і не змінює вже наявний str чи bytes.[^py314-library-os-fspath] Без цього кроку присвоєння `Path` у `os.environ` кидає `TypeError: str expected, not PosixPath`, бо значення змінних середовища мають бути str.

На практиці `pathlib` варто брати за замовчуванням, бо він читабельніший і має `glob()`, `rglob()` та `suffix`. `os` доречний тоді, коли потрібен файловий дескриптор або низькорівневий виклик, якого в `pathlib` немає.[^py314-library-os-open]

**Типові помилки:**
- передавати `Path` туди, де очікується str, наприклад в `os.environ`, без `os.fspath()`;
- вважати, що `pathlib` замінює весь `os`: fd-рівневих операцій (`os.open()`, `os.fstat()`) у `Path` немає;
- змішувати `Path` і рядок в одному виразі: `Path("report") + ".txt"` кидає `TypeError`; для нового імені використовуйте `with_name()`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

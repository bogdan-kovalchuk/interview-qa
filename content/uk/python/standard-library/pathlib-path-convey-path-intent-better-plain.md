---
id: py-stdlib-0009
title: "Чому `pathlib.Path` краще передає path intent, ніж звичайний string?"
track: python
section: standard-library
sources:
  - source_id: py314-library-pathlib-pure-paths
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html#pure-paths
  - source_id: py314-library-pathlib-concrete-paths
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html#concrete-paths
  - source_id: py314-library-pathlib-operators
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html#operators
  - source_id: py314-library-pathlib-general-properties
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html#general-properties
---

## Short answer

**`Path` – це об’єктна абстракція шляху, яка розрізняє операції з шляхом і роботу з файловою системою, на відміну від string, де шлях – просто текст.**[^py314-library-pathlib-pure-paths] `Path` стає `PosixPath` або `WindowsPath` залежно від ОС; оператор `/` створює дочірній шлях, а `exists()` і `is_file()` звертаються до файлової системи.[^py314-library-pathlib-concrete-paths][^py314-library-pathlib-operators] Шляхи immutable й hashable, тому їх можна використовувати як ключі dict.[^py314-library-pathlib-general-properties]

## Detailed explanation

Рядок тримає шлях як текст, тож роздільники, суфікси й склеювання частин лишаються на розробникові. `pathlib` розділяє два рівні. Pure paths (`PurePath`, `PurePosixPath`, `PureWindowsPath`) лише обчислюють над шляхом і не звертаються до файлової системи. Конкретний `Path` має ті самі операції і додає методи, що роблять системні виклики.[^py314-library-pathlib-pure-paths][^py314-library-pathlib-concrete-paths]

Приклад будує шлях через `/` і показує його частини. Вивід наведено для POSIX:

```python
from pathlib import Path, PureWindowsPath

p = Path("data") / "reports" / "2026.csv"
print(p)                                       # data/reports/2026.csv
print(p.suffix, p.name, p.parent)              # .csv 2026.csv data/reports
print(p.with_suffix(".json"))                  # data/reports/2026.json
print(PureWindowsPath("C:/logs") / "app.log")  # C:\logs\app.log on any OS
print({p: "report"}[Path("data/reports/2026.csv")])  # report
p.endswith(".csv")                             # AttributeError: 'PosixPath' object has no attribute 'endswith'
```

Оператор `/` створює дочірній шлях.[^py314-library-pathlib-operators] Властивості `name`, `suffix` і `parent` повертають частини шляху.[^py314-library-pathlib-pure-paths] Метод `with_suffix()` повертає новий об’єкт, бо шляхи immutable. Hashable означає, що шлях можна використати як ключ dict, як у прикладі вище.[^py314-library-pathlib-general-properties]

Порівняння теж залежить від ОС: `PurePosixPath('foo') == PurePosixPath('FOO')` дає `False`, а `PureWindowsPath('foo') == PureWindowsPath('FOO')` дає `True`. Тобто `Path` передає намір, але правила регістру й роздільників лишаються правилами конкретної системи.[^py314-library-pathlib-general-properties]

**Типові помилки:**
- вважати `Path` рядком: `p.endswith(".csv")` кидає `AttributeError`, а API, що очікує str, потребує `str(p)` або `os.fspath(p)`;
- вважати, що `Path` ніколи не звертається до диска: `exists()`, `is_file()` і `mkdir()` роблять системні виклики, на відміну від `PurePath`;
- порівнювати шляхи як рядки: для `PureWindowsPath` регістр ігнорується, для `PurePosixPath` ні.

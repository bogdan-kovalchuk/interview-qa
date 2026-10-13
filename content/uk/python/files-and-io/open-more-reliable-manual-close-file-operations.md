---
id: py-fileio-0006
title: "Чому `with open(...)` надійніше за ручний `close()` після операцій із файлом?"
description: "with (context manager) гарантує виклик close() навіть якщо всередині блоку виникне виняток."
track: python
section: files-and-io
level: middle
type: mechanism
tags: [with-open, close]
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
  - source_id: py314-library-io-iobase
    title: "Python 3.14: Library/io (IOBase)"
    url: https://docs.python.org/3.14/library/io.html#io.IOBase
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: IOBase як context manager; файл закривається після блоку with, навіть якщо виник виняток."
  - source_id: py314-reference-compound-stmts-with
    title: "Python 3.14: Reference/compound Stmts (with)"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-with-statement
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: __exit__ викликається, якщо __enter__ завершився без помилки, і при виході з блоку з винятком або без нього."
---

## Short answer

**`with` гарантує закриття файлу навіть тоді, коли всередині блоку виникає виняток.**[^py314-library-io-iobase] Оператор `with` викликає `__exit__` щоразу, коли `__enter__` завершився без помилки.[^py314-reference-compound-stmts-with] При ручному `f = open(...)` … `f.close()` виняток між цими викликами пропускає `close()`, і файл лишається відкритим, доки його об’єкт не звільнено (у CPython це відбувається, коли зникає останнє посилання, зокрема й через traceback).

## Detailed explanation

`with` – це context manager: оператор викликає `__enter__` на початку блоку та `__exit__` на його виході, незалежно від причини виходу – звичайного завершення, `return`, `break` чи винятку. Для файлового об’єкта `__exit__` закриває файл. Тож закриття прив’язане до межі блоку, а не до того, чи дійде виконання до рядка `close()`.[^py314-reference-compound-stmts-with][^py314-library-io-iobase]

Ручний варіант має слабке місце: `close()` стоїть після коду, який може впасти. Якщо між `open()` і `close()` виникає виняток, виконання переходить до обробника, і `close()` не викликається. Функція `manual()` піднімає виняток до `close()`, тож `close()` не викликається; `with_block()` теж піднімає виняток, але `__exit__` закриває файл. Після обробки видно, чи закрито файл у кожному випадку (`#` коментарі показують результат):

```python
import os
import tempfile

path = os.path.join(tempfile.mkdtemp(), 'data.txt')
with open(path, 'w') as f:
    f.write('hello\n')

def manual(p):
    f = open(p)
    raise ValueError('boom')   # the close() below is never reached
    f.close()

def with_block(p):
    with open(p) as f:
        raise ValueError('boom')

for func in (manual, with_block):
    try:
        func(path)
    except ValueError as e:
        f = e.__traceback__.tb_next.tb_frame.f_locals['f']  # local f of func
        print(func.__name__, 'file closed:', f.closed)
# manual file closed: False
# with_block file closed: True
```

Результат пояснюється підрахунком посилань у CPython. Поки traceback тримає фрейм функції `manual()`, локальна змінна `f` жива, і файл відкритий. Коли traceback відпущено, `f` звільняється, і файл закривається. Тобто дескриптор лишається відкритим, доки жив виняток, а не лише до виходу з функції. На реалізаціях без підрахунку посилань момент закриття може бути пізнішим. `with` же закриває файл на виході з блоку незалежно від того, як блок завершився.

`with` не робить запис атомарним і не відкочує вже записане. Якщо виняток виник посеред запису, частина даних уже потрапила в файл; для безпечної заміни файлу див. qid:py-fileio-0007. Файловий об’єкт, який винесли за межі блоку, уже закритий, і будь-яка операція з ним дає `ValueError`.

**Типові помилки:**
- вважати, що `with` потрібен лише для запису: він так само закриває файл після читання;
- залишати `f` поза блоком і звертатися до нього пізніше, коли файл уже закрито;
- вважати, що `with` робить запис атомарним: виняток посеред запису залишає частково записані дані.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

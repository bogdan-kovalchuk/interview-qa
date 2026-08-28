---
id: py-cpyint-0016
title: "Коли `gc.freeze()` може зменшити copy-on-write втрати перед `fork()` і які умови потрібні для цього pattern?"
description: "gc.freeze() переносить усі поточні об'єкти під контролем GC у permanent generation, де вони ігноруються подальшими колекціями – це запобігає модифікації gc_refs довгоживучих об'єктів у child після fork(), зменшуючи..."
track: python
section: cpython-internals
level: senior
type: practical
tags: [gc-freeze, fork]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`gc.freeze()` переносить усі поточні об'єкти під контролем GC у permanent generation, де вони ігноруються подальшими колекціями – це запобігає модифікації `gc_refs` довгоживучих об'єктів у child після `fork()`, зменшуючи copy-on-write.**[^py314-library-dis] Рекомендований workflow: (1) `gc.disable()` на початку parent; (2) `gc.freeze()` безпосередньо перед `fork()`; (3) `gc.enable()` на початку child. Умови: заморожені об'єкти мають бути дійсно довгоживучими й незмінними; child не повинен модифікувати ці об'єкти інакше CoW все одно станеться. Pattern ефективний для pre-fork web workers (gunicorn, uwsgi).

## Detailed explanation

`gc.freeze()` бере всі об'єкти, які на цей момент відстежує cyclic collector, і переносить їх у
permanent generation – групу, яку подальші виклики `gc.collect()` більше не перевіряють і не
чіпають.[^py314-library-gc]

Без freeze кожен прохід cyclic GC фізично записує службове поле (внутрішній лічильник для
trial-deletion алгоритму) у кожен tracked об'єкт, щоб порахувати досяжність. Навіть якщо з точки
зору Python-коду об'єкт не змінювався, ця службова модифікація на C-рівні "бруднить" сторінку
пам'яті. Після `fork()` така сторінка перестає бути спільною між parent і child і копіюється –
відбувається copy-on-write, хоча дані фактично не мінялись.[^py314-c-api-memory]

Типовий workflow: parent-процес (наприклад, pre-fork модель gunicorn чи uwsgi) завантажує довгоживучі
дані – конфіги, ORM-моделі, кеші – викликає `gc.freeze()` безпосередньо перед `fork()`, а кожен child
одразу після старту може викликати `gc.enable()`, якщо GC вимикали в parent для стабільності перед
freeze. Заморожені об'єкти child більше не переглядає жоден cyclic collector, тож їхні сторінки
лишаються спільними з parent.

Умови, за яких pattern дійсно працює: заморожені об'єкти мають бути дійсно довгоживучими й по суті
незмінними; якщо child модифікує їх на рівні Python (не лише GC-переходом), CoW все одно
станеться – freeze захищає лише від записів, спричинених самим collector, а не від мутацій коду.
Об'єкти, створені вже після `fork()` у кожному child, у permanent generation не потрапляють і
відстежуються окремо.

```python
import gc
import os

load_shared_data()   # populate long-lived objects
gc.freeze()           # move them out of future collections
pid = os.fork()
if pid == 0:
    serve_requests()   # child; frozen objects' pages stay shared
```

**Типові помилки:**
- викликати `gc.freeze()` до того, як усі довгоживучі дані завантажені – нові об'єкти лишаються
  tracked і writable;
- очікувати, що freeze захищає й від Python-рівневих мутацій – він прибирає лише GC-спричинені
  записи;
- забувати про `gc.unfreeze()` чи моніторинг `gc.get_freeze_count()`, коли pattern більше не
  потрібен, і накопичувати permanent generation, яку ніхто не збирає.

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

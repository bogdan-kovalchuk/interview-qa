---
id: py-gil-0010
title: "Які thread-safety assumptions про shared mutable objects треба переглянути під час переходу на free-threaded CPython?"
description: "У free-threaded build кілька threads одночасно виконують bytecode, тому всі access до shared mutable state потребує явної синхронізації – внутрішні блокування built-in типів є implementation detail, а не API-контрактом."
track: python
section: concurrency-and-gil
level: senior
type: practical
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython free-threaded build"
    version: "3.14"
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
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
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L689-L849
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**У free-threaded build кілька threads одночасно виконують bytecode, тому всі access до shared mutable state потребує явної синхронізації – внутрішні блокування built-in типів є implementation detail, а не API-контрактом.**[^py314-library-threading] Ітератори спільних колекцій не thread-safe (можливі пропущені або дубльовані елементи). Доступ до `frame.f_locals` з іншого thread може завершити інтерпретатор crash. У C extensions borrowed references (наприклад, `PyList_GET_ITEM`) небезпечні – потрібна міграція на strong-reference API (`PyList_GetItemRef`, `PyDict_GetItemRef`).

## Detailed explanation

Free-threaded CPython (build без GIL) – це режим, у якому кілька threads одного процесу можуть
виконувати Python bytecode буквально одночасно на різних ядрах, а не по черзі, як у GIL-enabled
build.[^py314-howto-free-threading-python]

У звичайному CPython GIL випадково, але зазвичай досить надійно, захищав окремі операції built-in
типів від переривання посеред виконання: наприклад, `list.append()` виглядав атомарним не тому, що
це гарантія API, а тому, що GIL не давав іншому thread втрутитися. У free-threaded build це
припущення більше не тримається – внутрішні locks built-in типів існують, щоб не пошкодити саму
структуру об'єкта, а не для того, щоб зробити послідовність операцій атомарною на рівні
застосунку.[^py314-howto-free-threading-python]

Це означає, що будь-який доступ до спільного mutable стану – dict, list, set, атрибутів об'єкта –
без явного `Lock` тепер реально небезпечний, а не лише теоретично. Ітерація по спільній колекції,
яку паралельно змінює інший thread, може пропустити елементи, повторити їх або кинути виняток.

Приклад коду, який раніше «випадково працював» під GIL, а на free-threaded build – ні:

```python
shared = {}

def writer():
    for i in range(1000):
        shared[i] = i  # mutating a dict from multiple threads without a lock

def reader():
    for key in shared:  # iterating while another thread mutates - unsafe here
        ...
```

Окрема небезпека – C extensions, написані під припущення GIL. Патерни на кшталт запозичених
посилань (`PyList_GET_ITEM`) більше не безпечні, бо власник об'єкта може звільнити його з іншого
thread; потрібна міграція на strong-reference API на кшталт `PyList_GetItemRef` і
`PyDict_GetItemRef`.[^py314-howto-free-threading-extensions]

**Що варто переглянути під час переходу на free-threaded build:**
- будь-який спільний mutable стан без явного `Lock` чи іншого synchronization primitive;
- ітерацію по спільних колекціях у одному thread, поки інший їх змінює;
- доступ до `frame.f_locals` з чужого thread – може призвести до crash інтерпретатора;
- C-розширення, що покладаються на borrowed references built-in типів.

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

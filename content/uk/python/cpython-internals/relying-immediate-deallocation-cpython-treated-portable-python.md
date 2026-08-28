---
id: py-cpyint-0008
title: "Чому покладатися на immediate deallocation у CPython не можна як на portable Python language guarantee?"
description: "Immediate deallocation при refcount=0 – це CPython implementation detail, а не гарантія мови Python; інші реалізації та free-threaded build можуть відкладати звільнення об'єктів."
track: python
section: cpython-internals
level: senior
type: pitfall
tags: []
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L27-L46
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Immediate deallocation при refcount=0 – це CPython implementation detail, а не гарантія мови Python; інші реалізації та free-threaded build можуть відкладати звільнення об'єктів.**[^py314-library-dis] Python Language Reference описує object lifecycle у загальних термінах і не зобов'язує негайної finalization. PyPy використовує tracing GC, free-threaded CPython застосовує deferred refcounting. Тому ресурси (файли, сокети, locking) слід керувати через `with` / context managers, а не покладатися на момент деструкції.

## Detailed explanation

Immediate deallocation – коли об'єкт звільняється рівно там, де зникає останнє посилання на нього –
є наслідком конкретної реалізації reference counting в CPython, а не гарантією, яку дає специфікація
мови Python.

Python Language Reference описує lifecycle об'єктів у загальних термінах: об'єкт колись буде
"reclaimed", можливо буде викликаний `__del__`, але специфікація не фіксує, коли саме це станеться,
і навіть не гарантує виклик `__del__` у всіх випадках – наприклад, при reference cycles або
наприкінці роботи інтерпретатора.[^py314-reference-datamodel-traceback-objects]

Інші реалізації дотримуються цієї специфікації, але не CPython-механізму: PyPy використовує
generational tracing GC, де об'єкти звільняються пачками під час collection pass, а не в момент
останнього decref. Це правда й для самого CPython у free-threaded build (3.13+), де deferred та
biased reference counting відкладають фактичне звільнення до найближчого safe point замість того,
щоб робити це синхронно.[^py314-howto-free-threading-python]

Практичний наслідок: код, який покладається на побічний ефект деструктора – закриття файлу,
звільнення lock, commit транзакції – одразу після того, як змінна вийшла з області видимості чи їй
присвоєно нове значення, працюватиме на "звичайному" CPython, але може накопичувати незакриті
ресурси (file descriptor leak, задачі, що тримають блокування довше, ніж потрібно) на PyPy чи в
майбутніх варіантах CPython.

**Типові помилки:**
- писати `f = open(path); ...; f = None`, розраховуючи, що файл закриється негайно, замість
  `with open(path) as f: ...`;
- покладатися на порядок виклику `__del__` для звільнення взаємопов'язаних ресурсів;
- тестувати лише на CPython і вважати поведінку деструкторів частиною мови, а не деталлю
  реалізації.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

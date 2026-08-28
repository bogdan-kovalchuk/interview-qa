---
id: py-gil-0005
title: "Що саме серіалізує GIL у звичайній GIL-enabled build CPython?"
description: "GIL серіалізує виконання Python bytecode – лише один thread одночасно виконує bytecode інтерпретатора."
track: python
section: concurrency-and-gil
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython with GIL"
    version: null
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

**GIL серіалізує виконання Python bytecode – лише один thread одночасно виконує bytecode інтерпретатора.**[^py314-library-threading] Це захищає внутрішні структури CPython (reference counts, стан об'єктів) від одночасного доступу з кількох threads. <span class="warn">GIL не серіалізує application-логіку:</span> між будь-якими двома bytecode-інструкціями GIL може бути передано іншому thread, тому складені операції не є атомарними на рівні Python-коду.

## Detailed explanation

GIL (global interpreter lock) – це один mutex на весь процес CPython, який потрібно утримувати,
щоб виконувати Python bytecode. У будь-який момент часу лише той thread, що тримає GIL, може
виконувати інструкції інтерпретатора – усі інші threads, готові до виконання, чекають своєї
черги.[^py314-library-threading]

Причина існування GIL – не сама по собі multithreading-модель, а внутрішня реалізація CPython.
Reference counting, яким CPython керує пам'яттю об'єктів, не є thread-safe операцією сам по собі:
інкремент і декремент лічильника посилань – це read-modify-write, і без глобального lock-а два
threads могли б одночасно зіпсувати лічильник того самого об'єкта, спричинивши передчасне
звільнення пам'яті або витік.[^py314-howto-free-threading-python]

GIL захищає саме ці внутрішні структури – лічильники посилань, стан списків, словників, самого
інтерпретатора – а не логіку, яку пише розробник програми. Це принципова відмінність: GIL робить
безпечними одиночні bytecode-операції на рівні CPython, але нічого не гарантує щодо послідовностей
операцій, які пише прикладний код.

```python
import sys

x = []
sys.getrefcount(x)  # internal refcount, protected by the GIL from concurrent corruption
```

Планувальник CPython періодично змушує thread, що тримає GIL, звільнити його – за замовчуванням
приблизно кожні 5 мілісекунд (`sys.setswitchinterval()`), або одразу, коли thread сам звільняє GIL
на блокуючому виклику. Це дає ілюзію паралельності на рівні ОС, хоча bytecode усе одно виконується
по одному thread за раз.

**Що саме серіалізує, а що ні:**
- серіалізує виконання bytecode-інструкцій інтерпретатора – одночасно виконує лише один thread;
- серіалізує доступ до внутрішнього стану CPython (reference counts, внутрішні структури
  об'єктів) – саме заради цього GIL і існує;
- не серіалізує весь Python-код як атомарний блок – композитні вислови з кількох bytecode можуть
  бути перервані між ними;
- не заважає C-розширенням явно звільняти GIL на час своїх обчислень – саме так numpy чи
  free-threaded build (3.13+) дають реальний паралелізм.[^py314-howto-free-threading-extensions]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

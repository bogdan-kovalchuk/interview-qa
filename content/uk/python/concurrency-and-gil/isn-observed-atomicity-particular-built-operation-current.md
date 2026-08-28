---
id: py-gil-0008
title: "Чому спостережена atomicity окремої built-in operation у поточній CPython не є стабільним synchronization contract?"
description: "Атомарність окремих built-in операцій (наприклад, list.append()) – це деталь реалізації CPython, а не гарантія мови."
track: python
section: concurrency-and-gil
level: senior
type: pitfall
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

**Атомарність окремих built-in операцій (наприклад, `list.append()`) – це деталь реалізації CPython, а не гарантія мови.**[^py314-library-threading] Ця поведінка може змінитися між версіями CPython, відрізнятися в інших реалізаціях (PyPy, GraalPy) або бути відсутньою у free-threaded build. <span class="warn">Application code ніколи не повинен покладатися на спостережену атомарність</span> – завжди використовуйте явні примітиви синхронізації (`Lock`, `RLock`) для захисту shared mutable state.

## Detailed explanation

Атомарність окремої built-in операції - це ситуація, коли операція виконується як один C-рівня
виклик без проміжних точок, у яких GIL міг би передати контроль іншому потоку, тому ззовні вона
виглядає неподільною. Але це наслідок конкретної реалізації байткод-циклу CPython, а не гарантія,
яку дає мова Python чи documented API.[^py314-library-threading]

GIL перемикає потоки між виконанням окремих байткод-інструкцій (або після певної кількості
"тіків"/часу), а не всередині C-функції, яка реалізує одну built-in операцію. Тому якщо весь ефект
операції - це один виклик на C-рівні (наприклад, `list.append(x)` для CPython - це один виклик
`list_append`), інший потік фізично не встигає втрутитися в середину цієї операції.

Проблема в тому, що зовні прості вирази часто компілюються в кілька байткод-інструкцій, між якими
GIL цілком може перемкнути потік:

```python
counter = 0

def increment():
    global counter
    counter += 1  # LOAD_GLOBAL, BINARY_ADD, STORE_GLOBAL - not one atomic step
```

`counter += 1` виглядає так само просто, як `list.append(x)`, але фактично це читання, додавання і
запис - три окремі кроки, між якими можливе перемикання потоку і втрата інкременту.

На free-threaded build ситуація стає ще менш передбачуваною: без GIL немає й серіалізації байткоду,
тому операції, які раніше виглядали атомарними лише завдяки GIL, перестають бути такими без явної
внутрішньої синхронізації в CPython. Те саме стосується альтернативних реалізацій (PyPy, GraalPy) -
вони не зобов'язані відтворювати ту саму випадкову атомарність, бо мова Python її ніде не
документує як гарантію.[^py314-howto-free-threading-python]

**Чому на це не можна покладатися:**
- атомарність конкретної операції - артефакт поточної реалізації байткоду, а не частина мовної
  специфікації;
- вона може зникнути після оптимізації CPython, зміни байткоду між версіями або переходу на
  free-threaded build;
- код, що покладається на неї, працює "випадково" і ламається непередбачувано при зміні версії чи
  реалізації інтерпретатора.

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

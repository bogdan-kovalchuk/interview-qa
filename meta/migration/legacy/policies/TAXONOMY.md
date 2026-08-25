# Таксономія підготовки

Канонічні TSV є вхідними даними production builder. Релізний пакет має root deck
`Python Interview Questions` і 23 підколоди, визначені в `authoring/manifest.json`. Нижченаведені
коди використовуються в назвах файлів і тегах `topic::`.

## Python Core

| Код | Тема | Основний фокус |
|---|---|---|
| 01 | `python_fundamentals` | модель мови, dynamic typing, execution model, Python vs CPython |
| 02 | `syntax_control_flow` | expressions/statements, truthiness, loops, matching, evaluation |
| 03 | `objects_types_mutability` | identity, equality, mutability, hashing, references, copying |
| 04 | `collections` | list, tuple, dict, set, protocols, complexity and trade-offs |
| 05 | `functions_scope_closures` | arguments, LEGB, closures, defaults, first-class functions |
| 06 | `oop_data_model` | classes, MRO, inheritance, composition, dunder protocols, descriptors |
| 07 | `decorators` | function/class decorators, wrapping, metadata, parameterization |
| 08 | `iterators_generators` | iterable/iterator protocols, generator state, lazy evaluation |
| 09 | `context_managers` | `with`, `__enter__`, `__exit__`, `contextlib` |
| 10 | `exceptions` | hierarchy, chaining, cleanup, custom exceptions, exception groups |
| 11 | `modules_packages_imports` | import system, package layout, `sys.modules`, circular imports |
| 12 | `files_io` | text/binary I/O, encoding, buffering, paths, resource lifetime |
| 13 | `comprehensions_functional` | comprehensions, lambdas, map/filter, partial, higher-order patterns |
| 14 | `cpython_internals_memory` | bytecode, frames, reference counting, GC, object layout |
| 15 | `gil_threads_processes` | GIL-enabled/free-threaded CPython, threading, multiprocessing |
| 16 | `asyncio` | coroutine, task, event loop, cancellation, structured concurrency |
| 17 | `standard_library` | найуживаніші модулі та вибір правильного інструмента |
| 18 | `testing` | pytest/unittest concepts, mocking, fixtures, test boundaries |
| 19 | `performance_best_practices` | profiling, complexity, allocation, readability, Pythonic trade-offs |
| 20 | `practical_coding` | короткі Python-задачі, refactoring, debugging, code review |

## General Engineering Awareness

Ці теми мають лише перевіряти базову обізнаність. Вони не повинні розростатися у повні
спеціалізовані курси.

The enforceable scope cap is 3 to 7 accepted cards per Overview topic. This is a ceiling, not a
quota. Exceeding seven requires an explicit user decision and a corresponding verifier change.

| Код | Тема | Межа покриття |
|---|---|---|
| 21 | `algorithms_data_structures` | Big O, базові структури, пошук/сортування, вибір структури |
| 22 | `databases_sql` | relational model, key/index, JOIN, transaction, базовий SQL |
| 23 | `git_cicd_sdlc` | Git mental model, CI/CD purpose, базові етапи SDLC |

## Виключено

- HTTP, REST, SOAP, RPC та проєктування API.
- Django, DRF, FastAPI, SQLAlchemy та інші вебфреймворки.
- JavaScript, DOM, HTML, CSS та frontend-фреймворки.
- AWS, Kubernetes, Docker, DDD, microservices і детальний System Design.

Останню групу можна колись винести в окремий необов’язковий проєкт, але вона не є частиною
цієї базової Python-колоди.

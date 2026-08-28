---
id: py-cpyint-0011
title: "Коли `gc.disable()` може бути виправданим і які measurements та invariants потрібні перед такою зміною?"
description: "gc.disable() виправданий у latency-sensitive коді, де паузи cyclic GC неприйнятні, за умови що reference cycles або відсутні, або збираються вручну через gc.collect() у передбачуваних точках."
track: python
section: cpython-internals
level: senior
type: practical
tags: [gc-disable]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L102-L197
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`gc.disable()` виправданий у latency-sensitive коді, де паузи cyclic GC неприйнятні, за умови що reference cycles або відсутні, або збираються вручну через `gc.collect()` у передбачуваних точках.**[^py314-library-dis] Після `gc.disable()` reference counting продовжує працювати: об'єкти без циклів звільняються негайно. Перед вимкненням потрібно виміряти baseline: частоту та тривалість автоматичних колекцій (`gc.get_threshold()`, `gc.get_count()`), перелік джерел cycles, та підтвердити invariant – пам'ять не зростає необмежено при ручному `gc.collect()` через фіксовані інтервали.

## Detailed explanation

`gc.disable()` вимикає лише cyclic-колектор – три generations, які періодично шукають reference
cycles – а не reference counting: об'єкти без циклів, як і завжди, звільняються негайно, щойно їхній
refcount падає до нуля.[^py314-library-gc]

Причина, чому це буває корисним: прохід cyclic GC зупиняє поточний потік на паузу, довжина якої
залежить від кількості tracked об'єктів у generation, що перевіряється. Для latency-sensitive коду
(наприклад, обробника запиту, де важливий p99) навіть рідкісна пауза в кілька мілісекунд помітна на
хвостових перцентилях, тоді як звичайне reference counting цю затримку не створює.

Ризик симетричний вигоді: якщо код усе ж створює reference cycles (батько<->дитина, closures, що
захоплюють `self`, збережені traceback-и), вони ніколи не звільняться самі, і пам'ять
зростатиме необмежено, доки хтось не викличе `gc.collect()` вручну.

Перед вимкненням варто виміряти baseline: `gc.get_stats()` і `gc.get_count()` показують частоту й
кількість зібраних об'єктів по generation, а профайлер алокацій чи `objgraph` – реальні джерела
циклів у коді й бібліотеках. Після вимкнення потрібно тримати invariant: або цикли гарантовано не
створюються, або `gc.collect()` викликається вручну в передбачувані, безпечні моменти (кінець
запиту, простій воркера), і за пам'яттю після цього спостерігають у продакшені, а не лише на етапі
рев'ю коду.

Типовий pattern:

```python
import gc

gc.disable()  # keep refcounting; stop only cyclic collection

def handle_request(request_count):
    ...
    if request_count % 1000 == 0:
        gc.collect()  # release accumulated cycles at a safe point
```

**Типові помилки:**
- вимикати GC без вимірювання baseline, просто сподіваючись, що стане краще;
- забувати про цикли всередині сторонніх бібліотек (ORM, callbacks event loop), які раніше
  прибирались автоматично;
- ніколи не викликати `gc.collect()` вручну, перетворюючи `disable()` на повільний memory leak;
- плутати `gc.disable()` з вимкненням reference counting – останнє взагалі не можна вимкнути.

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

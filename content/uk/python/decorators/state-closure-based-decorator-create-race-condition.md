---
id: py-decor-0010
title: "Чому state у closure decorator може створити race condition при паралельних викликах обгорнутої функції?"
description: "Closure зберігає спільний mutable state в enclosing scope, і всі потоки, що викликають декоровану функцію, звертаються до однієї й тієї ж змінної без синхронізації."
track: python
section: decorators
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
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L80-L111
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Closure зберігає спільний mutable state в enclosing scope, і всі потоки, що викликають декоровану функцію, звертаються до однієї й тієї ж змінної без синхронізації.**[^py314-glossary-term-decorator] У CPython з GIL прості операції типу `x += 1` для integer атомарні на рівні bytecode, але складніші патерни (check-then-act, оновлення dict/list з умовами) не є атомарними навіть з GIL. У free-threaded CPython (3.13+) навіть прості операції не захищені GIL, тому closure-state потребує явного lock (наприклад, `threading.Lock`) або immutable state.

## Detailed explanation

Closure-based decorator створює одну функцію-wrapper і одну область видимості (closure) один раз,
коли decorator застосовується до функції, а не при кожному виклику. Будь-яка змінна, яку wrapper
читає чи змінює через `nonlocal`, живе в цій єдиній closure-scope і є спільною для всіх викликів
декорованої функції – з будь-якого потоку.[^py314-glossary-term-decorator]

Race condition виникає не через сам факт спільного стану, а через непослідовні (non-atomic)
операції над ним. GIL гарантує, що одна bytecode-інструкція виконається без переривання, але навіть
операція, яка виглядає простою, як `count = count + 1`, компілюється в кілька окремих інструкцій:
зчитати `count`, обчислити нове значення, записати назад. Між будь-якими двома з цих кроків
інтерпретатор може перемкнути потік, тож два потоки, що одночасно читають старе значення `count`,
здатні втратити один інкремент.

Патерн check-then-act страждає ще сильніше: перевірка умови (`if key not in cache`) і подальша дія
(`cache[key] = value`) – це дві окремі операції, між якими GIL цілком може передати керування
іншому потоку. У free-threaded CPython (3.13+, без GIL за замовчуванням) навіть одинарний `x += 1`
для звичайного `int` більше не захищений автоматично, тож будь-яке спільне closure-state вимагає
явної синхронізації незалежно від того, наскільки простою виглядає операція.

Приклад decorator зі спільним лічильником, який демонструє втрачені інкременти:

```python
def call_counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        current = count
        count = current + 1  # two threads can read the same `current`
        return func(*args, **kwargs)
    return wrapper

@call_counter
def handler():
    ...
```

Якщо `handler()` викликають 1000 потоків одночасно, підсумкове значення `count` майже напевно
виявиться меншим за 1000 – частина інкрементів губиться, бо один потік читає `current` до того, як
інший потік встигає записати своє оновлення.

**Способи уникнути race condition у closure-state:**
- обгорнути читання-і-запис у `threading.Lock`, отриманий один раз при застосуванні decorator;
- замінити ручний лічильник на `itertools.count()` або `collections.Counter` там, де операція
  справді зводиться до одного atomic виклику;
- не тримати mutable стан у closure взагалі – переносити його у thread-local (`threading.local`)
  або передавати явно як аргумент, якщо кожен виклик має власний незалежний стан;
- у free-threaded build перевіряти це особливо уважно: код, що «випадково працював» під GIL, може
  почати губити оновлення там, де раніше здавався безпечним.

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

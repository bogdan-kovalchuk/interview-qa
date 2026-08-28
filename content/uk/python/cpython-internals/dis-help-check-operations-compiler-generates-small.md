---
id: py-cpyint-0017
title: "Як `dis` допомагає перевірити, які operations генерує compiler для невеликої function?"
description: "dis.dis(func) виводить таблицю bytecode-інструкцій: offset, opname (наприклад LOAD_FAST, CALL), аргумент та їх інтерпретацію – це дозволяє побачити, які саме операції згенерував compiler."
track: python
section: cpython-internals
level: middle
type: practical
tags: [dis]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L3-L26
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`dis.dis(func)` виводить таблицю bytecode-інструкцій: offset, opname (наприклад `LOAD_FAST`, `CALL`), аргумент та їх інтерпретацію – це дозволяє побачити, які саме операції згенерував compiler.**[^py314-library-dis] Наприклад, можна перевірити чи compiler обрав `LOAD_FAST` замість `LOAD_GLOBAL` для локальних змінних, як реалізовано closure через `LOAD_DEREF`/`STORE_DEREF`, або чи відбувається constant folding. Для програмного аналізу `dis.Bytecode(func)` дає ітерацію по `Instruction` named tuples з атрибутами `opcode`, `argval`, `offset`. <span class="warn">Bytecode – деталь реалізації CPython і може змінюватись між версіями.</span>

## Detailed explanation

`dis` – це вбудований модуль, який дизасемблює bytecode функції чи code object у читабельну таблицю
інструкцій, тому дозволяє побачити, що саме згенерував compiler, а не лише здогадуватися з
source code.[^py314-library-dis]

Виклик `dis.dis(func)` друкує один рядок на кожну bytecode-інструкцію: номер рядка source code (для
першої інструкції кожного рядка), offset у байтах, `opname` (наприклад `LOAD_FAST`, `CALL`,
`RETURN_VALUE`) і, де застосовно, аргумент та його інтерпретацію (`argval`) – наприклад ім'я
локальної змінної для `LOAD_FAST`.

Це робить видимими рішення compiler, які інакше довелося б вгадувати: чи звертання до змінної
скомпільоване як `LOAD_FAST` (локальна) або `LOAD_GLOBAL` (глобальна); як реалізовано closure –
через `LOAD_DEREF`/`STORE_DEREF` замість звичайного `LOAD_FAST`; чи спрацював constant folding, коли
`2 + 3` в source перетворюється на єдину константу `5` в `co_consts`, а не на дві окремі операції.

Приклад дизасемблювання невеликої функції:

```python
def add(a, b):
    return a + b

dis.dis(add)
#   1  RESUME                   0
#   2  LOAD_FAST                0 (a)
#      LOAD_FAST                1 (b)
#      BINARY_OP                0 (+)
#      RETURN_VALUE
```

Для програмного аналізу (а не лише читання очима) `dis.Bytecode(func)` повертає ітератор
`Instruction`-об'єктів з атрибутами `opcode`, `opname`, `arg`, `argval`, `offset` – це дозволяє,
наприклад, написати тест, який перевіряє відсутність певної інструкції в hot path.

**Практичні застосування `dis`:**
- перевірити, чи compiler інлайнить константний вираз, замість покладатися на здогад;
- порівняти bytecode тієї самої функції на двох версіях CPython, щоб побачити, що саме змінилося;
- знайти зайві `LOAD_GLOBAL` у hot loop і замінити на локальне ім'я для пришвидшення.

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

---
id: py-cpyint-0017
title: "Як `dis` допомагає перевірити, які operations генерує compiler для невеликої function?"
track: python
section: cpython-internals
sources:
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
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

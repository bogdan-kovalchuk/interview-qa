---
id: py-cpyint-0004
title: "Яку роль у CPython 3.14 відіграють adaptive bytecode та specialization під час виконання hot code?"
description: "Adaptive specialization замінює generic опкоди на спеціалізовані варіанти, оптимізовані під конкретні типи аргументів, використовуючи inline cache entries для зберігання runtime-інформації."
track: python
section: cpython-internals
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: "3.14"
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

**Adaptive specialization замінює generic опкоди на спеціалізовані варіанти, оптимізовані під конкретні типи аргументів, використовуючи inline cache entries для зберігання runtime-інформації.**[^py314-library-dis] Коли інтерпретатор бачить, що опкод часто виконується з певними типами, він «адаптується» – наприклад, `BINARY_OP` може стати спеціалізованою інструкцією для int+int. Якщо припущення перестає виконуватися, опкод деградує до базової версії (`baseopcode`). У 3.14 додано CLI-опцію `-S` (`--specialized`) для перегляду спеціалізованого bytecode.

## Detailed explanation

Adaptive bytecode specialization у CPython 3.14 (розвиток архітектури PEP 659) динамічно оптимізує виконання bytecode у Tier 1 інтерпретаторі, замінюючи повільні generic інструкції на спеціалізовані опкоди під час виконання «гарячого» (hot) коду.[^py314-library-dis] Коли компілятор генерує первинний bytecode, інструкції створюються у загальному вигляді (наприклад, `BINARY_OP`, `LOAD_ATTR`, `COMPARE_OP`), а поруч із ними виділяються слоти inline cache (`CACHE`). Під час повторних викликів функції або ітерацій циклу лічильник у слоті кешу зменшується, і коли ділянка стає hot, інтерпретатор аналізує типи операндів і переписує опкод безпосередньо в пам'яті на мономорфну спеціалізовану інструкцію (наприклад, `BINARY_OP_ADD_INT`).

Кожен спеціалізований опкод містить вбудований guard (швидку перевірку типу чи version tag об'єкта), завдяки чому операція виконується за лічені процесорні інструкції в обхід важкого динамічного пошуку в словниках та розв'язання методів.[^py314-library-dis] Якщо ж у ту саму точку програми надходить операнд іншого типу (наприклад, float замість int), guard не спрацьовує, викликаючи деоптимізацію: інструкція тимчасово деградує до базового опкоду з експоненційним back-off лічильником, що запобігає постійному перемиканню (thrashing) у разі поліморфного навантаження.

У CPython 3.14 адаптивна спеціалізація є не лише самостійним прискорювачем Tier 1, але й фундаментом для вищих рівнів оптимізації. Саме на основі даних про стабільність типів, зібраних спеціалізованим bytecode, інтерпретатор формує оптимізовані сліди виконання (execution traces) у Tier 2, які згодом передаються експериментальному copy-and-patch JIT-компілятору для генерації машинного коду.[^py314-library-dis]

Спостереження за переходом generic інструкції у спеціалізований опкод за допомогою модуля `dis`:

```python
import dis

def calculate(a, b):
    return a + b

# Cold bytecode: unspecialized generic opcode BINARY_OP
print("Before warm-up:")
dis.dis(calculate, adaptive=True)

# Warm up with uniform integer inputs to trigger adaptive specialization
for _ in range(64):
    calculate(10, 20)

# Hot bytecode: specialized opcode BINARY_OP_ADD_INT
print("After warm-up:")
dis.dis(calculate, adaptive=True)

# Expected output includes:
# Before warm-up: BINARY_OP         0 (+)
# After warm-up:  BINARY_OP_ADD_INT 0 (+)
```

**Архітектурні наслідки та оптимізаційні компроміси:**
- мономорфний код працює суттєво швидше: однорідні типи операндів дозволяють уникнути динамічного пошуку та узагальненого dispatch;
- поліморфізм призводить до деоптимізації: якщо одна й та сама інструкція регулярно отримує змінні типи, інтерпретатор повертається до generic форми;
- inline cache збільшує обсяг bytecode у пам'яті: резервування слотів `CACHE` для кожної інструкції розмінює пам'ять на швидкість виконання.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

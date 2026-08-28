---
id: py-cpyint-0003
title: "Чому output `dis` треба трактувати як implementation detail конкретної CPython version, а не language contract?"
description: "Bytecode є implementation detail CPython: документація явно стверджує, що інструкції можуть додаватися, видалятися або змінюватися між версіями без попередження."
track: python
section: cpython-internals
level: senior
type: pitfall
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

**Bytecode є implementation detail CPython: документація явно стверджує, що інструкції можуть додаватися, видалятися або змінюватися між версіями без попередження.**[^py314-library-dis] Опкоди, їх кодування та семантика не гарантовані навіть між minor releases CPython, і інші реалізації (PyPy, MicroPython) мають власний bytecode. Код, що покладається на конкретні опкоди або їх порядок, стане непереносимим і крихким при оновленні.

## Detailed explanation

Офіційна документація Python прямо називає bytecode деталлю реалізації: набір опкодів, їх
кодування й навіть кількість аргументів можуть змінюватися між будь-якими версіями CPython –
включно з minor-релізами – без гарантії зворотної сумісності.[^py314-library-dis]

Це не гіпотетичний ризик: наприклад, у 3.11 з'явився `RESUME` на початку кожного code object, а
кілька опкодів викликів (`CALL_FUNCTION`, `CALL_FUNCTION_KW`, `CALL_METHOD`) об'єднали в один
`CALL` зі спільною підготовкою стека. Код, написаний під bytecode однієї версії, після оновлення
interpreter може або впасти з помилкою, або – гірше – мовчки почати аналізувати неправильні
інструкції.

Мовний контракт – це синтаксис і семантика, які описані в reference-документації та мають процес
зміни через PEP з періодом deprecation. Bytecode такого процесу не проходить: він оптимізується під
конкретну версію eval loop, і зміна опкоду не вважається breaking change мови, навіть якщо код,
побудований поверх `dis`, ламається.

```python
# CPython 3.10 and earlier
CALL_FUNCTION            2

# CPython 3.11+: unified into CALL with a preceding PUSH_NULL/precall setup
CALL                      2
```

Інші реалізації Python підтверджують, що bytecode – не частина мови: PyPy має власний набір
опкодів для свого interpreter, а MicroPython генерує ще компактніший формат під обмежену пам'ять.
Обидві виконують той самий Python-код коректно, не маючи нічого спільного з bytecode CPython.

**Практичні наслідки для коду, що читає bytecode:**
- будь-яка перевірка чи інструмент на основі конкретних opcode-імен має бути прив'язана до версії
  interpreter і повторно перевірена після оновлення;
- не варто зберігати чи кешувати `code object` з одного patch-релізу CPython для виконання на
  іншому – формат `.pyc` теж версіюється;
- аналіз продуктивності чи покриття краще будувати на `sys.settrace`/`sys.monitoring`, а не на
  парсингу конкретних опкодів.

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

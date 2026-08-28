---
id: py-cpyint-0001
title: "Як CPython перетворює source code на code object і bytecode перед виконанням?"
description: "CPython компілює source code у code object, який містить bytecode, потім інтерпретатор виконує цей bytecode інструкцію за інструкцією."
track: python
section: cpython-internals
level: middle
type: mechanism
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L3-L26
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**CPython компілює source code у code object, який містить bytecode, потім інтерпретатор виконує цей bytecode інструкцію за інструкцією.**[^py314-library-dis] Процес проходить етапи parsing -> AST -> code object (через вбудований `compile()`). Code object зберігає `co_code` (bytecode), `co_consts`, `co_names`, `co_varnames` та інші статичні дані. При import скомпільований bytecode може кешуватися у `.pyc` файлах.

## Detailed explanation

Компіляція в CPython – це багатоетапний процес, який перетворює текст source code на виконуваний
`code object` ще до того, як інтерпретатор виконає бодай одну інструкцію.[^py314-library-dis]

Спочатку токенізатор і parser будують abstract syntax tree (AST) з тексту програми. Компілятор
обходить це AST і генерує `code object` – об'єкт, що містить `bytecode` (послідовність low-level
інструкцій для CPython eval loop) разом зі статичними даними, потрібними для його виконання. Сам
компілятор написаний на C і недоступний напряму з чистого Python, але вбудована функція `compile()`
виконує ті самі кроки і повертає готовий `code object`.

`Code object` зберігає декілька окремих полів: `co_code` – байти bytecode; `co_consts` – кортеж
літералів і вкладених `code object` (наприклад, тіл функцій); `co_names` – імена глобальних змінних
і атрибутів; `co_varnames` – імена локальних змінних. Інтерпретатор читає ці поля під час виконання,
а не парсить джерело повторно.

Приклад ручної компіляції та перегляду bytecode:

```python
src = "x = 1 + 2"
code = compile(src, "<string>", "exec")
print(code.co_consts)  # (1, 2, 3, None)
dis.dis(code)
```

Коли модуль імпортується (а не виконується як `__main__`), CPython кешує скомпільований
`code object` у файлі `.pyc` під `__pycache__/`, серіалізуючи його через `marshal`. Наступний
import того самого модуля пропускає повторний парсинг і компіляцію, якщо файл джерела не
змінився.

**Типові помилки в розумінні цього процесу:**
- вважати, що Python інтерпретує source code рядок за рядком без проміжного bytecode;
- думати, що `.pyc` кешується для скриптів, запущених напряму як `__main__` – це не так;
- плутати AST-рівень (структура мови) з bytecode-рівнем (деталь реалізації CPython).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

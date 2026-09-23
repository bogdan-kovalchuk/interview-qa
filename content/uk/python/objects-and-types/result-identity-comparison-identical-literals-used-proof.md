---
id: py-objtypes-0003
title: "Чому результат identity-порівняння двох однакових literals не можна використовувати як доказ interning або як переносиму гарантію Python?"
description: "Interning малих цілих чисел і деяких рядків – це деталь реалізації CPython, а не гарантія мови."
track: python
section: objects-and-types
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Interning малих цілих чисел і деяких рядків – це деталь реалізації CPython, а не гарантія мови.**[^py314-reference-datamodel] CPython може кешувати об'єкти в певному діапазоні (наприклад, цілі від -5 до 256), але цей діапазон і моменти intern можуть змінюватися між версіями. Два літерали з однаковим значенням можуть як збігатися, так і не збігатися за `id()` залежно від способу створення та оптимізацій компілятора.

## Detailed explanation

Специфікація мови Python гарантує еквівалентність значень однакових літералів, проте принципово розглядає спільне використання об'єктів у пам'яті та кешування як оптимізації конкретної реалізації.[^py314-reference-datamodel]

У CPython існує дві принципово різні оптимізації, які розробники часто помилково змішують: механізм runtime interning (попереднє виділення об'єктів для цілих чисел від -5 до 256 та інтернування імен-ідентифікаторів) і оптимізація компілятора constant folding на етапі створення байт-коду.[^py314-library-stdtypes] Коли компілятор обробляє один блок коду (один файл або одну функцію), він дедуплікує однакові незмінні літерали й зберігає їх в єдиному кортежі констант `co_consts`.

У результаті вираз `a = 1000; b = 1000` в одному модулі показує `a is b == True`, оскільки обидва імені посилаються на один запис у `co_consts`. Проте, якщо виконати ті самі рядки послідовно в інтерактивному інтерпретаторі REPL або обчислити значення динамічно через `int("1000")`, кожна операція виконується в окремому контексті компіляції і створює новий об'єкт. Спроба обґрунтувати наявність глобального interning за допомогою літералів у скрипті спирається на артефакт роботи компілятора, а не на реальну модель пам'яті.

Покладання на ідентичність замість рівності створює крихкий код, поведінка якого ламається при переході між CPython та іншими реалізаціями (PyPy, GraalPy), зміні рівня оптимізацій або виході значень за межі закешованого діапазону.

Приклад, що демонструє різницю між оптимізацією констант компілятором і кешуванням у runtime:

```python
# In a single function, the compiler merges duplicate constants via co_consts:
def demonstrate_constant_folding():
    x = 1000
    y = 1000
    print(x is y)  # True: both reference the identical object in co_consts

demonstrate_constant_folding()

# Dynamically evaluated numbers bypass constant folding:
a = 1000
b = int("1000")
print(a == b)  # True: values are equal
print(a is b)  # False: distinct heap objects with separate memory addresses

# Pre-allocated small integer cache (-5 to 256) in CPython:
small_a = 256
small_b = int("256")
print(small_a is small_b)  # True: both resolve to the global singleton in CPython
```

**Архітектурні компроміси та типові підводні камені:**
- змішування constant folding та interning: збіг адрес для літералів в одному файлі створює оманливе враження гарантованої єдиності екземплярів, яке руйнується при динамічному обчисленні значень;
- жорстка прив'язка до CPython: альтернативні середовища виконання (PyPy, GraalPy) або новіші релізи CPython застосовують інші стратегії оптимізації констант;
- приховані баги на межах діапазонів: перевірка `x is 100` успішно проходить локальні юніт-тести на малих тестових числах, але призводить до аварійних ситуацій на продакшені, коли значення перевищує `256`;
- попередження компілятора: починаючи з Python 3.8, інтерпретатор видає `SyntaxWarning: "is" with a literal. Did you mean "=="?` на будь-яке використання `is` з літералом.

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

---
id: py-funcs-0013
title: "Чим відрізняються `global` і `nonlocal` за тим, у якому scope вони шукають binding для присвоєння?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-simple-stmts-the-global-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-global-statement
  - source_id: py314-reference-simple-stmts-the-nonlocal-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-nonlocal-statement
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
---

## Short answer

**`global` прив’язує ім’я до namespace модуля (top-level), а `nonlocal` – до найближчого enclosing function scope.**[^py314-reference-executionmodel-resolution-of-names] Для `nonlocal` binding має існувати в одній з охоплюючих функцій і не шукається в модулі; якщо його немає, виникає `SyntaxError`.[^py314-reference-simple-stmts-the-nonlocal-statement] `global` же завжди посилається на модульний рівень, а не на ім’я в охоплюючій функції.[^py314-reference-executionmodel-resolution-of-names]

## Detailed explanation

`global` і `nonlocal` відповідають на одне питання: куди потрапить присвоєння імені в тілі функції. Без декларації присвоєння робить ім’я локальним для тіла, тому змінити модульне ім’я з функції без `global` неможливо.[^py314-reference-simple-stmts-the-global-statement]

`global` діє на весь поточний блок (модуль, тіло функції або тіло класу): перелічені імена трактуються як глобальні, тобто їхні звертання в блоці стосуються модульного namespace.[^py314-reference-simple-stmts-the-global-statement] Вкладена функція з `global x` не змінює `x` зовнішньої функції, навіть якщо та має власний `x`, а змінює модульний `x`. Це видно в прикладі:

```python
x = 'module'

def outer():
    x = 'outer'
    def use_global():
        global x
        x = 'global assigned'
    def use_nonlocal():
        nonlocal x
        x = 'nonlocal assigned'
    use_global()
    print(x)     # outer: the global assignment did not reach outer's x
    use_nonlocal()
    print(x)     # nonlocal assigned

outer()
print(x)         # global assigned: the global declaration reached the module
```

`nonlocal` працює інакше. Він шукає прив’язку лише в локальних scope охоплюючих функцій, а модуль у пошуку не бере участі. Тому `nonlocal x` у функції, вкладеній безпосередньо в модуль, без `x` в охоплюючій функції дає `SyntaxError`, навіть якщо модульний `x` існує.[^py314-reference-simple-stmts-the-nonlocal-statement]

Декларації мають межі. `global` має стояти раніше за будь-яке використання або присвоєння імені в тому самому блоці; інакше виникає `SyntaxError`.[^py314-reference-simple-stmts-the-global-statement] Аналогічно `nonlocal` на рівні модуля є `SyntaxError`, бо охоплюючих функцій немає.[^py314-reference-simple-stmts-the-nonlocal-statement]

**Типові помилки:**
- писати `nonlocal x` для модульного `x`: для модуля потрібна декларація `global`;
- очікувати, що `global x` у вкладеній функції змінить `x` зовнішньої функції;
- ставити `global x` після читання або присвоєння `x` у тому самому блоці: це `SyntaxError`.

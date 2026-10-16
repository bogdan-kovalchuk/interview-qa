---
id: py-prac-0004
title: "У Python 3.14 що надрукує `print(x)` після блоку `match 1:` з `case x: pass` і як capture pattern впливає на scope імені?"
track: python
section: practical-coding
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-match-statement
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#naming-and-binding
---

## Short answer

**Надрукує `1` – bare name у `case` є capture pattern і прив’язує subject до імені `x`.**[^py314-reference-compound-stmts] Як і `if` чи `for`, `match` не створює окремого блоку з власним scope: `x` стає звичайним іменем у поточній області видимості й лишається прив’язаним після `match`.[^py314-reference-executionmodel] <span class="warn">Щоб порівняти зі значенням іменованої константи, використовують dotted name, наприклад `case Color.RED`; bare name, крім `_`, завжди є capture.[^py314-reference-compound-stmts]</span>

## Detailed explanation

`match` порівнює subject з патернами `case` по черзі. Bare name – це capture pattern: він завжди збігається і прив’язує subject до імені.[^py314-reference-compound-stmts] Тому в `match 1` з `case x:` ім’я `x` отримує значення `1`, хоча жодного порівняння немає. Блок `pass` нічого не робить, але прив’язка вже відбулася:

```python
match 1:
    case x:
        pass
print(x)  # 1: x is a module-level name, still bound after the match
```

Прив’язка не перевіряє існуючі значення. Якщо `LIMIT` уже має значення, `case LIMIT:` його перепризначає, а не порівнює:

```python
LIMIT = 10
match 42:
    case LIMIT:  # capture pattern: always matches and rebinds LIMIT
        print("matched")  # matched
print(LIMIT)  # 42


class Color:
    RED = 1


match 2:
    case Color.RED:  # value pattern: compares 2 == Color.RED
        print("red")
    case _:
        print("other")  # other
```

Щоб порівняти з іменованим значенням, потрібен dotted name (value pattern): він збігається, якщо значення дорівнює subject за оператором `==`.[^py314-reference-compound-stmts] Символ `_` теж не прив’язує імені, тож після `match` його не можна прочитати.[^py314-reference-compound-stmts]

`match` не є блоком у розумінні мови. Блоками вважаються модуль, тіло функції й тіло класу, тому `match` нового scope не створює.[^py314-reference-executionmodel] Ім’я, прив’язане в `case` всередині функції, стає локальним у найближчій функції, якщо немає `global` чи `nonlocal`.[^py314-reference-compound-stmts]

**Типові помилки:**
- писати `case RED:` для константи `RED` і очікувати порівняння, а не прив’язку;
- вважати, що `case x:` не змінює вже існуюче `x`;
- вважати, що `_` прив’язує значення і його можна прочитати після `match`.

---
id: py-prac-0004
title: "У Python 3.14 що надрукує `print(x)` після блоку `match 1:` з `case x: pass` і як capture pattern впливає на scope імені?"
description: "Надрукує 1 – bare name у case є capture pattern і прив’язує subject до імені x."
track: python
section: practical-coding
level: middle
type: pitfall
tags: [match-1-nbsp-nbsp-case-x-passprint-x]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-match-statement
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ match: capture pattern прив’язує значення до імені й завжди збігається; одиночне _ не є capture pattern; value pattern (dotted name) збігається, коли значення дорівнює subject за =="
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#naming-and-binding
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ Naming and binding: блоками є модуль, тіло функції й тіло класу; ім’я, прив’язане в коді модуля, є глобальним."
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

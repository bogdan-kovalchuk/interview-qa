---
id: py-funcs-0002
title: "Коли й чому виклик `f(1, a=2)` для `def f(a): ...` завершується помилкою: до входу в тіло функції чи під час його виконання?"
description: "TypeError про повторне значення для параметра a виникає до входу в тіло функції, на етапі binding аргументів."
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: [f-1-a-2, def-f-a]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`TypeError` про повторне значення для `a` виникає до входу в тіло функції, на етапі binding аргументів.**[^py314-reference-expressions-calls] Позиційний аргумент `1` заповнює слот параметра `a`, а keyword `a=2` намагається заповнити той самий слот. Інтерпретатор перевіряє конфлікти під час зіставлення аргументів із параметрами, тому тіло функції не виконується взагалі.

## Detailed explanation

Виклик проходить у два етапи: спочатку Python зіставляє аргументи з параметрами, і лише потім виконується тіло функції. Для `def f(a): ...` позиційний `1` заповнює слот `a`, а keyword `a=2` адресований до того самого слота. Документація описує це як частину обробки аргументів: якщо слот уже заповнено, піднімається `TypeError`; інакше аргумент записується в слот, а після обробки всіх аргументів заповнені слоти стають списком аргументів виклику.[^py314-reference-expressions-calls]

Приклад показує різницю: друк у тілі спрацьовує лише тоді, коли тіло почало виконуватися:

```python
def f(a):
    print('body runs')
    return a

try:
    f(1, a=2)                # TypeError at binding: 'body runs' is not printed
except TypeError:
    print('TypeError')

def g(a):
    print('body runs')
    return len(a)

try:
    g(5)                     # 'body runs' is printed, then TypeError inside the body
except TypeError:
    print('TypeError')
```

Вирази аргументів обчислюються до того, як Python спробує виклик. Тому побічні ефекти в аргументах відбудуться, навіть якщо виклик потім завершиться `TypeError`. Документація прямо каже, що всі вирази аргументів обчислюються до спроби виклику.[^py314-reference-expressions-calls]

Важливо відрізняти два випадки: `TypeError` під час зіставлення аргументів і `TypeError` із самого тіла, як `len(a)` у `g(5)`. Формулювання повідомлення в різних прикладах документації та в CPython 3.13 відрізняється, тому орієнтуватися варто на поведінку: чи виконався перший рядок тіла.

**Типові помилки:**
- шукати причину помилки в тілі функції, хоча тіло ще не виконувалося;
- вважати, що вирази аргументів не обчислюються, якщо виклик завершився помилкою;
- не помітити конфлікт позиційного аргумента з розпакуванням `**`: `f(1, **{'a': 2})` дає ту саму помилку.[^py314-reference-expressions-calls]

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

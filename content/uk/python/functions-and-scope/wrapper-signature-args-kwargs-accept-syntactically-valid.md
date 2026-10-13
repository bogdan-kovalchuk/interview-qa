---
id: py-funcs-0005
title: "Чому wrapper із сигнатурою `(*args, **kwargs)` може прийняти синтаксично коректний виклик, який потім відхилить обгорнута функція, і на якому етапі виникає `TypeError`?"
description: "Wrapper `(*args, **kwargs)` приймає будь-який виклик, а невідповідність сигнатури видно лише всередині обгорнутої функції."
track: python
section: functions-and-scope
level: senior
type: mechanism
tags: [args-kwargs, typeerror]
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
  - source_id: py314-library-inspect-inspect-signature
    title: "Python 3.14: Library/inspect"
    url: https://docs.python.org/3.14/library/inspect.html#inspect.signature
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: functools.wraps додає до wrapper атрибут __wrapped__ і копіює метадані; не змінює, які аргументи wrapper приймає."
  - source_id: py314-library-inspect-signature-bind
    title: "Python 3.14: Library/inspect"
    url: https://docs.python.org/3.14/library/inspect.html#inspect.Signature.bind
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: Signature.bind зіставляє позиційні й іменовані аргументи з параметрами і кидає TypeError, якщо вони не відповідають сигнатурі."
---

## Short answer

**Wrapper `(*args, **kwargs)` приймає будь-яку комбінацію аргументів, тому перевірка сигнатури відбувається лише на етапі виклику обгорнутої функції.**[^py314-reference-expressions-calls] Наприклад, якщо внутрішня функція має сигнатуру `def inner(a, b)`, а wrapper викликають `wrapper(1, 2, 3)`, wrapper успішно зв’яже `args = (1, 2, 3)`, але розпакування `inner(*args)` дасть `TypeError: inner() takes 2 positional arguments but 3 were given`. Помилка виникає всередині wrapper, у момент виклику inner, а не на вході wrapper.

## Detailed explanation

Коли викликають `wrapper(1, 2, 3)`, Python спочатку зіставляє аргументи з параметрами самого wrapper. Сигнатура `(*args, **kwargs)` приймає будь-які позиційні й іменовані аргументи: зайві позиційні йдуть у кортеж `args`, а іменовані – у словник `kwargs`. Правило «позиційних аргументів більше, ніж параметрів» стосується функції, яку справді викликають. Для wrapper з `*args` такого ліміту немає, тому виклик він приймає.[^py314-reference-expressions-calls]

Помилка виникає тоді, коли wrapper передає аргументи далі. Виклик `inner(*args, **kwargs)` виконує те саме зіставлення для `inner`: три позиційні значення не вміщуються в параметри `a` і `b`, і виникає `TypeError`. Отже, помилка з’являється в рядку wrapper, де відбувається передача, а не на вході в wrapper. Наступний приклад показує це:

```python
def inner(a, b):
    return a + b

def wrapper(*args, **kwargs):
    print('wrapper got', args, kwargs)
    return inner(*args, **kwargs)

wrapper(1, 2)            # prints: wrapper got (1, 2) {}
try:
    wrapper(1, 2, 3)     # prints: wrapper got (1, 2, 3) {}
except TypeError as error:
    print(error)         # inner() takes 2 positional arguments but 3 were given
```

Рядок `print` виконується до помилки, бо wrapper уже прийняв виклик і почав роботу. Це важливо, коли wrapper робить щось до виклику: рахує виклики, пише лог, обмежує частоту або кешує. Такі побічні ефекти відбуваються раніше за помилку, тож неправильний виклик може змінити стан програми і лише потім завершитися винятком.

Якщо перевірку треба зробити на вході, аргументи можна зіставити заздалегідь: `inspect.signature(func).bind(*args, **kwargs)` створює відповідність аргументів параметрам і кидає `TypeError`, якщо вони не відповідають сигнатурі.[^py314-library-inspect-signature-bind] `functools.wraps` робить інше: він копіює метадані й додає атрибут `__wrapped__`,[^py314-library-functools-functools-wraps] тому `inspect.signature(wrapper)` показує сигнатуру обгорнутої функції, наприклад `(a, b)`.[^py314-library-inspect-inspect-signature] Це лише інтроспекція: виклик `wrapper(1, 2, 3)` усе одно приймає сам wrapper, а помилка виникає всередині.

**Типові помилки:**
- очікувати, що неправильні аргументи відхиляться на вході декоратора, тоді як wrapper їх приймає і передає далі;
- не враховувати побічні ефекти wrapper, які встигають виконатися до `TypeError`;
- вважати, що `functools.wraps` або `inspect.signature` роблять wrapper суворішим.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

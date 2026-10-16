---
id: py-funcs-0003
title: "Як без втрати позиційних та keyword arguments передати отримані `*args` і `**kwargs` іншій функції, і яку помилку легко зробити під час такого forwarding?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
  - source_id: py314-faq-programming
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html
---

## Short answer

**Потрібно розпаковувати їх при виклику: `target(*args, **kwargs)`, а не передавати як звичайні аргументи.**[^py314-reference-expressions-calls] `*` розгортає `args` як додаткові позиційні аргументи, а `**` розгортає `kwargs` як додаткові keyword аргументи.[^py314-reference-expressions-calls] Поширена помилка – написати `target(args, kwargs)`: тоді `args` (tuple) піде як один позиційний аргумент, а `kwargs` (dict) – як другий позиційний, а не як keyword. Залежно від сигнатури цільова функція або мовчки отримає хибні значення, або дасть `TypeError`.[^py314-reference-expressions-calls]

## Detailed explanation

Усередині функції `args` і `kwargs` є звичайними значеннями: `args` – це tuple, а `kwargs` – dict. Документація визначає саме так: параметр `*identifier` отримує tuple зайвих позиційних аргументів, а `**identifier` – dict зайвих keyword аргументів.[^py314-reference-expressions-calls] Щоб передати їх далі без втрат, їх треба розпакувати у виклику: `*` розгортає tuple як додаткові позиційні аргументи, а `**` розгортає dict як додаткові keyword аргументи.[^py314-reference-expressions-calls]

Найпоширеніша помилка – передати `args` і `kwargs` як звичайні значення. Позиційні аргументи заповнюють слоти по порядку, тому `args` стає першим аргументом `a`, а dict – другим аргументом `b`, і жодного keyword не доходить до `flag` чи `options`.[^py314-reference-expressions-calls] Нижче `forward` пересилає аргументи правильно, а `wrong` – ні; обидві функції викликають одну й ту саму `target`:

```python
def target(a, b, *rest, flag=False, **options):
    return a, b, rest, flag, options

def forward(*args, **kwargs):
    return target(*args, **kwargs)

def wrong(*args, **kwargs):
    return target(args, kwargs)

print(forward(1, 2, 3, flag=True, color='red'))
# (1, 2, (3,), True, {'color': 'red'})
print(wrong(1, 2, 3, flag=True, color='red'))
# ((1, 2, 3), {'flag': True, 'color': 'red'}, (), False, {})
```

У `wrong` помилка тиха: функція працює й повертає хибні значення. Якщо ж цільова функція не приймає стільки позиційних аргументів, замість цього виникає `TypeError`.

Є ще дві помилки. Виклик лише з `target(*args)` тихо відкидає всі keyword аргументи. Додавання keyword, який уже є в `kwargs`, як у `target(*args, **kwargs, flag=True)` при `kwargs` з ключем `flag`, дає `TypeError`, бо параметр уже отримав значення.[^py314-reference-expressions-calls]

**Типові помилки:**
- писати `target(args, kwargs)` або `target(*args, kwargs)`: тоді `kwargs` стає позиційним dict;
- передавати лише `*args`, забувши `**kwargs`: keyword аргументи зникають без помилки;
- додавати до виклику keyword, який уже є в `kwargs`: це `TypeError`.

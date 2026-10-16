---
id: py-funcs-0014
title: "Як Python шукатиме ім’я `len` усередині функції, якщо локального binding немає, але модуль визначив власний `len`?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
---

## Short answer

**Python шукає ім’я спочатку в local scope, потім в enclosing scope, далі в global namespace модуля і лише після цього в builtins; тому модульний `len` буде знайдено раніше за вбудований `len`.**[^py314-reference-executionmodel-resolution-of-names] Локального binding немає, а enclosing scope (якщо функція не вкладена) теж не містить `len`, тож пошук доходить до модуля, знаходить визначений там `len` і не доходить до builtins.

## Detailed explanation

Ім’я `len` у тілі функції визначається в момент використання, а не під час `def`. Python бере найближчий scope, у якому ім’я прив’язане: спочатку local namespace функції, потім enclosing функції (якщо вона вкладена), потім global namespace модуля, який містить код, і лише після цього builtins.[^py314-reference-executionmodel-resolution-of-names]

Модульний `len` перекриває вбудований для коду цього модуля. Приклад показує, як змінюється результат одного й того самого виклику `count`:

```python
def count(items):
    return len(items)               # the name is looked up when this call runs

print(count([1, 2, 3]))             # 3: no module-level len yet, so builtins len is used

def len(obj):
    return 'module len'

print(count([1, 2, 3]))             # module len: the module-level name is found first

import builtins
print(builtins.len([1, 2, 3]))      # 3: the builtin is still reachable explicitly

del len
print(count([1, 2, 3]))             # 3: without the module-level name, lookup reaches builtins

def outer():
    def len(obj):
        return 'enclosing len'
    def inner():
        return len([1])
    return inner()

print(outer())                      # enclosing len: the enclosing scope is searched before the module
```

Пошук відбувається під час виклику, тому важить стан namespace саме на той момент. `count` бачить модульний `len`, навіть якщо його визначено після `def count`, бо до виклику він уже існує. Вбудований `len` від цього не зникає: до нього можна звернутися як `builtins.len`, а `del len` знову відкриває шлях до нього. Builtins – це окремий namespace модуля `builtins`, що стоїть останнім у пошуку.[^py314-reference-executionmodel-resolution-of-names]

Вкладена функція має пріоритет над модулем: якщо зовнішня функція визначає свій `len`, то `inner` знаходить саме його, і пошук на ньому зупиняється. Це та сама послідовність, тільки enclosing scope стоїть між local і global.

**Типові помилки:**
- вважати, що ім’я `len` прив’язується під час `def`: пошук відбувається під час виклику, за станом namespace на той момент;
- не враховувати enclosing scope: `len` у зовнішній функції перекриває і модульний, і вбудований;
- вважати, що `builtins.len` недоступний, якщо модуль перевизначив `len`: його можна викликати явно.

---
id: py-perf-0016
title: "Коли перенесення hot loop у vectorized або native implementation виправдовує boundary-crossing та data-conversion cost?"
track: python
section: performance
sources:
  - source_id: py314-library-array
    title: "Python 3.14: Library/array"
    url: https://docs.python.org/3.14/library/array.html#module-array
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
---

## Short answer

**Перенесення hot loop у vectorized або native implementation виправдане, коли, серед інших умов, робота на кожен елемент висока і даних достатньо, щоб перекрити фіксовану вартість переходу з Python та конвертацію даних.** Спершу треба знайти hot spot, і для цього призначений модуль profile.[^py314-faq-programming-performance] Поріг залежить від коду, даних і машини, тому його вимірюють на репрезентативних розмірах: якщо на елемент припадає мало роботи або дані щоразу конвертуються туди й назад, boundary-crossing та data-conversion cost можуть з’їсти весь виграш.

## Detailed explanation

Перенесення циклу в native-код (векторизована бібліотека або C-розширення) має сенс, коли сам цикл є вузьким місцем. FAQ радить знаходити hot spots до будь-якої оптимізації, і для цього призначений модуль profile.[^py314-faq-programming-performance] У profile `tottime` – це час, проведений у самій функції без викликів підфункцій, тож він показує, де зосереджена робота.[^py314-library-profile] Якщо ж цикл займає малу частку часу, перенесення не змінить загальний час, навіть коли сам цикл став значно швидшим.

Вартість переходу складається з фіксованої вартості виклику з Python, конвертації аргументів і результатів та самої роботи. Вигода з’являється, коли робота на елемент велика відносно перших двох. Примітиви, написані на C, зазвичай швидші за власний Python-код: FAQ каже, що стандартна бібліотека ймовірно (але не гарантовано) швидша за альтернативу, яку ви напишете самі, і що це особливо справджується для C-примітивів.[^py314-faq-programming-performance]

Конвертація часто є прихованою вартістю. Модуль `array` описує себе як тип, що компактно зберігає масив базових значень,[^py314-library-array] тож масив, створений зі списку Python-об’єктів, означає копіювання кожного значення:

```python
from array import array

values = [float(i) for i in range(1_000_000)]  # 1,000,000 Python float objects
packed = array('d', values)                    # one O(n) conversion into C doubles
print(packed[:3])                              # array('d', [0.0, 1.0, 2.0])
```

Якщо такий масив створювати на кожному виклику, конвертація повторюватиметься. При простій арифметиці на елемент вона може зрівнятися з роботою або перевищити її, тож дані краще тримати в native-формі між викликами.

Порівнювати варіанти треба через `timeit` на тих самих даних і розмірах, що в роботі. Документація радить повторювати вимірювання і брати найкращий результат, бо інші програми на машині впливають на час.[^py314-library-timeit] Не варто порівнювати Python-цикл під cProfile із C-функцією: профайлер додає накладні витрати для Python-коду, але не для C-функцій, тож C-код у такому порівнянні виглядає швидшим, ніж є насправді.[^py314-library-profile]

**Типові помилки:**
- переносити цикл без профайлінгу, коли hot spot насправді в іншому місці;
- міряти на малих даних, де перехід займає більшість часу, і переносити висновок на великі дані;
- конвертувати дані туди й назад на кожному кроці;
- порівнювати час під профайлером із часом C-функції.

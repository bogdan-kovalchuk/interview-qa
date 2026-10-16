---
id: py-stdlib-0005
title: "Чим `islice()` корисний для лінивого iterable, який не підтримує indexing?"
track: python
section: standard-library
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
  - source_id: py314-library-itertools-islice
    title: "Python 3.14: Library/itertools, islice"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.islice
---

## Short answer

**`islice()` дозволяє брати перші N елементів або діапазон з будь-якого iterable без перетворення його на список.**[^py314-library-itertools-islice] Працює як зріз для списків, але для ітераторів: `islice(gen, 5)` дає перші 5 елементів, а `islice(gen, 2, 10, 2)` – елементи з позиціями 2, 4, 6 і 8. Від’ємні значення `start`, `stop` і `step` не підтримуються.[^py314-library-itertools-islice]

## Detailed explanation

`islice()` – це зріз для iterable. Його сигнатура `islice(iterable, stop)` або `islice(iterable, start, stop[, step])`. За документацією, він працює як зріз послідовності, але не приймає від’ємні значення `start`, `stop` і `step`.[^py314-library-itertools-islice] Він не потребує ні довжини, ні індексації: `islice` бере елементи з вхідного iterable один за одним, тож generator, файл або нескінченний iterable обробляються однаково.

Лінивість видно на нескінченному iterable: `count()` ніколи не вичерпується, але `islice` зупиняється на `stop`:

```python
from itertools import count, islice

print(list(islice(count(10, 5), 4)))         # [10, 15, 20, 25]: count() is infinite
print(list(islice('ABCDEFG', 2, 4)))         # ['C', 'D']
print(list(islice('ABCDEFG', 2, None)))      # ['C', 'D', 'E', 'F', 'G']
print(list(islice('ABCDEFG', 0, None, 2)))   # ['A', 'C', 'E', 'G']
```

Елементи до `start` пропускаються, а між кроками `step` елементи теж читаються з вхідного iterable.[^py314-library-itertools-islice] Для generator це означає, що пропущені елементи створюються. Приклад друкує кожен елемент, щоб було видно, які саме створюються:

```python
from itertools import islice

def numbers():
    for i in range(6):
        print(f'produce {i}')
        yield i

gen = numbers()
print(list(islice(gen, 3)))  # produce 0, 1, 2 are printed, then [0, 1, 2]
print(next(gen))             # produce 3 is printed, then 3
print(list(islice(numbers(), 2, 6, 2)))  # produce 0 to 5 are all printed, then [2, 4]
```

У CPython `islice` не запитує елемент понад `stop`: після `islice(gen, 3)` генератор стоїть перед четвертим елементом, і `next(gen)` створює його. Документація цього не описує, тож це спостережувана поведінка CPython, а не гарантія мови, і на неї не варто спиратися в коді.

**Типові помилки:**
- очікувати від `islice(it, -1)` останній елемент: від’ємні значення не підтримуються, і виклик дає `ValueError`;
- вважати, що `islice` не чіпає вхідний ітератор: він просуває його, і наступний `next()` продовжує з позиції, на якій зупинився `islice`;
- вважати, що елементи, пропущені через `start` або `step`, не обчислюються: для generator вони створюються.

---
id: py-stdlib-0002
title: "Як `Counter` спрощує frequency analysis і як він поводиться з missing keys?"
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
  - source_id: py314-library-collections-counter
    title: "Python 3.14: Library/collections, Counter objects"
    url: https://docs.python.org/3.14/library/collections.html#collections.Counter
---

## Short answer

**`Counter` повертає `0` для відсутніх ключів замість `KeyError`, що дозволяє рахувати елементи без перевірки наявності ключа.**[^py314-library-collections-counter] Ініціалізується з iterable або mapping, має методи `most_common(n)` для топ-N елементів і `subtract()` для віднімання лічильників. Підтримує арифметичні операції (`+`, `-`, `&`, `|`) між `Counter`-об’єктами.[^py314-library-collections-counter]

## Detailed explanation

`Counter` – це підклас `dict` для підрахунку hashable-об’єктів: ключі зберігають самі елементи, а значення – їхні лічильники.[^py314-library-collections-counter] Типова frequency analysis проходить iterable один раз і збільшує лічильник кожного елемента. Конструктор `Counter(iterable)` робить це одним викликом, а `most_common(n)` повертає `n` найчастіших елементів від найчастішого до найрідшого. Елементи з однаковою кількістю йдуть у порядку першої появи, тож `Counter('abracadabra').most_common(3)` дає `a`, потім `b` і `r`, обидва з лічильником 2.[^py314-library-collections-counter]

Найважливіша відмінність від звичайного `dict` – поведінка з відсутніми ключами. Лічильник відсутнього елемента дорівнює нулю, тому `counts['dog']` повертає `0`, а не піднімає `KeyError`.[^py314-library-collections-counter] У CPython це реалізовано методом `__missing__`, який лише повертає `0` і не записує ключ у словник. Тому одне читання нічого не змінює: `'dog' in counts` лишається `False`. Ключ з’являється тільки під час запису, наприклад `counts['dog'] += 1`.

Приклад: рахуємо слова, потім читаємо відсутній ключ:

```python
from collections import Counter

words = "the cat and the hat and the bat".split()
freq = Counter(words)
print(freq.most_common(2))  # [('the', 3), ('and', 2)]
print(freq['dog'])          # 0: a missing key gives 0, no KeyError
print('dog' in freq)       # False: the read did not insert the key
freq['dog'] += 1
print('dog' in freq, freq['dog'])  # True 1: a write does insert the key
```

Арифметичні операції повертають лише результати з додатними лічильниками: `c - d` відкидає елементи з нульовою або від’ємною кількістю, тоді як `subtract()` змінює лічильники на місці й допускає нульові та від’ємні значення.[^py314-library-collections-counter] Явно записаний нульовий лічильник теж лишається в `Counter`, доки його не видалено через `del`.[^py314-library-collections-counter]

**Типові помилки:**
- вважати, що читання `counts[key]` створює запис, і будувати на цьому перевірку наявності ключа;
- очікувати від’ємні лічильники після `+` або `-`: вони відкидаються, а від’ємні значення дає `subtract()`;
- плутати `Counter` з `defaultdict(int)`: обидва дають `0` для відсутнього ключа, але `defaultdict` вставляє ключ під час читання (див. qid:py-stdlib-0003).

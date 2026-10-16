---
id: py-perf-0018
title: "Чому premature micro-optimization може збільшити defect risk без помітного user-level benefit?"
track: python
section: performance
sources:
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
---

## Short answer

**Micro-optimization змінює код до того, як профайлінг показав, що саме ця ділянка є bottleneck.**[^py314-faq-programming-performance] Часто така зміна не змінює user-visible latency: кеш для функції, аргументи якої не повторюються, ніколи не дає попадання, але додає пам’ять і код; ручна реалізація замість стандартної або передчасний C extension додають місця для помилок і ускладнюють testing. <span class="warn">Спочатку профайлінг, потім hot spot, потім оптимізація саме його; інакше зусилля піде на код, який не визначає user experience.</span>

## Detailed explanation

Micro-optimization – це локальна зміна, яка прискорює дрібну ділянку: інший спосіб обчислити те саме, ручна реалізація замість стандартної функції, кеш, C-розширення. Пастка в тому, що таку зміну роблять наосліп. FAQ радить спершу знайти hot spots у програмі і прямо каже, що швидший алгоритм дає значно більший виграш, ніж micro-optimization-трюки, розкидані по коду.[^py314-faq-programming-performance] Інструмент для пошуку hot spots – `profile`: його внутрішня статистика часу допомагає знайти hot loops, які варто оптимізувати.[^py314-library-profile]

Defect risk зростає разом зі складністю: у складнішому коді більше гілок і крайніх випадків, які треба тестувати, а без тестів оптимізація легко ламає поведінку, яку ніхто не перевіряє. Тому покриття тестами йде перед складною оптимізацією.[^py314-faq-programming-performance]

Приклад – кеш без повторних аргументів. `lru_cache(maxsize=None)` вимикає обмеження розміру, і кеш може рости без межі.[^py314-library-functools-functools-lru-cache] У коді нижче кожен аргумент новий, тож кеш не дає жодного попадання, а лише накопичує записи:

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # unbounded: every new argument adds an entry
def parse_id(raw):
    return int(raw)

for i in range(5):
    parse_id(str(i))         # every argument is new, so the cache never hits
print(parse_id.cache_info())
# CacheInfo(hits=0, misses=5, maxsize=None, currsize=5)
```

Код коректний, але для цих викликів кеш не дав користі: лишилися пам’ять і зайвий рядок декоратора.

Навіть справді швидша ділянка не змінює end-to-end час, якщо bottleneck в іншому місці: в I/O, мережі чи SQL. Тому спершу профайлінг, потім оптимізація саме hot spot. Інакше зусилля піде на код, який не визначає user experience, а ризик регресій лишиться.

**Типові помилки:**
- оптимізувати функцію, бо вона «здається повільною», без профайлінгу;
- додавати кеш, не перевіривши, чи будуть повторні аргументи;
- переписувати код заради мікровиграшу без тестів на поведінку;
- вважати, що швидша локальна ділянка автоматично дає швидший запит.

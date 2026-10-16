---
id: py-perf-0002
title: "Яку проблему вирішує `timeit` порівняно з одноразовим заміром wall-clock time?"
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
  - source_id: py314-library-timeit-repeat
    title: "Python 3.14: Library/timeit (Timer.repeat)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.Timer.repeat
  - source_id: py314-library-timeit-timeit
    title: "Python 3.14: Library/timeit (Timer.timeit)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.Timer.timeit
  - source_id: py314-library-timeit-autorange
    title: "Python 3.14: Library/timeit (Timer.autorange)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.Timer.autorange
  - source_id: py314-library-timeit-default-timer
    title: "Python 3.14: Library/timeit (default_timer)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.default_timer
  - source_id: py314-library-timeit-cli
    title: "Python 3.14: Library/timeit (Command-Line Interface)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit-command-line-interface
  - source_id: py314-library-time-time
    title: "Python 3.14: Library/time (time.time)"
    url: https://docs.python.org/3.14/library/time.html#time.time
  - source_id: py314-library-profile-introduction
    title: "Python 3.14: Library/profile (Introduction to the profilers)"
    url: https://docs.python.org/3.14/library/profile.html#introduction-to-the-profilers
---

## Short answer

**`timeit` вирішує проблему шуму через повтори: найменше значення з повторів – нижня межа швидкості коду, бо більші значення зазвичай спричинені іншими процесами.**[^py314-library-timeit-repeat] Під час заміру він вимикає garbage collector,[^py314-library-timeit-timeit] а командний рядок сам підбирає кількість ітерацій і за замовчуванням повторює замір 5 разів.[^py314-library-timeit-cli] Одноразовий замір через `time.time()` такого захисту не має, і його значення може зменшитися, якщо системний годинник перевели назад.[^py314-library-time-time]

## Detailed explanation

Одноразовий замір (різниця двох відліків `time.time()`) фіксує все, що ОС і інші процеси зробили в цей інтервал. `time.time()` до того ж може повернути менше значення, ніж попередній виклик, якщо системний годинник перевели назад.[^py314-library-time-time] Шум від інших процесів лише додає час, тому найменший із повторів ближчий до справжньої вартості коду. Документація `timeit` пояснює це так: найменше значення дає нижню межу, а більші зазвичай спричинені іншими процесами, тож середнє і стандартне відхилення мало що дають.[^py314-library-timeit-repeat]

`timeit` автоматизує частину роботи, але не все. Setup виконується один раз, `timeit()` повертає час лише основного оператора, а під час заміру вимикається garbage collector, щоб заміри були порівнянішими. Кількість ітерацій (`number`) за замовчуванням дорівнює 1 000 000 і задається вами.[^py314-library-timeit-timeit] За замовчуванням таймер – `time.perf_counter()`.[^py314-library-timeit-default-timer] Автоматичний підбір кількості дає `autorange()`, який збільшує її, доки сумарний час не стане щонайменше 0.2 с.[^py314-library-timeit-autorange]

Приклад показує, що GC вимкнено під час заміру, а `repeat()` повертає список із 5 замірів, з якого береться найменший:

```python
import gc
import timeit

# The statement runs with the garbage collector turned off.
timer = timeit.Timer('print(gc.isenabled())', setup='import gc')
timer.timeit(1)                   # prints False: timeit disables GC while timing
print(gc.isenabled())             # True: the state is restored afterwards

times = timeit.repeat('sum(range(1000))', number=1000, repeat=5)
print(len(times))                 # 5: one total time per repeat
best = min(times)                 # the lower bound; higher values are usually noise
```

Найменший замір – це оцінка для цього коду на цій машині, з цією версією Python і за цього навантаження, а не універсальна константа. Порівнювати варіанти треба однаковим способом і з однаковим `setup`. Для точного часу профілювальник не підходить: документація профілювання прямо відсилає до `timeit`.[^py314-library-profile-introduction]

**Типові помилки:**
- брати середнє з одного заміру або з повторів замість `min()`;
- вважати, що `Timer.timeit()` сам повертає мінімум: він повертає час одного прогону з `number` ітераціями;
- виконувати в `stmt` те, що має бути в `setup` (наприклад, створення даних), бо це повторюється в кожній ітерації.

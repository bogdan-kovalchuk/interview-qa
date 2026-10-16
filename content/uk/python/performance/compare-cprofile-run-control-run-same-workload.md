---
id: py-perf-0004
title: "Як порівняти `cProfile` run з контрольним run на однаковому workload, щоб відрізнити instrumentation overhead від bottleneck?"
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
  - source_id: py314-library-profile-introduction
    title: "Python 3.14: Library/profile (Introduction to the profilers)"
    url: https://docs.python.org/3.14/library/profile.html#introduction-to-the-profilers
  - source_id: py314-library-profile-limitations
    title: "Python 3.14: Library/profile (Limitations)"
    url: https://docs.python.org/3.14/library/profile.html#limitations
  - source_id: py314-library-timeit-cli
    title: "Python 3.14: Library/timeit (Command-Line Interface)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit-command-line-interface
---

## Short answer

**Запустити той самий workload двічі – під `cProfile` і без нього на детермінованих вхідних даних – і порівняти загальний час та відносні частки функцій.** Якщо профільований прогін значно повільніший за контрольний, накладні витрати суттєві. Вони припадають на Python-код, тож C-реалізація на профілі виглядає швидшою, ніж є.[^py314-library-profile-introduction] Функції з великою кількістю викликів накопичують похибку, тому їхній `tottime` може бути завищений.[^py314-library-profile-limitations] <span class="warn">Для точного часу використовуйте `timeit`, а профілювальник – лише для пошуку гарячих точок.</span>[^py314-library-profile-introduction]

## Detailed explanation

Порівняння має відповісти на два різні питання: скільки часу з’їдає сам профілювальник і чи справді функція є вузьким місцем. Для цього потрібні два прогони того самого workload: контрольний без профілювальника і профільований під `cProfile`. Версія Python, машина, код і вхідні дані мають бути однакові, а вхід детермінований: фіксований seed або фіксовані дані.

Контрольний прогін беріть повторами. Документація `timeit` пояснює, що на вимірювання можуть впливати інші програми на машині, тому варто повторити заміри кілька разів і взяти найкращий час. Командний рядок `timeit` робить це за замовчуванням із 5 повторами.[^py314-library-timeit-cli]

Приклад міряє контрольний час без профілювальника, потім той самий виклик під `cProfile`. Через `pstats` видно, скільки подій профілювальник зафіксував для `leaf`:

```python
import cProfile
import pstats
import timeit

def leaf(x):
    return x * 2

def workload():
    return sum(leaf(i) for i in range(10_000))

# Control run: no profiler, best of 5 repeats, seconds per workload call.
control = min(timeit.repeat(workload, number=20, repeat=5)) / 20

# Profiled run: the same workload with the same input.
profiler = cProfile.Profile()
profiler.runcall(workload)
stats = pstats.Stats(profiler)
profiled = stats.total_tt         # seconds, including profiler overhead

for (filename, lineno, funcname), (cc, nc, tt, ct, callers) in stats.stats.items():
    if funcname == "leaf":
        print(nc)                 # 10000 recorded calls, each with profiler work
print(control > 0 and profiled > 0)   # True
```

Різниця між `profiled` і `control` – це накладні витрати, зокрема робота, яку профілювальник виконує між подіями. Їх не можна просто відняти від результатів окремих функцій, бо вони розподілені нерівномірно. Документація пояснює, що накладні витрати припадають на код Python, а не на C-рівневі функції, тому C-реалізація на профілі виглядає швидшою, ніж є.[^py314-library-profile-introduction] Похибка також накопичується у функцій, які викликаються багато разів, тож дрібна функція з великою кількістю викликів може отримати завищений `tottime`.[^py314-library-profile-limitations]

Щоб відрізнити накладні витрати від справжнього вузького місця, перевіряйте зміну на контрольному прогоні, а не на профілі. Якщо функція справді домінує, її оптимізація скорочує контрольний час приблизно на її частку в ньому. Якщо функція виглядає важкою лише в профілі, а контрольний час не змінюється, профіль завищував її частку в реальному часі.

**Типові помилки:**
- вважати функцію гарячою точкою лише за `tottime` профілю, без контрольного прогону;
- порівнювати профільований прогін з контрольним на різних вхідних даних або в різних процесах;
- брати один контрольний замір замість повторів.

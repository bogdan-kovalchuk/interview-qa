---
id: py-perf-0001
title: "Як deterministic profiler вимірює call counts та time і чому його instrumentation overhead треба враховувати під час інтерпретації?"
description: "Deterministic profiler (наприклад, cProfile) реєструє кожну подію виклику та повернення функції, фіксуючи ncalls, tottime (час у самому тілі) та cumtime (разом з підфункціями)."
track: python
section: performance
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-profile-deterministic
    title: "Python 3.14: Library/profile (What Is Deterministic Profiling?)"
    url: https://docs.python.org/3.14/library/profile.html#what-is-deterministic-profiling
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: означення детермінованого профілювання (події виклику, повернення і винятку) і згадка про малі накладні витрати у типових застосунках."
  - source_id: py314-library-profile-stats
    title: "Python 3.14: Library/profile (Analysis of the Profile Data)"
    url: https://docs.python.org/3.14/library/profile.html#profile-stats
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: значення ncalls, tottime і cumtime у звіті профілю. Не описує накладні витрати."
  - source_id: py314-library-profile-limitations
    title: "Python 3.14: Library/profile (Limitations)"
    url: https://docs.python.org/3.14/library/profile.html#limitations
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: обмеження точності, затримка між подією і зчитуванням годинника накопичується у функцій з багатьма викликами."
  - source_id: py314-library-profile-introduction
    title: "Python 3.14: Library/profile (Introduction to the profilers)"
    url: https://docs.python.org/3.14/library/profile.html#introduction-to-the-profilers
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: cProfile і profile, їхні накладні витрати і призначення для профілю виконання, а не для бенчмаркінгу."
---

## Short answer

**Deterministic profiler (наприклад, `cProfile`) реєструє події виклику, повернення і винятку та вимірює інтервали між ними: `ncalls` – кількість викликів, `tottime` – час у самій функції, `cumtime` – разом із підфункціями.**[^py314-library-profile-deterministic] Затримка між подією і зчитуванням годинника накопичується у функцій, які викликаються багато разів.[^py314-library-profile-limitations] `cProfile` має помірні накладні витрати, а `profile` (чистий Python) – значно більші.[^py314-library-profile-introduction] Профілювальник дає профіль виконання, а не точний бенчмарк.[^py314-library-profile-introduction]

## Detailed explanation

Deterministic profiling не вибирає зразки, а стежить за виконанням: інтерпретатор повідомляє профілювальник про кожну подію виклику, повернення і винятку, а час між подіями відносить до функцій.[^py314-library-profile-deterministic] Звідси три стовпці звіту, які зазвичай читають разом. `ncalls` – скільки разів функцію викликали. `tottime` – час у самій функції без підфункцій, `cumtime` – разом із підфункціями.[^py314-library-profile-stats] Отже, `tottime` показує, де час витрачається безпосередньо, а `cumtime` – яку роботу охоплює виклик.

Лічильник викликів найпростіше побачити на прикладі. Функція `leaf` викликається з генераторного виразу 10 000 разів, і кожен виклик фіксується як окрема подія:

```python
import cProfile
import pstats

def leaf(x):
    return x * 2

def workload():
    return sum(leaf(i) for i in range(10_000))

profiler = cProfile.Profile()
profiler.runcall(workload)
stats = pstats.Stats(profiler)
for (filename, lineno, funcname), (cc, nc, tt, ct, callers) in stats.stats.items():
    if funcname == "leaf":
        print(nc)                 # 10000: every call is recorded
        print(cc == nc)           # True: leaf is not recursive
```

Важливіші за лічильник накладні витрати. Профілювальник виконує власний код між подіями, і ця робота потрапляє в загальний час. Документація пояснює, що затримка від події до зчитування годинника накопичується у функцій, які викликаються багато разів або викликають багато функцій, тому їхні часи можуть бути завищені.[^py314-library-profile-limitations] Для типових застосунків накладні витрати від детермінованого профілювання невеликі.[^py314-library-profile-deterministic] Але для дрібних функцій з великою кількістю викликів спотворення помітне.[^py314-library-profile-limitations]

Вибір інструмента теж має значення. `cProfile` є C-розширенням з помірними накладними витратами і рекомендований для більшості користувачів, а `profile` на чистому Python додає значно більше.[^py314-library-profile-introduction] Для точного часу документація радить `timeit`, бо профілювальники призначені для профілю виконання, а не для бенчмаркінгу.[^py314-library-profile-introduction] Абсолютні числа з профілю варто читати як завищені. Відносний порядок функцій і кількість викликів корисні для пошуку кандидатів, але їх треба підтвердити контрольним заміром.

**Типові помилки:**
- брати `tottime` або `cumtime` з профілю як точний час функції;
- плутати `tottime` і `cumtime` і шукати вузьке місце серед верхніх викликів, бо вони охоплюють майже весь прогін;
- ігнорувати, що дрібні функції з великою кількістю викликів найбільше спотворюються накладними витратами.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

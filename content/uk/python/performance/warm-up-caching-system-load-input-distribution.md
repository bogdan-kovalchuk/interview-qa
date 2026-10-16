---
id: py-perf-0003
title: "Як warm-up, caching, system load та input distribution можуть змістити microbenchmark result?"
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
  - source_id: py314-library-timeit-repeat
    title: "Python 3.14: Library/timeit (Timer.repeat)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.Timer.repeat
  - source_id: py314-howto-sorting
    title: "Python 3.14: Sorting HOWTO (Sort Stability and Complex Sorts)"
    url: https://docs.python.org/3.14/howto/sorting.html#sort-stability-and-complex-sorts
---

## Short answer

**Warm-up, caching, system load і input distribution змінюють те, що вимірює benchmark, а не лише «чисту» продуктивність коду.** Фонові процеси додають час, тому вищі значення в повторах зазвичай спричинені ними.[^py314-library-timeit-repeat] `lru_cache` зберігає результати останніх викликів, тож повторний виклик з тими самими аргументами може не виконувати функцію.[^py314-library-functools-functools-lru-cache] Вхідні дані теж важливі: Timsort, алгоритм сортування Python, використовує впорядкованість, яка вже є в даних.[^py314-howto-sorting] <span class="warn">Порада: беріть `min()` з повторів і тестуйте на кількох розподілах вхідних даних.</span>

## Detailed explanation

Benchmark вимірює виконання за конкретних умов, а не абстрактну властивість коду. Перший прогін може включати імпорт модуля, якщо той опиняється у вимірюваному коді, і холодні кеші процесора, тому він зазвичай повільніший за наступні. Повтори з `min()` відсікають такий прогін: найменше значення з серії найближче до вартості коду без цих ефектів.

Кеш змінює саму роботу, яку вимірюють. `functools.lru_cache` зберігає результати до `maxsize` останніх викликів і може заощаджувати час, коли дорога функція періодично викликається з тими самими аргументами.[^py314-library-functools-functools-lru-cache] Якщо перший виклик заповнює кеш, а повтори беруть результат звідти, найменший замір описує пошук у кеші, а не обчислення. Кешування на рівні ОС або застосунку може мати такий самий ефект; його видно лише порівнянням із вимкненим кешем.

Системне навантаження додає шум нерівномірно: фонові процеси, планувальник ОС і інші програми на машині зсувають окремі заміри. Документація `timeit` описує це саме так: вищі значення в повторах зазвичай спричинені тим, що інші процеси заважають точності заміру.[^py314-library-timeit-repeat]

Вхідні дані змінюють сам шлях виконання. Timsort, алгоритм сортування Python, використовує впорядкованість, яка вже є в даних.[^py314-howto-sorting] Лічильник порівнянь показує різницю на списках однакового розміру (у CPython):

```python
class Counted:
    count = 0

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        Counted.count += 1
        return self.value < other.value

n = 1000
already_sorted = [Counted(i) for i in range(n)]
permuted = [Counted((i * 7919) % n) for i in range(n)]   # a permutation of 0..999

Counted.count = 0
sorted(already_sorted)
print(Counted.count)              # 999: one comparison per adjacent pair (CPython)

Counted.count = 0
sorted(permuted)
print(Counted.count)              # 8532: about 8.5 times more on the same-size input (CPython)
```

Той самий `sorted()` робить 999 порівнянь на вже відсортованому списку і 8532 на перестановці з 1000 елементів. Синтетичний вхід, який виглядає типовим, але не відповідає реальному розподілу, може показати швидшу або повільнішу роботу, ніж та, що буде в застосунку.

Практичний висновок: повторювати замір і брати `min()`, відокремлювати прогрів від вимірювання, тестувати на кількох розподілах вхідних даних і явно вказувати, що кешується. Ці дії не замінюють одне одного: повтори не прибирають ефект кешу, а кеш не прибирає шуму.

**Типові помилки:**
- вважати один замір після імпорту стабільною оцінкою;
- порівнювати кешований варіант з некешованим, не врахувавши кеш;
- тестувати лише на вхідних даних, вигідних для реалізації (вже відсортованих або однорідних).

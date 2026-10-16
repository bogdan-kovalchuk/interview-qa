---
id: py-perf-0013
title: "Як task batching та `chunksize` можуть зменшити serialization і scheduling overhead у process pool, але погіршити load balancing?"
track: python
section: performance
sources:
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.map
---

## Short answer

**`chunksize` у `ProcessPoolExecutor.map()` групує елементи iterable у chunk-и, які надсилаються в пул як окремі задачі.**[^py314-library-concurrent-futures] Для дуже довгих iterable великий `chunksize` може суттєво покращити продуктивність[^py314-library-concurrent-futures], бо задач стає менше. За `chunksize=1` (значення за замовчуванням) кожен елемент є окремою задачею: балансування краще, але накладні витрати платяться за кожну задачу. <span class="warn">`chunksize` не впливає на `ThreadPoolExecutor.map()` – там він ігнорується.</span>[^py314-library-concurrent-futures]

## Detailed explanation

`ProcessPoolExecutor` передає кожну задачу в інший процес: функцію й аргументи треба серіалізувати, а результат повернути назад. Фіксовані витрати (повідомлення між процесами, планування) платяться за задачу, а не за елемент. Документація описує механізм: `Executor.map()` розбиває iterable на chunk-и, які надсилаються в пул як окремі задачі, а приблизний розмір chunk-а задає `chunksize`.[^py314-library-concurrent-futures]
Розмір chunk-а змінює кількість задач:

```python
from concurrent.futures import ProcessPoolExecutor


def square(x):
    return x * x


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as pool:
        # chunksize=1 (default): 10 000 items -> 10 000 separate tasks
        list(pool.map(square, range(10_000)))
        # chunksize=500: 10 000 items -> 20 tasks of up to 500 items each
        list(pool.map(square, range(10_000), chunksize=500))
```

Вибір розміру – компроміс. Великий chunk зменшує кількість задач, але робить одиницю роботи грубішою. Нехай є 1000 елементів, 4 workers і `chunksize=250`: вийде 4 chunk-и, по одному на worker. Якщо всі повільні елементи потрапили в перший chunk, один worker працює довго, а три інші простоюють після завершення своїх chunk-ів. З `chunksize=1` ті самі 1000 задач розбирають вільні workers, тож балансування краще, але накладні витрати платяться 1000 разів.

Виграш залежить від співвідношення вартості елемента до фіксованих витрат. Якщо елемент коштує значно більше за пересилання, `chunksize` майже не змінює картини; якщо тривалість елементів сильно різниться, великий chunk шкодить. Універсального числа немає, тож значення вимірюють на реальних даних. У `ThreadPoolExecutor` chunksize ігнорується. З 3.14 `map()` має параметр `buffersize`, який обмежує кількість задач без отриманого результату; це не спосіб групувати задачі, а обмеження їхньої кількості в черзі.[^py314-library-concurrent-futures]

**Типові помилки:**
- шукати параметр `chunksize` у `submit()`: його там немає, батчі формують вручну;
- ставити великий `chunksize` для нерівномірних задач і отримувати простої наприкінці;
- міряти на короткому iterable, де переважають запуск пулу й старт процесів.

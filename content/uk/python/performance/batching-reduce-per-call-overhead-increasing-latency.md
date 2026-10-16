---
id: py-perf-0015
title: "Як batching може зменшити per-call I/O overhead, але збільшити latency та memory use?"
track: python
section: performance
sources:
  - source_id: py314-library-io-performance
    title: "Python 3.14: Library/io (Performance)"
    url: https://docs.python.org/3.14/library/io.html#performance
  - source_id: py314-library-functions-open
    title: "Python 3.14: Built-in Functions (open)"
    url: https://docs.python.org/3.14/library/functions.html#open
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

**Batching об’єднує багато дрібних I/O-операцій в один виклик.** Той самий принцип лежить в основі буферизованого I/O стандартної бібліотеки: він читає й записує великими фрагментами, приховуючи неефективність викликів ОС на кожен дрібний запис.[^py314-library-io-performance] Ціна – накопичення даних у пам’яті: весь batch треба зібрати до відправки, а перший елемент чекає, поки batch заповниться або спрацює таймаут. <span class="warn">Надто великий batch може вичерпати пам’ять або перевищити ліміти розміру запиту, які встановлює сервер чи протокол.</span>

## Detailed explanation

Batching – це накопичення багатьох дрібних операцій (записів, запитів, повідомлень) і виконання їх одним викликом, коли batch заповнився або спрацював таймаут. Найпростіший приклад зі стандартної бібліотеки – буферизований I/O. Документація пояснює, що він читає й записує великими фрагментами, навіть коли програміст просить один байт, і тим самим приховує неефективність викликів нижчого рівня операційної системи.[^py314-library-io-performance] Для бінарних файлів без аргументу `buffering` функція `open()` теж використовує буфер фіксованого розміру.[^py314-library-functions-open]

Виграш залежить від ОС і виду I/O: на деяких сучасних ОС, наприклад Linux, небуферизований дисковий I/O може бути таким самим швидким, як буферизований.[^py314-library-io-performance] Буферизований I/O дає передбачувану продуктивність незалежно від платформи та пристрою, тому для бінарних даних його майже завжди варто віддавати перед небуферизованим.[^py314-library-io-performance] Тож вигоду від batching треба вимірювати, а не вважати за замовчуванням.

Та сама схема без жодної I/O-бібліотеки: функція `send` імітує один виклик I/O, а цикл збирає елементи в пакети по три (ілюстративний приклад):

```python
BATCH_SIZE = 3
batch = []

def send(items):  # stand-in for one I/O call
    print(f"send {len(items)} item(s): {items}")

for item in range(7):
    batch.append(item)      # item 0 waits in memory until the batch is full
    if len(batch) == BATCH_SIZE:
        send(batch)         # 7 items use 3 calls here instead of 7
        batch = []
if batch:
    send(batch)             # the last, partial batch
# Output:
# send 3 item(s): [0, 1, 2]
# send 3 item(s): [3, 4, 5]
# send 1 item(s): [6]
```

Ціна batching – пам’ять і затримка. Елементи тримаються в пам’яті до відправки, тож пік використання RAM росте з розміром batch, а перший елемент чекає, поки batch заповниться або спрацює таймаут. Розмір batch підбирають під обидва обмеження.

Порівнювати варіанти варто через `timeit` на тих самих даних і розмірах, що в роботі. Документація радить повторити вимірювання кілька разів і взяти найкращий результат, бо інші програми на тій самій машині можуть впливати на час.[^py314-library-timeit]

**Типові помилки:**
- вважати, що batching завжди швидший: якщо накладні витрати на виклик малі або дані вже буферизовані, виграш може бути нульовим;
- збільшувати batch без межі, не рахуючи пам’ять і затримку першого елемента;
- забути відправити останній, неповний batch.

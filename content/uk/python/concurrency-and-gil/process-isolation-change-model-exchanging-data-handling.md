---
id: py-gil-0004
title: "Як process isolation змінює модель обміну даними та обробку worker crash порівняно з threads?"
description: "Process isolation вимагає серіалізації даних (pickle) для IPC, але забезпечує ізоляцію crash – падіння worker не завершує батьківський process."
track: python
section: concurrency-and-gil
level: senior
type: comparison
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Process isolation вимагає серіалізації даних (pickle) для IPC, але забезпечує ізоляцію crash – падіння worker не завершує батьківський process.**[^py314-library-threading] Обмін даними відбувається через `Queue`/`Pipe` (pickle), `Value`/`Array` (shared memory для C-типів) або `Manager` (proxy-об'єкти через серверний process). У threads обмін безкоштовний (спільна пам'ять), але необроблений exception у thread завершує весь process. Trade-off: ізоляція та безпека process проти накладних витрат на серіалізацію та додаткову пам'ять.

## Detailed explanation

Ізоляція процесів базується на роздільних віртуальних адресних просторах на рівні операційної системи: кожен дочірній процес отримує власний heap, власну таблицю дескрипторів та окремий екземпляр інтерпретатора CPython з власним GIL.[^py314-library-multiprocessing] У потоках (`threading`) усі потоки виконуються в єдиному адресному просторі процесу, де читання й запис спільних структур даних відбувається безпосередньо за вказівниками пам'яті, але вимагає синхронізації примітивами (`Lock`, `RLock`) для запобігання race conditions.

Оскільки процеси не мають прямого доступу до пам'яті одне одного, обмін даними вимагає міжпроцесної комунікації (IPC). При використанні черг `multiprocessing.Queue` або каналів `Pipe` дані проходять повний цикл серіалізації (`pickle.dumps`) у процесі-відправнику та десеріалізації (`pickle.loads`) у процесі-отримувачі, що створює помітні CPU-накладні витрати й вимагає сумісності об'єктів із pickle. Альтернативні шляхи – спільна пам'ять (`multiprocessing.shared_memory`, `Value`, `Array`), яка передає сирі байти без серіалізації, або `Manager`-процеси, що надають доступ до віддалених об'єктів через IPC-проксі за рахунок суттєвого падіння швидкодії.

Модель обробки збоїв (worker crash) демонструє фундаментальну перевагу ізоляції. Фатальний збій потоку на рівні ОС – наприклад, segmentation fault у C extension, переповнення стека або завершення через OS OOM killer – негайно завершує весь процес разом із усіма іншими потоками. У багатопроцесній архітектурі апаратний захист пам'яті ОС локалізує збій: аварійне завершення дочірнього процесу залишає батьківський процес неушкодженим, дозволяючи зчитати код повернення (exitcode) або перехопити виняток `BrokenProcessPool` у пулах `concurrent.futures` і виконати відновлення чи перезапуск worker.[^py314-library-concurrent-futures]

Приклад різниці між серіалізацією даних через IPC та виживанням батьківського процесу при збої worker:

```python
import multiprocessing as mp
import os

def worker(queue):
    # IPC requires serialization (pickle) over pipes/sockets
    item = queue.get()
    item["value"] += 1
    queue.put(item)
    # Abrupt worker crash does not kill parent process
    os._exit(1)

if __name__ == "__main__":
    q = mp.Queue()
    data = {"value": 10}
    q.put(data)

    p = mp.Process(target=worker, args=(q,))
    p.start()
    p.join()

    # Data in parent remains unchanged due to isolated memory space
    print(data["value"])         # 10 (isolated from child modifications)
    print(q.get()["value"])      # 11 (received through IPC)
    print(p.exitcode)            # 1 (child terminated abnormally, parent survives)
```

**Практичні наслідки та архітектурні компроміси:**
- передача великих структур даних (наприклад, багатогігабайтних датафреймів) через черги призводить до serialization bottleneck; у таких сценаріях слід використовувати `SharedMemory` або передавати шляхи до файлів;
- не всі об'єкти Python є picklable: генератори, файлові дескриптори, мережеві сокети та lambda-функції не можуть передаватися через стандартні IPC-канали;
- на відміну від потоків, падіння worker через segmentation fault чи OOM killer не призводить до втрати основного процесу програми, що критично для високонадійних сервісів;
- завершення процесу worker під час утримання IPC-блокування або запису в pipe може призвести до зависання черги, якщо не налаштовано тайм-аути чи механізми виявлення broken process pool.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

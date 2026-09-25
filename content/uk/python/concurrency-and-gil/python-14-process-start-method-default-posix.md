---
id: py-gil-0021
title: "У Python 3.14 який process start method є default на POSIX і Windows, та коли потрібно явно обрати `spawn`, `fork` чи `forkserver`?"
description: "У Python 3.14 default на POSIX – forkserver, на Windows – spawn."
track: python
section: concurrency-and-gil
level: senior
type: comparison
tags: [spawn, fork, forkserver]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: "3.14"
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

**У Python 3.14 default на POSIX – `forkserver`, на Windows – `spawn`.**[^py314-library-threading] <span class="warn">Зміна POSIX-default з `fork` на `forkserver` сталася саме в 3.14 для уникнення проблем багатопотокового `fork()`.</span> `spawn` – найбезпечніший (новий інтерпретатор), але повільніший; `fork` – швидкий, але небезпечний якщо батьківський процес має threads (може призвести до crash/deadlock); `forkserver` – баланс: один server-процес стартує через `spawn`, подальші fork-и від нього. `fork` слід обирати лише для legacy-коду без threads; `spawn` – коли потрібна максимальна ізоляція.

## Detailed explanation

Історично на POSIX-системах (Linux та інші Unix) CPython використовував `fork` як метод за замовчуванням, оскільки системний виклик `fork()` створює дочірній процес майже миттєво через механізм copy-on-write пам'яті без повторного завантаження інтерпретатора чи імпорту модулів.[^py314-library-multiprocessing] Однак `fork()` у багатопотоковому процесі копіює у новий процес лише той потік, що здійснив виклик; усі інші потоки раптово зникають. Якщо будь-який фоновий потік у цей момент утримував блокування (наприклад, внутрішній mutex аллокатора пам'яті, блокування логера чи сокета бази даних), цей лок назавжди залишається заблокованим у дочірньому процесі, призводячи до невідворотного deadlock або пошкодження стану пам'яті.

Через масове використання фонових потоків у сторонніх бібліотеках (наприклад, OpenMP, системних бібліотеках C та нових версіях CPython), у Python 3.14 стандартний метод запуску для POSIX було змінено з `fork` на `forkserver`.[^py314-library-multiprocessing] На Windows метод `spawn` завжди був і залишається єдиним можливим, оскільки ядро Windows не має аналога системного виклику `fork`. На macOS перехід на `spawn` відбувся ще в Python 3.8 через несумісність `fork()` із системними фреймворками CoreFoundation та Cocoa.

Механізми відрізняються способом створення та ступенем ізоляції:
- `spawn`: запускає абсолютно новий процес інтерпретатора (`python`), виконує модуль заново до блоку `if __name__ == '__main__':` і передає стан виключно через pickle. Це найнадійніший метод із повною ізоляцією, але він має найвищий час старту;
- `fork`: миттєво клонує процес через виклик ОС `fork()`, успадковуючи весь стан пам'яті. Небезпечний у будь-яких програмах із потоками;
- `forkserver`: компроміс, що вирішує проблему багатопотокового `fork()`. При першому запиті створюється спеціальний серверний процес через `spawn`, який залишається строго однопотоковим. Усі подальші worker-процеси форкаються вже від цього сервера. Це забезпечує безпеку багатопотокового середовища і суттєво менші накладні витрати на старт порівняно зі `spawn`.

Визначення поточного системного методу запуску та явне використання безпечного контексту `spawn`:

```python
import multiprocessing as mp

def task(name):
    # Retrieve current active context method
    method = mp.get_start_method()
    print(f"Task '{name}' executed under start method: {method}")

if __name__ == "__main__":
    # In Python 3.14: POSIX defaults to 'forkserver', Windows defaults to 'spawn'
    default_method = mp.get_start_method()
    print(f"System default start method: {default_method}")

    # Best practice: use explicit contexts rather than global set_start_method()
    # 'spawn' guarantees a clean interpreter and identical behavior across OSes
    spawn_ctx = mp.get_context("spawn")
    p = spawn_ctx.Process(target=task, args=("worker-1",))
    p.start()
    p.join()
```

**Практичні наслідки та вибір методу:**
- обирайте `spawn` для кросплатформного коду, який однаково працює на Windows, macOS та Linux, або при взаємодії з бібліотеками (CUDA, PyTorch, GUI), що не підтримують fork;
- використовуйте `forkserver` на POSIX-серверах із частим створенням короткоживучих процесів; за допомогою `mp.set_forkserver_preload(['numpy', 'torch'])` можна заздалегідь завантажити важкі модулі у серверний процес;
- залишайте `fork` лише для legacy POSIX-утиліт, де гарантовано відсутні будь-які вторинні потоки виконання, а швидкість створення процесу є критичною;
- уникайте мутації глобального стану через `mp.set_start_method()`, оскільки це може спричинити конфлікти між незалежними бібліотеками; надавайте перевагу локальним контекстам `mp.get_context('...')`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

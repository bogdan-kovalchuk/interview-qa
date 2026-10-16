---
id: py-funcs-0018
title: "Як `nonlocal` дозволяє closure змінювати captured state, і який ризик це створює при конкурентних викликах?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-simple-stmts-the-nonlocal-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-nonlocal-statement
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
  - source_id: py314-faq-library-what-kinds-of-global-value-mutation-are-thread-safe
    title: "Python 3.14: Faq/library"
    url: https://docs.python.org/3.14/faq/library.html#what-kinds-of-global-value-mutation-are-thread-safe
  - source_id: py314-library-threading-lock-objects
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html#lock-objects
---

## Short answer

**`nonlocal` дозволяє closure перезаписувати змінну в enclosing function scope, перетворюючи її на спільний мутабельний стан між усіма викликами closure.**[^py314-reference-simple-stmts-the-nonlocal-statement] У однопотоковому коді це стандартний патерн stateful closure (лічильник, кеш). <span class="warn">У багатопотоковому коді на CPython з GIL оновлення спільного стану через read-modify-write (наприклад, `count += 1`) не є атомарним: потік може бути перерваний між читанням і записом, що призводить до race condition.</span>[^py314-faq-library-what-kinds-of-global-value-mutation-are-thread-safe] Для синхронізації потрібен примітив на кшталт `threading.Lock`.[^py314-library-threading-lock-objects]

## Detailed explanation

`nonlocal` прив’язує ім’я у вкладеній функції до найближчого enclosing scope, де воно вже зв’язане, тож присвоєння змінює саме цю змінну, а не створює нову локальну.[^py314-reference-simple-stmts-the-nonlocal-statement] Ім’я, яке використано в блоці, але не визначено там, є free variable.[^py314-reference-executionmodel-resolution-of-names] Closure, створені одним викликом фабрики, бачать одну й ту саму cell, тому стан накопичується між викликами.

Небезпека в тому, що `count += 1` – це читання, додавання і запис. Python перемикає потоки лише між bytecode-інструкціями, тож перемикання може статися між читанням і записом. FAQ прямо відносить `i = i + 1` до неатомарних операцій.[^py314-faq-library-what-kinds-of-global-value-mutation-are-thread-safe]

У тесті на CPython 3.14 `count += 1` без жодного виклику всередині не давав втрат, а виклик Python-функції в правій частині давав. Це не робить просту форму безпечною: відсутність втрат – деталь поточної реалізації, а не гарантія; FAQ називає `i = i + 1` неатомарним.[^py314-faq-library-what-kinds-of-global-value-mutation-are-thread-safe] Приклад:

```python
def price(item):
    return item                       # illustrative: any Python-level call

def make_total():
    total = 0

    def add(item):
        nonlocal total
        total = total + price(item)   # read total, call price(), then store total
        return total

    return add
```

Чотири потоки по 50 000 викликів `add(1)` з `sys.setswitchinterval(1e-6)` дали 151 605 і 140 043 замість 200 000 у двох запусках. Один правильний запуск нічого не доводить.

Виправлення – `threading.Lock`. Потік, що викликає `acquire()` на зайнятому lock, блокується, доки інший потік не викличе `release()`, а `with lock:` виконує обидві дії автоматично.[^py314-library-threading-lock-objects] Виклик `price(item)` винесено за межі lock:

```python
import threading

# price() is defined in the previous example
def make_safe_total():
    total = 0
    lock = threading.Lock()

    def add(item):
        nonlocal total
        value = price(item)           # outside the critical section
        with lock:
            total = total + value     # read and store inside one critical section
        return total

    return add
```

**Типові помилки:**
- вважати, що однопотоковий тест доводить безпеку closure з `nonlocal`;
- прочитати `total` поза lock, а записати всередині нього: втрата оновлення все одно можлива;
- вважати, що GIL робить `count += 1` атомарним.

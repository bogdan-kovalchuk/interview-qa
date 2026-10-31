---
id: py-cpyint-0006
title: "Як reference count зазвичай визначає moment deallocation у GIL-enabled CPython 3.14 і чому це не описує free-threaded build?"
track: python
section: cpython-internals
sources:
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
---

## Short answer

**У GIL-enabled CPython об’єкт deallocate-иться негайно, коли його reference count досягає нуля; у free-threaded build це не гарантовано через biased, deferred та per-thread reference counting.**[^py314-library-dis] GIL забезпечує атомарність операцій з refcount, тому zero -> immediate deallocation. У free-threaded build (Python 3.13+) деякі об’єкти використовують deferred refcounting (звільняються лише при наступному GC), per-thread counting (звільняються при safe point або виході потоку), або biased counting (об’єкт «queued» для відкладеного звільнення).

## Detailed explanation

У GIL-enabled build кожен об’єкт має один лічильник `ob_refcnt`, а GIL гарантує, що incref і decref
виконуються без перегонів між потоками. Коли decref зменшує лічильник до нуля, тут-таки, синхронно,
в тому самому виклику, викликається деструктор об’єкта.[^py314-c-api-memory]

У free-threaded build (PEP 703, з Python 3.13) GIL немає, тож наївний atomic incref/decref на
кожному зверненні до об’єкта був би завеликою вартістю при конкурентному доступі багатьох
потоків.[^py314-howto-free-threading-python]

CPython вирішує це через biased reference counting: кожен об’єкт має "локальний" лічильник, який
non-atomically змінює лише потік-власник, і "спільний" (shared) лічильник для decref з інших потоків,
який оновлюється atomically. Частину decref з інших потоків узагалі відкладають (deferred reference
counting) до найближчого safe point, замість негайного atomic decrement.[^py314-c-api-memory]

Тому "локальний" лічильник теоретично може виглядати нульовим, а фактичний стан об’єкта
з’ясується лише коли runtime зведе (merge) local, shared і deferred лічильники на найближчому safe
point чи під час GC-паузи. Deallocation через це стає відкладеною подією, а не миттєвим наслідком
останнього decref.

**Типові помилки:**
- очікувати ідентичну поведінку `__del__` і деструкторів між GIL-enabled і free-threaded build;
- вважати, що free-threaded build "ламає" reference counting – він лише робить момент deallocation
  менш детермінованим;
- писати код, що покладається на негайне звільнення ресурсів (файли, locks) через побічний ефект
  refcount, замість явного `with`/`close()`.

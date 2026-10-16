---
id: py-itergen-0015
title: "Чому не варто покладатися на garbage collection generator для своєчасного звільнення external resource?"
track: python
section: iterators-and-generators
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
  - source_id: py314-reference-datamodel-object-del
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__del__
  - source_id: py314-reference-datamodel-objects-values-and-types
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#objects-values-and-types
  - source_id: py314-library-gc-set-threshold
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html#gc.set_threshold
---

## Short answer

**Момент виклику `close()` для generator, який не доведено до кінця, не гарантовано: його викликає finalization, а вона залежить від reference count і від реалізації.**[^py314-reference-expressions-yield-expressions] У CPython reference cycle утримує generator живим, коли зовнішніх посилань уже немає; його звільняє cyclic GC пізніше, і момент запуску GC не передбачуваний.[^py314-reference-datamodel-object-del][^py314-library-gc-set-threshold] Інші реалізації можуть відкласти збирання сміття або взагалі його не виконувати.[^py314-reference-datamodel-objects-values-and-types] Для детермінованого звільнення ресурсів викликайте `close()` явно у `try/finally` або використовуйте context manager.

## Detailed explanation

Generator може тримати ресурс у `try/finally`, але `finally` виконується лише тоді, коли generator завершився або хтось викликав його `close()`. Якщо generator призупинений у `yield` і на нього більше ніхто не посилається, Python під час finalization сам викликає `close()`.[^py314-reference-expressions-yield-expressions] `close()` піднімає `GeneratorExit` у точці призупинення, і `finally` виконується, коли виняток проходить через нього.[^py314-reference-expressions-generator-iterator-methods] Але момент finalization визначає життєвий цикл посилань, а не код generator.

У CPython об’єкт звільняється, щойно його reference count стає нулем, тож у простих випадках ресурс закривається вчасно, і це легко сприйняти як гарантію. Проблема в reference cycle: об’єкти, які посилаються один на одного, не доходять до нуля, і прибрати їх може лише cyclic GC.[^py314-reference-datamodel-object-del] Нижче `Stream` тримає generator, а frame generator тримає `Stream` як аргумент:

```python
import gc

def read_lines(stream):
    print('acquire')
    try:
        yield 'line 1'
    finally:
        print('release')        # runs only when the generator is closed

class Stream:
    def __init__(self):
        self.lines = read_lines(self)   # the generator's frame refers back to self

gc.disable()                    # keep automatic cyclic GC out of this demo
s = Stream()
print(next(s.lines))            # prints 'acquire', then 'line 1'
del s                           # the reference cycle keeps Stream and the generator alive
print('after del')              # 'release' is not printed yet
gc.collect()                    # the cyclic GC closes the generator here
print('after gc.collect()')
```

Після `del s` рядок `release` не виводиться, бо цикл живий; він з’являється лише після `gc.collect()`. Без `gc.disable()` момент визначає автоматичний GC, який стартує, коли різниця між алокаціями і звільненнями перевищує `threshold0`.[^py314-library-gc-set-threshold] Затримка залежить від стану пам’яті всієї програми, а не від логіки, яка володіє ресурсом.

Надійний варіант – не покладатися на фіналізацію: викликати `close()` явно у `finally` або обгорнути ресурс у context manager, що звільняє його в `__exit__`. Інші реалізації Python можуть відкласти збирання сміття або взагалі його не виконувати, тож на них ресурс може закритися значно пізніше.[^py314-reference-datamodel-objects-values-and-types]

**Типові помилки:**
- вважати, що `finally` у generator завжди спрацьовує одразу, щойно цикл перервано;
- переносити момент звільнення з CPython на інші реалізації Python без перевірки;
- використовувати фіналізацію як таймер для закриття файлів, сокетів чи з’єднань.

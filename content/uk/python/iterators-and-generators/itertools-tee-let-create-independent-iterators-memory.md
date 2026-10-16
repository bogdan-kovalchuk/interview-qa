---
id: py-itergen-0018
title: "Як `itertools.tee()` дозволяє створити незалежні iterators і який memory trade-off виникає, якщо consumers рухаються з різною швидкістю?"
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
  - source_id: py314-library-itertools-tee
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.tee
---

## Short answer

**`itertools.tee(iterable, n)` повертає `n` незалежних iterators над одним вхідним iterable.**[^py314-library-itertools-tee] Цей itertool може вимагати значного обсягу додаткової пам’яті, а якщо один iterator майже повністю проходить дані до того, як почне інший, `list()` працює швидше.[^py314-library-itertools-tee] У CPython значення, які найшвидша копія вже прочитала, а найповільніша ще ні, зберігаються в буфері, тож пам’ять росте з відставанням між копіями.

## Detailed explanation

`tee()` потрібен, коли один вхідний iterable треба прочитати кільком consumers незалежно один від одного.[^py314-library-itertools-tee] У CPython вхідний iterable читається лише тоді, коли якась копія просить наступне значення, а вже прочитане значення зберігається в буфері для решти копій. Тому буфер і є тією пам’яттю, яку витрачає `tee()`.

Приклад вимірює пам’ять, яку утримує буфер у CPython. Це спостереження, а не гарантія мови:

```python
import itertools
import tracemalloc

def kept_bytes(lockstep):
    a, b = itertools.tee(range(1_000_000))
    tracemalloc.start()
    if lockstep:
        for _x, _y in zip(a, b):     # both copies move together
            pass
    else:
        for _x in a:                 # a reads everything; b has not started
            pass
    current, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current

print(kept_bytes(lockstep=False) > 10_000_000)  # True: tee keeps the items b has not read
print(kept_bytes(lockstep=True) < 1_000_000)    # True: little is kept when both move together
```

Пам’ять залежить від відставання між копіями. Якщо копія `a` пройшла весь вхід, а `b` ще не починала, буфер тримає всі значення, тобто за пам’яттю це приблизно як `list(iterable)` (спостереження в CPython). Якщо копії рухаються разом, відставання мале і буфер майже порожній. Документація радить `list()`, коли один iterator використовує майже всі дані до того, як починає інший.[^py314-library-itertools-tee]

Окремо: tee-iterators не є thread-safe. Одночасне використання копій з одного виклику `tee()` з різних потоків може викликати `RuntimeError`, навіть якщо вхідний iterable thread-safe.[^py314-library-itertools-tee]

**Типові помилки:**
- вважати, що `tee()` дешевший за `list()`, коли одна копія повністю проходить дані першою;
- залишати копію, яка не читає дані, поки інша копія рухається: буфер росте з відставанням;
- ділити tee-iterators між потоками без синхронізації.

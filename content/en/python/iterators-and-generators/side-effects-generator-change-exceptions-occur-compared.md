---
id: py-itergen-0008
title: "How do side effects in a generator change when exceptions occur, compared to eager list construction?"
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
  - source_id: py314-reference-expressions-generator-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-expressions
---

## Short answer

**The generator body runs during `next()`, so side effects and exceptions from the body appear when values are consumed, not when the generator is created.**[^py314-reference-expressions-yield-expressions] Unlike a list comprehension, which builds the whole list before returning anything, a generator yields values one at a time, so results produced before an error are already available to the consumer. Code after the last consumed `yield` does not run, and `close()` raises `GeneratorExit` at the paused point, so `finally` blocks run.[^py314-reference-expressions-generator-iterator-methods]

## Detailed explanation

A generator body does not run at creation, so its side effects and exceptions are deferred until consumption. Execution starts when one of the generator's methods is called, and at each `yield` the body is suspended with its state kept.[^py314-reference-expressions-yield-expressions] To see the difference, compare an eager list comprehension with a generator expression that uses the same function, which prints each of its items:

```python
def divide(x):
    print("processing", x)            # side effect of each element
    return 10 // x                    # ZeroDivisionError for x == 0

items = [2, 0, 5]

# eager: the whole list is built before anything is returned
try:
    values = [divide(x) for x in items]
except ZeroDivisionError:
    print("eager: no values returned")

# lazy: values come out one by one
gen = (divide(x) for x in items)      # nothing printed yet
print(next(gen))                      # processing 2, then 5
try:
    next(gen)                         # processing 0, then the error
except ZeroDivisionError:
    print("lazy: error after 5 was already returned")
```

In the eager version, the error occurs while the list is being built. The side effects of all items up to the error have already happened, but the consumer receives no value at all. In the lazy version, values come out one at a time: `5` is already with the consumer when the error on zero appears. So an error in a generator can "arrive late", and part of the work never runs at all if consumption stops early.

For an unfinished generator, several rules apply. Code after the last consumed `yield` does not run, because the body is suspended. When a generator is finalized before it finishes (by reaching a zero reference count or by being garbage collected), Python calls `close()`, which raises `GeneratorExit` at the paused point, so `finally` performs the cleanup.[^py314-reference-expressions-yield-expressions] For that reason, a resource that must be released reliably should be closed explicitly with `close()`, rather than relying on when garbage collection happens.

One caveat applies only to generator expressions: the leftmost iterable is evaluated immediately. An error in it appears when the expression is created, not when it is consumed.[^py314-reference-expressions-generator-expressions]

**Common mistakes:**
- expecting an error to appear as soon as the generator is created, rather than at the first `next()`;
- assuming the side effects of all items have happened when the generator was only partly consumed;
- relying on GC instead of an explicit `close()` for resource cleanup.

---
id: py-itergen-0005
title: "When does the body of a generator function run: when the function is called, or on the first `next()`?"
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
  - source_id: py314-reference-expressions-generator-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-expressions
---

## Short answer

**The body of a generator function does not run when the function is called; it starts on the first `next()`.**[^py314-reference-expressions-yield-expressions] Calling the function immediately returns a generator object, without executing any line of the body. The first `next()` (or a `for` loop) runs the body from the start up to the first `yield`. So errors in the body appear during iteration, not when the generator is created.

## Detailed explanation

The body of a generator function does not run during the call to the function itself. Calling a function that contains `yield` returns a generator, an iterator that keeps the execution state and controls the body. The body starts when one of the generator's methods is called, most often `next()` through a `for` loop or the built-in `next()`. Execution proceeds to the first `yield`, suspends there, and produces its value.[^py314-reference-expressions-yield-expressions]

Each following `next()` continues from the point of suspension. An error inside the body, such as `int("x")`, appears only when execution reaches that line. Argument binding is a separate matter: in CPython, a wrong number of arguments raises `TypeError` already during the call, before any `next()`. The example below shows both moments; the `print` in the body runs only on the first `next()`:

```python
def parse(values):
    print("body started")           # runs on the first next(), not on the call
    for value in values:
        yield int(value)

gen = parse(["1", "x"])             # prints nothing: the body has not started
print("generator created")
print(next(gen))                    # prints "body started", then 1
try:
    next(gen)                       # int("x") raises inside the body
except ValueError:
    print("ValueError on the second next()")
```

The output starts with `generator created`, then `body started` and `1`. The second `next()` raises `ValueError`, which the example catches.

A generator expression `(x for x in items)` has one difference: its leftmost iterable is evaluated immediately, so an error in that iterable appears when the expression is created, not at `next()`.[^py314-reference-expressions-generator-expressions]

**Common mistakes:**
- expecting `gen = parse(...)` to run code up to the first `yield`, such as printing or opening a file;
- assuming an error in the body appears as soon as the generator is created;
- confusing creating a generator with consuming it: without `next()` or a `for` loop the body never runs.

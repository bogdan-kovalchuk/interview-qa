---
id: py-itergen-0002
title: "Why does `iter(container)` usually return a new iterator, while `iter(iterator)` must return the same object?"
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
  - source_id: py314-glossary-term-iterator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterator
---

## Short answer

**`container.__iter__()` usually creates a new iterator with its own state, whereas `iterator.__iter__()` returns the iterator itself.**[^py314-glossary-term-iterator] This is required so that both containers and iterators can be used in `for` and `in` statements.[^py314-library-stdtypes-iterator-types] So a second `for` over a container starts from the beginning, while a second `for` over the same iterator continues from where it stopped and yields nothing if it is already exhausted.[^py314-glossary-term-iterator]

## Detailed explanation

When a `for` loop or `iter()` takes a container, the iteration position is not stored in the container itself. An iterator holds it, and the container's `__iter__()` creates that iterator. The documentation recommends that `container.__iter__()` return a new iterator that goes over all the elements of the container.[^py314-reference-datamodel-object-iter] So two independent loops over the same `list` do not interfere with each other:

```python
nums = [1, 2, 3]
a = iter(nums)                # a new iterator, position 0
b = iter(nums)                # another iterator, its own position 0
print(next(a))                # 1
print(next(b))                # 1: b does not share a's position
print(list(a))                # [2, 3]: a continues from where it stopped
print(iter(a) is a)           # True: iter() on an iterator returns the same object
```

The other case is when `iter()` returns the same object because it is already an iterator. A generator expression creates an iterator, so looping over it a second time gives an empty result:

```python
gen = (x * x for x in range(3))  # a generator expression creates an iterator
print(iter(gen) is gen)          # True
print(list(gen))                 # [0, 1, 4]
print(list(gen))                 # []: the same iterator is already exhausted
```

The practical rule follows: a function that must go over its data twice should receive a container (for example a `list`), not an iterator. Otherwise the first pass consumes the elements, and the second pass sees an empty result:

```python
def count_and_list(items):
    n = sum(1 for _ in items)   # the first pass consumes a generator
    return n, list(items)       # the second pass sees nothing

print(count_and_list([1, 2, 3]))             # (3, [1, 2, 3])
print(count_and_list(x for x in [1, 2, 3]))  # (3, [])
```

The rule "a container gives a new iterator" is a recommendation in the documentation, not something the interpreter checks. A class can return an existing iterator from `__iter__()`, and then all loops over it share one position. So a container class should create a new iterator on every `__iter__()` call.

**Common mistakes:**
- expecting a second `for` over an iterator to start from the beginning: it continues from where it stopped, or yields nothing;
- confusing `iterator.__iter__()` (returns self) with `container.__iter__()` (creates a new iterator), and returning self from a container class;
- calling `next()` on a `list`: `next([1, 2])` raises `TypeError`, because a list is an iterable, not an iterator.

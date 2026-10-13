---
id: py-stdlib-0003
title: "When can a `defaultdict` factory create an unwanted mutation from a simple key read?"
description: "When can a `defaultdict` factory create an unwanted mutation from a simple key read?"
track: python
section: standard-library
level: senior
type: pitfall
tags: [defaultdict]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-collections-defaultdict
    title: "Python 3.14: Library/collections, defaultdict.__missing__"
    url: https://docs.python.org/3.14/library/collections.html#collections.defaultdict.__missing__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: defaultdict.__missing__ (calling default_factory and inserting the value; KeyError when the factory is None; get() and in do not call __missing__)."
---

## Short answer

**Any `d[key]` lookup of a missing key calls `default_factory` and inserts a new entry, provided a factory is set, even if you only read the value.**[^py314-library-collections-defaultdict] For example, `if d[key]:` on a key that does not exist yet creates an entry with the default value. The `get()` method does not call the factory and does not change the dictionary, so use it for safe reads.[^py314-library-collections-defaultdict]

## Detailed explanation

A `defaultdict` is a plain `dict` with a `default_factory` attribute. For a missing key a `dict` raises `KeyError`, while a `defaultdict` calls `default_factory()` without arguments, inserts the result under that key, and returns it.[^py314-library-collections-defaultdict] This is done by the `__missing__` method, which `__getitem__` calls only when the key is absent. So if `default_factory` is set, every subscript lookup of a missing key changes the dictionary, even when the code only meant to read the value.

The condition is that `default_factory` is not `None`. If there is no factory, `__missing__` raises `KeyError` with the key as its argument and inserts nothing.[^py314-library-collections-defaultdict] Other operations, such as `get()` and the `in` test, do not call `__missing__`.[^py314-library-collections-defaultdict]

Subscript reads insert the key, while `get()` and `in` do not:

```python
from collections import defaultdict

groups = defaultdict(list)
if groups['admin']:            # a plain read: 'admin' is inserted with []
    print('has admins')
print('admin' in groups)      # True
print(groups.get('guest'))    # None: get() does not call default_factory
print('guest' in groups)     # False
```

The most dangerous case is iteration. If a loop reads a missing key from the same dictionary, the insertion changes its size, and in CPython the iterator raises `RuntimeError` on its next step:

```python
from collections import defaultdict

inventory = defaultdict(int, {'apple': 3, 'pear': 0})
try:
    for item in inventory:
        if inventory['kiwi'] == 0:   # a read of a missing key adds 'kiwi'
            pass
except RuntimeError as error:
    print(error)                     # dictionary changed size during iteration
print(sorted(inventory))             # ['apple', 'kiwi', 'pear']
```

A practical rule: use the factory where insertion is the intent, for example `groups[key].append(item)`. For a check or a read that must not change the dictionary, use `key in d` or `d.get(key)`.[^py314-library-collections-defaultdict]

**Common mistakes:**
- assuming that `if d[key]:` only tests the value and changes nothing;
- reading `d[key]` inside a loop over the same `d` and getting a `RuntimeError` or extra keys in the result;
- assuming that `get()` creates the key through `default_factory`: it returns `None` (or the default you pass) and does not call the factory.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

---
id: py-stdlib-0006
title: "Why does `itertools.groupby()` only group consecutive equal keys, and when does the input need to be sorted first?"
track: python
section: standard-library
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
  - source_id: py314-library-itertools-groupby
    title: "Python 3.14: Library/itertools, groupby"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.groupby
---

## Short answer

**`groupby()` starts a new group every time the key value changes, like the Unix `uniq` filter rather than SQL `GROUP BY`.**[^py314-library-itertools-groupby] Equal keys must be consecutive, so if they are scattered through the input, sort the data by the same key function first. Each group is an iterator that shares the underlying iterable with `groupby`, so store it as a `list` right away if you need its data later.[^py314-library-itertools-groupby]

## Detailed explanation

`groupby(iterable, key=None)` passes over the input iterable once and compares the key of each element with the key of the previous one. When the key changes, a new group starts. So `groupby` sees only adjacent elements, just as the Unix `uniq` filter sees only adjacent lines.[^py314-library-itertools-groupby] In CPython the keys are compared with `==`; ordering (`<`) is not needed for this.

The documentation generally requires the iterable to be already sorted by the same key function.[^py314-library-itertools-groupby] Sorting is one way to bring equal keys together, but not the only one: it is enough that they already appear consecutively. Without sorting, an equal key is split into several groups, and a dictionary loses data:

```python
from itertools import groupby
from operator import itemgetter

data = ['b', 'a', 'a', 'b', 'b', 'c']
print([(k, list(g)) for k, g in groupby(data)])
# [('b', ['b']), ('a', ['a', 'a']), ('b', ['b', 'b']), ('c', ['c'])]

rows = [('b', 1), ('a', 2), ('b', 3)]
by_key = {k: [v for _, v in g] for k, g in groupby(rows, key=itemgetter(0))}
print(by_key)   # {'b': [3], 'a': [2]}: the first 'b' group was overwritten
rows.sort(key=itemgetter(0))
by_key = {k: [v for _, v in g] for k, g in groupby(rows, key=itemgetter(0))}
print(by_key)   # {'a': [2], 'b': [1, 3]}
```

The second trap is the lifetime of a group. A group shares its state with `groupby`, so as soon as `groupby` moves on to the next group, the previous one becomes empty. A list of groups collected without `list()` therefore contains empty groups:

```python
from itertools import groupby

pairs = [(k, g) for k, g in groupby([1, 1, 2])]
print([(k, list(g)) for k, g in pairs])  # [(1, []), (2, [])]: a group is empty once groupby moves on
```

The correct pattern: the data is sorted by the same key (or is already consecutive), and each group that must be kept is turned into a `list` immediately. For aggregation that does not depend on input order, `groupby` is the wrong tool; accumulate into a dictionary instead, for example a `defaultdict(list)` (see qid:py-stdlib-0003).

**Common mistakes:**
- expecting `groupby` to merge all equal keys from the whole input, as SQL `GROUP BY` does;
- building a dictionary from `groupby` without sorting: a repeated key overwrites the earlier group;
- storing a group as an iterator and reading it after `groupby` has moved on to the next group.

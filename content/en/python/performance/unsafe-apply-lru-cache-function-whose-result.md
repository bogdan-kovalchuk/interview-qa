---
id: py-perf-0021
title: "Why is it unsafe to apply `lru_cache` to a function whose result depends on the current time, randomness, external mutable state, or side effects?"
track: python
section: performance
sources:
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
---

## Short answer

**`lru_cache` returns a stored result only for a repeated call with the same arguments while the entry is still cached, so for a function that depends on time, randomness or external state it gives a stale value, and side effects are skipped on a cache hit.**[^py314-library-functools-functools-lru-cache] The documentation says it makes no sense to cache functions with side effects or impure functions such as `time()` or `random()`.[^py314-library-functools-functools-lru-cache]

```python
from functools import lru_cache
import time

@lru_cache()
def fetch_now():
    return time.time()

first = fetch_now()
time.sleep(0.1)
print(fetch_now() == first)  # True - stale cached value
```

<span class="warn">Warning:</span> the cache keeps references to arguments and return values until they are evicted; with `maxsize=None` it can grow without bound.[^py314-library-functools-functools-lru-cache]

## Detailed explanation

`lru_cache` wraps a function and stores its results in a dictionary keyed by the call arguments, so the arguments must be hashable.[^py314-library-functools-functools-lru-cache] When the same arguments come again while their entry is cached, the decorator returns the stored value without calling the function again.[^py314-library-functools-functools-lru-cache] This is what makes the cache useful for expensive computations, and dangerous for anything that depends on state outside the arguments.

The decorator sees only the arguments. If the result depends on `time.time()`, `random`, a global dictionary, a file or a database, the cache returns a value that no longer matches the state. The documentation states that it makes no sense to cache functions with side effects, functions that need to create distinct mutable objects on each call (such as generators and async functions), or impure functions such as `time()` or `random()`.[^py314-library-functools-functools-lru-cache]

Side effects do not happen on a cache hit, because the body does not run. In the example, the second call does not add an entry to `calls`:

```python
from functools import lru_cache

calls = []

@lru_cache(maxsize=None)
def save(name):
    calls.append(name)   # side effect: runs only on a cache miss
    return len(calls)

print(save("a"), save("a"))  # 1 1 : second call is a cache hit, body skipped
print(calls)  # ['a']
```

A cached result can also be mutable. The same object is returned to every caller with the same arguments, so a change made through one reference is visible through all the others:

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def new_bucket(name):
    return []  # a new list on each call without the cache


first = new_bucket("a")
first.append("x")
second = new_bucket("a")  # cache hit: the same list object is returned
print(second)  # ['x']
print(first is second)  # True
```

The cache keeps references to arguments and return values until the entries are evicted or the cache is cleared. With `maxsize=None` the LRU eviction is disabled, and the cache can grow without bound.[^py314-library-functools-functools-lru-cache] The safe case is a pure function with hashable arguments whose result is expensive and does not depend on state outside its arguments. When freshness matters, clear the cache with `cache_clear()`,[^py314-library-functools-functools-lru-cache] or do not cache the function at all.

**Common mistakes:**
- caching a function that reads `time.time()`, `random` or a file, and assuming that a repeated call checks the state again;
- expecting logging or a counter inside a cached function to run on every call;
- returning a mutable object from a cached function and then changing it at the call site.

---
id: py-perf-0012
title: "How do you design cache invalidation and eviction when the source data can change?"
description: "How do you design cache invalidation and eviction when the source data can change?"
track: python
section: performance
level: senior
type: practical
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: LRU eviction with maxsize, cache_clear() clears the whole cache of the function, with maxsize=None the cache can grow without bound, and the cache is thread-safe but the function may run more than once."
---

## Short answer

**You need to combine an eviction strategy (a size limit) with an invalidation mechanism (discarding stale entries when the source data changes).** `functools.lru_cache` provides LRU eviction with `maxsize` and a `cache_clear()` method[^py314-library-functools-functools-lru-cache], but it does not track the source data. For mutable source data, use a TTL cache (a dict with timestamps and periodic purging), a versioned cache key (a version or hash in the key), or a write-through cache with invalidation events. <span class="warn">If `maxsize=None`, the cache can grow without bound[^py314-library-functools-functools-lru-cache], and without invalidation it serves stale values.</span>

## Detailed explanation

Eviction and invalidation solve different problems. Eviction bounds memory: when the cache is full, the least recently used entry is dropped. Invalidation means that after the source data changes, the stale entry is no longer served. `lru_cache(maxsize=N)` provides the first, and `cache_clear()` clears the whole cache of the function.[^py314-library-functools-functools-lru-cache] There is no way to remove a single key from `lru_cache`. If `maxsize=None`, the LRU feature is disabled and the cache can grow without bound.[^py314-library-functools-functools-lru-cache]

A version in the key is one way to invalidate without events. The version comes from the source through a cheap query (for example, `updated_at` or a revision number), and the result is cached under the pair `(name, version)`:

```python
from functools import lru_cache


@lru_cache(maxsize=256)
def load_config(name, version):
    print(f"loading {name} v{version}")
    return {"name": name, "version": version}


load_config("db", 1)  # loading db v1
load_config("db", 1)  # no output: cache hit
load_config("db", 2)  # loading db v2: a new version is a new key
print(load_config.cache_info())  # CacheInfo(hits=1, misses=2, maxsize=256, currsize=2)
```

A new key never returns a stale result. But the `('db', 1)` entry stays in the cache until LRU evicts it: `cache_info()` shows `currsize=2`. The scheme pays off only if checking the version costs less than rereading the data; otherwise the cache gains nothing.

When there is no version, a TTL is used: the entry stores its load time and is reloaded after the TTL expires. This bounds the age of stale data but does not guarantee freshness: until the TTL expires, the entry may already be stale. Precise freshness needs change events: the code that changes the source data removes the matching key from your own dict, because `lru_cache` has no such removal.

Scope. `lru_cache` lives in the memory of one process. Each worker of a `ProcessPoolExecutor` has its own cache, so `cache_clear()` in one process does not clear the others; across several processes or machines, invalidation has to go through a shared store or messages. The cache itself is thread-safe, but the function may run more than once if another thread calls it with the same arguments before the first call completes.[^py314-library-functools-functools-lru-cache]

**Common mistakes:**
- using `functools.cache` for data that changes: there is no limit, and stale values stay until the process restarts;
- clearing the cache in one process while assuming that all workers were cleared;
- setting a TTL longer than the acceptable update delay, or checking a version with an expensive query, so the cache gains nothing.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

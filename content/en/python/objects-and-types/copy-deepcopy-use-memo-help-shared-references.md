---
id: py-objtypes-0010
title: "Why does `copy.deepcopy()` use a memo, and how does that help with shared references or cyclic structures?"
description: "Why does `copy.deepcopy()` use a memo, and how does that help with shared references or cyclic structures?"
track: python
section: objects-and-types
level: senior
type: mechanism
tags: [copy-deepcopy]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**A memo is a `{id(original): copy}` dictionary that prevents infinite recursion in cyclic data structures and preserves the topology of shared references.**[^py314-reference-datamodel] When `deepcopy` encounters an object that has already been copied (tracked in the memo), it returns the existing replica instead of recursing again. For a cyclic structure like `a = []; a.append(a)`, this memoization is the only way to terminate successfully without triggering a `RecursionError` while faithfully preserving shared references in the copied graph.

## Detailed explanation

The `copy.deepcopy()` function relies on a `memo` dictionary mapping `{id(original): copy}` to memoize already copied nodes while traversing an arbitrary object graph.[^py314-library-copy]

Deep-copying compound data structures encounters two fundamental challenges: cyclic references (where an object directly or transitively references itself) and shared references (where multiple nodes point to the exact same object in memory). Without tracking previously visited objects, graph traversal would trigger infinite recursion on cycles or generate redundant duplicate instances for shared references, thereby corrupting the structural topology of the original data.

The timing of updating the `memo` table is critical to the algorithm's correctness. When `deepcopy()` encounters a container, it allocates the new instance and registers it in `memo` under `id(original)` **before** descending recursively into its elements or attributes.[^py314-reference-datamodel] When a descendant element contains a reference back to the parent container, the nested lookup finds the already-allocated replica in `memo` and returns that reference immediately, resolving the cycle cleanly without raising a `RecursionError`.

For acyclic graphs, the `memo` table ensures identity preservation. If an original list contains repeated references to the same object `[shared, shared]`, the duplicated graph preserves that exact relationship `[new_shared, new_shared]`. When implementing custom cloning logic via `__deepcopy__(self, memo)`, classes must accept `memo` as a second argument and forward it into all recursive `copy.deepcopy()` calls.

An example showing cyclic reference handling, shared reference preservation, and the `__deepcopy__` protocol:

```python
import copy

# 1. Cyclic structure handling without infinite recursion
cyclic = []
cyclic.append(cyclic)

copied_cyclic = copy.deepcopy(cyclic)
print(copied_cyclic is cyclic)           # False (brand new object)
print(copied_cyclic[0] is copied_cyclic)  # True (cycle preserved without RecursionError)

# 2. Shared reference topology preservation
shared = {"count": 0}
graph = [shared, shared]

copied_graph = copy.deepcopy(graph)
print(copied_graph[0] is copied_graph[1])  # True (shared identity maintained)

copied_graph[0]["count"] += 1
print(copied_graph[1]["count"])            # 1 (both references see mutation)

# 3. Custom class integration with memo
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        dup = Node(copy.deepcopy(self.value, memo))
        memo[id(self)] = dup
        dup.next = copy.deepcopy(self.next, memo)
        return dup
```

**Architectural considerations and common pitfalls:**
- omitting the `memo` argument in recursive `copy.deepcopy()` calls within custom `__deepcopy__` implementations, which breaks cycle resolution down the call chain;
- failing to register the newly allocated instance in `memo` before recursively copying child attributes in `__deepcopy__`, causing stack overflows on cyclic structures;
- leveraging user-supplied `memo` dictionaries via `copy.deepcopy(x, memo=custom_memo)` to preserve singletons, substitute mocks, or bypass uncopyable resources like active network sockets;
- accounting for performance overhead: maintaining a comprehensive `memo` dictionary incurs memory and lookup costs, making custom domain-specific cloning methods preferable for large graphs.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

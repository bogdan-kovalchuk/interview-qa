---
id: py-prac-0009
title: "Design a copy operation for a tree with shared subtrees and possible cycles, preserving the graph topology without aliasing with the original."
track: python
section: practical-coding
sources:
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
  - source_id: py314-library-functions-id
    title: "Python 3.14: Library/functions, id"
    url: https://docs.python.org/3.14/library/functions.html#id
---

## Short answer

**Use a memo dict keyed by the `id()` of the original node: before recursing, check whether the node is already copied, and return the existing copy.**[^py314-library-copy]

```python
def deep_copy_graph(root):
    memo = {}
    def _copy(node):
        nid = id(node)
        if nid in memo:
            return memo[nid]
        if isinstance(node, list):
            new_list = []
            memo[nid] = new_list
            new_list.extend(_copy(item) for item in node)
            return new_list
        if isinstance(node, dict):
            new_dict = {}
            memo[nid] = new_dict
            for k, v in node.items():
                new_dict[_copy(k)] = _copy(v)
            return new_dict
        return node
    return _copy(root)
```

`id()` is unique and constant while an object is alive, and the original graph stays alive during the copy, so the keys do not coincide for different nodes.[^py314-library-functions-id] The code copies only `list` and `dict`; other objects, such as a `tuple`, are returned as they are and remain shared with the original.

## Detailed explanation

Copying a graph has two requirements: a shared node must be copied once, and a cycle must not cause infinite recursion. Naive recursion meets neither. It creates a separate copy for every reference, and a structure that contains itself recurses without end. The `copy` module describes this problem directly: recursive objects may cause a recursive loop, and `deepcopy()` avoids it by keeping a memo dictionary of objects already copied during the current copying pass.[^py314-library-copy]

The naive version without a memo fails on a cycle:

```python
def naive_copy(node):
    if isinstance(node, list):
        return [naive_copy(item) for item in node]
    return node


cycle = [1]
cycle.append(cycle)
try:
    naive_copy(cycle)
except RecursionError as error:
    print(type(error).__name__)  # RecursionError: nothing stops the recursion
```

The order in the memo code matters. `memo[nid]` is written before the recursive descent: the empty `new_list` goes into the memo and is filled only afterwards by `extend`. When the descent comes back to the same node, the function returns the copy that already exists, still incomplete, and does not start a new recursion. For a `dict` the order is the same: `new_dict` goes into the memo first, then keys and values are copied. If the memo were written after the descent, a cycle would again raise `RecursionError`.

The key is `id(node)`, not the contents. `id()` is unique for live objects, so two distinct lists with equal values, such as `[1]` and `[1]`, are not merged into one copy.[^py314-library-functions-id]

The limits of this code: it copies only `list` and `dict`. Other types are returned unchanged, so after `deep_copy_graph({"t": t})["t"] is t` with `t = ("x", ["inner"])` the result is `True`: the tuple and the list inside it remain shared with the original. This follows from the code itself, which returns everything except `list` and `dict` unchanged. For `copy.deepcopy` the same check (`copy.deepcopy(t) is t`) gives `False`; the documentation does not state this, so it is an observation on 3.13 and 3.14. To close the gap, either handle every container type or give classes their own `__deepcopy__`: the `copy` module lets user-defined classes override the copying operation.[^py314-library-copy]

**Common mistakes:**
- writing the memo after the recursive descent: on a cycle this raises `RecursionError`;
- using a contents-based key, for example `repr(node)`, instead of `id()`: distinct but equal lists are then merged into one copy;
- assuming that a `tuple` or a custom object is copied together with its containers: it stays shared with the original.

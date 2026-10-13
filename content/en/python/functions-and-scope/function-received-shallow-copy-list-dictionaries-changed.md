---
id: py-funcs-0011
title: "A function received a shallow copy of a list of dictionaries and changed a value in a nested dictionary. Why can the change be visible to the caller even though the outer list was copied?"
description: "copy.copy creates a new outer list, but its items are references to the same nested objects as in the original."
track: python
section: functions-and-scope
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
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-faq-programming-why-did-changing-list-y-also-change-li
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-did-changing-list-y-also-change-list-x
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`copy.copy` (shallow copy) creates a new outer list, but inserts references to the same nested objects that the original contains.**[^py314-library-copy] So mutating a nested dictionary through the copied list changes the same object that the original refers to. When nested objects must be independent, use `copy.deepcopy`, which recursively copies the nested objects.[^py314-library-copy]

## Detailed explanation

A shallow copy copies the container, not its contents. `copy.copy(obj)` creates a new compound object and inserts references to the objects from the original into it.[^py314-library-copy] For a list of dictionaries this means two levels: the outer list is now separate, but the dictionaries inside remain the same objects, so `shallow[0] is original[0]` gives `True`. A plain assignment `b = a` is weaker still: it creates no copy at all, only a second name for the same list.[^py314-faq-programming-why-did-changing-list-y-also-change-li]

The caller passes a shallow copy to the function. The function changes a nested dictionary, and that change is visible in the original; adding an element to the copy's outer list is not:

```python
import copy

original = [{'name': 'sensor', 'value': 1}]

def update(config):
    config[0]['value'] = 99          # changes the nested dict shared with the caller
    config.append({'name': 'new'})   # changes only the outer list of the copy

shallow = copy.copy(original)
update(shallow)
print(original)                      # [{'name': 'sensor', 'value': 99}]
print(len(original))                 # 1

deep = copy.deepcopy(original)
deep[0]['value'] = 5
print(original[0]['value'])          # 99: the deep copy did not share the dict
```

Two operations must be distinguished. `config[0] = {...}` changes only the outer list of the copy, while `config[0]['value'] = 99` changes a dictionary shared with the original. Both run inside one function but act at different levels, so whether a change is visible depends on what exactly is modified.

A deep copy made by `copy.deepcopy` recursively copies the nested objects, so a change in it does not reach the original.[^py314-library-copy] The cost is that it may also copy data that was meant to stay shared between the copies.[^py314-library-copy]

**Common mistakes:**
- thinking that `copy.copy` recursively copies every level of nesting;
- thinking that `x[:]` or `list.copy()` gives a deep copy: they also create a shallow copy;[^py314-library-copy]
- always using `copy.deepcopy`, even when sharing the nested object is a deliberate choice.

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

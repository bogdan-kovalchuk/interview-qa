---
id: py-prac-0009
title: "Спроєктуйте copy operation для tree з shared subtrees та possible cycles, зберігши graph topology без aliasing з original."
description: "Використати memo-dict, ключований за id() оригінального вузла: перед рекурсивним копіюванням перевіряти, чи вузол вже скопійований, і повертати існуючу копію."
track: python
section: practical-coding
level: senior
type: practical
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-time-time-monotonic
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html#time.monotonic
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L294-L341
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Використати memo-dict, ключований за `id()` оригінального вузла: перед рекурсивним копіюванням перевіряти, чи вузол вже скопійований, і повертати існуючу копію.**[^py314-tutorial]

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

Memo гарантує: shared subtree копіюється один раз (ідентичність зберігається в копії), а cycle не викликає нескінченну рекурсію, бо `memo[nid]` заповнюється до рекурсивного спуску.

## Detailed explanation

TODO

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

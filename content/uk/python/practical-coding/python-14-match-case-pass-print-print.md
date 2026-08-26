---
id: py-prac-0004
title: "У Python 3.14 що надрукує `match 1:   case x: pass print(x)` і як capture pattern впливає на scope імені?"
description: "Надрукує 1 – bare name у case є capture pattern і прив'язує subject до імені x."
track: python
section: practical-coding
level: middle
type: pitfall
tags: [match-1-nbsp-nbsp-case-x-passprint-x]
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
---

## Short answer

**Надрукує `1` – bare name у `case` є capture pattern і прив'язує subject до імені `x`.**[^py314-tutorial] На відміну від звичайних блоків, `match/case` не створює окремого scope: змінна `x`, оголошена в `case x:`, залишається доступною після всього `match`. <span class="warn">Щоб збігтися з літералом, потрібен dotted name (наприклад, `case Color.RED`); bare name завжди є capture.</span>

## Detailed explanation

TODO

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

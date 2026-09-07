---
id: emb-cppfound-0035
title: "Trap: `int *p = NULL; if(p) *p = 5;` vs `int *p = NULL; *p = 5;` – is the first safe?"
description: "A NULL check before dereference is safe, but it does not protect against dangling or wild pointers that are non-null yet invalid."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**The first is safe**. `if(p)` ≡ `if(p != NULL)` – a check before dereferencing. If `p == NULL` -> the condition is false, `*p` is not executed.

<span class="warn">The second is undefined behavior</span>: `*p = 5` when `p == NULL` -> HardFault on Cortex-M.

However: a NULL check does not protect against a dangling pointer or a wild pointer – they are non-null but invalid; a NULL check is necessary but not sufficient for safety.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

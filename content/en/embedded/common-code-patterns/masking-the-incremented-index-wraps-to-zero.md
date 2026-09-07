---
id: emb-patterns-0036
title: "What does this return and why?"
description: "next == 0 means wraparound to the start of the buffer."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Question code

```c
#define RB_SIZE 8
#define RB_MASK (RB_SIZE - 1)
uint16_t head = 7;
uint16_t next = (head + 1) & RB_MASK;
```

## Short answer

**`next == 0`** – wraparound to the start of the buffer.

`(7 + 1) & 7 = 8 & 0b0111 = 0`. The `SIZE-1` mask = `0b0111` clears the overflow bit, so the index wraps around without `%` or `if`.

Rule: this trick works only when `SIZE` is a power of two.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

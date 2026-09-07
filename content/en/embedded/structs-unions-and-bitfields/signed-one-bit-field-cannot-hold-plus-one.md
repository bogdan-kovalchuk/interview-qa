---
id: emb-structs-0022
title: "Trap: why is a one-bit signed bit-field almost always a trap?"
description: "A 1-bit signed field cannot represent +1 in the two's complement model."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
struct F {
    signed int flag : 1;
};
```

## Short answer

<span class="warn">A 1-bit signed field cannot represent the value `+1` in the two's complement model.</span>

The typical range for a signed 1-bit is `-1` and `0`. If you expect a boolean `0/1`, reading after assigning `flag = 1` may yield `-1`. This breaks comparisons like `flag == 1`.

Defence: for flags use `unsigned int flag : 1` or `bool` where layout is not critical.[^embeddedinterviewlab]

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

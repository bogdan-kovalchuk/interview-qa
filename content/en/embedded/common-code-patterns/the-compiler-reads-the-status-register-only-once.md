---
id: emb-patterns-0025
title: "Trap: why does this polling loop become endless without `volatile`?"
description: "The compiler reads SR once and never re-reads it because nothing in the C abstract machine changes SR"
track: embedded
section: common-code-patterns
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
while (!(REG->SR & FLAG))
    ;
```

## Short answer

<span class="warn">The compiler reads `SR` once, sees the flag is not set, and never re-reads it</span> – in the C abstract machine nothing changes `SR`.

Result: the loop spins on the cached value forever, even after the hardware has already set the flag.

Defense: declare the register `volatile` – then `SR` is re-read on every iteration.[^embeddedinterviewlab]

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

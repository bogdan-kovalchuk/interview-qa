---
id: emb-volconst-0005
title: "What can happen to this loop without `volatile`?"
description: "The compiler can turn the loop into an infinite one because the flag never changes within the visible code."
track: embedded
section: volatile-and-const
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
uint8_t flag = 0;

while (flag == 0) {
    /* flag встановлює ISR */
}
```

## Short answer

The compiler can turn the loop into an <span class="warn">infinite</span> one because `flag` never changes within the visible code.

At `-O2` it is allowed to read `flag` once, keep the value in a CPU register, and never re-read RAM. The ISR will physically change the byte in memory, but the main loop may never see it.

Mitigation: declare the flag as `volatile uint8_t flag`. If the flag is wider than the platform atomic access or there are more complex invariants, add a critical section or an atomic API.[^embeddedinterviewlab]

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

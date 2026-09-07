---
id: emb-volconst-0034
title: "Trap: what is wrong with this delay loop?"
description: "The compiler can remove an empty loop entirely because it has no observable side effects."
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
for (uint32_t i = 0; i < 100000; ++i) {
}
```

## Short answer

<span class="warn">The compiler can remove an empty loop entirely</span> because it has no observable side effects.

Adding `volatile` to the counter sometimes forces the increments to execute, but this is a poor basis for accurate timing: optimization level, CPU frequency, wait states, and pipeline all change the real delay.

Protection: for delays, use a hardware timer, SysTick, DWT cycle counter, or RTOS delay. `volatile` is not a timing API.[^embeddedinterviewlab]

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

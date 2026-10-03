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
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
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

<span class="warn">The compiler can remove an empty loop entirely</span> because it has no observable side effects.[^iso-c-n1570]

Adding `volatile` to the counter sometimes forces the increments to execute, but this is a poor basis for accurate timing: optimization level, CPU frequency, wait states, and pipeline all change the real delay.

Protection: for delays, use a hardware timer, SysTick, DWT cycle counter, or RTOS delay. `volatile` is not a timing API.[^iso-c-n1570]

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

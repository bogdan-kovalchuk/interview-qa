---
id: emb-patterns-0012
title: "Why is a ring buffer sized to a power of two?"
description: "A power-of-two size replaces modulo with a single AND instruction, avoiding expensive division."
track: embedded
section: common-code-patterns
level: junior
type: concept
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
  - source_id: arm-divide
    title: "Arm: Divide and Conquer"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/divide-and-conquer
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Confirms Cortex-M0 lacks hardware divide instructions and that `%` cost depends on implementation; it gives no fixed speedup ratio."
---

## Question code

```c
#define RB_SIZE 64
#define RB_MASK (RB_SIZE - 1)
```

## Short answer

**For a power-of-two `SIZE`, `(index + 1) & MASK` performs the same wrap; speed depends on the target and compiler.**

Cortex-M0 has no hardware divide instructions, but the cost of `%` and any speedup depend on generated code and the operation. A power of two allows replacing the remainder operation with a bit mask.

In the shown macros, `RB_SIZE` is 64 and `RB_MASK` is 63. Check the power-of-two condition and index range, and measure performance on the target build.[^arm-divide]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

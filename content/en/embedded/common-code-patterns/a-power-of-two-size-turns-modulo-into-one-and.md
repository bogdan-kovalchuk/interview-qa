---
id: emb-patterns-0012
title: "Why is a ring buffer sized to a power of two?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-divide
    title: "Arm: Divide and Conquer"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/divide-and-conquer
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

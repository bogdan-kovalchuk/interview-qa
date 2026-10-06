---
id: emb-patterns-0036
title: "What value does `next` get, and why?"
description: "next == 0 means wraparound to the start of the buffer."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Supports integer promotions (6.3.1.1), bitwise AND (6.5.10) and modular unsigned arithmetic (6.2.5, paragraph 9); says nothing about specific devices or toolchains."
  - source_id: linux-circular-buffers
    title: "Circular Buffers (The Linux Kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Confirms that for a power-of-two circular buffer a bitwise AND replaces the modulus (division), that the index wraps with `(head + 1) & (size - 1)`, and that the buffer is full when `head` is one less than `tail`. This is Linux kernel documentation, not an MCU specification."
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

`(7 + 1) & 7 = 8 & 0b0111 = 0`: the `SIZE-1` mask = `0b0111` keeps only the low three bits, so bit `0b1000` is discarded and the index wraps around without `%` or `if`.[^linux-circular-buffers][^iso-c-n1570]

Rule: this trick works only when `SIZE` is a power of two.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

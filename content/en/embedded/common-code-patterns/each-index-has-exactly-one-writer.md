---
id: emb-patterns-0041
title: "Which shared invariant makes an SPSC ring buffer safe without locks?"
description: "Each index has exactly one writer: the producer writes only head, the consumer writes only tail."
track: embedded
section: common-code-patterns
level: junior
type: concept
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
    applicability: "Confirms that a data race on non-atomic objects is undefined behavior (5.1.2.4 para. 25), that `volatile` only requires accesses to follow the abstract machine (6.7.3 para. 7), and describes _Atomic, memory_order (7.17.3) and atomic_signal_fence (7.17.4.2); the choice of primitives for a particular MCU depends on the toolchain."
  - source_id: linux-circular-buffers
    title: "Circular Buffers (Linux kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
    accessed: 2026-10-06
    kind: official
    version: "7.3.0-rc6"
    applicability: "Describes the lock-free scheme with one producer and one consumer, the mask for a power-of-two buffer size, the always-empty slot, and release/acquire ordering of data and index writes. It is Linux kernel (SMP) documentation, not bare-metal MCU documentation: the idea transfers, the specific macros and barriers do not."
---

## Short answer

**Each index has exactly one writer: the producer writes only `head`, the consumer – only `tail`.**

Since there is no shared variable modified by both sides (like `count`), there is no read-modify-write race either.[^linux-circular-buffers] Each side only reads the other's index; that is safe only if the access is atomic and ordered against the buffer data (release/acquire or a barrier), not merely `volatile`.[^iso-c-n1570]

Rule: "one writer per variable" is the basis of lock-free SPSC (single-producer / single-consumer) queues, but only for exactly one producer and one consumer.[^linux-circular-buffers]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

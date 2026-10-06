---
id: emb-patterns-0035
title: "Why does the ISR write the slot before advancing `head`?"
description: "So the consumer never sees an advanced head pointing at a byte not yet written."
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
    applicability: "Supports the release/acquire semantics of atomic operations (5.1.2.4, 7.17.3) and the rules for ordinary and volatile accesses (5.1.2.3); says nothing about interrupts, hardware cores or specific devices."
  - source_id: linux-circular-buffers
    title: "Circular Buffers (The Linux Kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Describes the single-producer/single-consumer protocol: the item is written before `head` is published with a release store, the consumer reads `head` with an acquire load and frees the slot through `tail`; this is Linux kernel documentation, so for an MCU it is a model of the protocol, not a specification."
  - source_id: gcc-volatiles
    title: "GCC 16.1.0: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Volatiles.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Confirms that accesses to non-volatile objects are not ordered with respect to volatile accesses and that a volatile object cannot serve as a memory barrier; does not cover hardware ordering between cores."
---

## Short answer

**To ensure the consumer never sees an advanced `head` pointing at a byte not yet written.**

`head` publishes the record: the consumer treats every slot before it as ready, so the data must be written and visible first. This matters when the consumer can run "in the middle" (another core, a nested interrupt, a preempted task) and against compiler or CPU reordering – so publish `head` with a release store and read it with an acquire load.[^linux-circular-buffers][^iso-c-n1570]

Rule: producer: data -> `head`; consumer: data -> `tail`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-patterns-0007
title: "What is an SPSC ring buffer, and when can it operate without a lock?"
description: "An SPSC ring buffer can operate without a mutex when indices are atomic and the platform provides the required access ordering."
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
  - source_id: linux-circular-buffers
    title: "Linux kernel documentation: Circular Buffers"
    url: https://docs.kernel.org/core-api/circular-buffers.html
    accessed: 2026-10-04
    kind: official
    version: current
    applicability: "Describes SPSC, head/tail indices, and acquire/release/barrier ordering; Linux details do not automatically transfer to an MCU or ISR."
---

## Short answer

**An SPSC (single-producer / single-consumer) ring buffer** can avoid a mutex when indices are atomic and the platform provides the required ordering for publishing data. A single writer per index is not enough.[^linux-circular-buffers]

One typical arrangement has an ISR (interrupt service routine), such as UART RX (universal asynchronous receiver-transmitter receive), as producer and the main loop as consumer. `head` and `tail` have separate owners, but atomic access and ordering depend on the platform.[^linux-circular-buffers]

It suits streaming data with defined full/empty behaviour; check platform guarantees before using it.[^linux-circular-buffers]

## Detailed explanation

TODO

## Sources
<!-- generated from frontmatter -->

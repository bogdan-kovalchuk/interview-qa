---
id: emb-patterns-0007
title: "What is an SPSC lock-free ring buffer and what is it for?"
description: "SPSC ring buffer, safe without disabling interrupts when each index has one writer and is accessed atomically."
track: embedded
section: common-code-patterns
level: junior
type: concept
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

## Short answer

**SPSC (single-producer / single-consumer) ring buffer**, safe without disabling interrupts provided each index has a single writer and is read/written atomically for that MCU (microcontroller unit).

Typically: producer is the ISR (interrupt service routine), for example UART RX (universal asynchronous receiver-transmitter receive), consumer is the main loop. `head` and `tail` are each updated by their own side, so there is no shared read-modify-write.

Rule: SPSC ring buffer is the standard for UART RX/TX (receive/transmit), ADC (analog-to-digital converter) sample queues and logging; always static allocation, no `malloc`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

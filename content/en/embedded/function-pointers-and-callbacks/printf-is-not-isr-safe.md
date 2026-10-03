---
id: emb-fnptr-0027
title: "Trap: what is unsafe about calling `printf` from an ISR callback?"
description: "printf is usually not ISR-safe and may be blocking or reentrant-unsafe."
track: embedded
section: function-pointers-and-callbacks
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
  - source_id: newlib-stdio
    title: "The Red Hat newlib C Library: Standard C library I/O and reentrancy"
    url: https://www.sourceware.org/newlib/libc.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Shows stdio's dependence on stream state, reentrancy, and system support in Newlib; it does not guarantee behaviour of other C libraries or backends."
  - source_id: arm-interrupt-latency
    title: "Arm: A Beginner’s Guide on Interrupt Latency"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/beginner-guide-on-interrupt-latency-and-interrupt-latency-of-the-arm-cortex-m-processors
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Explains interrupt latency and interrupt handling on Cortex-M; priority and nesting details depend on the specific core and MCU."
---

## Short answer

<span class="warn">Do not assume `printf` is ISR-safe without a guarantee from the specific libc and output backend.</span>

Depending on the libc and backend, `printf` may use stream state or a lock, or wait for UART transmission to finish. Re-entry while main code or a task is printing can corrupt or interleave output and keep the ISR busy.

Protection: in the ISR callback save a compact record to a buffer or set a flag, then print in task or main context; use a dedicated backend only if its ISR safety is documented.[^embeddedinterviewlab] [^newlib-stdio]

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

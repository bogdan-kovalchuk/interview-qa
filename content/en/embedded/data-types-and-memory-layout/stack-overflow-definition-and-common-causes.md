---
id: emb-dtypes-0029
title: "What is a stack overflow, and what causes it in embedded systems?"
description: "A stack overflow occurs when stack use exceeds its reserved bounds; causes include deep recursion and nested calls."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

Stack overflow occurs when the stack pointer leaves the reserved stack region; consequences depend on the memory map and protection and can include data corruption or a fault.[^iso-c-n1570]

Causes:
1. **Large local arrays**: `uint8_t buf[2048]` on the stack;
2. Deep recursion;
3. Nested ISRs and interrupt context saving (the amount depends on architecture and configuration);
4. Stack too small in the linker script.

Diagnostics: stack canaries, stack-usage analysis, MPU protection, or filling the stack with a pattern to estimate its high-water mark.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

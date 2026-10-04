---
id: emb-fnptr-0058
title: "What should a good interview answer about embedded callbacks contain?"
description: "Mechanism, contract and risks."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**Mechanism, contract and risks.**

Mechanism: a function pointer with a concrete signature. Contract: who registers, who calls, when, with which context pointer and lifetime. Risks: null pointer, incompatible call signature (undefined behavior in C), ISR context, dangling context, reentrancy, blocking calls and dispatch index validation.[^iso-c-n1570]

Rule: a strong embedded answer does not stop at the syntax of `void (*cb)(void)`; it explains runtime ownership and execution context.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

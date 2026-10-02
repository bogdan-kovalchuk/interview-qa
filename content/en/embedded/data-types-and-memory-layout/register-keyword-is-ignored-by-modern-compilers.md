---
id: emb-dtypes-0079
title: "What does the `register` storage class mean, and does it still matter today?"
description: "In C, `register` does not guarantee CPU-register placement and forbids taking the address of the declared object."
track: embedded
section: data-types-and-memory-layout
level: junior
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
  - source_id: cpp17-register-removal
    title: "C++17 draft: Removal of register storage-class specifier"
    url: https://eel.is/c%2B%2Bdraft/diff.cpp14.dcl.dcl
    accessed: 2026-10-04
    kind: spec
    version: "C++17"
    applicability: "Supports the removal of the register specifier in C++17; it does not describe the C rule."
---

## Short answer

In C11, `register` is an obsolescent storage-class hint: it does not guarantee that an object is kept in a CPU register, and an implementation may ignore it.[^iso-c-n1570] In C, unary `&` cannot be applied to an object declared with `register`.[^iso-c-n1570] C++17 removed the `register` specifier; keep that rule distinct from C.[^cpp17-register-removal]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-structs-0035
title: "What is an opaque struct pointer in a C API?"
description: "An opaque pointer hides the struct definition from the API user; the header has only a forward declaration."
track: embedded
section: structs-unions-and-bitfields
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
---

## Short answer

An **opaque pointer** hides the struct definition from the API user: the header contains only a forward declaration.

For example, `typedef struct UartDriver UartDriver;`, while the fields of `struct UartDriver` are defined only in the `.c` file. The caller works with `UartDriver *` through API functions and does not depend on the internal layout.

This lets the implementation change its internal layout without exposing fields to clients; ABI compatibility still depends on the entire public interface.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

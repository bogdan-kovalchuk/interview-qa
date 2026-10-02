---
id: emb-dtypes-0089
title: "What is type punning, and when is it undefined behavior in C++?"
description: "In C, type punning through a union is accepted; in C++ only memcpy or std::bitcast is safe."
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

**Type punning** means interpreting an object’s bytes as another type. In C, reading a different `union` member has an implementation-defined result; accessing the same storage through an incompatible pointer can violate effective-type rules. In C++, reading an inactive `union` member is generally not a permitted conversion technique; for trivially copyable types use `memcpy` or C++20 `std::bit_cast`, and ensure the target representation is valid.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

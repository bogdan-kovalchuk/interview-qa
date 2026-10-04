---
id: emb-align-0033
title: "Why is `memcpy` safer than a typed-pointer cast for multi-byte access?"
description: "memcpy has no alignment requirement and does not violate strict aliasing."
track: embedded
section: memory-alignment-and-endianness
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

`memcpy` copies bytes without reading a value through a misaligned typed pointer or violating strict aliasing.[^iso-c-n1570] The destination must hold `n` bytes, and later reading it as `T` requires a properly aligned `T` object; copying does not convert byte order.[^iso-c-n1570] Optimization depends on the compiler and target, so C guarantees neither particular instructions nor a speed advantage.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

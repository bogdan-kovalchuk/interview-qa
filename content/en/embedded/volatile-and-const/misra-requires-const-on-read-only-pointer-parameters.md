---
id: emb-volconst-0029
title: "What is the MISRA approach to `const` for pointer parameters?"
description: "A pointer parameter should point to a const-qualified type if the function does not modify the pointed-to object."
track: embedded
section: volatile-and-const
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
  - source_id: mathworks-misra-813
    title: "MISRA C:2012 Rule 8.13 – A pointer should point to a const-qualified type whenever possible"
    url: https://www.mathworks.com/help/bugfinder/ref/misrac2012rule8.13.html
    accessed: 2026-10-04
    kind: community
    version: "R2026b"
    applicability: "Reports the wording, rationale, and advisory status of Rule 8.13; this is tool documentation, not the full normative MISRA text."
---

## Short answer

**MISRA C:2012 Rule 8.13 says a pointer should point to a const-qualified type whenever possible; it is an advisory recommendation.**

This is a recommendation, not a mandatory requirement: it discourages giving a function unnecessary permission to modify an object and lets a static analyzer flag pointer parameters that could be `const`-qualified.[^mathworks-misra-813]

Practical rule: for a parser that only reads a frame, use `void parse(const uint8_t *frame, size_t len)`. Deviate when the function genuinely needs to modify the object or there is another justified reason.[^mathworks-misra-813] [^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-fnptr-0021
title: "Why can a dispatch table be better than a large `switch`?"
description: "It separates the opcode-to-handler mapping from handler logic and simplifies adding commands."
track: embedded
section: function-pointers-and-callbacks
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**It stores the opcode -> handler mapping separately from handler implementations** and can simplify adding commands.

In a protocol parser, the table can collect handler selection in one place while each function implements a separate command. This is a structural benefit, not a guarantee of smaller code or faster execution.

For a few branches, `switch` is often easier to read; a table fits when the mapping is data or the command set grows. Measure performance instead of inferring it from syntax.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

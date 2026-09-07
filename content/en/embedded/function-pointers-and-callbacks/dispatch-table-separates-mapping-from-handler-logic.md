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

**It separates the opcode -> handler mapping from handler logic** and simplifies adding commands.

In an embedded protocol parser this can reduce cyclomatic complexity and allow storing the table in Flash as `static const`. But indirect calls can be less transparent to the optimizer and harder for static analysis.

Rule: a dispatch table is good for stable opcode maps; for a small switch with 3–5 cases a plain `switch` is often more readable.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

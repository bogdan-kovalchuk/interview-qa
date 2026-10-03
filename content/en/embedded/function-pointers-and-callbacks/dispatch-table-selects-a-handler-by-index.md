---
id: emb-fnptr-0018
title: "What is a dispatch table of function pointers?"
description: "A dispatch table is an array of function pointers where an index or opcode selects the function to call."
track: embedded
section: function-pointers-and-callbacks
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

**A dispatch table** is an array of function pointers where an index or opcode selects the function to call.

For example, a command parser can have `cmd_handler_t table[256]`, where `table[opcode](ctx, frame)` handles the command. This eliminates a large `switch`, but requires bounds checking and a default handler.

Embedded use cases: CLI commands, protocol opcodes, state machine actions, test command handlers.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-fnptr-0005
title: "Why do callback APIs often carry a `void *context` parameter?"
description: "context passes the callback user state without global variables."
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

**`context` gives a callback access to state for a particular instance.**

A C function pointer and a data pointer are distinct types; `void *` here carries the address of an object, such as a state structure, rather than the address of the callback function.[^iso-c-n1570]

The driver stores the callback with that data pointer and passes it when invoking the callback. The same callback code can then serve several independent devices without separate global variables.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

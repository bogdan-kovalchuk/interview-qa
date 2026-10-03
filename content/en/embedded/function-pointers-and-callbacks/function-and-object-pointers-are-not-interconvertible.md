---
id: emb-fnptr-0049
title: "Trap: why should you not store a function pointer in `void *`?"
description: "ISO C guarantees conversion between void * and object pointers, but defines no equivalent rule for function pointers."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
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

<span class="warn">C does not guarantee portable conversion between a function pointer and the object pointer `void *`.</span>

Representations and sizes of pointer categories are implementation-dependent; ISO C defines conversion between `void *` and object pointers, but specifies no equivalent general rule for function pointers. POSIX has separate requirements for `dlsym`, but that is not a general ISO C rule or an embedded guarantee.[^iso-c-n1570]

Defence: keep function pointers in function pointer types and data pointers in `void *`. Do not put a callback address into a generic data pointer field.[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

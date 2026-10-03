---
id: emb-fnptr-0036
title: "Trap: can a callback be an ordinary nested function in standard C?"
description: "No; standard C has no nested functions."
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
  - source_id: gcc-nested-functions
    title: "GCC documentation: Nested Functions"
    url: https://gcc.gnu.org/onlinedocs/gcc/Nested-Functions.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents GNU C as an extension, trampolines, and address lifetime limits; it does not describe ISO C."
---

## Short answer

<span class="warn">No. ISO C does not define nested functions; GCC provides them as a GNU C extension.</span> [^iso-c-n1570] [^gcc-nested-functions]

GCC implements taking a nested function's address with trampolines; the address also becomes unsafe after the containing function exits.[^gcc-nested-functions]

Protection: use a file-scope `static` function and `void *context`; this keeps the callback independent of a GNU extension.[^iso-c-n1570]

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

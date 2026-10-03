---
id: emb-volconst-0027
title: "Trap: does a local `const` array always live in Flash?"
description: "No; const forbids writes through the identifier, but storage placement depends on storage duration, ABI, optimization, and the linker script."
track: embedded
section: volatile-and-const
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
  - source_id: avr-libc-program-space
    title: "AVR-LibC: Data in Program Space"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual/pgmspace.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "AVR-GCC and AVR linker-script example: const does not determine physical placement, and Flash access depends on architecture and linker script."
---

## Short answer

<span class="warn">No, not always.</span>

`const` forbids modification through that identifier, but does not determine physical placement. A local automatic `const` object may require stack storage or be optimized away; file-scope or `static const` objects commonly go into a read-only section, but not necessarily Flash.

For a large immutable LUT, use `static const` or file-scope `const`, then check the map file for its actual placement.[^avr-libc-program-space]

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

---
id: emb-volconst-0048
title: "Trap: why does \"works in debug, breaks in release\" often point at a missing `volatile`?"
description: "A debug build typically uses -O0, while a release build enables optimizations."
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
---

## Short answer

<span class="warn">A debug/release difference can expose missing `volatile`, but the configuration name alone proves nothing.</span>

Different optimization flags can change generated code, and a register access without `volatile` may not be reread as the program expects. However, `-O0` does not guarantee the required ordering, and `-O2` does not necessarily cache every value; behaviour depends on the code and compiler.[^iso-c-n1570]

If peripheral polling returns stale data, check register pointer types and MCU access requirements; `volatile` is needed for applicable memory-mapped registers, but does not solve every concurrency or ordering problem.[^iso-c-n1570]

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

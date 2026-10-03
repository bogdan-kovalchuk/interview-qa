---
id: emb-volconst-0054
title: "Which type is better for an ISR flag: `volatile bool` or `bool`?"
description: "For a flag written by an ISR and read by the main loop, volatile is often needed, for example static volatile bool button_pressed."
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
---

## Short answer

For a flag changed by an ISR and checked by the main loop, `volatile` is often required by the specific compiler and MCU rules, for example `static volatile bool button_pressed;`.[^iso-c-n1570]

Without the relevant guarantee, the compiler may not repeat the access. `volatile` does not guarantee atomicity: the MCU and compiler must specify that the type can be read and written atomically. C does not guarantee this universally.[^iso-c-n1570]

Rule: use the platform-defined volatile access for an ISR flag and verify its atomicity; complex state needs a synchronization protocol.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

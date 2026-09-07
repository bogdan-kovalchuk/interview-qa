---
id: emb-volconst-0054
title: "Which type is better for an ISR flag: `volatile bool` or `bool`?"
description: "For a flag written by an ISR and read by the main loop, volatile is needed, for example static volatile bool buttonpressed."
track: embedded
section: volatile-and-const
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

For a flag written by an ISR and read by the main loop, `volatile` is needed: for example `static volatile bool button_pressed;`.

Without `volatile` the main loop may not reload the flag from memory. But the type itself must also be readable and writable atomically on the target platform. For simple Cortex-M byte/word flags this is usually fine, but it depends on the access and alignment.

Rule: simple ISR flag = volatile + a simple atomic type; complex state = critical section or queue/event mechanism.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

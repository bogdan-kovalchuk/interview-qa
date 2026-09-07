---
id: emb-patterns-0035
title: "Why does the ISR write the slot before advancing `head`?"
description: "So the consumer never sees an advanced head pointing at a byte not yet written."
track: embedded
section: common-code-patterns
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

**To ensure the consumer never sees an advanced `head` pointing at a byte not yet written.**

If `head` were incremented first and data written afterwards, an interrupt or reschedule between those two steps would let the consumer read garbage. Updating the index is always the producer's last action. ISR here means interrupt service routine.

Rule: producer: data -> `head`; consumer: data -> `tail` – the index publishes the record only once the data is ready.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

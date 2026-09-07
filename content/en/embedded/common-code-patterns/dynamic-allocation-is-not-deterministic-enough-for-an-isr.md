---
id: emb-patterns-0030
title: "Trap: why can `malloc` not be used for a ring buffer?"
description: "Dynamic memory is non-deterministic and fragments, unacceptable for real-time and ISR contexts"
track: embedded
section: common-code-patterns
level: junior
type: pitfall
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

<span class="warn">Dynamic memory is non-deterministic and fragments</span> – unacceptable for a real-time or ISR context.

A ring buffer often lives for the entire system lifetime and is used from interrupts, where `malloc` is forbidden (non-reentrant, may block). The size is known in advance.

Defense: always use static allocation of a fixed power-of-two size.[^embeddedinterviewlab]

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

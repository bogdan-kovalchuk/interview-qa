---
id: emb-patterns-0030
title: "Why can `malloc` be unsuitable for a ring buffer used in an ISR?"
description: "Runtime allocation can have variable latency; an ISR commonly uses a buffer allocated in advance."
track: embedded
section: common-code-patterns
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

<span class="warn">`malloc` can have variable latency, so its suitability in an ISR depends on the allocator and platform contract.</span>

C does not impose a universal ban on calling `malloc` from an ISR. In a system with a hard timing budget, preallocate the buffer unless the allocator guarantees bounded latency and safe use in that context.[^iso-c-n1570]

A power-of-two size is needed only to optimize index wrapping with a mask, not for every ring buffer.

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

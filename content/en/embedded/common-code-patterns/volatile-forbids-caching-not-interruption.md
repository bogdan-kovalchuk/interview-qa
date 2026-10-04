---
id: emb-patterns-0031
title: "Why is `volatile` not enough for a safe `count++` between an ISR and main?"
description: "`volatile` requires accesses to volatile objects under C rules but does not make `count++` atomic."
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

<span class="warn">`volatile` does not make `count++` atomic or synchronize an ISR with main.</span>

Increment is a read-modify-write: an interrupt between the read and write can lose an update. `volatile` affects accesses to volatile objects under the implementation's rules, but does not guarantee atomicity or inter-context ordering; ISR interaction rules depend on the implementation.[^iso-c-n1570]

Use a documented atomic type or a short critical section supported by the target platform; `volatile` alone is not enough.[^iso-c-n1570]

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

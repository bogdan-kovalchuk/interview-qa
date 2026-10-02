---
id: emb-dtypes-0044
title: "What is a stack canary, and how does it guard against stack overflow?"
description: "A stack canary is a magic value placed before the return address; if it changes on exit, a stack overflow occurred."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: gcc-stack-protector
    title: "GCC instrumentation options: stack protection"
    url: https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "GCC stack protector flags, instrumentation conditions, guard checking, and failure handling; details depend on target and runtime."
---

## Short answer

A stack canary is a guard value that the compiler places in some function frames and checks before returning; its exact placement depends on the ABI and implementation.[^gcc-stack-protector]

If the check detects a change, the runtime takes a failure path; this indicates damage to a protected frame but does not prove that stack overflow was the cause.[^gcc-stack-protector]

GCC can enable protection with `-fstack-protector-strong`; bare-metal requires a compatible runtime and failure handler.[^gcc-stack-protector]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

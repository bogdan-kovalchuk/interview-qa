---
id: emb-dtypes-0067
title: "What does `-fstack-usage` do in GCC, and how do you read its output?"
description: "-fstack-usage emits .su files with file:line:col:function bytes type lines for stack-frame analysis."
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
  - source_id: gcc-stack-usage
    title: "GCC: Developer Options, -fstack-usage"
    url: https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Defines .su record fields and static, dynamic, bounded qualifiers; per-function figures are not the maximum for a complete call chain."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

GCC `-fstack-usage` writes per-function use to a `.su` file named from `auxname`.[^gcc-stack-usage] Each tab-separated record gives function and source location, mangled name, bytes, and qualifier: `static` is fixed, `dynamic` is variable, and `dynamic,bounded` has a known upper bound.[^gcc-stack-usage]

Without `bounded`, the byte count is not a maximum. Use the call graph because the largest frame is not the nested-call peak; include interrupts, recursion, RTOS tasks, and libraries. `-Wstack-usage=256` is a warning threshold, not proof of sufficient stack.[^gcc-stack-usage]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

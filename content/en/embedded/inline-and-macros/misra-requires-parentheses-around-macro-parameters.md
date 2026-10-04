---
id: emb-macros-0020
title: "What does MISRA C Rule 20.7 require and why?"
description: "MISRA C Rule 20.7 requires parenthesizing expressions resulting from macro parameter expansion."
track: embedded
section: inline-and-macros
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
  - source_id: misra-rule-20-7-reference
    title: "MathWorks Polyspace: MISRA C:2012 Rule 20.7"
    url: https://www.mathworks.com/help/bugfinder/ref/misrac2012rule20.7.html
    accessed: 2026-10-04
    kind: official
    version: "R2026b"
    applicability: "Provides the wording of Rule 20.7 and an operator-precedence example; this is checker documentation, not the full normative MISRA text."
---

## Short answer

**MISRA C Rule 20.7 requires expressions resulting from macro parameter expansion to be parenthesized** to avoid operator precedence errors.

For example, `#define ADD(a,b) a+b` should be rewritten as `#define ADD(a,b) ((a) + (b))`. Otherwise `ADD(1,2) * 3` expands to `1 + 2 * 3`, grouping the expression differently.[^misra-rule-20-7-reference]

Rule 20.7 addresses parentheses in the resulting expression; it is not a general recommendation to use macros instead of functions.[^misra-rule-20-7-reference]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

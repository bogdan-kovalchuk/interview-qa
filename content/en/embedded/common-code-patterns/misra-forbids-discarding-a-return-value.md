---
id: emb-patterns-0022
title: "What does MISRA C require when code does not use a function's return value?"
description: "MISRA C Rule 17.7 requires using a value returned by a non-void function, except for an explicit cast to void."
track: embedded
section: common-code-patterns
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
  - source_id: misra-c-2023-rule-17-7
    title: "MISRA C:2023 Addendum 2"
    url: https://misra.org.uk/app/uploads/2024/10/MISRA-C-2023-ADD2.pdf
    accessed: 2026-10-04
    kind: official
    version: "2023 Addendum 2"
    applicability: "The official change summary confirms R.17.7's status; the exact rule wording is in the licensed full MISRA C:2023 standard."
---

## Short answer

**MISRA C Rule 17.7 requires using a non-void function's value or explicitly discarding it with a cast to `void`.** This does not mean every function that can fail must return an error code.[^misra-c-2023-rule-17-7]

The rule concerns use of the returned value, not one required error-handling pattern: status may be returned separately, in a result structure, or the contract may establish that failure is impossible. The project must define and check the appropriate response to meaningful outcomes.

An explicit `(void)call()` marks deliberate discarding, but does not replace risk analysis.[^misra-c-2023-rule-17-7]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

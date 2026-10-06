---
id: emb-patterns-0039
title: "Why do guard clauses speed up an audit of safety-critical code?"
description: "They make the function contract visible up front: null, range, state and permissions checked before the main logic."
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Supports that dereferencing a pointer with an invalid value, including a null pointer, is undefined behavior (6.5.3.2, paragraph 4); says nothing about check style or safety-standard requirements."
  - source_id: holzmann-power-of-ten
    title: "The Power of Ten – Rules for Developing Safety Critical Code (G. J. Holzmann, NASA/JPL)"
    url: https://spinroot.com/gerard/pdf/P10.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Paper by a NASA/JPL author, hosted on his site: rule 7 requires checking parameter validity inside each function, rule 5 describes assertions that can be disabled after testing, and the note to rule 1 admits that an early error return is often simpler than a single exit point. It is a guideline, not the requirement of a specific safety standard."
---

## Short answer

**Guard clauses move the input checks (null, range, state, permissions) into the first lines of the function, so the contract is visible at once and the main logic runs without nested `if`.**

A reviewer can more easily confirm that dangerous inputs are rejected before any side effect, and the JPL guidelines for safety-critical code require parameter validity to be checked inside each function.[^holzmann-power-of-ten] This does not prove correctness: a `NULL` check will not catch a bad non-null pointer, and a faster audit is a consequence of readability, not a guarantee.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-patterns-0022
title: "Why are return codes the default pattern in safety-critical code?"
description: "MISRA C requires return values not to be ignored and IEC 62304 requires a controlled software fault handling process"
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

**MISRA C (Motor Industry Software Reliability Association C) requires that return values not be ignored, and IEC 62304 requires a controlled process for handling software faults.**

Return codes force the caller to inspect the result, whereas a sentinel or a silent failure is easy to ignore. This makes errors visible in an audit.

Rule: in certified systems every call that can fail returns a defined code, and every code is checked.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

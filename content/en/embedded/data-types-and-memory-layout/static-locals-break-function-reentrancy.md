---
id: emb-dtypes-0057
title: "What is a reentrant function, and why do `static` locals break reentrancy?"
description: "A static local is shared across all calls, so an ISR and the main loop racing through it causes a data race."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
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
  - source_id: strtok-r-manpages
    title: "strtok_r(3) Linux man-pages"
    url: https://manpages.debian.org/testing/manpages-dev/strtok_r.3.en.html
    accessed: 2026-10-04
    kind: official
    version: "POSIX.1-2008"
    applicability: "Describes the reentrant POSIX strtok_r function and saveptr argument; does not guarantee availability in ISO C or every embedded libc."
---

## Short answer

**A reentrant function** can be called again before an earlier call finishes if each call has independent state or shared state is properly protected. A `static` local is shared across calls, but its presence alone does not make a function unsafe; conflicting access to mutable state is the issue.[^iso-c-n1570]

If an ISR reenters the function, both invocations may use the same static value. `strtok()` retains state between calls; POSIX `strtok_r()` takes a separate `saveptr`.[^iso-c-n1570][^strtok-r-manpages]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

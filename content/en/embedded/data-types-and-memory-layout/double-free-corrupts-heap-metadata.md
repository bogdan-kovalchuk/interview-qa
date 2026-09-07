---
id: emb-dtypes-0056
title: "Trap: what happens? `free(ptr); free(ptr);`"
description: "A double free is undefined behavior that corrupts heap metadata and can open a security exploit."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

<span class="warn">Double free -> undefined behavior.</span> Consequences:
1. Corrupt heap metadata -> crash at the next `malloc`/`free`;
2. <span class="warn">Security exploit</span>: heap-based buffer overflow, use-after-free;
3. Silent data corruption.

Protection: always after `free`: `ptr = NULL;`. `free(NULL)` is a safe no-op.

In RTOS/embedded: heap corruption often manifests far from the error location.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

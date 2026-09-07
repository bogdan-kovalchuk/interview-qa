---
id: emb-dtypes-0080
title: "Find the bug: `char* get_name(void) { char buf[32] = \"test\"; return buf; }`"
description: "buf is destroyed on return, so the function returns a dangling pointer into invalid stack memory."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

<span class="warn">Returning a pointer to a local array -> undefined behavior.</span> `buf[32]` is on the stack, destroyed after return.

The caller gets a dangling pointer – a pointer to already invalid memory. Reading it -> garbage or crash.

Solutions:
1. `static char buf[32];` (but not reentrant);
2. Pass the buffer as a parameter: `void get_name(char *buf, size_t len);`
3. `malloc` + document that the caller must `free`.

GCC: `warning: function returns address of local variable`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

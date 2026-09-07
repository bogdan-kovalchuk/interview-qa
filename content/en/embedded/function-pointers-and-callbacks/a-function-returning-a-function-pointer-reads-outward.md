---
id: emb-fnptr-0048
title: "How do you declare a function that returns a function pointer?"
description: "Without typedef: int (selectop(int id))(int, int); with typedef it is far more readable."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
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

Example without typedef:

`int (*select_op(int id))(int, int);`

This means: `select_op` takes an `int` and returns a pointer to a function that takes two `int` values and returns an `int`. With a typedef it is cleaner: `typedef int (*op_t)(int, int); op_t select_op(int id);`

Rule: if a declaration is hard to read at first glance, typedef is the right engineering choice.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

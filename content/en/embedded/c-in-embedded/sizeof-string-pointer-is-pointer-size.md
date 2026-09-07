---
id: emb-cppfound-0048
title: "What does this return on 32-bit?"
description: "Why sizeof on a string pointer returns the pointer size."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 4
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Question code

```c
char *p = "hello";
printf("%zu", sizeof(p));
```

## Short answer

**4** (on 64-bit – 8).

`p` is a pointer of type `char*`, so `sizeof(p) = sizeof(char*) = 4` on 32-bit. Not the string length, not 6 (with '\0'), but only the pointer size.

For the string length: `strlen(p) + 1` = 6 (with null terminator) or `strlen(p)` = 5.

Compare: `char arr[] = "hello"; sizeof(arr) = 6` – here it is an array, not a pointer.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

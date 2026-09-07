---
id: emb-cppfound-0100
title: "Trap: where is the error?"
description: "Why allocating five bytes is insufficient for the string hello and its terminator."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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
char *p = malloc(5);
strcpy(p, "hello");
p[5] = '\0';
```

## Short answer

<span class="warn">Buffer overflow.</span> `malloc(5)` – 5 bytes, but `"hello"` = `{'h','e','l','l','o','\0'}` – 6 bytes including the null terminator.

`strcpy(p, "hello")` already overflows the buffer (6 bytes into 5), and `p[5] = '\0'` is a sixth write past the end.

Correct: `malloc(strlen("hello") + 1)` = `malloc(6)`, or `strncpy(p, "hello", 5); p[4]='\0';` – truncate if needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

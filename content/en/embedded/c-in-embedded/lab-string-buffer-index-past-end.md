---
id: emb-cppfound-0076
title: "What is wrong with this code?"
description: "Why writing at the first index after a string buffer is a buffer overflow."
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
    applicability: "Source question and answer; answer not independently verified."
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
char buf[4]="abc";
buf[4]='\0';
```

## Short answer

<span class="warn">Buffer overflow!</span> `char buf[4] = "abc"` -> `buf = {'a','b','c','\0'}` – the array has 4 elements, indices 0..3, so `buf[4]` is the fifth element, outside the array. Another issue: `"abc"` already has '\0' at position 3 – the null-terminator is already there, so the string is valid. If `char buf[3] = "abc"` – the compiler warns or stores 'a','b','c' without '\0' (truncation); always make buffer size > string length + 1.[^embeddedinterviewlab]

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

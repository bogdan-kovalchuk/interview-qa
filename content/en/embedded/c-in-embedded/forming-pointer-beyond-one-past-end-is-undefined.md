---
id: emb-cppfound-0051
title: "Trap: UB?"
description: "Why forming arr+5 is undefined for a four-element array."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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
int arr[4]={1,2,3,4};
int *p=arr;
int *q=arr+5;
```

## Short answer

<span class="warn">Yes, undefined behavior already when forming `arr+5`</span>.

For array `arr[4]` (4 elements), valid pointers are: `arr` through `arr+4` inclusive (one-past-the-end). `arr+5` goes beyond one-past-the-end -> <span class="warn">undefined behavior even without dereferencing</span>.

The compiler may use this assumption for optimization, leading to unpredictable behavior. GCC with `-fsanitize=undefined` will detect it.[^embeddedinterviewlab]

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

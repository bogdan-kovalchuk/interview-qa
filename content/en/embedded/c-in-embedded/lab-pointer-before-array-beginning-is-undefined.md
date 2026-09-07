---
id: emb-cppfound-0071
title: "Is this code undefined behavior?"
description: "Why decrementing a pointer at the beginning of an array is undefined."
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
int arr[3]={1,2,3};
int *p=arr;
p--;
printf("%d",*p);
```

## Short answer

<span class="warn">Yes, UB.</span> `p = arr` -> pointer to `arr[0]`. `p--` -> `arr-1`, which is <span class="warn">outside the array</span>. Valid pointers for `arr[3]`: `arr` (=arr+0) to `arr+3` (one-past-the-end). `arr-1` – UB already when formed, not only when dereferenced; the compiler may assume UB does not occur -> unpredictable optimizations, so arr-1 must not be formed.[^embeddedinterviewlab]

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

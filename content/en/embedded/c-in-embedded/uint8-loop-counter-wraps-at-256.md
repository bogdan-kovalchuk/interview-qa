---
id: emb-cppfound-0086
title: "Trap: does this loop run forever?"
description: "Why an 8-bit loop counter cannot reach the terminating value 256."
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
int arr[256];
int *p=arr;
for(uint8_t i=0;
i<256;
i++) *p++=i;
```

## Short answer

<span class="warn">Yes, an infinite loop!</span> `uint8_t i` is an unsigned 8-bit type. At `i=255` -> `i++` -> wraps to 0 -> condition `0 < 256` -> true; the loop never terminates. Fix: `for(int i=0; i<256; i++)` or `for(size_t i=0; i<256; i++)`. GCC with `-Wtype-limits` warns if the condition is always true; this is a typical mistake when working with buffers of size 256.[^embeddedinterviewlab]

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

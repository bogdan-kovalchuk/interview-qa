---
id: emb-cppfound-0034
title: "Find the bug"
description: "Casting a byte buffer to uint32t and looping 256 times writes 1024 bytes, four times the buffer size, and may also misalign."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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
uint8_t buf[256];
uint32_t *p = (uint32_t*)buf;
for(int i=0;
i<256;
i++) p[i]=0;
```

## Short answer

<span class="warn">Out-of-bounds write!</span> `buf` – 256 bytes. `p` – `uint32_t*`, each element = 4 bytes. The loop `p[0]..p[255]` writes `256 × 4 = 1024 bytes` – 4 times the buffer size.

Correct: `for(int i=0; i < 256/sizeof(uint32_t); i++) p[i]=0;` or `memset(buf, 0, sizeof(buf))`.

Also: `uint8_t buf[256]` may not be aligned for `uint32_t` -> misaligned access.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-cppfound-0068
title: "What does this print on a little-endian system?"
description: "How little-endian byte order affects reading a byte array as a 32-bit integer."
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
uint8_t arr[4]={0x01,0x02,0x03,0x04};
uint32_t *p=(uint32_t*)arr;
printf("%08X",*p);
```

## Short answer

`04030201`. On little-endian (Cortex-M), bytes in memory: `[01][02][03][04]`. When read as `uint32_t`: the least significant byte comes first in memory – LSB=0x01, then 0x02, 0x03, MSB=0x04; value: `0x04030201`. <span class="warn">Warning</span>: such a cast may be misaligned on MCUs without support; safe approach: `uint32_t val; memcpy(&val, arr, 4);`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

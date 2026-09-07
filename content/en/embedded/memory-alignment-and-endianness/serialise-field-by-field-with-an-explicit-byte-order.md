---
id: emb-align-0021
title: "How do you serialise a struct into a byte buffer correctly?"
description: "Field by field, with explicit byte order and fixed offsets."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

## Question code

```c
uint32_t ts = htonl(r->ts);
uint16_t v  = htons(r->val);
memcpy(&buf[0], &ts, 4);
memcpy(&buf[4], &v,  2);
buf[6] = r->id;
```

## Short answer

**Field by field, with explicit byte order and fixed offsets.**

Each multi-byte field is first converted (`htonl`/`htons`), then placed at a known offset via `memcpy`. A single-byte `id` needs no swap.

Rule: `memcpy` here also guards against unaligned traps, even if `buf` is not aligned.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

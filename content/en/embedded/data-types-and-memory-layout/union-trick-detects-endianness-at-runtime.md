---
id: emb-dtypes-0073
title: "How do you detect a platform's endianness at runtime using a union?"
description: "Writing a known value into union.word and reading bytes[0] reveals whether the platform is little- or big-endian."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

`union { uint32_t word; uint8_t bytes[4]; } u;
u.word = 0x01020304;
if(u.bytes[0] == 0x04) { /* little-endian */ }`

Little-endian: `bytes[0] = 0x04` (LSB first). Cortex-M is little-endian by default.

Via pointer: `uint32_t x = 1; if(*(char*)&x == 1)` -> little-endian.

For networking: `htonl()`/`ntohl()` convert between host and network byte order (big-endian).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

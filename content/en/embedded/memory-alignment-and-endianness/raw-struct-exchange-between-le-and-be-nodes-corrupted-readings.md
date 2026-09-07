---
id: emb-align-0024
title: "Trap: a real \"every second sensor\" bug. What happened?"
description: "Raw memcpy structs between LE and BE MCUs had different padding, shifting fields by two bytes."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
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

## Short answer

<span class="warn">An M4 gateway (LE, little-endian) and a PowerPC node (BE, big-endian) were exchanging raw `memcpy` structs.</span>

The `uint8_t sensor_id` field had different padding (3 bytes on M4, 1 byte on PowerPC), which shifted the next `uint32_t` by 2 bytes. Odd IDs "happened to work"; even IDs produced garbage (~14000 degrees C).

Guard: explicit wire format plus field-by-field serialization with `htonl`/`htons`. Never assume two compilers produce the same layout.[^embeddedinterviewlab]

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

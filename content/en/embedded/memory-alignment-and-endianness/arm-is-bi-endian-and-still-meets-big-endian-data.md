---
id: emb-align-0013
title: "Trap: why can you not say \"endianness does not matter on ARM, it is always little-endian\"?"
description: "ARM is bi-endian and network protocols are always big-endian so byte order conversion is unavoidable"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

<span class="warn">ARM is bi-endian, and even an LE (little-endian) system constantly deals with big-endian data.</span>

Cortex-M defaults to little-endian, but the architecture also supports big-endian mode. The key point is that network and field protocols (TCP/IP – Transmission Control Protocol/Internet Protocol, CAN – Controller Area Network, Modbus TCP) are big-endian, so conversion is always needed.

Fix: in an interview, talk about byte order explicitly and use `htonl`/`ntohl` rather than "platform assumptions".[^embeddedinterviewlab]

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

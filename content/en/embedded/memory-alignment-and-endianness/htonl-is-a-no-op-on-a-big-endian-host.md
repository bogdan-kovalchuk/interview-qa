---
id: emb-align-0015
title: "What does `htonl()` return on a big-endian host?"
description: "On a big-endian host htonl returns the same value unchanged because host and network order match"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
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

**The same value unchanged – it is a no-op.**

On a big-endian host, host order equals network order, so there is nothing to convert. On a little-endian host `htonl`/`ntohl` swap the bytes. The key point: the code does not need to know which case it is – always write `htonl` and it will do the right thing on any platform.

Rule: never do a byte swap "manually based on the platform" when `hton*`/`ntoh*` is available.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

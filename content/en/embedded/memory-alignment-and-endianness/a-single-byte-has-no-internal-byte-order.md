---
id: emb-align-0040
title: "Why do single-byte fields need no byte swap when serialising?"
description: "Endianness concerns only the byte order within a multi-byte value; a single byte has no internal order."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: linux-byteorder
    title: "byteorder(3) - Linux manual page"
    url: https://man7.org/linux/man-pages/man3/htonl.3.html
    accessed: 2026-10-04
    kind: official
    version: "man-pages 6.19; POSIX.1-2008"
    applicability: "The htonl and htons signatures and their 32-bit and 16-bit types; this page documents the POSIX interface on Linux."
---

## Short answer

**Endianness concerns only the byte order within a multi-byte value.**

A single byte has no "internal order", so `uint8_t` is the same on LE and BE and is placed into the buffer as is.

Rule: apply `htons` to 16-bit and `htonl` to 32-bit values; no conversion is needed for `uint8_t` and byte arrays.[^linux-byteorder]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

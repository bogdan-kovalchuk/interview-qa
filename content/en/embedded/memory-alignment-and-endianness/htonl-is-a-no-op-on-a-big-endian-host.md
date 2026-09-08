---
id: emb-align-0015
title: "What does `htonl()` return on a big-endian host?"
description: "On a conforming big-endian host htonl returns the same numerical value because host and network order match"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  uk: 4
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
  - source_id: posix-htonl
    title: "htonl, htons, ntohl, ntohs"
    url: https://pubs.opengroup.org/onlinepubs/000095399/functions/htonl.html
    accessed: 2026-09-08
    kind: spec
    version: "The Open Group Base Specifications Issue 6"
    applicability: "Normative POSIX specification of host-to-network and network-to-host conversion."
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary background for the byte rearrangement required on other host orders."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian learning roadmap; not normative evidence for htonl."
---

## Short answer

**The same numerical value – host order already matches network order.**

On a big-endian host, an implementation can make `htonl` an identity macro or function. On a little-endian host it normally rearranges the bytes. The caller should use `htonl` at the network boundary in both cases instead of testing the platform.

Rule: never do a byte swap "manually based on the platform" when `hton*`/`ntoh*` is available.[^embeddedinterviewlab]

## Detailed explanation

POSIX specifies `htonl` in terms of a conversion from host byte order to network byte order, not in terms of an unconditional byte swap.[^posix-htonl] Consequently, if the host already stores a 32-bit value in the same most-significant-octet-first order, the converted result has the same numerical value and representation.

This distinction matters because "always swap" is wrong. A hand-written unconditional swap works on a little-endian host but corrupts the value on a big-endian host. Conversely, omitting `htonl` because today's target is little-endian sends host representation rather than network representation.

Keep conversion at the interface:

- call `htonl` when producing a 32-bit field defined in network order;
- copy the resulting bytes into the message without assuming structure layout;
- copy received bytes into a suitably aligned 32-bit object and call `ntohl` before using the value.

The function covers one 32-bit unsigned integer. It does not convert 64-bit values, floating-point objects, arrays, or an entire structure, and it should not be applied twice to the same field. Other formats need helpers that implement their own specified order.

Bitwise operations explain the rearrangement an implementation may use on a nonmatching host,[^learncpp-bitwise] while the aCode roadmap is a supplementary guide for broader C and C++ study.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->

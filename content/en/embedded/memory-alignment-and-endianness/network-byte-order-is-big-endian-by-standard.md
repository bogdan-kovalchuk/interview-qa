---
id: emb-align-0014
title: "Why is network byte order big-endian and how do you work with it?"
description: "POSIX network byte order is big-endian and provides htonl, ntohl, htons, and ntohs for conversion"
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
  - source_id: posix-byte-order
    title: "General Concepts: Data Types"
    url: https://pubs.opengroup.org/onlinepubs/009696699/basedefs/xbd_chap04.html
    accessed: 2026-09-08
    kind: spec
    version: "The Open Group Base Specifications Issue 6"
    applicability: "Defines network byte order and the conversion model for network data."
  - source_id: posix-htonl
    title: "htonl, htons, ntohl, ntohs"
    url: https://pubs.opengroup.org/onlinepubs/000095399/functions/htonl.html
    accessed: 2026-09-08
    kind: spec
    version: "The Open Group Base Specifications Issue 6"
    applicability: "Normative POSIX specification of the 16-bit and 32-bit host/network conversion functions."
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary background for understanding explicit byte conversion."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian learning roadmap; not normative evidence for network byte order."
---

## Short answer

**POSIX network byte order is big-endian: the most-significant octet comes first.**

POSIX (Portable Operating System Interface) provides host-vs-network converters:

```c
uint32_t net = htonl(host);
uint32_t host_again = ntohl(net);
```

For 16-bit values – `htons`/`ntohs`.

Rule: convert fields whose API or protocol specifies network byte order; do not assume every wire protocol uses it.[^embeddedinterviewlab]

## Detailed explanation

Network byte order gives communicating systems one representation independent of their host order. POSIX defines it with the most-significant octet first and recommends direct transfer for byte data, but host/network conversion for 16-bit and 32-bit integer data.[^posix-byte-order]

The conversion pairs are directional and symmetric in use:

- `htonl` converts a 32-bit unsigned value from host to network order; `ntohl` converts it back.
- `htons` and `ntohs` do the corresponding job for 16-bit unsigned values.[^posix-htonl]

On a little-endian host, an implementation normally changes the byte representation. On a big-endian host whose order already matches network order, it can be an identity operation. Application code should call the function in either case because the interface documents intent and keeps the code portable.

These functions do not serialize a complete C structure. A structure may contain padding, and its member widths or layout may differ across ABIs. Convert each specified integer field, then copy its bytes to or from the message buffer without creating an unaligned typed pointer. Also note that another protocol may explicitly choose little-endian or define a more complex layout; its own specification wins.

LearnCpp's bitwise overview helps explain what a byte-order conversion computes,[^learncpp-bitwise] and the aCode roadmap is supplementary guidance for broader C and C++ study.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->

---
id: emb-align-0014
title: "Why is network byte order big-endian and how do you work with it?"
description: "Network protocols use big-endian byte order and POSIX provides htonl and ntohl for conversion"
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

**Network protocols are standardized on big-endian (network byte order).**

POSIX (Portable Operating System Interface) provides host-vs-network converters:

```c
uint32_t net = htonl(host); // to BE
uint32_t h   = ntohl(net);  // back to host
```

For 16-bit values – `htons`/`ntohs`.

Rule: always convert multi-byte fields when sending or receiving over the network.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

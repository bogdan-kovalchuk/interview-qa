---
id: emb-align-0043
title: "What should a candidate demonstrate on alignment and endianness questions?"
description: "Predict padding and reorder fields, explain endianness, use htonl/ntohl correctly, serialize field by field, and understand the cost of packed and misaligned access."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: posix-htonl
    title: "The Open Group Base Specifications: htonl, htons, ntohl, ntohs"
    url: https://pubs.opengroup.org/onlinepubs/000095399/functions/htonl.html
    accessed: 2026-10-04
    kind: spec
    version: "Issue 6"
    applicability: "Defines conversions of 16- and 32-bit values between host and network byte order; it does not define arbitrary serialization formats."
  - source_id: arm-cortex-m-faults
    title: "Arm: Debugging Embedded Systems Part 2: Fault handling and diagnosis"
    url: https://developer.arm.com/community/arm-community-blogs/b/embedded-and-microcontrollers-blog/posts/debugging-embedded-systems-part-2-fault-handling-and-diagnosis
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Describes fault types and configurable unaligned-access faults on Cortex-M3/M4 and HardFault-only reporting on Cortex-M0; it is not a complete architecture manual."
---

## Short answer

**Predict possible padding, explain endianness, and serialize fields in a defined format.**

A structure's member layout and padding depend on the ABI; `htonl`/`ntohl` convert 32-bit values to and from network byte order, not arbitrary wire formats.[^iso-c-n1570] [^posix-htonl]

Serialize fields explicitly: sizes, byte order, and padding values belong to the protocol, not to an accidental `struct` image.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

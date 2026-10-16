---
id: emb-align-0043
title: "What should a candidate demonstrate on alignment and endianness questions?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: posix-htonl
    title: "The Open Group Base Specifications: htonl, htons, ntohl, ntohs"
    url: https://pubs.opengroup.org/onlinepubs/000095399/functions/htonl.html
  - source_id: arm-cortex-m-faults
    title: "Arm: Debugging Embedded Systems Part 2: Fault handling and diagnosis"
    url: https://developer.arm.com/community/arm-community-blogs/b/embedded-and-microcontrollers-blog/posts/debugging-embedded-systems-part-2-fault-handling-and-diagnosis
---

## Short answer

**Predict possible padding, explain endianness, and serialize fields in a defined format.**

A structure's member layout and padding depend on the ABI; `htonl`/`ntohl` convert 32-bit values to and from network byte order, not arbitrary wire formats.[^iso-c-n1570] [^posix-htonl]

Serialize fields explicitly: sizes, byte order, and padding values belong to the protocol, not to an accidental `struct` image.[^iso-c-n1570]

## Detailed explanation

TODO

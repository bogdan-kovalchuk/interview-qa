---
id: emb-align-0013
title: "Trap: why can you not say \"endianness does not matter on ARM, it is always little-endian\"?"
description: "Arm systems and external formats can use different byte orders, so code must follow the concrete target and interface specifications"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
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
  - source_id: arm-library-endianness
    title: "Selection of Arm C and C++ library variants based on build options"
    url: https://developer.arm.com/documentation/dui0475/latest/the-arm-c-and-c---libraries/c-and-c---runtime-libraries/selection-of-arm-c-and-c---library-variants-based-on-build-options
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Arm documentation showing that library selection distinguishes little-endian and big-endian build variants."
  - source_id: posix-byte-order
    title: "General Concepts: Data Types"
    url: https://pubs.opengroup.org/onlinepubs/009696699/basedefs/xbd_chap04.html
    accessed: 2026-09-08
    kind: spec
    version: "The Open Group Base Specifications Issue 6"
    applicability: "Defines big-endian network byte order for POSIX networking types and conversions."
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary background for explicit byte extraction and assembly."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian learning roadmap; not normative evidence for Arm or protocol byte order."
---

## Short answer

<span class="warn">The Arm ecosystem includes little-endian and big-endian configurations, and an external data format can use an order different from the processor.</span>

A concrete microcontroller, however, has a specific implemented and configured byte order. Internet network byte order is big-endian, but field-bus payloads and file formats follow their own specifications; CAN payload bytes, for example, do not acquire one universal integer byte order from the CAN transport itself.

Fix: name both sides of the boundary – the target's host order and the external format's specified order – then convert only where required.[^embeddedinterviewlab]

## Detailed explanation

"Arm" names an architecture family, not one fixed board configuration. Toolchains and runtime libraries have distinct little-endian and big-endian variants,[^arm-library-endianness] while the selected MCU, reset configuration, ABI, and toolchain determine what a particular firmware image actually uses. Therefore, neither "Arm is always little-endian" nor "every Arm chip can switch at runtime" is a safe claim.

Byte order at an interface is an independent contract. POSIX defines network byte order with the most-significant octet first and provides host/network conversions.[^posix-byte-order] That supports statements about IP networking APIs, not a blanket statement that every protocol is big-endian. A peripheral register map, CAN application payload, Modbus register sequence, binary file, or custom packet can specify another ordering or define order separately for bytes, words, and bits.

Conversion is needed only for multibyte fields whose external order differs from the host representation. Single-byte fields need no byte-order conversion. Explicit shifts and masks are one portable decoding technique; the LearnCpp bitwise material covers those operations.[^learncpp-bitwise]

## Symptom

Firmware works on the developer's little-endian board but reads swapped lengths, timestamps, or register values when data comes from another implementation or interface.

## Why it happens

The code treats a local object representation as though it were the protocol representation. It also replaces the concrete device and protocol specifications with broad labels such as "Arm" or "network".

## How to avoid

Document byte order per multibyte field, use named encode/decode helpers at the boundary, and test them with fixed byte vectors. Use `htonl`/`ntohl` only where POSIX network order is the relevant contract; otherwise implement the format named by the device or protocol specification. The aCode roadmap is useful supplementary guidance for continuing the wider C and C++ learning path.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->

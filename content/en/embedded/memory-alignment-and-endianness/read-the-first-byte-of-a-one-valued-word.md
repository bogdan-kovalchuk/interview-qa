---
id: emb-align-0016
title: "How do you detect endianness at runtime?"
description: "Store one in a multi-byte integer and inspect its first representation byte with memcpy"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
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
  - source_id: learncpp-object-sizes
    title: "Object sizes and the sizeof operator"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary explanation of bytes and multi-byte object storage."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian learning roadmap; not normative evidence for runtime byte-order detection."
---

## Question code

```c
bool is_little_endian(void) {
    const uint32_t word = 1;
    unsigned char first;
    memcpy(&first, &word, sizeof first);
    return first == 1;
}
```

## Short answer

**If the byte at the lowest address is `1`, the `uint32_t` representation is little-endian.**

The value `1` has only its least-significant byte set. Copying the object's first byte into an `unsigned char` yields `0x01` on a conventional little-endian target and `0x00` on a conventional big-endian target.

Rule: for a target MCU the endianness is usually known at compile time; a runtime check is only needed in portable libraries and tests.[^embeddedinterviewlab]

## Detailed explanation

`memcpy` copies object-representation bytes without violating alignment or effective-type rules. It also avoids a portability difference: reading a different union member is permitted with qualifications in C, but is not the general portable type-punning technique in C++.

For `word == 1`, a little-endian representation stores `01 00 00 00` from the lowest address upward, so the function returns `true`. A big-endian representation stores `00 00 00 01`, so it returns `false`. Strictly, `false` only means "not the tested little-endian layout"; unusual mixed-endian representations would need a fuller four-byte check.

The C standard defines object representation and permits copying it as character bytes, but it does not prescribe one integer byte order.[^iso-c-n1570] This test therefore observes the implementation rather than establishing a language guarantee.

In firmware built for one known MCU and ABI, compile-time target information is normally clearer and lets dead conversion branches disappear. Runtime detection is mainly useful when one binary truly supports multiple host layouts, or in diagnostic tests. It does not determine the byte order of an external packet or register; those come from the relevant specification.

LearnCpp's object-size material provides supporting context for representation bytes,[^learncpp-object-sizes] and the aCode roadmap offers a broader Ukrainian path for continued C and C++ study.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->

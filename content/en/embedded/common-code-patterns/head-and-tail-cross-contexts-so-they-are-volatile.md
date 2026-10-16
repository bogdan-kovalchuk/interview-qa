---
id: emb-patterns-0013
title: "Why are the fields of a ring buffer struct marked `volatile`?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**On many MCUs, `volatile` is used for indexes modified by an ISR and read by main, but it is not a portable synchronization guarantee.**

Without an appropriate mechanism, the compiler may reuse an earlier index value. `volatile` requires accesses to volatile objects under the implementation's rules, but does not by itself guarantee atomicity or cross-context ordering for the data buffer.

Check the compiler and MCU documentation for ISR behavior, index atomicity, and barriers; use a supported atomic mechanism or critical section when stronger synchronization is needed.[^iso-c-n1570]

## Detailed explanation

TODO

---
id: emb-fnptr-0052
title: "What is a weak callback hook in embedded firmware?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-weak-attribute
    title: "GCC: Common Function Attributes – weak"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
---

## Short answer

**A weak hook** is a function with a weak symbol that an application can override with a strong implementation on a toolchain supporting that linker semantics.[^gcc-weak-attribute]

On supported ELF or a.out targets, a GCC declaration with `__attribute__((weak))` emits a weak symbol; a strong definition of the same symbol can override it at link time.[^gcc-weak-attribute]

This is a GNU/toolchain-specific mechanism, not an ISO C property. It is convenient for startup defaults; runtime multiple instances usually need explicit callback registration with context.

## Detailed explanation

TODO

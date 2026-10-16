---
id: emb-fnptr-0056
title: "Why do function pointers affect optimisation?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-indirect-calls
    title: "GCC manual: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
---

## Short answer

**An indirect call is harder to optimise than a direct call.**

The compiler may not know the exact callee, so it usually cannot inline the call or perform optimisations that depend on the specific body. Analysis of visible values and LTO can sometimes identify a target and transform the call, but this depends on the program and toolchain.[^gcc-indirect-calls]

Embedded conclusion: function pointers give flexibility, but an indirect call can have extra cost; in hot paths inspect generated assembly and measurements.[^gcc-indirect-calls]

## Detailed explanation

TODO

---
id: emb-macros-0016
title: "How does `#pragma once` differ from a classic include guard?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-once-headers
    title: "GCC: Once-Only Headers"
    url: https://gcc.gnu.org/onlinedocs/cpp/Once-Only-Headers.html
  - source_id: msvc-once
    title: "Microsoft Learn: once pragma"
    url: https://learn.microsoft.com/en-us/cpp/preprocessor/once?view=msvc-170
---

## Short answer

**`#pragma once` asks the compiler to include a header at most once** per translation unit, without a separate guard macro.

Downside: the directive <span class="warn">does not have this behavior standardized by C or C++</span>, so support depends on the compiler. A classic `#ifndef` guard uses standard conditional directives and is more portable.

Check your toolchain documentation for support and include-path behavior before choosing it.[^gcc-once-headers] [^iso-c-n1570]

## Detailed explanation

TODO

---
id: emb-macros-0032
title: "What does `__attribute__((always_inline))` do and when is it needed?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-always-inline
    title: "GCC: Common Function Attributes – always_inline"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Function-Attributes.html
---

## Short answer

**For a direct call GCC requires inlining**, diagnosing a failure if it cannot do so; an indirect call has no equivalent guarantee. This is a GNU extension, not a C standard requirement.[^gcc-always-inline]

In embedded code it is sometimes used for a measured critical path, but size and speed must be checked on the target; the opposite GCC extension is `__attribute__((noinline))`. The C keyword `inline` alone also does not require body substitution.[^iso-c-n1570] [^gcc-always-inline]

## Detailed explanation

TODO

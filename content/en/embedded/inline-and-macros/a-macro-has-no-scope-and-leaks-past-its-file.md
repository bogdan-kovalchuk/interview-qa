---
id: emb-macros-0035
title: "Trap: how can a macro in a header affect code that includes it?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-cpp-macro-processing
    title: "GCC CPP: Object-like Macros and Undefining and Redefining Macros"
    url: https://gcc.gnu.org/onlinedocs/cpp/Object-like-Macros.html
---

## Short answer

<span class="warn">A macro has no block or file scope</span>: after `#define`, the preprocessor replaces its name in the remaining text of the current translation unit, including headers included afterward. A separately compiled `.c` file does not automatically inherit the definition.[^gcc-cpp-macro-processing]

For example, `#define max(a,b) ...` in a header can break `std::max` or the field `obj.max` in the translation unit that includes it.[^gcc-cpp-macro-processing]

Use distinctive UPPER_CASE names with a project prefix to reduce collisions; remove a macro with `#undef` when it is no longer needed.[^gcc-cpp-macro-processing]

## Detailed explanation

TODO

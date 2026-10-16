---
id: emb-macros-0047
title: "What should a candidate say when asked to choose between a macro and `inline`?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Distinguish the phase, list the macro risks, and default to `static inline`.**

Strong answer: preprocessing is not compilation; a macro is text without types or scope, at risk of double evaluation and precedence bugs; `static inline` gives the same speed plus type safety, single evaluation, and debuggability. Macros I keep for register defs, conditional compilation, `#`/`##`, X-macros, `STATIC_ASSERT`, and I mention MISRA C (Motor Industry Software Reliability Association C) 4.9/20.7.

Rule: do not stop at syntax – explain why and when.[^iso-c-n1570]

## Detailed explanation

TODO

---
id: emb-macros-0021
title: "What is an X-macro and which problem does it solve?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-cpp-overview
    title: "GCC CPP: Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
---

## Short answer

**An X-macro is a list defined once that is expanded in different contexts**.

The classic task is keeping an `enum` and a string or handler table in sync. The elements are listed as `X(...)` calls, then `X` is defined differently at each expansion site to generate an enum, a name array, a switch, and so on.

Adding an element to the single list updates each generated location, provided each location uses that list.[^gcc-cpp-overview]

## Detailed explanation

TODO

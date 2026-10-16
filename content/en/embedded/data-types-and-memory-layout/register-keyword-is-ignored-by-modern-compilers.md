---
id: emb-dtypes-0079
title: "What does the `register` storage class mean, and does it still matter today?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cpp17-register-removal
    title: "C++17 draft: Removal of register storage-class specifier"
    url: https://eel.is/c%2B%2Bdraft/diff.cpp14.dcl.dcl
---

## Short answer

In C11, `register` is an obsolescent storage-class hint: it does not guarantee that an object is kept in a CPU register, and an implementation may ignore it.[^iso-c-n1570] In C, unary `&` cannot be applied to an object declared with `register`.[^iso-c-n1570] C++17 removed the `register` specifier; keep that rule distinct from C.[^cpp17-register-removal]

## Detailed explanation

TODO

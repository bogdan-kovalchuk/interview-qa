---
id: emb-fnptr-0037
title: "Can a C++ non-capturing lambda be passed to a C-style callback?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cpp-lambda-closure
    title: "C++ working draft: Closure types"
    url: https://eel.is/c++draft/expr.prim.lambda.closure
---

## Short answer

**Yes, if the lambda has no captures and the signature is compatible.**

A non-generic lambda with no captures has a conversion function to a function pointer with compatible parameter and return types. A capturing lambda has no such conversion; pass state separately through a context pointer or use a C++ callback abstraction.[^cpp-lambda-closure]

For a C HAL callback, also check the exact signature and calling convention required by the API.[^cpp-lambda-closure]

## Detailed explanation

TODO

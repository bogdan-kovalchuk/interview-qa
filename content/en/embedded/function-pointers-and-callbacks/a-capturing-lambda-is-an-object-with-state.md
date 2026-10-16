---
id: emb-fnptr-0038
title: "Trap: why can't a capturing lambda be passed as an ordinary C function-pointer callback?"
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

<span class="warn">A capturing lambda has no standard conversion to an ordinary function pointer: its closure object carries captured state.</span> [^cpp-lambda-closure]

Invocation goes through the closure object's `operator()`, while a function pointer does not store an instance of that object. Also, `void (*)(void)` specifically requires a function with no parameters and a `void` result; the target signature must match.

For a C callback, pass state separately through `void *ctx`; otherwise use a C++ callback abstraction that stores the closure object.[^cpp-lambda-closure]

## Detailed explanation

TODO

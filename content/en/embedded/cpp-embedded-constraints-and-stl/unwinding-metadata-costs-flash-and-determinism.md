---
id: emb-cppstl-0001
title: "Why are exceptions often disabled in embedded (`-fno-exceptions`)?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Exception/unwinding metadata can noticeably increase the binary, and stack unwinding is ill-suited for hard real-time analysis.**

The exact cost depends on the ABI (application binary interface), compiler runtime and standard library. Some implementations also carry extra runtime infrastructure for `throw`/`catch`.

Rule: on flash- and real-time-constrained targets exceptions are often disabled, and errors are passed via codes or `Result` types.[^embeddedinterviewlab]

## Detailed explanation

TODO

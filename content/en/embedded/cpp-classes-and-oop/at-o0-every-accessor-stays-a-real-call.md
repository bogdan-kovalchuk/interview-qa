---
id: emb-cppoop-0031
title: "Trap: why do methods inline into bare-metal access only with optimization (for example `-O2`) and not at `-O0`?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
  - source_id: cpp-draft-class-mfct
    title: "C++ working draft: Member functions ([class.mfct])"
    url: https://eel.is/c++draft/class.mfct
  - source_id: cpp-draft-dcl-inline
    title: "C++ working draft: The inline specifier ([dcl.inline])"
    url: https://eel.is/c++draft/dcl.inline
---

## Short answer

<span class="warn">At `-O0` GCC does not expand functions inline by default, apart from those marked `always_inline`, so every `set()` stays a real function call.</span>[^gcc-optimize-options]

That is, the wrapper's "zero overhead" shows up only with optimization: `-finline-small-functions` is enabled at `-O2`, `-O3` and `-Os`,[^gcc-optimize-options] while in a debug build the wrapper class costs a call with prologue and epilogue.

Defence: measure the size and speed of C++ abstractions with release flags (`-O2`/`-Os`), not at `-O0`, and check the assembly.

## Detailed explanation

TODO

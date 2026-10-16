---
id: emb-cppoop-0009
title: "Trap: why can merely declaring a destructor inflate ROM?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
  - source_id: cpp-draft-basic-start-term
    title: "C++ working draft: Termination ([basic.start.term])"
    url: https://eel.is/c++draft/basic.start.term
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
  - source_id: gcc-cxx-cxa-atexit
    title: "GCC: C++ Dialect Options, -fuse-cxa-atexit"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fuse-cxa-atexit
  - source_id: gcc-int-init-macros
    title: "GCC Internals: Macros Controlling Initialization Routines"
    url: https://gcc.gnu.org/onlinedocs/gccint/Macros-for-Initialization.html
---

## Short answer

<span class="warn">A global object with a non-trivial destructor makes the compiler register its destruction at startup (`__cxa_atexit`, `__aeabi_atexit` on Arm), which can pull in the atexit runtime – extra ROM.</span>[^itanium-abi-atexit][^arm-cpp-abi] The destructor runs only on `exit` or when `main` returns,[^cpp-draft-basic-start-term] and in firmware `main()` normally never returns, so this infrastructure is dead weight. The `-fno-use-cxa-atexit` flag only changes the mechanism, so its effect depends on the target.[^gcc-cxx-cxa-atexit]

Protection: make the destructor trivial (`= default`, no `virtual`)[^cpp-draft-class-dtor] or create the object in static storage with placement new and never destroy it.

## Detailed explanation

TODO

---
id: emb-cppoop-0013
title: "What does a virtual function cost in memory?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
---

## Short answer

**Typically one vtable per polymorphic class in ROM (`.rodata`) and one hidden vptr per polymorphic object in RAM.** Rough estimate: vtable ≈ number of virtual functions × pointer size plus ABI slots (offset-to-top, typeinfo), with a virtual destructor taking two entries; vptr ≈ one pointer per instance, more with several polymorphic bases.[^itanium-cxx-abi] These are ABI details, not C++ standard rules; Arm declares no different ones.[^arm-cpp-abi] With hundreds of objects the RAM cost becomes significant.

## Detailed explanation

TODO

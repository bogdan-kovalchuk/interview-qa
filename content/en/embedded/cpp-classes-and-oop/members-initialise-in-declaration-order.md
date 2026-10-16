---
id: emb-cppoop-0032
title: "What is the initialisation order of members in a constructor?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-base-init
    title: "C++ working draft: Initializing bases and members ([class.base.init])"
    url: https://eel.is/c++draft/class.base.init
  - source_id: cpp-draft-basic-indet
    title: "C++ working draft: Indeterminate and erroneous values ([basic.indet])"
    url: https://eel.is/c++draft/basic.indet
  - source_id: cppcg-c47-member-init-order
    title: "C++ Core Guidelines: C.47 – Define and initialize data members in the order of member declaration"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c47-define-and-initialize-data-members-in-the-order-of-member-declaration
  - source_id: gcc-cpp-dialect-options
    title: "GCC 16.1.0: Options Controlling C++ Dialect (-Wreorder)"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-Wreorder
---

## Short answer

**Non-static members are initialised in the order of declaration in the class, not in the order they appear in the init list.**[^cpp-draft-class-base-init] So if `a_` is declared before `b_` and the list reads `: b_{x}, a_{b_ + 1}`, `a_` is initialised first and reads a not-yet-initialised `b_` – an error, usually undefined behavior. Defence: write the list in declaration order; GCC warns through `-Wreorder`, which `-Wall` enables.[^gcc-cpp-dialect-options]

## Detailed explanation

TODO

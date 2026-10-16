---
id: emb-cppoop-0006
title: "What is a member initialisation list in a constructor for?"
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
  - source_id: cpp-draft-dcl-type-cv
    title: "C++ working draft: The cv-qualifiers ([dcl.type.cv])"
    url: https://eel.is/c++draft/dcl.type.cv
  - source_id: cpp-draft-dcl-init-ref
    title: "C++ working draft: References ([dcl.init.ref])"
    url: https://eel.is/c++draft/dcl.init.ref
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
  - source_id: cppcg-c47-member-init-order
    title: "C++ Core Guidelines: C.47 – Define and initialize data members in the order of member declaration"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c47-define-and-initialize-data-members-in-the-order-of-member-declaration
  - source_id: cppcg-c49-init-not-assign
    title: "C++ Core Guidelines: C.49 – Prefer initialization to assignment in constructors"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c49-prefer-initialization-to-assignment-in-constructors
  - source_id: gcc-cpp-dialect-options
    title: "GCC 16.1.0: Options Controlling C++ Dialect (-Wreorder)"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-Wreorder
---

## Question code

```c
Gpio(uint32_t base, uint8_t pin)
  : odr_{(volatile uint32_t*)(base + 0x14)}, pin_{pin} {}
```

## Short answer

**It initializes bases and members before entering the constructor body, so `const` and reference members taking their value from parameters can be set only here.**[^cpp-draft-class-base-init] In the body, `pin_ = pin` would be an assignment, and it does not compile: the left operand must be a modifiable lvalue.[^cpp-draft-expr-assign] For constant values a default member initializer can be used instead of the list. For class-type members, direct initialization can also beat "default + assignment".[^cppcg-c49-init-not-assign] Members are initialized in the order they are declared in the class, not in the order of the list.[^cpp-draft-class-base-init]

## Detailed explanation

TODO

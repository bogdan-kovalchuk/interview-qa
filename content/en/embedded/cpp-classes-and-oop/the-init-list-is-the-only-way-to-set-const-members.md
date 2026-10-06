---
id: emb-cppoop-0006
title: "What is a member initialisation list in a constructor for?"
description: "It initializes bases and members before the constructor body; for const and reference members whose value comes from constructor parameters it is the only way."
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-06
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-class-base-init
    title: "C++ working draft: Initializing bases and members ([class.base.init])"
    url: https://eel.is/c++draft/class.base.init
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines the initialization order (bases, then members in declaration order, then the body), the role of default member initializers and the ban on binding a temporary to a reference member; says nothing about efficiency."
  - source_id: cpp-draft-dcl-type-cv
    title: "C++ working draft: The cv-qualifiers ([dcl.type.cv])"
    url: https://eel.is/c++draft/dcl.type.cv
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that the definition of a const object or subobject must specify an initializer or be subject to default-initialization, and that modifying a const subobject is an error."
  - source_id: cpp-draft-dcl-init-ref
    title: "C++ working draft: References ([dcl.init.ref])"
    url: https://eel.is/c++draft/dcl.init.ref
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that a reference must be initialized and cannot be rebound; for a class member the initializer may be omitted in the declaration itself."
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Requires a modifiable lvalue as the left operand of assignment; this is why assigning to a const member in a constructor body does not compile."
  - source_id: cppcg-c47-member-init-order
    title: "C++ Core Guidelines: C.47 – Define and initialize data members in the order of member declaration"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c47-define-and-initialize-data-members-in-the-order-of-member-declaration
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A guideline with an example of a bug caused by list order; not a language requirement."
  - source_id: cppcg-c49-init-not-assign
    title: "C++ Core Guidelines: C.49 – Prefer initialization to assignment in constructors"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c49-prefer-initialization-to-assignment-in-constructors
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "States that initialization can be more elegant and efficient than default construction followed by assignment and prevents use-before-set; the example is a std::string member, and no benefit is claimed for scalars."
  - source_id: gcc-cpp-dialect-options
    title: "GCC 16.1.0: Options Controlling C++ Dialect (-Wreorder)"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-Wreorder
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents -Wreorder: a warning when the order of mem-initializers differs from the order of execution; enabled by -Wall. GCC-specific."
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

## Sources

<!-- generated from frontmatter -->

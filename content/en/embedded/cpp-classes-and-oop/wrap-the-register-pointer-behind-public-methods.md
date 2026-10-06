---
id: emb-cppoop-0004
title: "How do you encapsulate a GPIO register in a class?"
description: "A private pointer to the GPIO register plus public accessor methods that typically inline to bare-metal access."
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
  - source_id: cpp-draft-class-access
    title: "C++ working draft: Member access control, general ([class.access.general])"
    url: https://eel.is/c++draft/class.access.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines that a private member can be named only by members and friends of the class; this is language-level access control, not hardware protection of the register."
  - source_id: cpp-draft-class-mfct
    title: "C++ working draft: Member functions ([class.mfct])"
    url: https://eel.is/c++draft/class.mfct
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Confirms that a member function defined in its class body is inline; this alone does not guarantee that the body is substituted."
  - source_id: cpp-draft-dcl-inline
    title: "C++ working draft: The inline specifier ([dcl.inline])"
    url: https://eel.is/c++draft/dcl.inline
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that inline only indicates a preference for inline substitution and an implementation is not required to perform it."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Options That Control Optimization"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents -finline-small-functions and -finline-functions, enabled heuristically at -O2; the exact set depends on target and GCC configuration, and other compilers can differ."
  - source_id: cpp-draft-dcl-type-cv
    title: "C++ working draft: The cv-qualifiers ([dcl.type.cv])"
    url: https://eel.is/c++draft/dcl.type.cv
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that the semantics of access through a volatile glvalue are implementation-defined and that volatile is a hint to avoid aggressive optimization; the actual access instructions depend on toolchain and target."
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines E1 op= E2 as E1 = E1 op E2 with E1 evaluated once; gives no atomicity guarantee with respect to interrupts or other bus masters."
---

## Question code

```cpp
class Gpio {
  volatile uint32_t *const odr_;
  const uint8_t pin_;
public:
  Gpio(volatile uint32_t *odr, uint8_t pin) : odr_{odr}, pin_{pin} {}
  void set() const { *odr_ |= (UINT32_C(1) << pin_); }
  void clear() const { *odr_ &= ~(UINT32_C(1) << pin_); }
};
```

## Short answer

**A private pointer to the GPIO (general-purpose input/output) register plus public accessor methods.** A `private` member can be named only by the class's own code (and its friends), so no raw read-modify-write can be done from outside.[^cpp-draft-class-access] Small methods defined in the class body are implicitly `inline`, and GCC at `-O2` usually substitutes them, but the standard does not require it.[^cpp-draft-class-mfct][^gcc-optimize-options] Rule: a wrapper class gives encapsulation and type safety, and the release-build overhead is usually minimal – check the assembly, and remember `|=` is not atomic.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

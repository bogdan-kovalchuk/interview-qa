---
id: emb-cppoop-0004
title: "How do you encapsulate a GPIO register in a class?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-access
    title: "C++ working draft: Member access control, general ([class.access.general])"
    url: https://eel.is/c++draft/class.access.general
  - source_id: cpp-draft-class-mfct
    title: "C++ working draft: Member functions ([class.mfct])"
    url: https://eel.is/c++draft/class.mfct
  - source_id: cpp-draft-dcl-inline
    title: "C++ working draft: The inline specifier ([dcl.inline])"
    url: https://eel.is/c++draft/dcl.inline
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Options That Control Optimization"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
  - source_id: cpp-draft-dcl-type-cv
    title: "C++ working draft: The cv-qualifiers ([dcl.type.cv])"
    url: https://eel.is/c++draft/dcl.type.cv
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
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

---
id: emb-cppoop-0004
title: "How do you encapsulate a GPIO register in a class?"
description: "A private pointer to the GPIO register plus public accessor methods that inline to bare-metal access."
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
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

**A private pointer to the GPIO (general-purpose input/output) register plus public accessor methods.**

Private members prevent raw read-modify-write from outside; the methods inline at `-O2` into the same code as bare-metal access.

Rule: a wrapper class provides type safety and encapsulation with no runtime overhead in a release build.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

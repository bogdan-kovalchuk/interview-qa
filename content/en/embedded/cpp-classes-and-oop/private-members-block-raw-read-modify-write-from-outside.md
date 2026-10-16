---
id: emb-cppoop-0030
title: "Why do private members matter for correct register handling?"
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
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
  - source_id: tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (SPMS376E)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
---

## Short answer

**`private` keeps external code from touching the register directly:** a `private` member can be named only by members and friends of the class, so a raw read-modify-write from outside cannot go through the class.[^cpp-draft-class-access] All access goes through methods (`set`/`clear`/`read`) that form the mask in one place and preserve the class invariants. This is language-level protection, not hardware protection: another pointer to the same address bypasses it, and `|=` inside a method is `*odr_ = *odr_ | mask`, a read-modify-write,[^cpp-draft-expr-assign] so it is not atomic with respect to an ISR.

## Detailed explanation

TODO

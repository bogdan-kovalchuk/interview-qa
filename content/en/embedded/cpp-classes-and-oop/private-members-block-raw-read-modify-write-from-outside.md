---
id: emb-cppoop-0030
title: "Why do private members matter for correct register handling?"
description: "Private members prevent external raw read-modify-write that would bypass class invariants"
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
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
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines E1 op= E2 as E1 = E1 op E2 with E1 evaluated once; gives no atomicity guarantee with respect to interrupts or other bus masters."
  - source_id: tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (SPMS376E)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
    accessed: 2026-10-06
    kind: official
    version: "SPMS376E"
    applicability: "Documentation Conventions (Table 2): the value of a reserved bit should be preserved across a read-modify-write. Section 10.2.1.2: GPIODATA lets a single write change individual pins using a mask in address bits [9:2], which is more efficient than read-modify-write. An example from one MCU; other chips differ."
---

## Short answer

**`private` keeps external code from touching the register directly:** a `private` member can be named only by members and friends of the class, so a raw read-modify-write from outside cannot go through the class.[^cpp-draft-class-access] All access goes through methods (`set`/`clear`/`read`) that form the mask in one place and preserve the class invariants. This is language-level protection, not hardware protection: another pointer to the same address bypasses it, and `|=` inside a method is `*odr_ = *odr_ | mask`, a read-modify-write,[^cpp-draft-expr-assign] so it is not atomic with respect to an ISR.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

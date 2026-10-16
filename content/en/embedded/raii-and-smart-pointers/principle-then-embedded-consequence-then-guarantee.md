---
id: emb-raii-0033
title: "What should a candidate say about why RAII matters in embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
  - source_id: cpp-draft-class-temporary
    title: "C++ working draft: Temporary objects ([class.temporary])"
    url: https://eel.is/c++draft/class.temporary
---

## Short answer

**Answer structure: principle -> embedded consequence -> compiler guarantee.**

Principle: ctor acquires, dtor releases.[^cppcg-r1-raii] Consequence: no OS to release resources for you, so a leak or deadlock can persist until reset. Guarantee: the dtor of a local object runs on every exit from its scope, including early return, except when the program ends through `exit` or `abort`.[^cpp-draft-stmt-jump]

Rule: emphasise that RAII removes a class of human errors rather than adding capabilities.[^embeddedinterviewlab]

## Detailed explanation

TODO

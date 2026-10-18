---
id: emb-cppemb-0001
title: "Why is a virtual destructor needed in C++, and when does it matter in embedded C++?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

A virtual destructor is needed when an object is deleted through a pointer/reference to the base class: then the derived class destructor is called. Without it, `delete basePtr` on a polymorphic object has undefined behavior. In embedded C++ this matters for driver interfaces, HAL abstractions or state machines, but dynamic allocation is often replaced with static lifetime or placement new.[^dou-embedded-interview]

## Detailed explanation

TODO

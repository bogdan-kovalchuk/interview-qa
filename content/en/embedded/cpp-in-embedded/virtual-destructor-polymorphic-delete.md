---
id: emb-cppemb-0001
title: "Why is a virtual destructor needed in C++, and when does it matter in embedded C++?"
description: "A virtual destructor ensures the derived destructor runs when deleting through a base pointer; without it, deletion of a polymorphic object is undefined behavior, and in embedded C++ this applies to driver and HAL interfaces."
track: embedded
section: cpp-in-embedded
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for cpp in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

A virtual destructor is needed when an object is deleted through a pointer/reference to the base class: then the derived class destructor is called. Without it, `delete basePtr` on a polymorphic object has undefined behavior. In embedded C++ this matters for driver interfaces, HAL abstractions or state machines, but dynamic allocation is often replaced with static lifetime or placement new.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-cppoop-0017
title: "Why does a base class with virtual methods need a virtual destructor?"
description: "Without a virtual destructor, deleting a derived object through a base pointer is undefined behavior"
track: embedded
section: cpp-classes-and-oop
level: junior
type: pitfall
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

## Short answer

<span class="warn">Without a virtual destructor, deleting a derived object through a `Base*` is undefined behavior.</span>

`Base* p = new Derived; delete p;` calls only `~Base()`, not `~Derived()` -> the derived resources are never freed.

Protection: if a class has virtual functions and is deleted polymorphically, declare `virtual ~Base()`. (In embedded without a heap this is less critical, but the interface contract is still worth keeping.)[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

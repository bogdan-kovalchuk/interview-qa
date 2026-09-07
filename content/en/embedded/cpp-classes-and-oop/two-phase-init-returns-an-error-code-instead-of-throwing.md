---
id: emb-cppoop-0011
title: "How do you initialise an object when exceptions are disabled (`-fno-exceptions`)?"
description: "Two-phase init: a trivial constructor plus a separate init method that returns an error code the caller checks"
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
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

**Two-phase init: trivial constructor + a separate `init()` method that returns an error code.**

The constructor cannot signal failure without exceptions, so "heavy" initialization (the kind that can fail) is moved into `err_t init()`, which the caller checks.

Rule: on targets without exceptions, keep the constructor simple (no-fail) and put fallible logic into a separate init with a return code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

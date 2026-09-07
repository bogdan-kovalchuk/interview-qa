---
id: emb-cemb-0001
title: "Describe the use of the `static` modifier in C and C++."
description: "In C, static extends a local variable lifetime or limits a global symbol to one file; in C++ it also provides one class member copy shared by all objects and methods without an instance."
track: embedded
section: c-in-embedded
level: junior
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**In C:**
- Local variable: `static int cnt = 0;` – preserves state between calls.
- Global variable/function: `static void helper()` – visible only in the current `.c` file.[^dou-embedded-interview]

**Additionally in C++:**
- Static class member: `static int count;` – one copy for all objects, initialized outside the class.
- Static method: `static void reset();` – called as `MyClass::reset()`, has no access to `this`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-build-0005
title: "What happens if two files define a function with the same name and parameters? At which stage does the error occur?"
description: "Two non-static functions with the same name in different translation units compile separately but the linker rejects them as a multiple definition or duplicate symbol error."
track: embedded
section: toolchain-and-build
level: junior
type: pitfall
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for toolchain and build concepts; details of specific devices and toolchains can differ."
---

## Short answer

If you define a non-`static` function with the same name in two `.c`/`.cpp` files, compilation of each translation unit may succeed because each is compiled separately.[^dou-embedded-interview]

The error will usually occur at the **linking** stage: the linker will see two global symbols with the same name and emit a multiple definition / duplicate symbol error. If you make the functions `static`, each will have internal linkage and there will be no conflict between files. In C++, overloading is only possible if the signatures differ; the same signature still violates the ODR.

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

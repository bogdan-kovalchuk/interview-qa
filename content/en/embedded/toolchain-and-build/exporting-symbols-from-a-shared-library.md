---
id: emb-build-0004
title: "How do you export/import functions from a dynamic library?"
description: "On Linux, shared library symbols in .so are exported by default and controlled via visibility attributes; Windows DLLs require explicit dllexport/dllimport or a .def file."
track: embedded
section: toolchain-and-build
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for toolchain and build concepts; details of specific devices and toolchains can differ."
---

## Short answer

In Linux/Unix, functions from a shared library are typically exported as symbols in a `.so`.[^dou-embedded-interview] For a C API it is enough to not make the function `static`, compile with `-fPIC`, and link with `-shared`; visibility can be controlled via `__attribute__((visibility("default")))` and a linker version script.

In Windows DLLs, `__declspec(dllexport)` is typically used when building the library and `__declspec(dllimport)` on the consumer side, or a `.def` file. For C++ APIs, `extern "C"` is often added for stable C symbols, or C++ is exported with the ABI of a specific compiler in mind.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

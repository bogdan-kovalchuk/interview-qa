---
id: emb-build-0008
title: "How do static and dynamic libraries differ during build and linking?"
description: "Static libraries are linked into the image by the linker, while dynamic libraries remain separate artifacts loaded at runtime."
track: embedded
section: toolchain-and-build
level: middle
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  uk: 4
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

**Static library** (`.a`/`.lib`) is copied by the linker into the firmware or executable using only the needed object files. **Dynamic library** (`.so`/`.dll`) is loaded by the loader at runtime and remains a separate artifact. Bare-metal MCUs typically use static linking; Embedded Linux often supports both.[^dou-embedded-interview]

## Detailed explanation

A **static library** (`.a` on Linux/macOS, `.lib` on Windows) is an archive of object files. When the linker processes a static library, it extracts only the object files needed to resolve the current symbol references. Unused object files do not end up in the final executable or firmware. This means the binary size depends only on the library code actually used.[^gcc-overall-options]

Static linking happens at build time. The linker copies the needed code from the `.a`/`.lib` into the executable. After that, the library is not needed to run the program – all the code is already inside the binary.

A **dynamic library** (`.so` on Linux, `.dll` on Windows, `.dylib` on macOS) is a separate binary artifact loaded by the operating system's loader at runtime. When the program starts, the OS finds the required shared libraries, loads them into memory, and resolves symbol references through the dynamic linker. The program can use a single copy of the library in memory, even if multiple programs use it.

For bare-metal MCUs, static linking is typically used because:
- There is no OS to load shared libraries
- Flash memory is limited, and static linking allows precise control over firmware size
- There is no dynamic linker to resolve symbols at runtime
- Firmware is usually monolithic – a single binary image

Embedded Linux often supports both options:
- Static linking for performance-critical components (less overhead, no dynamic linking at runtime)
- Dynamic linking for general-purpose libraries (libc, libpthread) to reduce firmware size and allow library updates without recompiling all programs


## Evaluation guide

### Expected signals

- Distinguishes static and dynamic libraries by linking and loading method
- Understands that static linking copies code into the binary, while dynamic linking loads the library at runtime
- Knows that bare-metal MCUs typically use static linking due to the absence of an OS
- Understands the trade-off between firmware size, performance, and update flexibility

### Red flags

- Confuses static library with static linking (these are different things)
- Does not know the difference between `.a`/`.lib` and `.so`/`.dll`
- Believes dynamic libraries are always better than static
- Does not understand why bare-metal MCUs do not use dynamic linking

### Level-up follow-up

- How does the static linker decide which object files to extract from the archive?
- What overhead does dynamic linking have at runtime?
- How to update a shared library on an embedded Linux device in production?


## Sources

<!-- generated from frontmatter -->

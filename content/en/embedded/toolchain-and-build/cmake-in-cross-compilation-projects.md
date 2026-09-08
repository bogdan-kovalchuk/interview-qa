---
id: emb-build-0009
title: "How does CMake work in a cross-compilation project for an MCU or Embedded Linux?"
description: "CMake configures the build graph from CMakeLists.txt and a toolchain file, then the build tool invokes the cross-compiler, assembler, linker, and post-build utilities."
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

CMake first configures the build graph: it reads `CMakeLists.txt`, the toolchain file, target flags, and generates a Ninja/Make project. Then the build tool invokes the cross-compiler, assembler, linker, and post-build utilities such as `objcopy`. It is important to separate host tools, which run on the PC, from target binaries, which are intended for the MCU or Linux target.[^dou-embedded-interview]

## Detailed explanation

In a cross-compilation project, CMake works in two stages: configure and build. During configure, CMake reads `CMakeLists.txt`, the toolchain file, and generates the build system (Ninja or Makefiles). During build, the build tool invokes the cross-compiler, assembler, linker, and post-build utilities.[^gcc-overall-options]

**Toolchain file** is a CMake script that defines the target platform:
```cmake
set(CMAKE_SYSTEM_NAME Generic)  # or Linux, bare-metal
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
```

CMake distinguishes **host tools** (which run on the PC during build) from **target binaries** (which will execute on the MCU). For example, a code generator might be a host tool that generates code for the target.

**Configure step**:
```bash
cmake -B build -G Ninja \
  -DCMAKE_TOOLCHAIN_FILE=arm-toolchain.cmake \
  -DCMAKE_BUILD_TYPE=Release
```

**Build step**:
```bash
cmake --build build --target firmware.elf
```

CMake automatically adds target flags from the toolchain file to every compile command. The linker script is set via `target_link_options()` or `CMAKE_EXE_LINKER_FLAGS`. Post-build steps (objcopy to .hex/.bin) are added via `add_custom_command()`.

## Evaluation guide

### Expected signals
- Understands the difference between host tools and target binaries
- Knows that the toolchain file specifies the cross-compiler and target flags
- Can explain the configure and build stages
- Understands the role of sysroot and linker script

### Red flags
- Confuses host compiler with cross-compiler
- Does not know what a toolchain file is
- Does not understand why you cannot just change the compiler to a cross-compiler without a toolchain file

### Level-up follow-up
- How does CMake handle find_package() in cross-compilation?
- How to set different optimization levels for different targets?
- How to integrate a code generator as a host tool?

## Sources

<!-- generated from frontmatter -->

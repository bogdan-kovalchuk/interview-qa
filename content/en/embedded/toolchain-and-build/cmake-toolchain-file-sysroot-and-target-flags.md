---
id: emb-build-0010
title: "What is a CMake toolchain file, and what roles do the compiler, sysroot, and target flags play?"
description: "A toolchain file tells CMake to build for a target rather than the host, specifying the compiler, sysroot, ABI, and platform flags."
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

**Toolchain file** tells CMake that the build targets a platform other than the host: `CMAKE_SYSTEM_NAME`, compilers, archiver, objcopy, sysroot, and flags. `sysroot` provides the target system's headers and libraries, and target flags specify the ABI, FPU, CPU core, linker script, etc. Without this, CMake may silently find host libraries and build an incompatible binary.[^dou-embedded-interview]

## Detailed explanation

A **toolchain file** in CMake is a CMake script that tells the build system you are building for a target platform, not the host. It specifies the cross-compiler, sysroot, and target-specific flags.[^gcc-overall-options]

**Main toolchain file variables**:
```cmake
set(CMAKE_SYSTEM_NAME Generic)  # Target OS (Generic for bare-metal)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
```

**Sysroot** (`CMAKE_SYSROOT`) is a directory with the target system's headers and libraries. When the cross-compiler searches for headers or libraries, it looks in the sysroot, not on the host system. This prevents accidental use of host libraries.

**Target flags** are set via `CMAKE_C_FLAGS`, `CMAKE_CXX_FLAGS`, `CMAKE_ASM_FLAGS`:
```cmake
set(CMAKE_C_FLAGS "-mcpu=cortex-m4 -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16")
set(CMAKE_EXE_LINKER_FLAGS "-T${CMAKE_SOURCE_DIR}/linker.ld -specs=nosys.specs")
```

These flags include:
- `-mcpu=cortex-m4` – CPU architecture
- `-mthumb` – Thumb instruction set
- `-mfloat-abi=hard` – Hardware FPU
- `-mfpu=fpv4-sp-d16` – FPU type
- `-T linker.ld` – Linker script
- `-specs=nosys.specs` – Syscall stubs for bare-metal

Without a toolchain file, CMake uses the host compiler and host libraries, resulting in a binary that does not work on the target MCU.

## Evaluation guide

### Expected signals
- Knows that the toolchain file specifies the cross-compiler and target flags
- Understands the role of sysroot for isolation from the host system
- Can explain the main target flags (CPU, FPU, linker script)
- Understands why you cannot just change the compiler without a toolchain file

### Red flags
- Does not know what a toolchain file is
- Confuses sysroot with include directories
- Does not understand the difference between host and target
- Does not know where to specify the linker script and CPU flags

### Level-up follow-up
- How to set different flags for different build types (Debug/Release)?
- How to integrate a toolchain file with CMake presets?
- How to handle different ABIs (soft-float vs hard-float)?

## Sources

<!-- generated from frontmatter -->

---
id: emb-build-0012
title: "How can you obtain preprocessing, assembly, and object files during compilation?"
description: "GCC/Clang flags -E, -S, and -c produce preprocessed output, assembly, and object files, and tools like objdump and readelf help analyze firmware."
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

For GCC/Clang: `-E` produces preprocessed output, `-S` – assembly, `-c` – object file without linking. For firmware analysis, `objdump -d`, `readelf -S`, and the linker map are useful. In CMake, these flags can be temporarily added to a target or the compiler command can be run from `compile_commands.json`.[^dou-embedded-interview]

## Detailed explanation

GCC and Clang provide flags to obtain intermediate files at each compilation stage.[^gcc-overall-options]

**Preprocessing** (`-E`):
```bash
gcc -E main.c -o main.preprocessed.c
```
Result: file with all `#include` expanded, macros replaced, comments removed. Useful for debugging macros and conditional compilation.

**Assembly** (`-S`):
```bash
gcc -S main.c -o main.s
```
Result: assembly file. Useful for analyzing generated code, checking optimization, debugging compiler issues.

**Object file** (`-c`):
```bash
gcc -c main.c -o main.o
```
Result: object file without linking. Useful for checking symbol visibility, compilation errors without linking.

**Firmware analysis**:
```bash
objdump -d firmware.elf      # Disassembly
objdump -h firmware.elf      # Section headers
readelf -S firmware.elf      # Section details
readelf -s firmware.elf      # Symbol table
size firmware.elf            # Text/data/bss sizes
```

**Linker map file** is generated with `-Wl,-Map=firmware.map` and shows:
- Placement of all sections in memory
- Addresses of all symbols
- Size of each section
- Memory usage by regions (FLASH, RAM)

**In CMake**, you can temporarily add flags to a target:
```cmake
target_compile_options(firmware PRIVATE -save-temps)
```
Or run the compiler command from `compile_commands.json`:
```bash
grep -A5 "main.c" compile_commands.json
# Copy the command and add -E/-S/-c
```

## Evaluation guide

### Expected signals
- Knows the `-E`, `-S`, `-c` flags and what they do
- Can name tools for firmware analysis (objdump, readelf, size)
- Understands what a linker map file is and why it is needed
- Knows how to obtain intermediate files in CMake

### Red flags
- Does not know the difference between `-E`, `-S`, `-c`
- Cannot name tools for firmware analysis
- Does not understand what the linker map file shows
- Does not know how to view preprocessed output

### Level-up follow-up
- How to view assembly for a specific function?
- What is `-save-temps` and when to use it?
- How to analyze memory usage from the map file?

## Sources

<!-- generated from frontmatter -->

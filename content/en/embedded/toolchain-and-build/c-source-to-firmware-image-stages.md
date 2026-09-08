---
id: emb-build-0011
title: "What stages does a C file pass through from preprocessing to an executable or firmware image?"
description: "A C file passes through preprocessing, compilation, assembly, linking, and for firmware, conversion into a target image format."
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

First, preprocessing expands `#include`, `#define`, and conditional compilation. Then the compiler generates assembly or IR, the assembler produces an object file, the linker combines objects/libraries and places sections. For firmware, `objcopy` into `.hex`/`.bin` is often performed and a map file is generated.[^dou-embedded-interview]

## Detailed explanation

A C file goes through several stages before becoming an executable or firmware image.[^gcc-overall-options]

**1. Preprocessing** (`cpp` or `gcc -E`):
- Expands `#include` – inserts header file contents
- Expands `#define` – replaces macros with their values
- Processes `#ifdef`/`#ifndef`/`#endif` – conditional compilation
- Removes comments
- Result: `.c` file with all includes expanded

**2. Compilation** (`cc1` or `gcc -S`):
- Parses C code and builds an AST (Abstract Syntax Tree)
- Performs optimization (if `-O1`, `-O2`, `-O3` is specified)
- Generates assembly code or LLVM IR
- Result: `.s` file (assembly) or `.ll` (IR)

**3. Assembly** (`as` or `gcc -c`):
- Converts assembly code to machine code
- Creates an object file with symbols and relocation entries
- Result: `.o` file (object file)

**4. Linking** (`ld` or `gcc`):
- Combines all object files and libraries
- Resolves symbol references (external symbols)
- Places sections (.text, .data, .bss) according to the linker script
- Generates an executable or firmware image
- Result: `.elf` file (executable) or `.axf` (ARM)

**5. Post-build** (for firmware):
- `objcopy -O ihex firmware.elf firmware.hex` – Intel HEX format
- `objcopy -O binary firmware.elf firmware.bin` – Raw binary
- `objdump -h firmware.elf` – Section sizes
- `size firmware.elf` – Text/data/bss sizes
- Map file generation (`-Wl,-Map=firmware.map`)

Each stage can be run separately for debugging or analysis.

## Evaluation guide

### Expected signals
- Knows the main stages: preprocessing, compilation, assembly, linking
- Understands what each stage does
- Can name the tools for each stage (cpp, cc1, as, ld)
- Knows about post-build steps for firmware (objcopy, map file)

### Red flags
- Confuses compilation with linking
- Does not know that preprocessing is a separate stage
- Does not understand the difference between an object file and an executable
- Does not know how to get .hex/.bin from .elf

### Level-up follow-up
- How to view intermediate files (preprocessed, assembly)?
- What are relocation entries and why are they needed?
- How does the linker script affect section placement?

## Sources

<!-- generated from frontmatter -->

---
id: emb-build-0006
title: "Describe the stages of developing a library or program."
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
---

## Short answer

Typical cycle: requirements, API/architecture design, implementation, tests, integration, documentation, release, and maintenance.[^dou-embedded-interview] For a library it is especially important to define the public API, invariants, errors, dependencies, and version compatibility upfront.

In practice this means: write headers and function contracts, implement modules, add unit tests and usage examples, check edge cases, set up build/CI, document limitations. In embedded, memory checks, execution time, interrupt-safety, and behavior on target hardware are also added.

## Detailed explanation

Library or program development typically goes through several stages, each with its own goals and artifacts.[^gcc-overall-options]

**Requirements** – defining what the library/program should do. For a library this includes: which functions to export, which data types to support, which errors to return, which dependencies to use. It is important to define the public API – the interface that clients will use.

**API Design** – designing the interface. For a C library this is header files with function declarations, types, constants. For C++ – classes, methods, templates. It is important to consider ABI stability (whether the library can be updated without recompiling clients), backward compatibility, error handling strategy (returning error codes, errno, exceptions).

**Implementation** – writing code. Modular structure: each module is responsible for one functionality. Unit tests for each function. Code review for quality checking.

**Testing** – unit tests (checking individual functions), integration tests (checking module interaction), system tests (checking the entire system). For embedded, hardware-in-the-loop tests, stress tests, and memory leak detection are added.

**Integration** – connecting the library to the main program. For a static library – linking. For a shared library – setting up the runtime path. For embedded – checking firmware size, execution time, memory usage.

**Documentation** – API description, usage examples, limitations, known issues. For C libraries, Doxygen is typically used. It is important to document thread safety, reentrancy, error codes.

**Release** – versioning (semver: major.minor.patch), changelog, tagged release in VCS. For embedded – flashing to target hardware, validation testing.

**Maintenance** – bug fixes, security patches, new features. It is important to maintain backward compatibility within a major version.

For embedded, it is especially important: memory usage checks (stack, heap, flash), execution time (worst-case execution time – WCET), interrupt safety (whether it can be called from interrupt context), power consumption (for battery-powered devices).

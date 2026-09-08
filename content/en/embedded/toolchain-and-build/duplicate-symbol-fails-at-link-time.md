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

If you define a non-`static` function with the same name in two `.c`/`.cpp` files, compilation of each translation unit may succeed because each is compiled separately.[^dou-embedded-interview]

The error will usually occur at the **linking** stage: the linker will see two global symbols with the same name and emit a multiple definition / duplicate symbol error. If you make the functions `static`, each will have internal linkage and there will be no conflict between files. In C++, overloading is only possible if the signatures differ; the same signature still violates the ODR.

## Detailed explanation

When the compiler processes a `.c` or `.cpp` file, it creates an object file (`.o` or `.obj`) with symbols. Each non-`static` function or global variable becomes a global symbol in the object file. During compilation of each file separately, the compiler does not know about other translation units, so it cannot check for name conflicts.[^gcc-overall-options]

The linker collects all object files together and builds a symbol table. If it sees two global symbols with the same name (for example, `void process_data()` defined in `file1.c` and `file2.c`), it cannot decide which version to use and emits an error:

```
file2.o: In function `process_data':
file2.c:(.text+0x0): multiple definition of `process_data'
file1.o:file1.c:(.text+0x0): first defined here
```

If you make the functions `static`, each will have internal linkage and be visible only within its own translation unit. The linker will not see a conflict because internal symbols are not exported.

In C++ the situation is more complex due to name mangling. The compiler adds type information to the function name, so `void process(int)` and `void process(double)` have different mangled names. But if the signatures are the same, the ODR (One Definition Rule) is violated, and the linker still emits a duplicate symbol error.

In C there is an exception for `inline` functions in header files: if an `inline` function is defined in a header and included in multiple translation units, the linker picks one definition (usually the most optimized one). But this works only for `inline`, not for regular functions.


## Symptom

Linker error: `multiple definition of 'function_name'` or `duplicate symbol: _function_name`.

## Why it happens

Two translation units define a non-`static` function with the same name. The compiler does not check this during compilation of a single file, but the linker sees two global symbols and cannot decide which one to use.

## How to avoid

- Use `static` for functions needed only in one file
- For header-only libraries, use `inline` or `static inline`
- In C++, use anonymous namespaces instead of `static` for internal linkage
- Check that you are not defining a function in a header file without `inline`


## Sources

<!-- generated from frontmatter -->

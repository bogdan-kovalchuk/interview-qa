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

In Linux/Unix, functions from a shared library are typically exported as symbols in a `.so`.[^dou-embedded-interview] For a C API it is enough to not make the function `static`, compile with `-fPIC`, and link with `-shared`; visibility can be controlled via `__attribute__((visibility("default")))` and a linker version script.

In Windows DLLs, `__declspec(dllexport)` is typically used when building the library and `__declspec(dllimport)` on the consumer side, or a `.def` file. For C++ APIs, `extern "C"` is often added for stable C symbols, or C++ is exported with the ABI of a specific compiler in mind.

## Detailed explanation

In Linux/Unix, a shared library (`.so`) exports symbols through the dynamic symbol table. When the compiler builds a `.so`, it adds all non-static global symbols to the export table by default. For a C API it is enough to declare the function without the `static` keyword, compile with `-fPIC` (position-independent code), and link with `-shared`.[^gcc-overall-options]

For visibility control, `__attribute__((visibility("default")))` explicitly exports or `__attribute__((visibility("hidden")))` hides symbols. A linker version script (`.map` file) allows precise control over which symbols are exported:

```
LIBMYLIB_1.0 {
    global:
        my_public_function;
        my_other_function;
    local:
        *;
};
```

In Windows DLLs the mechanism is different. `__declspec(dllexport)` when building the library adds the symbol to the export table. `__declspec(dllimport)` on the consumer side tells the compiler that the function is in a DLL and needs to use an indirect call through the import address table (IAT). An alternative is a `.def` file with an `EXPORTS` section, which does not require source code modification.

For C++ APIs, `extern "C"` is added to prevent name mangling and ensure a stable ABI. Without it, the C++ compiler mangles names (adds type information to the function name), which complicates binary compatibility between compilers.

In embedded Linux, shared libraries are typically used to reduce firmware size (multiple programs can use one library) and to update libraries without recompiling the entire application. In bare-metal MCUs, static linking is usually used because there is no OS to load shared libraries at runtime.


## Sources

<!-- generated from frontmatter -->

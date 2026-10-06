---
id: emb-cppoop-0031
title: "Trap: why do methods inline into bare-metal access only with optimization (for example `-O2`) and not at `-O0`?"
description: "At -O0 GCC does not inline by default, so every set() stays a real function call with prologue and epilogue"
track: embedded
section: cpp-classes-and-oop
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents that without optimization GCC does not expand functions inline (-fno-inline is the default, except for functions with always_inline) and that -finline-small-functions is enabled at -O2, -O3 and -Os; the actual heuristic decisions depend on the code, and this source states nothing here about -O1 or -Og."
  - source_id: cpp-draft-class-mfct
    title: "C++ working draft: Member functions ([class.mfct])"
    url: https://eel.is/c++draft/class.mfct
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Confirms that a member function defined in its class body is inline; this alone does not guarantee that the body is substituted."
  - source_id: cpp-draft-dcl-inline
    title: "C++ working draft: The inline specifier ([dcl.inline])"
    url: https://eel.is/c++draft/dcl.inline
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that inline only indicates a preference for inline substitution and an implementation is not required to perform it."
---

## Short answer

<span class="warn">At `-O0` GCC does not expand functions inline by default, apart from those marked `always_inline`, so every `set()` stays a real function call.</span>[^gcc-optimize-options]

That is, the wrapper's "zero overhead" shows up only with optimization: `-finline-small-functions` is enabled at `-O2`, `-O3` and `-Os`,[^gcc-optimize-options] while in a debug build the wrapper class costs a call with prologue and epilogue.

Defence: measure the size and speed of C++ abstractions with release flags (`-O2`/`-Os`), not at `-O0`, and check the assembly.

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

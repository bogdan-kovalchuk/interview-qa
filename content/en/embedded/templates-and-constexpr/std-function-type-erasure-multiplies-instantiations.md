---
id: emb-tmplcx-0017
title: "Trap: why can `std::function` inflate Flash sharply?"
description: "std::function is template-heavy type erasure that can produce a lot of separate code for different signatures."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-func-wrap-func
    title: "C++ working draft: Class template function ([func.wrap.func])"
    url: https://eel.is/c++draft/func.wrap.func
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "The function class template is a call wrapper whose call signature is R(ArgTypes...). Does not define code size or Flash use."
  - source_id: cpp-draft-func-wrap-func-con
    title: "C++ working draft: Constructors and destructor ([func.wrap.func.con])"
    url: https://eel.is/c++draft/func.wrap.func.con
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "The template constructor accepts a callable F and stores it as an object of type decay_t<F>; dynamic memory may be allocated (bad_alloc may be thrown), and implementations are advised to avoid it for small callable objects. Does not define code size."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Defines when a function or class template is implicitly instantiated: when it is referenced in a context that requires a definition. Says nothing about binary size or code placement."
  - source_id: gnu-ld-print-map
    title: "GNU ld: Command-line options (-Map, --print-map)"
    url: https://sourceware.org/binutils/docs/ld/Options.html
    accessed: 2026-10-13
    kind: official
    version: "current"
    applicability: "Describes -Map=mapfile (link map written to a file) and --print-map (printed to stdout); map contents depend on the linker script and toolchain."
---

## Short answer

<span class="warn">`std::function` is template-heavy type erasure; different signatures and callable types can produce a lot of separate code.</span>

Each callable type `F` is stored as an object of type `decay_t<F>`.[^cpp-draft-func-wrap-func-con] Its template handlers are instantiated separately for each such type.[^cpp-draft-temp-inst]

Defense: for simple callbacks a function pointer + `void* context` is often sufficient. On flash-constrained MCUs check the size of `std::function` via the linker map.[^gnu-ld-print-map]

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

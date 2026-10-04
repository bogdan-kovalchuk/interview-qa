---
id: emb-macros-0035
title: "Trap: how can a macro in a header affect code that includes it?"
description: "After #define, a macro replaces tokens later in the same translation unit, including subsequently included headers; a separately compiled file does not inherit the definition."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: gcc-cpp-macro-processing
    title: "GCC CPP: Object-like Macros and Undefining and Redefining Macros"
    url: https://gcc.gnu.org/onlinedocs/cpp/Object-like-Macros.html
    accessed: 2026-10-04
    kind: official
    version: current
    applicability: "Sequential preprocessing, macro expansion, and #undef in GNU CPP; describes the typical C preprocessor workflow."
---

## Short answer

<span class="warn">A macro has no block or file scope</span>: after `#define`, the preprocessor replaces its name in the remaining text of the current translation unit, including headers included afterward. A separately compiled `.c` file does not automatically inherit the definition.[^gcc-cpp-macro-processing]

For example, `#define max(a,b) ...` in a header can break `std::max` or the field `obj.max` in the translation unit that includes it.[^gcc-cpp-macro-processing]

Use distinctive UPPER_CASE names with a project prefix to reduce collisions; remove a macro with `#undef` when it is no longer needed.[^gcc-cpp-macro-processing]

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

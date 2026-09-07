---
id: emb-tmplcx-0019
title: "Trap: how is `if constexpr` safer than `#ifdef` against mistakes?"
description: "#ifdef completely cuts out the unselected branch so syntax errors in it are never caught."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Short answer

<span class="warn">`#ifdef` completely cuts out the unselected branch – syntax errors/typos in it are never noticed.</span>

`if constexpr` forces the compiler to check the syntax of both branches (if they do not depend on a template parameter), so a bug in the "inactive" platform is caught immediately.

Defense: for platform switching prefer `if constexpr` – fewer hidden bugs in untested paths.[^embeddedinterviewlab]

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

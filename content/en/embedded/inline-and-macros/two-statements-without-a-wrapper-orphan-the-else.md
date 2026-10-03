---
id: emb-macros-0011
title: "Trap: why does this macro break `if/else`?"
description: "A macro without do-while-zero leaves else without a matching if and causes unconditional execution of trailing statements."
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
---

## Question code

```c
#define RST() a(); b()

if (err)
    RST();
else
    ok();
```

## Short answer

<span class="warn">Expands to `if (err) a(); b(); else ok();`</span> – `else` no longer has a matching `if` -> compile error, or (with a single statement) `b()` is always called.

Only `a()` belongs to the `if`, but the following `else` makes this example a syntax error; without `else`, the separate `b();` would run regardless of the condition.[^iso-c-n1570]

Fix: `#define RST() do { a(); b(); } while(0)` – then the whole block is bound to the `if`.[^iso-c-n1570]

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

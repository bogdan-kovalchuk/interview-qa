---
id: emb-fnptr-0040
title: "Trap: what is wrong with passing a non-static method as a C callback?"
description: "&App::on_rx has pointer-to-member type, not void (*)(uint8_t)."
track: embedded
section: function-pointers-and-callbacks
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
  - source_id: cppreference-member-pointers
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Explains the distinction between function pointers and C++ pointers to members; it does not specify a particular C callback API signature."
---

## Question code

```cpp
class App {
public:
    void on_rx(uint8_t b);
};

uart_register(&App::on_rx);
```

## Short answer

<span class="warn">`&App::on_rx` has pointer-to-member type, not `void (*)(uint8_t)`.</span>

The method needs a specific object for `this`. The C callback ABI does not know which object to call. Even if a cast forces the types to match, the call will be incorrect.

Protection: write `static void on_rx_thunk(void *ctx, uint8_t b) { static_cast<App *>(ctx)->on_rx(b); }` and register `this` as the context.[^cppreference-member-pointers]

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

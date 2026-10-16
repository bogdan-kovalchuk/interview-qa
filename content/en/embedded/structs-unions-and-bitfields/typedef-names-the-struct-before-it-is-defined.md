---
id: emb-structs-0050
title: "What does `typedef struct Foo Foo;` mean?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**It creates a typedef name `Foo` for the type `struct Foo`**, often before the struct is fully defined.

If the struct body is not given, `Foo` is an incomplete type. You can use `Foo *` in an API, but you cannot create a `Foo` object by value until the full definition.

Embedded use case: opaque handles for drivers: `Foo_Init(Foo *self)` or `Foo *Foo_Open(...)`.[^iso-c-n1570]

## Detailed explanation

TODO

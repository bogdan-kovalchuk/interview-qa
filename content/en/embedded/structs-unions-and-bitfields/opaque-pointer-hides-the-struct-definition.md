---
id: emb-structs-0035
title: "What is an opaque struct pointer in a C API?"
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

An **opaque pointer** hides the struct definition from the API user: the header contains only a forward declaration.

For example, `typedef struct UartDriver UartDriver;`, while the fields of `struct UartDriver` are defined only in the `.c` file. The caller works with `UartDriver *` through API functions and does not depend on the internal layout.

This lets the implementation change its internal layout without exposing fields to clients; ABI compatibility still depends on the entire public interface.[^iso-c-n1570]

## Detailed explanation

TODO

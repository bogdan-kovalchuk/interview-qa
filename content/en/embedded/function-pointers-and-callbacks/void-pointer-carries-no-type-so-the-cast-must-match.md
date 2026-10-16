---
id: emb-fnptr-0031
title: "Trap: why must `void *context` be cast back to the right type?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">A cast from `void *` does not check the type; undefined behavior occurs if the result is used to access the object incorrectly.</span>

`void *` carries no runtime type information. If a callback expects `struct Uart *` but receives a pointer to `struct Spi`, dereferencing it as `struct Uart` may violate alignment or typed-object access rules.[^iso-c-n1570]

Protection: use a typed registration API where possible; verify the object type; use a wrapper for incompatible contexts.[^iso-c-n1570]

## Detailed explanation

TODO

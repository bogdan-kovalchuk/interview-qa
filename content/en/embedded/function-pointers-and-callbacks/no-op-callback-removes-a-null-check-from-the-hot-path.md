---
id: emb-fnptr-0010
title: "For an optional callback, is a `NULL` check or a no-op function better?"
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

Both options are valid, but a no-op callback can simplify the hot path.[^iso-c-n1570]

If the callback is optional and called frequently, the driver can initialize it with `static void noop(void *ctx) { (void)ctx; }`. Then the call site has no `if (cb)` branch. But this must be documented so the callback pointer is never left uninitialized.

Rule: for a simple API a `NULL` check is often clearer; for a dispatch table a no-op entry may simplify the common call path, but it does not guarantee a performance gain.[^iso-c-n1570]

## Detailed explanation

TODO

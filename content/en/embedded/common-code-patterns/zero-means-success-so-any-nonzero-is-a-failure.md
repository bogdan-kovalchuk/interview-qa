---
id: emb-patterns-0019
title: "Why do many APIs use zero for `ERR_OK`?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**So that `0` means success and any non-zero value means an error** (truthiness).

Then `if (result) { handle_error(); }` and `if (sensor_read(...) != ERR_OK)` work naturally. This is the typical convention of a HAL (hardware abstraction layer) and many POSIX-like APIs (application programming interface): 0 = success, non-zero/negative value = error.

Rule: in an error enum `ERR_OK = 0` comes first; real codes are non-zero.[^iso-c-n1570]

## Detailed explanation

TODO

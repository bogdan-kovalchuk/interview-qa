---
id: emb-dtypes-0043
title: "Find the bug: `int sum; for(int i = 0; i < n; i++) sum += arr[i];`"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

An uninitialized automatic local `int sum;` has an indeterminate value. For an ordinary automatic object in C, reading that uninitialized value is undefined behavior; it is not necessarily “stack garbage.”[^iso-c-n1570]

Initialize the accumulator explicitly, for example `int sum = 0;`, before adding elements.[^iso-c-n1570]

## Detailed explanation

TODO

---
id: emb-fnptr-0048
title: "How do you declare a function that returns a function pointer?"
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

Example without typedef:

`int (*select_op(int id))(int, int);`

This means: `select_op` takes an `int` and returns a pointer to a function that takes two `int` values and returns an `int`. With a typedef it is cleaner: `typedef int (*op_t)(int, int); op_t select_op(int id);`

Rule: if a declaration is hard to read at first glance, a typedef usually makes the type clearer.[^iso-c-n1570]

## Detailed explanation

TODO

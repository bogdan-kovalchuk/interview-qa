---
id: emb-macros-0015
title: "What is an include guard and which problem does it solve?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
#ifndef SENSOR_H
#define SENSOR_H
/* вміст header */
#endif
```

## Short answer

**An include guard prevents a header from being included more than once** in the same translation unit.

Without it, repeated inclusion can repeat a type or object definition and cause a diagnostic; compatible repeated function declarations are allowed by themselves. On the first pass `SENSOR_H` is defined, and later passes skip the conditional block.

Use a guard name specific enough to the project to avoid macro collisions.[^iso-c-n1570]

## Detailed explanation

TODO

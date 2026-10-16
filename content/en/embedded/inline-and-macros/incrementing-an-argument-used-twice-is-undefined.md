---
id: emb-macros-0046
title: "Trap: how many times is `a` incremented?"
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
#define SQR(x) ((x) * (x))
int a = 2;
int b = SQR(a++);
```

## Short answer

<span class="warn">The C standard does not define this expression's result: this is undefined behavior.</span>

The macro substitutes the argument in two places: `((a++) * (a++))`. Parentheses save you from precedence issues, but not from double evaluation. Two increments of the same scalar object within one expression are unsequenced relative to each other, so the C standard defines neither the multiplication result nor the final value of `a`.

Fix: correct parentheses do not cure side effects; for arguments with effects, use a `static inline` function or a local variable assigned before the macro.[^iso-c-n1570]

## Detailed explanation

TODO

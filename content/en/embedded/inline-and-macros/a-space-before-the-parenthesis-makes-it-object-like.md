---
id: emb-macros-0040
title: "Trap: why is this not a function-like macro?"
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
#define F (x) (x) * (x)
int r = F(3);
```

## Short answer

<span class="warn">The space between `F` and `(x)` makes it an object-like macro.</span>

The preprocessor sees the name `F` replaced with the entire text `(x) (x) * (x)`. Then `F(3)` expands to `(x) (x) * (x)(3)` – it uses an undefined `x`, an obvious error.

Fix: in a function-like macro the opening parenthesis `(` must follow the name immediately, with no space: `#define F(x) ((x) * (x))`.[^iso-c-n1570]

## Detailed explanation

TODO

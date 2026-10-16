---
id: emb-macros-0014
title: "Trap: why does `STR(__LINE__)` give `\"__LINE__\"` instead of the line number?"
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
#define STR(x) #x
```

## Short answer

<span class="warn">`#` stringifies the argument spelling without expanding it first</span>, so `STR(__LINE__)` produces the string `"__LINE__"`.

To get the line number as text, add an intermediate level: expand the macro first, then stringify:

```c
#define STR(x) #x
#define XSTR(x) STR(x)
// XSTR(__LINE__) expands to the current line number as a string
```

This is the standard two-level stringification pattern.[^iso-c-n1570]

## Detailed explanation

TODO

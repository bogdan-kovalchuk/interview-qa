---
id: emb-macros-0041
title: "How do you generate a unique variable name from the line number?"
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
#define CAT(a, b) a##b
#define XCAT(a, b) CAT(a, b)
#define UNIQUE(p) XCAT(p, __LINE__)
```

## Short answer

**Two levels are needed**: `CAT` pastes tokens, while `XCAT` first expands `__LINE__` into a number before pasting.

Then `int UNIQUE(tmp_);` on line 42 yields `int tmp_42;`. Used for scope guards, RAII helpers, test macros.

Rule: an extra level is needed when an argument must expand before `##` is applied; pasting itself suppresses prior expansion of the corresponding parameter.[^iso-c-n1570]

## Detailed explanation

TODO

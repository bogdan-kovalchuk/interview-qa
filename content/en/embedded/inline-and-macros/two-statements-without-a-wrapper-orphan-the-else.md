---
id: emb-macros-0011
title: "Trap: why does this macro break `if/else`?"
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
#define RST() a(); b()

if (err)
    RST();
else
    ok();
```

## Short answer

<span class="warn">Expands to `if (err) a(); b(); else ok();`</span> – `else` no longer has a matching `if` -> compile error, or (with a single statement) `b()` is always called.

Only `a()` belongs to the `if`, but the following `else` makes this example a syntax error; without `else`, the separate `b();` would run regardless of the condition.[^iso-c-n1570]

Fix: `#define RST() do { a(); b(); } while(0)` – then the whole block is bound to the `if`.[^iso-c-n1570]

## Detailed explanation

TODO

---
id: emb-fnptr-0017
title: "Why does casting a function pointer often hide the real bug?"
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

<span class="warn">A cast disables type checking but does not change the actual function signature.</span>

If the API expects `void (*)(void *)` and you pass `void (*)(int)` through a cast, the caller still invokes the function according to the API contract. Arguments will be passed differently from what the callee expects. This is not portable and may be UB.

Defense: write a thin wrapper: `static void wrapper(void *ctx) { real_handler((int)(intptr_t)ctx); }`, if that model is truly needed.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

TODO

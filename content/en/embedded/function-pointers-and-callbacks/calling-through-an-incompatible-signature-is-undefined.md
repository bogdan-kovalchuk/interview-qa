---
id: emb-fnptr-0016
title: "Trap: what is wrong with calling a callback through an incompatible signature?"
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

## Question code

```c
void f(int x);
void (*cb)(void) = (void (*)(void))f;
cb();
```

## Short answer

<span class="warn">Calling through a function pointer of an incompatible type is undefined behavior.</span>

Even if the function address is physically correct, the calling convention expects different arguments, return value, or register usage. On an embedded ABI this can corrupt the stack/registers or pass garbage values.

Defense: do not fix the `-Wincompatible-pointer-types` warning with a cast. Write an adapter function with the correct signature.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

TODO

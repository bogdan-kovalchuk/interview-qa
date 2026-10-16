---
id: emb-cppfound-0080
title: "What does this code print?"
track: embedded
section: c-in-embedded
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
int x=42;
void *p=&x;
printf("%d", *(int*)p);
```

## Short answer

`42`.

`void *p = &x` is allowed in C (implicit conversion); `p` holds the address of `x`, but the type is "erased".

`*(int*)p` – cast to `int*`, then dereference. Correct because `p` points to an actual `int`.

If cast to the wrong type: `*(float*)p` -> UB (strict aliasing), so the rule is: always cast `void*` back to the type it was obtained from.[^embeddedinterviewlab]

## Detailed explanation

TODO

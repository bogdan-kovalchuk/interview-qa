---
id: emb-cppfound-0080
title: "Що виведе?"
track: embedded
section: pointers-and-arrays
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

`void *p = &x` – дозволено у C (implicit conversion), `p` зберігає адресу `x`, але тип "erased".

`*(int*)p` – cast до `int*`, потім розіменування. Коректно оскільки `p` вказує на справжній `int`.

Якби cast до неправильного типу: `*(float*)p` -> UB (strict aliasing), тож правило: cast `void*` завжди до того типу, з якого він був отриманий.[^embeddedinterviewlab]

## Detailed explanation

TODO

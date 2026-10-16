---
id: emb-structs-0019
title: "What is wrong with this variant payload?"
track: embedded
section: structs-unions-and-bitfields
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
union Payload {
    uint16_t temperature;
    uint32_t pressure;
};

union Payload p;
```

## Short answer

<span class="warn">A `union` does not store a tag indicating which member is currently intended.</span>

A `union` lets different variants share storage, but it does not store a discriminator. If the receiver does not know the payload type from a header or enum, reading another member is not a reliable way to identify the payload type or value.[^iso-c-n1570]

Defense: store the discriminator separately, for example in `struct Message { enum Type type; union Payload payload; };`, and check it before accessing the corresponding member.[^iso-c-n1570]

## Detailed explanation

TODO

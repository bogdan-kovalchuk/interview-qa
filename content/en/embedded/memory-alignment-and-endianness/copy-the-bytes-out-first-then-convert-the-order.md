---
id: emb-align-0022
title: "How do you deserialise a byte buffer back into a struct?"
track: embedded
section: memory-alignment-and-endianness
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
uint32_t ts; uint16_t v;
memcpy(&ts, &buf[0], 4);
memcpy(&v,  &buf[4], 2);
r->ts  = ntohl(ts);
r->val = ntohs(v);
r->id  = buf[6];
```

## Short answer

**First read the bytes safely via `memcpy`, then convert from network to host order.**

The order is the mirror of serialization; offsets must match the defined wire format exactly.

Rule: `memcpy` from a `uint8_t*` into an aligned variable lets you read multi-byte fields even from an unaligned buffer.[^iso-c-n1570][^embeddedinterviewlab]

## Detailed explanation

TODO

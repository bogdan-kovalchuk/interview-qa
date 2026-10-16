---
id: emb-dtypes-0108
title: "How to safely parse a binary protocol frame without invalid type punning and alignment issues?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Check the frame length, then read each field from the `uint8_t` buffer via `memcpy` or byte shifts. For multi-byte fields, explicitly apply `le16toh`/`ntohs` or a custom conversion. <span class="warn">Do not cast a wire-format buffer to a struct</span> unless layout, packing, alignment, and endianness are fixed and verified.[^iso-c-n1570]

## Detailed explanation

TODO

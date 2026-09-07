---
id: emb-structs-0005
title: "Яким буде типовий розмір після перестановки полів?"
description: "Типово sizeof(struct S) == 8 на ABI, де uint32_t має alignment 4."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
struct S {
    uint32_t b;
    uint8_t a;
    uint8_t c;
};
```

## Short answer

Типово `sizeof(struct S) == 8` на ABI, де `uint32_t` має alignment 4.

`b` займає offset 0..3, `a` offset 4, `c` offset 5, потім 2 байти tail padding, щоб розмір структури був кратним 4. Це менше за 12 байт у варіанті `uint8_t, uint32_t, uint8_t`.

Embedded-висновок: у масиві з 1000 елементів така перестановка економить приблизно 4 KB.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

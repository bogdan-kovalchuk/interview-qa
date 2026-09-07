---
id: emb-structs-0013
title: "Чому pointer на packed поле може бути небезпечним?"
description: "&pkt.value може бути unaligned address для uint32_t ."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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

## Short answer

```c
struct __attribute__((packed)) P {
    uint8_t tag;
    uint32_t value;
};

uint32_t *p = &pkt.value;
```

<span class="warn">`&pkt.value` може бути unaligned address для `uint32_t *`.</span>

Звичайний `uint32_t *` несе припущення, що адреса достатньо вирівняна для `uint32_t`. Якщо поле packed, це припущення може бути хибним. Розіменування такого pointer може бути undefined behavior або fault на MCU.

Захист: не бери pointer на packed multi-byte fields; використовуй `memcpy(&tmp, &pkt.value, sizeof tmp)` або byte parser.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

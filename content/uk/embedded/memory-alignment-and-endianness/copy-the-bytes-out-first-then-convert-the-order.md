---
id: emb-align-0022
title: "Як десеріалізувати байтовий буфер назад у структуру?"
description: "Спершу безпечно зчитай байти через memcpy, потім конвертуй з network у host order."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
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
uint32_t ts; uint16_t v;
memcpy(&ts, &buf[0], 4);
memcpy(&v,  &buf[4], 2);
r->ts  = ntohl(ts);
r->val = ntohs(v);
r->id  = buf[6];
```

**Спершу безпечно зчитай байти через `memcpy`, потім конвертуй з network у host order.**

Порядок дзеркальний до серіалізації; зсуви мають точно збігатися з визначеним wire-форматом.

Правило: `memcpy` з `uint8_t*` у вирівняну змінну дозволяє читати багатобайтові поля навіть із невирівняного буфера.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

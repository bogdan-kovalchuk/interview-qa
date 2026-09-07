---
id: emb-fnptr-0029
title: "Trap: що не так із таким context pointer?"
description: "&app стає dangling pointer після повернення з init."
track: embedded
section: function-pointers-and-callbacks
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
void init(void) {
    struct App app;
    timer_register(on_timer, &app);
}
```

<span class="warn">`&app` стає dangling pointer після повернення з `init`.</span>

Якщо timer callback спрацює пізніше, він отримає адресу stack object-а, якого вже не існує. На MCU це може виглядати як випадкова корупція стану, HardFault або нестабільний баг.

Захист: зроби `app` static/global, збережи його в caller-owned storage, або unregister callback до завершення lifetime object-а.[^embeddedinterviewlab]

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

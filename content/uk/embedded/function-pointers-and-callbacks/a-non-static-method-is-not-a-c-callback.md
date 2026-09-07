---
id: emb-fnptr-0040
title: "Trap: що не так із передачею нестатичного методу як C callback?"
description: "&App::on_rx має тип pointer-to-member, не void ()(uint8_t)."
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

## Question code

```cpp
class App {
public:
    void on_rx(uint8_t b);
};

uart_register(&App::on_rx);
```

## Short answer

<span class="warn">`&App::on_rx` має тип pointer-to-member, не `void (*)(uint8_t)`.</span>

Метод потребує конкретний object для `this`. C callback ABI не знає, який object викликати. Навіть якщо cast-ом змусити типи збігтися, виклик буде неправильний.

Захист: зроби `static void on_rx_thunk(void *ctx, uint8_t b) { static_cast<App *>(ctx)->on_rx(b); }` і зареєструй `this` як context.[^embeddedinterviewlab]

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

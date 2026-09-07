---
id: emb-patterns-0021
title: "Trap: у чому небезпека sentinel-значень для помилок?"
description: "Працює лише якщо sentinel-значення ніколи не буває валідним даним."
track: embedded
section: common-code-patterns
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
uint16_t adc_read(uint8_t ch) {
  if (ch >= NUM_CH) return UINT16_MAX; // "invalid"
  // ...
}
```

<span class="warn">Працює лише якщо sentinel-значення ніколи не буває валідним даним.</span>

Якщо `UINT16_MAX` – легітимне показання ADC (analog-to-digital converter), викликач не відрізнить помилку від реального максимуму.

Захист: sentinel – для випадків, де спеціальне значення фізично неможливе; інакше – return code + output pointer.[^embeddedinterviewlab]

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

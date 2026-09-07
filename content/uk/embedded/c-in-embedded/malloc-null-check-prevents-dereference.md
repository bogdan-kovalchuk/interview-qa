---
id: emb-cppfound-0084
title: "Навіщо завжди перевіряти повернення `malloc` на NULL?"
description: "Why failed allocation must be handled before dereferencing the result."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`malloc` повертає **NULL** при помилці виділення (нема пам'яті, heap fragmentation). Якщо не перевірити і розіменувати NULL -> <span class="warn">HardFault на MCU</span>.

```c
int *p = malloc(n * sizeof(int));
if(p == NULL) { error_handler(); return; }
// Тепер безпечно використовувати
```

У embedded: malloc може провалитися навіть при малих запитах через fragmentation. Safety-critical стандарти забороняють malloc взагалі – але якщо використовуєш, перевірка обов'язкова.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

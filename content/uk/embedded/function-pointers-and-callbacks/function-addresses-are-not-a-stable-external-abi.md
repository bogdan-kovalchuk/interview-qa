---
id: emb-fnptr-0055
title: "Trap: чому адреси function pointers не варто серіалізувати або зберігати у Flash config?"
description: "Адреси функцій не є стабільним зовнішнім ABI."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 2
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

<span class="warn">Адреси функцій не є стабільним зовнішнім ABI.</span>

Після rebuild, link-time optimization, зміни linker script або firmware update адреси зміняться. На MCU з bootloader/application layout адреса може залежати від slot-а. Виклик старої збереженої адреси може перейти в неправильний код.

Захист: серіалізуй symbolic ID/opcode, а не function address, і після boot обирай handler через актуальну dispatch table.[^embeddedinterviewlab]

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

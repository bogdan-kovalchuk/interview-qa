---
id: emb-align-0037
title: "Навіщо під час розробки вмикати `UNALIGN_TRP` на M3/M4?"
description: "Щоб деякі підтримувані процесором misaligned accesses завершувалися UsageFault під час налагодження."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: arm-cortex-m3-trm
    title: "Arm Cortex-M3 Technical Reference Manual"
    url: https://documentation-service.arm.com/static/6036810d5319e554d4ba108e
    accessed: 2026-10-04
    kind: official
    version: "DDI 0337E"
    applicability: "Описує підтримку unaligned доступів і біт UNALIGN_TRP у Cortex-M3; конкретні інструкції мають різні правила."
  - source_id: arm-cortex-m4-guide
    title: "Cortex-M4 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/5f2ac76d60a93e65927bbdc5
    accessed: 2026-10-04
    kind: official
    version: "DUI 0553B"
    applicability: "Описує перелік unaligned load/store інструкцій Cortex-M4 та рекомендацію застосовувати UNALIGN_TRP; це не універсальна гарантія для всіх доступів."
---

## Short answer

**Щоб деякі misaligned accesses завершувалися явним UsageFault під час налагодження.**

M3/M4 підтримують unaligned доступи лише для частини load/store інструкцій; інші інструкції вже fault-яться. `UNALIGN_TRP` у `SCB->CCR` змушує підтримувані unaligned доступи викликати UsageFault, але не діагностує всі порушення alignment у коді C.[^arm-cortex-m3-trm] [^arm-cortex-m4-guide] [^iso-c-n1570]

Використовуй цей режим як додаткову перевірку на конкретному ядрі, а в коді дотримуйся alignment-вимог мови та платформи.[^arm-cortex-m4-guide] [^iso-c-n1570]

## Detailed explanation

`UNALIGN_TRP` – біт у Configuration and Control Register, який на відповідних ядрах Cortex-M налаштовує реакцію на частину unaligned load/store операцій. Його призначення під час розробки – перетворити деякі доступи, що інакше виконалися б із додатковими циклами, на UsageFault, аби місце помилки було помітним у debugger.[^arm-cortex-m3-trm] [^arm-cortex-m4-guide]

Це не універсальний детектор усіх неправильних адрес. На Cortex-M4 лише визначені інструкції, зокрема `LDR`, `LDRH`, `STR` і `STRH`, підтримують unaligned доступ; решта load/store інструкцій fault-яться незалежно від цього біта. Деякі області пам’яті також можуть не підтримувати unaligned операції. Поведінка залежить від ядра, конкретної інструкції та області пам’яті, тож звіряйся з документацією потрібного MCU.[^arm-cortex-m4-guide]

Рівень C окремий: приведення адреси до typed pointer не гарантує вирівнювання. Якщо результат не вирівняний для цільового типу, розіменування має undefined behavior навіть тоді, коли певний процесор іноді завершує відповідну інструкцію успішно. Тому `UNALIGN_TRP` допомагає знаходити апаратні випадки, але не робить некоректний cast допустимим і не замінює перевірку коду та compiler warnings.[^iso-c-n1570]

**Приклад:**

Якщо debugger зупинився на UsageFault після ввімкнення `UNALIGN_TRP`, перевір адресу операнда, ширину доступу й згенеровану інструкцію. Для байтового формату краще читати через `unsigned char` або копіювати в належно вирівняний об’єкт, а не вимикати trap і покладатися на поведінку одного ядра. Таке виправлення усуває причину й зберігає переносимість між MCU.[^arm-cortex-m4-guide] [^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

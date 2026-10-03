---
id: emb-volconst-0047
title: "Що означає `const volatile` для memory-mapped device ID register?"
description: "Firmware не має права записувати register, але повинна читати його як volatile hardware value."
track: embedded
section: volatile-and-const
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 3
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
---

## Short answer

**`const volatile` забороняє запис через цей lvalue і зберігає семантику volatile-доступу.**

Device ID може бути read-only з точки зору firmware, але його значення надає hardware. `const` і `volatile` задають різні властивості доступу; вони не гарантують фізичну незмінність або конкретну поведінку пристрою.[^iso-c-n1570]

Для memory-mapped register використай `const volatile` лише коли документація MCU визначає register як доступний тільки для читання.[^iso-c-n1570]

## Detailed explanation

`const volatile` поєднує дві незалежні кваліфікації типу C: через такий lvalue програма не може модифікувати об’єкт, а доступ до нього лишається volatile-доступом. Це відповідає типовій моделі read-only device register: firmware читає значення, яке належить периферії.[^iso-c-n1570]

`const` не означає, що байти фізично не можуть змінитися. Воно обмежує модифікацію через конкретний типізований шлях доступу. Інший агент, наприклад hardware, DMA або інший alias, може змінювати пам’ять; qualifier `volatile` повідомляє реалізації C про важливість volatile-доступів, але не визначає, як саме шина взаємодіє з периферією.[^iso-c-n1570]

Для прикладу, declaration на кшталт `const volatile uint32_t * const DEVICE_ID` має два рівні `const`: покажчик не можна перенаправити, а через нього не можна записати у значення. `volatile` стосується об’єкта за адресою. Тип треба звірити з документацією: деякі status registers мають write-one-to-clear біти або окремі правила читання, тому механічно вважати будь-який ID register безпечним для читання не варто.[^iso-c-n1570]

**Типова помилка:** прибрати `volatile`, бо ID «ніколи не змінюється». Значення може бути стабільним, однак вимога до кожного доступу є окремою від того, чи очікується зміна. Так само `const volatile` не робить читання atomic і не є загальним механізмом синхронізації; воно описує доступ, а не протокол взаємодії пристрою.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

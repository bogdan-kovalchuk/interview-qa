---
id: emb-structs-0039
title: "Чим відрізняються assignment і `memcpy` для структур?"
description: "Structure assignment копіює значення всіх members; padding bytes не мають гарантованого значення."
track: embedded
section: structs-unions-and-bitfields
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

**Structure assignment копіює значення всіх members структури**, але не гарантує збереження padding bytes.

`memcpy` копіює object representation байт за байтом, включно з padding. Стандарт C дозволяє padding bytes набувати unspecified values під час запису значення структури, тому assignment і `memcpy` не обіцяють однакове представлення в пам’яті.

Для копіювання структури в C використовуй assignment, а для wire/storage serialization кодуй поля явно, не покладаючись на padding або layout конкретного компілятора.[^iso-c-n1570]

## Detailed explanation

Structure assignment копіює значення кожного member з однієї структури до іншої сумісного типу; воно не визначає операцію як побайтове клонування пам’яті. Це важливо, бо компілятор може вставляти padding між members або наприкінці структури, щоб задовольнити alignment вимоги. Padding не є окремим member і не має прикладного значення.[^iso-c-n1570]

`memcpy(&dst, &src, sizeof src)` працює на іншому рівні: копіює кожен байт object representation. Це зручно для копіювання локального POD-подібного значення в межах тієї самої програми, але отримані байти не стають переносимим форматом. Розмір типів, byte order, padding та представлення деяких значень залежать від реалізації. Стандарт також визначає, що padding bytes структури отримують unspecified values під час запису значення, зокрема при structure assignment; тому не можна спиратися на їхню стабільність між копіями.[^iso-c-n1570]

Приклад: якщо `struct S` має `uint8_t kind` і `uint32_t count`, між полями може бути padding, але його наявність і точний розмір залежать від ABI. Assignment гарантує коректне значення `kind` і `count`; `memcmp` або запис `sizeof(struct S)` у файл включає також байти представлення, які не є частиною цих значень.[^iso-c-n1570]

**Типові помилки:**

- Вважати, що assignment обов’язково копіює padding так само, як `memcpy`.
- Надсилати raw representation структури як мережевий пакет або формат файлу.
- Порівнювати структури через `memcmp`, замість порівняння потрібних members.

Якщо потрібен стабільний протокол, задай ширину, byte order і кодування кожного поля явно. Це також дає змогу змінювати внутрішній layout структури без зміни зовнішнього формату.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

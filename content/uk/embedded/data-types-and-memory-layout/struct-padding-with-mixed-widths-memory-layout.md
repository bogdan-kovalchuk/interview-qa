---
id: emb-dtypes-0018
title: "Намалюйте memory layout без packing `struct { uint8_t a; uint32_t b; uint8_t c; }`"
description: "Компілятор вставляє padding між uint8_t і uint32_t полями, тож struct займає 12, а не 6 байт."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

За типової ABI, де `uint32_t` має розмір і вирівнювання 4 байти: `a` @ offset 0 (1B) -> <span class="warn">3B padding</span> -> `b` @ offset 4 (4B) -> `c` @ offset 8 (1B) -> <span class="warn">3B trailing padding</span>.

За цих припущень разом **12 байт**. Компілятор може додати padding для вирівнювання полів і розміру структури; точні offsets та `sizeof` залежать від ABI й реалізації.[^iso-c-n1570]

Перестановка полів часто зменшує padding на цільовій ABI, але результат треба перевірити через `sizeof` та `offsetof`; стандарт не гарантує, що альтернативний порядок дасть рівно 8 байт.[^iso-c-n1570]

## Detailed explanation

Компілятор має забезпечити, щоб кожне поле структури мало адресу, придатну для вимог вирівнювання його типу. Через це між полями можуть бути невикористані байти padding; вони входять до `sizeof` структури, хоча не є окремими полями. C гарантує порядок адрес полів у порядку оголошення, але конкретні вимоги alignment і кількість padding залежать від реалізації та ABI.[^iso-c-n1570]

Для наведеного поширеного випадку припустімо, що `uint8_t` має alignment 1, а `uint32_t` – розмір і alignment 4. Після байта `a` наступна адреса, кратна 4, має offset 4, тож перед `b` потрібні три байти. Після `b` поле `c` розміщується на offset 8. Структура мусить мати розмір, кратний її alignment, аби елементи масиву структури теж вирівнювалися; тому додаються три кінцеві байти, і `sizeof` дорівнює 12 за цих умов.[^iso-c-n1570]

Якщо розмістити `uint32_t` першим, на типовій 32-бітній ABI два байти `uint8_t` можуть поміститися після нього, а загальний розмір часто становить 8 байт. Це оптимізація для конкретної ABI, не переносима гарантія. Перевіряйте `sizeof`, `_Alignof` і `offsetof` для фактичного target; для wire format або регістрів периферії не покладайтеся на неявний layout C-структури.

Навіть коли сумарний розмір збігається, padding bytes можуть містити невизначені значення, тому байтове порівняння структур через `memcmp` не завжди еквівалентне порівнянню їхніх полів. Якщо формат має точні offsets, задавайте серіалізацію по байтах або використовуйте перевірену специфікацію ABI, а не виводьте її з одного запуску компілятора.

**Типова помилка:** запам’ятати число 12 як властивість мови. Воно випливає з конкретних розмірів та alignment; інша ABI або packing option може змінити layout.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

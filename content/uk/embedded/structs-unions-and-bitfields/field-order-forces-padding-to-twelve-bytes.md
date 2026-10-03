---
id: emb-structs-0003
title: "Яким буде типовий розмір `struct S` за 4-byte alignment для `uint32_t`?"
description: "За ABI, де `uint32_t` має 4-byte alignment, типовий sizeof(struct S) дорівнює 12 байтам."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
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

## Question code

```c
struct S {
    uint8_t a;
    uint32_t b;
    uint8_t c;
};
```

## Short answer

За поширеної ABI, де `uint8_t` має розмір та alignment 1 байт, а `uint32_t` – розмір та alignment 4 байти, `sizeof(struct S) == 12`.[^iso-c-n1570]

У такому layout `a` має offset 0, `b` – offset 4, `c` – offset 8, а після `c` іде tail padding. Розмір залежить від ABI; позначка 32-bit сама по собі не гарантує цих offsets.[^iso-c-n1570]

Порядок полів впливає на footprint, бо padding повторюється в кожному елементі масиву структур.[^iso-c-n1570]

## Detailed explanation

Розмір `struct S` становить 12 байтів за поширеної ABI, де `uint8_t` має розмір і alignment 1 байт, а `uint32_t` – розмір і alignment 4 байти. Ці припущення важливі: стандарт C дозволяє padding, але не встановлює цей точний layout для кожної цілі.[^iso-c-n1570]

Компілятор розташовує `a` за offset 0. Перед `b` потрібне місце, кратне його alignment, тому після `a` з’являються три байти padding, а `b` починається з offset 4 і займає байти 4–7. Поле `c` має offset 8. Структура має врахувати alignment своїх членів і для наступного об’єкта масиву, тому за цих умов наприкінці розміщуються ще три байти tail padding.[^iso-c-n1570]

Для масиву з `N` елементів footprint становить `N * sizeof(struct S)`, тобто тут `12 * N` байтів. Padding повторюється між кожною парою елементів, а не виникає один раз для всього масиву. Перестановка полів може зменшити окремі проміжки, але змінює offsets і може порушити зовнішній формат, на який покладається hardware чи код обміну.[^iso-c-n1570]

**Приклад:** для `struct S arr[10]` очікуваний розмір за цією ABI – 120 байтів. Це розрахунок за умовою про `sizeof(struct S) == 12`, а не універсальна гарантія для будь-якого 32-bit MCU.

**Типова помилка:** виводити розмір лише з ширини вказівника або назви архітектури. ABI визначає розміри й alignment типів; перед оптимізацією RAM/Flash перевірте `sizeof` та `offsetof` тим самим компілятором і прапорцями, якими збирається firmware.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

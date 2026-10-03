---
id: emb-structs-0011
title: "Що таке `packed` структура?"
description: "Packed structure просить компілятор не вставляти звичайний padding між полями або зменшити alignment структури."
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
  - source_id: gcc-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Документація GCC для розширень атрибутів і їхніх обмежень."
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

**Packed structure** просить компілятор не вставляти звичайний padding між полями або зменшити alignment структури.

Це корисно для wire-format headers, on-flash records або точно заданого binary layout. Але packed може створити unaligned accesses: поле `uint32_t` може опинитися на offset 1, що на деяких MCU повільно або навіть fault.

Правило: packed застосовують на межі формату, а не як універсальний спосіб економити RAM. Для internal data краще переставити поля.[^gcc-attributes]

## Detailed explanation

`packed` – це розширення компілятора, яке просить використати щільніше розміщення членів структури й зменшити звичайне вирівнювання, коли це підтримує конкретний toolchain. У стандарті C немає атрибута `__attribute__((packed))`; його значення, область дії та взаємодію з ABI визначає компілятор.[^gcc-attributes]

У типовій непакованій структурі компілятор може вставити padding перед полем, щоб його адреса відповідала alignment типу, а також наприкінці структури, щоб елементи масиву залишалися вирівняними. Для структури з `uint8_t tag` і `uint32_t value` це часто означає padding між полями. GNU `packed` просить прибрати таке проміжне вирівнювання та дає полям щільне розміщення, але точні правила слід перевіряти для вибраного компілятора й цілі.[^gcc-attributes]

**Приклад:**

Якщо `tag` займає один байт, `value` може починатися одразу з наступного байта в packed-представленні. Це заощаджує простір і може відповідати wire format або формату запису у Flash. Проте адреса `value` тоді може не задовольняти природне вирівнювання `uint32_t`, а доступ стає потенційно дорожчим або непідтримуваним цільовим процесором.[^gcc-attributes]

**Типові помилки:**

- Вважати `packed` переносимою частиною мови C або гарантією однакового бінарного формату між компіляторами.
- Застосовувати його до внутрішніх структур без вимоги зовнішнього формату, очікуючи безумовного виграшу швидкості чи пам’яті.
- Забувати про byte order, розмір типів, версію формату та alignment при серіалізації.

Для внутрішніх даних спершу можна переставити поля так, щоб зменшити padding без втрати природного alignment. На межі протоколу часто надійніше явно кодувати й декодувати байти, аніж трактувати довільний буфер як packed C-структуру. Якщо packed layout є частиною контракту, зафіксуйте компілятор і ABI та перевіряйте `sizeof` і offsets assertions-ами.[^gcc-attributes]

## Sources

<!-- generated from frontmatter -->

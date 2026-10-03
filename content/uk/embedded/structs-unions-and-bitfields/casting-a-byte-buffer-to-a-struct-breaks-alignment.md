---
id: emb-structs-0045
title: "Trap: чому overlay структури на raw buffer може порушити alignment?"
description: "buf має alignment для uint8_t, не обов’язково для struct Header."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
uint8_t buf[8];
struct Header *h = (struct Header *)buf;
```

## Short answer

<span class="warn">Адреса `buf` не гарантовано задовольняє alignment для `struct Header`.</span> Перетворення невирівняного pointer на pointer до типу з суворішим alignment уже має undefined behavior за C; розіменування такого pointer також небезпечне.[^iso-c-n1570]

Масив `uint8_t` не стає `struct Header` через cast; читання через `h` може порушити effective type rules.

Безпечніше розбирати байти явно або копіювати їх у справжній локальний `struct Header` через `memcpy`, попередньо перевіривши довжину, поля, endian та binary layout протоколу.[^iso-c-n1570]

## Detailed explanation

Перетворення pointer на `uint8_t`-буфер до `struct Header *` не гарантує ані потрібного alignment, ані того, що в буфері існує об’єкт цього типу.[^iso-c-n1570]

Alignment – це вимога до адреси, на якій дозволено розташувати об’єкт певного типу. Адреса масиву байтів має задовольняти вимогу його елемента, але стандарт не обіцяє, що ця сама адреса підходить для будь-якої структури. Якщо адресу неможливо коректно вирівняти для цільового типу, саме перетворення pointer має undefined behavior; на деяких MCU апаратний невирівняний доступ додатково викликає fault, а на інших може бути повільним або виконуватися з обмеженнями.[^iso-c-n1570]

Навіть правильне alignment не розв’язує питання типу. `buf` є оголошеним масивом байтів, а не об’єктом `struct Header`; доступ до його вмісту через несумісний lvalue може порушити effective type / aliasing rules. Також формат повідомлення не зобов’язаний збігатися з padding, endian чи розмірами полів структури в поточному ABI.[^iso-c-n1570]

**Приклад:** якщо протокол передає 6 байтів, а `sizeof(struct Header)` дорівнює 8 через padding, копіювання 8 байтів прочитає за межами пакета. Спершу перевір довжину та розбирай поля за визначеними зсувами. Коли двійковий формат навмисно відповідає структурі, скопіюй рівно доступний розмір у вирівняний локальний об’єкт; `memcpy` не усуває endian-конверсію, перевірку значень чи можливі trap representations.[^iso-c-n1570]

**Типова помилка:** cast сприймають як декодування wire format. Помилка може проявитися лише на іншій архітектурі, при іншому оптимізаторі або для буфера з іншим зсувом. Щоб уникнути її, перевіряй довжину до читання, декодуй багатобайтові числа явно та не покладайся на збіг ABI з форматом пакета.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

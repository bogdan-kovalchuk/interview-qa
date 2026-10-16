---
id: emb-structs-0001
title: "Що таке `struct` у C і для чого вона потрібна в embedded?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`struct`** групує кілька полів різних типів в один об’єкт; порядок їх оголошення визначений, але точні offsets і padding залежать від реалізації C.[^iso-c-n1570]

У embedded структури використовують для peripheral register maps, protocol frames, driver state, configuration blocks і DMA descriptors. Важливо: структура має не лише логічні поля, а й фізичний layout у пам’яті: offsets, padding, alignment.[^iso-c-n1570]

Правило: коли структура перетинає межу з hardware, binary protocol або Flash layout, її розмір і offsets треба перевіряти явно.[^iso-c-n1570]

## Detailed explanation

`struct` – це визначений програмою тип, об’єкти якого містять послідовність іменованих членів. На відміну від окремих змінних, спільний об’єкт зручно передавати функціям або зберігати як один стан: наприклад, `struct State` може тримати лічильник, прапорці та покажчик на буфер driver.[^iso-c-n1570]

Порядок полів у пам’яті відповідає порядку їх оголошення, але з цього не випливає, що вони стоять без проміжків. Компілятор може додавати padding для alignment, а конкретні offsets залежать від ABI та параметрів компіляції. Тому `struct` задає логічну форму даних у вихідному коді, але не автоматично переносимий формат байтів для протоколу чи Flash.[^iso-c-n1570]

**Приклад:** функція `update_state(struct State *state)` може отримати адресу структури й оновлювати кілька пов’язаних полів через `state->count` та `state->flags`. Саме групування полів спрощує інтерфейс функції та робить належність даних очевидною.

Коли структура відображає memory-mapped registers, protocol frame або запис у Flash, перевіряйте `sizeof`, `offsetof` та вимоги конкретного ABI. Для протоколу часто надійніше явно кодувати кожне поле у визначеній послідовності байтів. Кваліфікатор `volatile` може бути потрібен для доступу до регістрів, однак сам по собі не задає offsets і не обіцяє атомарності.[^iso-c-n1570]

**Типова помилка:** вважати, що фіксований порядок декларацій означає суміжні поля без padding. Порядок гарантовано, точний layout – ні; перевіряйте його для компілятора й цілі, з якими збирається firmware.[^iso-c-n1570]

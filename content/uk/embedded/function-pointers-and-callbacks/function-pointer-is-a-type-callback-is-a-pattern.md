---
id: emb-fnptr-0013
title: "Чим function pointer відрізняється від callback?"
description: "Function pointer – це тип/значення, callback – архітектурний патерн."
track: embedded
section: function-pointers-and-callbacks
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

**Function pointer – це тип/значення, callback – архітектурний патерн.**

Function pointer може лежати в таблиці команд, vector table або vtable-like struct. Callback – це коли один модуль реєструє функцію, а інший модуль викликає її пізніше, зазвичай у відповідь на подію.

Embedded-приклад: `void (*isr)(void)` у vector table – function pointer; user hook `on_rx(ctx, byte)`, який викликає UART driver, – callback.[^iso-c-n1570]

## Detailed explanation

Function pointer – це значення вказівникового типу, що посилається на функцію з певною сигнатурою; callback – роль, яку функція отримує в домовленості між двома компонентами. Іншими словами, перше описує механізм мови C, а друге – спосіб організації взаємодії коду.

Вказівник на функцію можна зберігати, передавати аргументом або поміщати в таблицю; виклик через нього передає керування функції, на яку він вказує. Тип вказівника важливий: функції з несумісними параметрами чи типом результату не можна безпечно викликати через довільне приведення типів.[^iso-c-n1570]

Callback виникає, коли API приймає такий вказівник як зареєстровану дію і викликає її за подією чи умовою. Вказівник у таблиці команд може вибирати обробник за індексом, але це ще не обов’язково callback: якщо він лише використовується локально для негайного dispatch, немає домовленості про передавання функції іншому компоненту для виклику згодом. І навпаки, callback реалізується не лише голим function pointer у будь-якій мові чи бібліотеці, хоча це звичний C-механізм.

Розгляньмо `void (*on_rx)(void *ctx, uint8_t byte)`: це оголошення вказівника на функцію. Якщо UART-драйвер зберігає його, а після приймання байта викликає `on_rx(ctx, byte)`, функція клієнта виконує роль callback. Змінна задає форму виклику, а API – момент і значення цього виклику.

**Типові помилки:**

- Визначати callback як окремий тип C: стандарт мови має типи функцій і вказівники, а callback є домовленістю використання.
- Ігнорувати сигнатуру й приводити довільний function pointer до очікуваного типу.
- Вважати, що сам function pointer визначає подію, час виклику або власника переданого стану.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

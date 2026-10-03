---
id: emb-fnptr-0004
title: "Що означає такий typedef?"
description: "timer_cb_t – це тип вказівника на функцію, яка приймає void * і повертає void."
track: embedded
section: function-pointers-and-callbacks
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
typedef void (*timer_cb_t)(void *ctx);
```

## Short answer

**`timer_cb_t`** – це тип pointer to function, яка приймає `void *ctx` і повертає `void`.

Після цього можна писати `timer_cb_t cb;`, `void timer_start(timer_cb_t cb, void *ctx);`. Такий typedef різко зменшує шум у driver APIs і робить callback contract видимим.

Тип callback краще оголосити один раз у header; його декларація має описувати сумісну сигнатуру функції.[^iso-c-n1570]

## Detailed explanation

`typedef void (*timer_cb_t)(void *ctx);` визначає `timer_cb_t` як псевдонім типу «вказівник на функцію, що приймає один аргумент `void *` і повертає `void`». Усередині декларатора ім’я `timer_cb_t` стоїть там, де в звичайній декларації стояло б ім’я змінної, тому воно позначає весь тип функціонального вказівника, а не тип самої функції.[^iso-c-n1570]

Після оголошення псевдоніма `timer_cb_t cb;` створює змінну-вказівник цього типу, а параметр `timer_cb_t cb` у прототипі функції приймає callback. `void *ctx` є одним параметром – вказівником на об’єкт невідомого тут типу. Callback зазвичай повертає цей контекст функції-виклику як аргумент, щоб спільний scheduler або driver міг працювати з різними станами без глобальної змінної. Сам typedef нічого не викликає й не створює callback автоматично; він лише дає ім’я типу.[^iso-c-n1570]

Тип параметра `void *` дозволяє передати адресу об’єкта будь-якого типу через стандартні правила перетворення вказівників на об’єкти, але callback має привести її назад до очікуваного типу перед використанням. Важливо, щоб функція, яку призначають у `cb`, мала сумісний тип функції: назва параметра `ctx` не впливає на тип, проте кількість і типи параметрів та тип повернення мають відповідати правилам сумісності C. Виклик через несумісний тип є undefined behaviour.[^iso-c-n1570]

Приклад:

```c
typedef void (*timer_cb_t)(void *ctx);
void timer_start(timer_cb_t callback, void *ctx);
void report_timeout(void *ctx);
timer_start(report_timeout, state);
```

Тут `timer_start` отримує і функцію, і окремий контекст, який згодом передає їй. Типова помилка – оголосити typedef без дужок навколо `*timer_cb_t`, через що вийде функція, що повертає вказівник, а не псевдонім function pointer. Порівнюй декларацію з потрібною сигнатурою або компілюй невеликий приклад, а не покладайся на назву типу.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

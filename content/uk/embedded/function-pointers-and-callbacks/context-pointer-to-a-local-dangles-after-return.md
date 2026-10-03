---
id: emb-fnptr-0029
title: "Trap: що не так із таким context pointer?"
description: "&app стає dangling pointer після повернення з init."
track: embedded
section: function-pointers-and-callbacks
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
void init(void) {
    struct App app;
    timer_register(on_timer, &app);
}
```

## Short answer

<span class="warn">`&app` стає dangling pointer після повернення з `init`.</span>

Якщо timer callback спрацює пізніше, він отримає адресу stack object-а, якого вже не існує. На MCU це може виглядати як випадкова корупція стану, HardFault або нестабільний баг.

Захист: зроби `app` static/global, збережи його в caller-owned storage, або unregister callback до завершення lifetime object-а.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

Проблема виникає тому, що `app` має automatic storage duration: його lifetime обмежений виконанням блока `init`. Виклик `timer_register` отримує адресу `app`, але це передає лише pointer, а не сам об’єкт і не продовжує його час життя. Після повернення з `init` об’єкт більше не існує, тож збережений timer-ом pointer не можна безпечно розіменовувати.[^iso-c-n1570]

Стандарт C формулює наслідок суворіше за «пам’ять може змінитися»: коли lifetime об’єкта закінчується, значення pointer, який на нього вказував, стає indeterminate. Отже, callback не повинен ані читати `app`, ані записувати в нього після повернення з функції. Те, що адреса ще виглядає правдоподібною в debugger, не робить доступ коректним; stack slot може бути використаний іншою функцією, а прояв залежатиме від оптимізації й таймінгу.[^iso-c-n1570]

Типовий симптом – стан наче випадково змінюється після спрацювання timer, іноді виникає fault, а іноді помилка зникає при додаванні debug-повідомлень. Це можливі наслідки, а не гарантований результат: undefined behaviour може проявлятися по-різному. Такий часовий зв’язок із пізнішим callback допомагає запідозрити lifetime defect, але треба перевірити також сам callback і периферійний код.[^iso-c-n1570]

Захист – передавати адресу об’єкта, який живе достатньо довго, наприклад статичного стану, поля довгоживучого `App`-об’єкта або caller-owned storage. Альтернативно, скасуй timer чи unregister callback і дочекайся, поки активний callback завершиться, перш ніж виходити з lifetime контексту. Порядок зупинки має відповідати контракту timer API: одне лише встановлення flag не гарантує, що callback уже не виконується.[^iso-c-n1570]

Приклад: якщо `timer_register` асинхронно зберігає callback та context, локальна змінна в `init` непридатна, навіть коли перше спрацювання очікується через секунду. Caller може створити `struct App app` у довшому за життя таймера scope і передати `&app`, але мусить скасувати таймер до виходу з цього scope. Якщо ж timer API копіює контекст або гарантує синхронне завершення callback до повернення, оцінка інша; це треба підтвердити його документацією, а не припускати.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

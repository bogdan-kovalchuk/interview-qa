---
id: emb-fnptr-0006
title: "Як виглядає типовий embedded callback contract?"
description: "Типовий контракт: зареєструвати function pointer і context, а driver викликає їх при події."
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

Callback contract зберігає function pointer і data pointer `context`, щоб driver передав контекст під час події.

`typedef void (*uart_rx_cb_t)(void *ctx, uint8_t byte);` `int uart_set_rx_callback(Uart *u, uart_rx_cb_t cb, void *ctx);`

`void *` призначений для адрес об’єктів, а не функцій.[^iso-c-n1570] `ctx` має вказувати на живий об’єкт правильного типу.

API має визначити момент і контекст виклику та обмеження callback-а.

## Detailed explanation

Callback contract – це угода між кодом застосунку та driver-ом про те, як зареєстрований обробник буде викликано. Зазвичай реєструють сумісний function pointer і data pointer `ctx`; обидва зберігаються разом у стані driver-а. Коли настає подія, наприклад приймання байта, driver викликає функцію з контекстом і додатковими даними події.

Типова декларація показує окремі ролі цих параметрів:

```c
typedef void (*uart_rx_cb_t)(void *ctx, uint8_t byte);
int uart_set_rx_callback(Uart *u, uart_rx_cb_t cb, void *ctx);
```

`cb` має саме той тип функції, якого вимагає API. `ctx` є покажчиком на дані користувача; у C `void *` дозволено перетворити на покажчик на object type і назад зі збереженням рівності значення, але це правило не робить `void *` покажчиком на функцію.[^iso-c-n1570] Код, що реєструє обробник, і сам callback мають однаково трактувати фактичний тип цих даних.

Передавання контексту дає змогу повторно використовувати одну реалізацію callback-а для кількох екземплярів UART. Кожен екземпляр отримує власну структуру стану, тож обробники не ділять випадково один глобальний буфер. Власник стану мусить забезпечити його lifetime щонайменше до останнього можливого виклику або скасування реєстрації.

Прикладом є callback у перериванні: тоді обмеження щодо блокування, пріоритету та потокобезпеки задаються платформою й driver-ом, а не самим C callback contract. Документація API повинна сказати, коли та звідки викликається обробник, чи може він бути null, чи дозволені blocking operations і як припиняється реєстрація.

**Типова помилка:** зберегти адресу локальної змінної в `ctx`, повернутися з функції реєстрації, а потім розіменувати вже нечинний покажчик. Передавай об’єкт, який житиме достатньо довго, і узгодь його тип із реалізацією callback-а.

## Sources

<!-- generated from frontmatter -->

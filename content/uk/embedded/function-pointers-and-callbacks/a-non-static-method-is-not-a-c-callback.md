---
id: emb-fnptr-0040
title: "Trap: що не так із передачею нестатичного методу як C callback?"
description: "&App::on_rx має тип pointer-to-member, не void ()(uint8_t)."
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
  - source_id: cppreference-member-pointers
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює відмінність вказівників на функції та вказівників на члени C++; не визначає сигнатуру конкретного C callback API."
---

## Question code

```cpp
class App {
public:
    void on_rx(uint8_t b);
};

uart_register(&App::on_rx);
```

## Short answer

<span class="warn">`&App::on_rx` має тип pointer-to-member, не `void (*)(uint8_t)`.</span>

Метод потребує конкретний object для `this`. C callback ABI не знає, який object викликати. Навіть якщо cast-ом змусити типи збігтися, виклик буде неправильний.

Захист: зроби `static void on_rx_thunk(void *ctx, uint8_t b) { static_cast<App *>(ctx)->on_rx(b); }` і зареєструй `this` як context.[^cppreference-member-pointers]

## Detailed explanation

`&App::on_rx` є вказівником на нестатичний метод, який можна викликати лише разом з об’єктом `App`; це не звичайний вказівник на функцію, який очікує типовий C API callback.[^cppreference-member-pointers]

У нестатичного методу є неявний об’єктний параметр `this`. Вираз `&App::on_rx` зберігає адресу методу, але не обирає конкретний екземпляр `App`; для виклику потрібні і цей вказівник, і об’єкт, наприклад `(object.*method)(byte)`. Звичайний C callback має заздалегідь визначену сигнатуру, наприклад `void (*)(uint8_t)`, і не має місця, де зберегти `this`. Тому передати адресу методу напряму не можна: несумісність типів виявляється вже під час компіляції. Приведення типу не створює відсутній об’єктний параметр і не робить виклик коректним.[^cppreference-member-pointers]

Типовий інтерфейс вирішує це двома аргументами: звичайним вказівником на функцію та непрозорим `void *context`. Статичний thunk відповідає очікуваній сигнатурі, перетворює контекст назад на `App *` і викликає метод. Контекст має вказувати на живий об’єкт протягом усього часу, коли callback може бути викликаний; для асинхронного driver це включає активні interrupt та відкладені події.

Наприклад, `uart_register(&App::on_rx, this)` не працюватиме, якщо API вимагає звичайний function pointer: типи аргументів не збігаються. Натомість thunk приймає і `ctx`, і байт, а потім виконує `static_cast<App *>(ctx)->on_rx(b)`.

**Типові помилки:**

- плутати вказівник на метод із вказівником на функцію;
- вважати, що `static_cast` компенсує відсутній `this`;
- реєструвати thunk із контекстом, час життя якого закінчиться до завершення callback-ів.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

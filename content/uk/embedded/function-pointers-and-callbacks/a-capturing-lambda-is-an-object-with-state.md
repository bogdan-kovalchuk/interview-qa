---
id: emb-fnptr-0038
title: "Trap: чому capturing lambda не можна передати як звичайний C function pointer callback?"
description: "Capturing lambda не має стандартного перетворення на звичайний function pointer, бо її closure object містить стан."
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
  - source_id: cpp-lambda-closure
    title: "C++ working draft: Closure types"
    url: https://eel.is/c++draft/expr.prim.lambda.closure
    accessed: 2026-10-04
    kind: spec
    version: "current working draft"
    applicability: "Правила closure type та conversion function lambda; не визначає конкретні ABI чи вимоги C callback API."
---

## Short answer

<span class="warn">Capturing lambda не має стандартного перетворення на звичайний function pointer: її closure object містить захоплений стан.</span> [^cpp-lambda-closure]

Виклик відбувається через `operator()` closure object, а сам function pointer не зберігає екземпляр цього об’єкта. Крім того, `void (*)(void)` вимагає саме функцію без параметрів, що повертає `void`; цільова сигнатура також має збігатися.

Для C callback передавай state окремо через `void *ctx`; в іншому разі використовуй C++ callback abstraction, що зберігає closure object.[^cpp-lambda-closure]

## Detailed explanation

Capturing lambda створює closure object, який представляє конкретний екземпляр із захопленими значеннями або посиланнями. Його call operator використовує цей стан, коли lambda викликається. Звичайний function pointer містить адресу функції, але не екземпляр closure object, тому стандарт C++ не надає capturing lambda conversion function до function pointer.[^cpp-lambda-closure]

У діагностиці компілятора помилка зазвичай з’являється під час передавання lambda параметру callback або ініціалізації function pointer. Для типу `void (*)(void)` є ще одна незалежна вимога: callback не приймає аргументів і повертає `void`. Навіть без capture lambda з іншою сигнатурою не підходить, а lambda з capture не має потрібного перетворення навіть за збігу параметрів.[^cpp-lambda-closure]

Розділи функцію та стан: передай file-scope функцію й адресу об’єкта через пару `callback`/`context`. Callback відновлює правильний тип context і звертається до стану; власник має гарантувати, що об’єкт не знищено до останнього можливого виклику. Якщо API приймає лише один function pointer, потрібен окремий стабільний адаптер або таблиця диспетчеризації, а не приховане захоплення локальної змінної.[^cpp-lambda-closure]

**Як уникнути:** спершу перевір тип callback у декларації API, потім виріши, де зберігатиметься стан і хто контролює його час життя. Для систем із обмеженнями пам’яті це також робить місце зберігання явним замість неявної алокації, яку можуть використовувати деякі абстракції.

Приклад із C-style API, що має context parameter:

```cpp
struct Device { void on_event() {} };
static void callback(void *ctx) {
    auto *self = static_cast<Device *>(ctx);
    self->on_event();
}
```

Тут `callback` сам не захоплює стан; стан передається окремим покажчиком, який API має повертати разом із викликом.[^cpp-lambda-closure]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

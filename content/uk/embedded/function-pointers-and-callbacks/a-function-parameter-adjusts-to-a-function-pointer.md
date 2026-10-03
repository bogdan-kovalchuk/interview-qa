---
id: emb-fnptr-0015
title: "Що означає параметр функції `void cb(int)` у декларації?"
description: "У параметрах функції це adjust-иться до function pointer: майже еквівалентно void register_cb(void (cb)(int));."
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

## Question code

```c
void register_cb(void cb(int));
```

## Short answer

У параметрах функції це adjust-иться до function pointer: майже еквівалентно `void register_cb(void (*cb)(int));`.

Функції не передаються by value. Параметр function type у function prototype автоматично перетворюється на pointer to function. Це схоже на array parameter, який перетворюється на pointer.

Правило: для ясності в callback API краще писати pointer syntax або typedef.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

Параметр `void cb(int)` у списку параметрів функції має тип «функція, що приймає `int` і повертає `void`», але в цьому контексті тип параметра автоматично коригується до pointer to function: `void (*cb)(int)`. Це правило стосується декларації параметра, а не довільних оголошень: функції не є об’єктами, які можна передавати за значенням або зберігати в масиві. [^iso-c-n1570]

Декларація `void register_cb(void cb(int));` тому оголошує `register_cb` із callback-параметром. Усередині реалізації `cb` поводиться як звичайний вказівник на функцію: його можна перевірити на null, зберегти за потреби й викликати як `cb(7)`. Параметр не несе самого коду функції; він містить адресу, за якою виконання переходить до функції сумісного типу. [^iso-c-n1570]

Для масиву параметрів існує подібне коригування масиву до pointer, але це окреме правило й не означає, що будь-який об’єкт автоматично перетворюється на вказівник. Явний запис `void (*cb)(int)` зазвичай легше читати в API, а typedef на кшталт `typedef void (*callback_t)(int);` корисний, коли тип повторюється. [^iso-c-n1570]

Приклад читання: `void (*cb)(int)` читається від імені `cb` назовні – `cb` є pointer, що вказує на функцію з параметром `int` і результатом `void`. Типова плутанина – думати, що `void cb(int)` описує функцію, яку параметр прийме за значенням. Коригування змінює тип параметра в декларації, а не дозволяє передавати тіло функції чи копіювати його. [^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

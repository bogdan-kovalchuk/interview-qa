---
id: emb-fnptr-0055
title: "Trap: чому адреси function pointers не варто серіалізувати або зберігати у Flash config?"
description: "Адреси функцій не є стабільним зовнішнім ABI."
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
  - source_id: c11-function-pointers
    title: "ISO/IEC 9899:2011 Committee Draft N1570, 6.3.2.3"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-10-04
    kind: spec
    version: "N1570"
    applicability: "Описує правила перетворення вказівників C; стандарт не визначає формат серіалізації function pointer або стабільність адреси між збірками."
---

## Short answer

<span class="warn">Значення function pointer не є переносним стабільним ідентифікатором.</span>

Після rebuild, link-time optimization, зміни linker script або firmware update адреса може змінитися. На MCU з bootloader/application layout вона може залежати від slot-а. Старе значення може стати недійсним або позначати інший код; C не задає для function pointer формат довготривалого зовнішнього збереження.[^c11-function-pointers]

Захист: серіалізуй symbolic ID/opcode, а не function address, і після boot обирай handler через актуальну dispatch table.[^c11-function-pointers]

## Detailed explanation

Function pointer зберігає значення, придатне для виклику функції в межах конкретного виконуваного образу; це не стабільний зовнішній ID функції.[^c11-function-pointers]

Компілятор і linker розміщують функції відповідно до конкретної збірки, параметрів оптимізації та linker script. Зміна версії коду, увімкнення LTO або інша конфігурація розміщення може змінити адреси. У firmware з кількома slot-ами адреса також залежить від того, звідки запускається образ. Мова C не визначає механізму, який перетворював би збережене у Flash числове значення на сумісне посилання після оновлення.[^c11-function-pointers]

Це відрізняється від збереження даних у стабільному форматі. Наприклад, конфігурація може містити числовий код команди, а нова версія програми зіставить його з актуальною функцією. Такий формат потребує правил версіонування: невідомий код слід відхилити або обробити безпечно, а не трактувати як адресу. Під час оновлення також потрібно вирішити, чи сумісні старі ID з новим набором операцій.

Приклад: якщо таблиця у Flash містить адресу `0x08004121`, після перенесення application у другий slot це саме значення не обов’язково відповідає початку тієї самої функції. Фіксоване розташування може бути частиною конкретного boot ABI, але тоді його має гарантувати платформа й підтримувати linker configuration; це не загальна гарантія мови C.

**Типова помилка:** трактувати адресу з однієї прошивки як постійне ім’я функції. Зберігай символічний opcode або ID, перевіряй його при читанні й обирай callback із таблиці, зібраної разом із поточним образом.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

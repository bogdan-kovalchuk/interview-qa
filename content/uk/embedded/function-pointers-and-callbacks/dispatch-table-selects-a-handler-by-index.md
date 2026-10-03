---
id: emb-fnptr-0018
title: "Що таке dispatch table на function pointers?"
description: "Dispatch table – це масив function pointer-ів, де індекс або opcode вибирає функцію для виклику."
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

**Dispatch table** – це масив function pointer-ів, де індекс або opcode вибирає функцію для виклику.

Наприклад, command parser може мати `cmd_handler_t table[256]`, де `table[opcode](ctx, frame)` обробляє команду. Це прибирає великий `switch`, але потребує перевірки індексу і default handler-а.

Embedded-use case: CLI commands, protocol opcodes, state machine actions, test command handlers.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

Dispatch table – це масив pointer to function одного сумісного типу, де значення індексу вибирає функцію для виклику. Такий спосіб організовує вибір обробника як дані: замість довгого ланцюжка умов програма бере елемент таблиці та викликає функцію через нього. У C елементи масиву мають один оголошений тип, тому всі обробники повинні відповідати спільній сигнатурі. [^iso-c-n1570]

Для parser-а команд таблиця може пов’язувати opcode з функцією на кшталт `void (*)(context_t *, frame_t *)`. Обробники різних команд приймають той самий набір параметрів, а відрізняється їхня реалізація. Якщо наявні обробники мають різні сигнатури, їх не можна безпечно змішати одним cast-ом; потрібні wrapper-и зі спільною сигнатурою або явний розгалужений код. [^iso-c-n1570]

Перед індексацією перевіряйте, що opcode входить у діапазон таблиці, а обраний елемент ініціалізований. Зовнішнє повідомлення або пошкоджений пакет може містити будь-яке значення; саме перетворення числа на індекс не робить його допустимим. Для розріджених кодів команд корисна окрема перевірка валідності чи таблиця пошуку, а не припущення, що кожен слот заповнений. [^iso-c-n1570]

Приклад: якщо є чотири команди з кодами від 0 до 3, перевірка `opcode < 4` перед `table[opcode](ctx, frame)` відхиляє решту значень. Для невідомої команди можна викликати окремий default handler, який повертає помилку протоколу. [^iso-c-n1570]

**Типові помилки:**

- Індексувати таблицю без перевірки меж.
- Залишати нульовий або неініціалізований слот і викликати його.
- Вважати, що dispatch table автоматично краща за `switch`: для кількох простих випадків `switch` може бути зрозумілішим.

## Sources

<!-- generated from frontmatter -->

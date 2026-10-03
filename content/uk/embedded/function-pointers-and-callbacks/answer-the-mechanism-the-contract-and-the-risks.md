---
id: emb-fnptr-0058
title: "Що має містити хороша відповідь на інтерв’ю про callbacks в embedded?"
description: "Механізм, контракт і ризики."
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

**Механізм, контракт і ризики.**

Механізм: function pointer з конкретною сигнатурою. Контракт: хто реєструє, хто викликає, коли, з яким context pointer і lifetime. Ризики: null pointer, несумісна сигнатура виклику (undefined behaviour у C), ISR context, dangling context, reentrancy, blocking calls і валідація dispatch index.[^iso-c-n1570]

Правило: сильна embedded-відповідь не зупиняється на синтаксисі `void (*cb)(void)`; вона пояснює runtime ownership і execution context.[^embeddedinterviewlab]

## Detailed explanation

Callback – це функція, яку один компонент передає іншому для виклику у визначений момент; зазвичай передається function pointer з потрібною сигнатурою.[^iso-c-n1570]

Сигнатура задає тип результату й параметрів, тому обидві сторони мають домовитися про однаковий контракт. Наприклад, producer може викликати `void (*)(int, void *)`, передаючи подію та context pointer. Сам context дає змогу одному handler працювати з різними екземплярами стану. У C виклик функції через несумісний тип function pointer має undefined behaviour, тому cast не виправляє невідповідність сигнатури.[^iso-c-n1570]

Контракт охоплює більше, ніж тип. Треба знати, хто реєструє і скасовує callback, чи може його викликати interrupt handler, на якому пріоритеті й чи дозволені blocking calls. Також визначають lifetime context: вказівник на локальну змінну стає dangling після виходу з функції, яка її створила. Якщо callback може викликатися повторно або з кількох контекстів, потрібно окремо визначити правила reentrancy і синхронізації.

Приклад: драйвер UART може зберегти callback і context під час ініціалізації, а потім викликати їх при отриманні байта. Власник має забезпечити, що context живий до unregister, а callback не виконує довгу операцію, якщо його викликано з ISR. Чи саме так працює драйвер, задає його API, а не сама мова C.

**Типові помилки:** перевірити лише синтаксис `void (*cb)(void)`, забути null і lifetime, або викликати callback у контексті з жорсткими часовими обмеженнями, хоча він блокується. Перед використанням звіряй сигнатуру, момент виклику, ownership context та обмеження execution context.

## Sources

<!-- generated from frontmatter -->

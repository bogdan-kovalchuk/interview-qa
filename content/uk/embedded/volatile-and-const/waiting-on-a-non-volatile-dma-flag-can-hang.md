---
id: emb-volconst-0059
title: "Trap: що не так із таким очікуванням DMA?"
description: "Якщо dma_done змінює ISR або callback, потрібен узгоджений із toolchain спосіб асинхронної синхронізації."
track: embedded
section: volatile-and-const
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
uint8_t dma_done = 0;

while (!dma_done) { }
```

## Short answer

<span class="warn">Якщо `dma_done` змінює ISR або callback, звичайний non-volatile flag не задає надійного спостереження зміни.</span>

За контрактом поширених embedded toolchain compiler може зберегти non-volatile значення в регістрі або винести читання з циклу, і main loop не помітить оновлення. DMA hardware не змінює C-змінну напряму: ISR/callback повідомляє CPU про завершення.

Захист: узгоджений із compiler/MCU volatile flag або atomic/RTOS механізм; для RTOS краще semaphore/event notification замість busy-wait.[^iso-c-n1570]

## Detailed explanation

Проблема циклу в тому, що `dma_done` є звичайним об’єктом C, хоча його значення нібито змінюється незалежно від циклу. Compiler не зобов’язаний припускати, що невидимий для потоку виконання код змінить non-volatile змінну; за оптимізації він може завантажити значення один раз і повторювати перевірку незмінної копії. Поведінка interrupt service routine залежить від embedded ABI та compiler extension, а не від переносимої моделі стандартного C.[^iso-c-n1570]

У конкретному embedded toolchain `volatile` зазвичай повідомляє compiler, що спостереження об’єкта має зберегтися за правилами volatile access. Це може бути достатньо для прапорця, який ISR установлює, а main loop читає, якщо платформа гарантує потрібний розмір і спосіб доступу. Стандарт не гарантує атомарність довільного типу чи синхронізацію інших даних; volatile не замінює atomic operations або memory barrier.[^iso-c-n1570]

Приклад у платформі, де byte access є атомарним за документацією:

```c
static volatile uint8_t dma_done;
while (dma_done == 0u) {
    /* очікування прапорця, який установлює ISR */
}
```

Цей фрагмент ілюструє лише pattern. Для RTOS використовуй semaphore/event notification, сумісний з ISR, замість зайнятого циклу. Якщо ISR публікує вміст буфера, окремо визнач порядок запису даних, повідомлення і потрібні cache maintenance дії для DMA.[^iso-c-n1570]

**Типова помилка:** додати volatile й вважати протокол повністю синхронізованим. Зависання може з’являтися лише з оптимізацією, а застарілі дані – після DMA. Перевір документацію compiler щодо ISR, атомарності, ordering і coherency.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

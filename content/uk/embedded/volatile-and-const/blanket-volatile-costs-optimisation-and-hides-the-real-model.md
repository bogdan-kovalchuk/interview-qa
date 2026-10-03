---
id: emb-volconst-0060
title: "Чому `volatile` не треба ставити на всі змінні \"про всяк випадок\"?"
description: "Надмірний volatile погіршує оптимізацію і може маскувати неправильну модель синхронізації."
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

## Short answer

<span class="warn">Надмірний `volatile` погіршує оптимізацію і може маскувати неправильну модель синхронізації.</span>

Для volatile-qualified об’єктів compiler має враховувати volatile accesses за правилами реалізації, що може обмежити окремі оптимізації. Вартість залежить від compiler та target; volatile не задає загального порядку для non-volatile data і не лікує race conditions чи atomicity.

Правило: використовуй `volatile` як точний контракт для hardware/ISR/DMA observable state, а не як загальне «антиоптимізаційне» заклинання.[^iso-c-n1570]

## Detailed explanation

`volatile` варто застосовувати лише до об’єктів, доступи до яких мають спеціальне значення для реалізації: наприклад, memory-mapped register або прапорця, який змінює ISR за правилами конкретного toolchain. C залишає реалізації визначення того, що саме є volatile access, тому з qualifier не можна вивести точну кількість інструкцій чи гарантовану вартість.[^iso-c-n1570]

Для volatile-qualified об’єктів compiler мусить враховувати volatile accesses згідно з правилами реалізації. Це може завадити зберігати значення в регістрі або прибирати повторні читання. Наслідком можуть бути повільніший код чи додаткові інструкції, але конкретний ефект залежить від compiler та MCU; його треба вимірювати, а не вважати універсальним.[^iso-c-n1570]

Водночас volatile не є memory barrier для звичайних об’єктів. Воно не задає порядок між volatile і non-volatile accesses, не робить операцію атомарною і не усуває data race між потоками C. Для потоків використовують atomic types та memory ordering, для RTOS – її synchronization primitives, а для пристроїв – правила архітектури, DMA API та cache maintenance.[^iso-c-n1570]

Приклад помилкового мислення: позначити весь packet buffer volatile, аби «гарантувати, що він готовий». Qualifier може вплинути на compiler accesses, але не повідомляє, чи DMA завершив передачу, чи CPU має актуальну cache line і кому належить буфер. Правильна модель окремо визначає completion event, coherency та момент передачі ownership.[^iso-c-n1570]

**Типова помилка:** використовувати volatile як загальний засіб від оптимізацій або race conditions. Назви зовнішній агент, який читає чи змінює об’єкт, і перевір контракт платформи; для решти стану застосовуй відповідний механізм синхронізації.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

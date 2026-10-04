---
id: emb-patterns-0001
title: "Які сім базових патернів embedded C варто знати на інтерв’ю?"
description: "State machines, ring buffers, bit manipulation, error handling, memory-mapped I/O, volatile-safe patterns, guard clauses."
track: embedded
section: common-code-patterns
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

**State machines, ring buffers, bit manipulation, error handling, memory-mapped I/O, volatile-safe patterns, guard clauses.**

Хороша embedded-версія цих патернів зазвичай heap-free і має чітку відповідь, чи безпечна вона для ISR (interrupt service routine) / main loop взаємодії. Не кожен патерн автоматично ISR-safe – безпека залежить від shared state, atomicity і blocking calls.[^iso-c-n1570]

Правило: на питання «які патерни ти використовуєш» називай їх із trade-off’ами, а не просто перелік.[^embeddedinterviewlab]

## Detailed explanation

Це сім поширених засобів структурування embedded C: state machine, ring buffer, bit manipulation, error handling, memory-mapped I/O, робота з `volatile`-об’єктами та guard clauses. Вони охоплюють різні задачі, тому це перелік прикладів, а не сім правил, які треба застосовувати разом.[^iso-c-n1570]

State machine робить стани й переходи явними, що спрощує огляд логіки пристрою. Ring buffer зберігає послідовність елементів у фіксованому масиві й зручно передає дані між producer та consumer. Bit manipulation допомагає працювати з масками регістрів, але вирази мають використовувати unsigned типи та маски потрібної ширини. Error handling має визначати, як виклик повідомляє про помилку та що система робить далі.

Memory-mapped I/O надає периферію через адреси регістрів, але конкретні адреси й правила доступу залежать від MCU та його документації. `volatile` допомагає змусити реалізацію виконувати доступи до volatile-об’єкта відповідно до правил мови; він сам по собі не робить складені операції атомарними й не синхронізує ISR із main loop.[^iso-c-n1570]

Guard clause завершує функцію рано, якщо передумова не виконана, що зменшує вкладеність. У всіх цих патернах важливо враховувати обмежений RAM, передбачуваний час і спільний стан. Наприклад, ring buffer між ISR і main loop потребує узгодженого протоколу доступу; сам вибір цього патерну не гарантує відсутності race condition.

**Типові помилки:**

- Вважати `volatile` синонімом atomic або thread-safe.[^iso-c-n1570]
- Копіювати приклад роботи з регістром без перевірки reference manual конкретного MCU.
- Називати патерн ISR-safe без аналізу блокувань, спільних даних і атомарності.

## Sources

<!-- generated from frontmatter -->

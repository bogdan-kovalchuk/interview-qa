---
id: emb-volconst-0003
title: "Назви три типові use cases для `volatile` в embedded C."
description: "Типові випадки: memory-mapped hardware registers, змінні, спільні з ISR, і пам’ять, яку змінює DMA; потрібні гарантії залежать від платформи."
track: embedded
section: volatile-and-const
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
  - source_id: gcc-volatile
    title: "GCC documentation: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Поведінка volatile-доступів і відсутність гарантії memory barrier у GCC; інші компілятори можуть відрізнятися."
---

## Short answer

Три типові use cases: memory-mapped hardware registers, змінні, спільні з ISR, і пам’ять, яку змінює DMA.

У всіх трьох випадках компілятор не бачить звичайного C-запису, який змінює значення. Без `volatile` він може закешувати старе значення або прибрати доступ як redundant.

Це не універсально обов’язкові випадки: правила для ISR і DMA визначаються компілятором та платформою; одного `volatile` недостатньо для синхронізації.[^iso-c-n1570] [^gcc-volatile]

## Detailed explanation

Три типові embedded-сценарії для `volatile` – memory-mapped registers, дані, якими обмінюються main code та ISR, і пам’ять, яку читає або змінює DMA. Спільна причина така: зміна або побічний ефект може відбутися без звичайного присвоєння в поточному потоці C-коду, а реалізація має трактувати доступи до кваліфікованого об’єкта спеціально.[^iso-c-n1570]

Для регістра периферії `volatile` допомагає зберегти читання або запис, бо саме звернення до адреси може бути дією. Треба ще оголосити регістр із правильною шириною й адресою та врахувати його семантику з reference manual: наприклад, читання може скидати прапорець, а запис одиниці – очищати його. Кваліфікатор не виправляє помилкову адресу чи неправильну послідовність роботи з регістром.[^iso-c-n1570]

Для прапорця ISR приклад залежить від ABI й компілятора: стандартне C формулює вузьку гарантію для сигналів, а MCU interrupt handler є платформним механізмом. Для DMA ситуація ще складніша: навіть якщо CPU виконує volatile-доступ, DMA може бачити кешовану або ще не опубліковану пам’ять. Можуть знадобитися cache clean/invalidate, бар’єри, вирівнювання чи правила когерентності контролера.[^iso-c-n1570] [^gcc-volatile]

Практичний приклад – DMA заповнює буфер, а ISR встановлює прапорець завершення. `volatile` може змусити main loop перечитати прапорець за правилами тулчейна, але не гарантує, що весь буфер уже доступний CPU, не забезпечує atomicity та не задає потрібного порядку апаратних транзакцій.

**Типова помилка:** називати ці три ситуації безумовно обов’язковими. Визнач, який саме асинхронний агент змінює дані, як платформа визначає доступ і яка окрема гарантія потрібна.

## Sources

<!-- generated from frontmatter -->

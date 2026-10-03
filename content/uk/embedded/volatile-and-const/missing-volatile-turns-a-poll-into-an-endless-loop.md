---
id: emb-volconst-0005
title: "Що може статися з таким циклом без `volatile`?"
description: "Компілятор може перетворити цикл на нескінченний, бо в межах видимого коду flag ніколи не змінюється."
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
  - source_id: gcc-volatile
    title: "GCC documentation: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Поведінка volatile-доступів і відсутність гарантії memory barrier у GCC; інші компілятори можуть відрізнятися."
---

## Question code

```c
uint8_t flag = 0;

while (flag == 0) {
    /* flag встановлює ISR */
}
```

## Short answer

Якщо платформа дозволяє ISR змінювати цей об’єкт асинхронно, а компілятор не має відповідної інформації, він може перетворити цикл на <span class="warn">нескінченний</span>, бо звичайний C-код не змінює `flag`.

За таких платформних припущень оптимізатор може прочитати `flag` один раз і надалі використовувати це значення; ISR фізично змінить пам’ять, але main loop може не перечитати її.

Захист: оголоси прапорець як `volatile uint8_t flag`, якщо цього вимагає модель ISR твого тулчейна. Якщо важливі atomicity або порядок інших даних, додай відповідну critical section чи atomic/barrier API.[^iso-c-n1570] [^gcc-volatile]

## Detailed explanation

Цей приклад показує, чому цикл опитування може не помітити зміну, яку вносить ISR. У циклі звичайного C-коду немає присвоєння `flag`, тому оптимізатор може вважати, що значення залишається нульовим, винести читання з циклу або повторно використовувати вже прочитане значення. Точна оптимізація залежить від рівня оптимізації та моделі interrupt handler у компіляторі; `-O2` сам по собі не є універсальною гарантією такого перетворення.[^iso-c-n1570]

Якщо ISR справді змінює цей об’єкт поза звичайним control flow, його оголошення має узгоджуватися з правилами конкретного компілятора й MCU. На типовому bare-metal тулчейні `volatile` на прапорці змушує main loop виконувати повторні volatile-доступи, тож він може побачити оновлення. Це не означає, що стандартне C описує будь-який MCU ISR: стандарт має окрему, вузьку модель для signal handler та `volatile sig_atomic_t`, а interrupt extensions визначає реалізація.[^iso-c-n1570]

Для одиночного байтового прапорця доступ часто є атомарним на конкретному MCU, але це треба звіряти з ABI та архітектурою. Якщо прапорець ширший або читання пов’язане з іншими даними, потрібен захист від часткового оновлення чи механізм публікації. Для взаємної видимості буфера з DMA потрібні правила кешу та бар’єрів платформи; `volatile` прапорець не гарантує, що попередні зміни буфера вже видимі DMA або CPU.[^gcc-volatile]

**Приклад:** після завершення таймера ISR встановлює `done = 1`, а main loop чекає `while (!done)`. Якщо `done` оголошений звичайним об’єктом, compiled code може не перечитувати його. Платформно коректний volatile-прапорець дає повторні читання, але не перетворює кілька полів стану на атомарну операцію.

**Типова помилка:** вважати будь-який цикл без `volatile` гарантовано нескінченним або вважати `volatile` повним протоколом синхронізації. Уточни платформний контракт і окремо перевір ширину, atomicity та порядок даних.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

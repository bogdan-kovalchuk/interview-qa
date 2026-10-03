---
id: emb-volconst-0048
title: "Trap: чому \"працює в debug, ламається в release\" часто натякає на missing `volatile`?"
description: "Бо debug build зазвичай має -O0, а release build вмикає оптимізації."
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

<span class="warn">Різниця між debug і release може виявити відсутній `volatile`, але сама назва конфігурації нічого не доводить.</span>

Різні прапорці оптимізації можуть змінити машинний код, і доступ до регістра без volatile може не перечитуватись так, як очікує програма. Однак `-O0` не гарантує потрібного порядку, а `-O2` не обов’язково кешує кожне значення; конкретна поведінка залежить від коду й компілятора.[^iso-c-n1570]

Якщо peripheral polling повертає stale data, перевір register pointer types і вимоги MCU до доступу; `volatile` потрібен для відповідних memory-mapped регістрів, але не виправляє всі concurrency чи ordering проблеми.[^iso-c-n1570]

## Detailed explanation

Відмінність між debug і release може бути симптомом коду, який покладався на випадкову поведінку неоптимізованої збірки. Якщо значення читається через звичайний вказівник, компілятор бачить звичайний доступ до пам’яті; C не обіцяє перечитувати його лише тому, що фізично за адресою розташована периферія.[^iso-c-n1570]

Наприклад, цикл очікування на прапорець може працювати під debugger, але зависати в оптимізованій збірці, якщо register pointer не volatile-qualified. Оптимізатор має право перетворювати програму відповідно до правил мови, а не до непозначених припущень про hardware. Водночас не можна виводити причину лише з назв `debug` і `release`: збірки можуть відрізнятися також макросами, linker script, частотою, таймінгами й іншими параметрами.[^iso-c-n1570]

**Приклад перевірки:** подивись на declaration pointer, тип expression для читання, assembly та memory map пристрою; зістав це з compiler documentation і reference manual. Для регістра, який змінюється поза потоком C, застосовують volatile-qualified access відповідно до platform contract. Це не гарантує atomicity, міжпотокової синхронізації чи потрібного порядку пристроєвих транзакцій.[^iso-c-n1570]

**Типова помилка:** бездумно додати `volatile` до всіх змінних або вважати, що `-O0` є виправленням. Спершу встанови, хто змінює значення і які гарантії потрібні; для shared state між потоками потрібні відповідні atomic або synchronization primitives, а для peripheral доступів – правила конкретної платформи.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

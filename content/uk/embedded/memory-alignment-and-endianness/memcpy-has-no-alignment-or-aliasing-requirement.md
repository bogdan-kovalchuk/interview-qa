---
id: emb-align-0033
title: "Чому `memcpy` для multi-byte доступу безпечніший за typed-pointer cast?"
description: "memcpy не має вимоги вирівнювання для джерела/призначення і не порушує strict aliasing."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 4
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

`memcpy` копіює байти, не читаючи значення через misaligned typed pointer і не порушуючи strict aliasing.[^iso-c-n1570] Призначення має вміщувати `n` байтів, а подальше читання як `T` вимагає належно вирівняного об’єкта `T`; копіювання не конвертує byte order.[^iso-c-n1570] Оптимізація залежить від компілятора й платформи, тому стандарт C не гарантує певних інструкцій чи переваги у швидкості.[^iso-c-n1570]

## Detailed explanation

`memcpy` копіює представлення об’єкта як послідовність байтів і не виконує доступ через вказівник на багатобайтовий тип. На відміну від cast на кшталт `(uint32_t *)buffer`, це не розіменовує misaligned typed pointer: якщо адреса не задовольняє alignment для `uint32_t`, розіменування такого вказівника має undefined behavior у C.[^iso-c-n1570]

Функції потрібні коректні межі пам’яті: джерело має надати щонайменше `n` читабельних байтів, а призначення – `n` записуваних байтів. Для декодування числа можна скопіювати байти в локальну змінну потрібного типу, яка має належне вирівнювання. Або зібрати значення з байтів масками та зсувами, якщо формат задає їх порядок явно.[^iso-c-n1570]

Наприклад, чотири байти протоколу, що починаються з непарної адреси, можна скопіювати в локальний `uint32_t value` і уникнути misaligned typed access. Але отримане число відображає object representation цільової платформи: `memcpy` не виконує перетворення byte order. Для формату з фіксованим порядком байтів їх треба переставити або скласти відповідно до специфікації.[^iso-c-n1570]

Типова помилка – вважати cast безпечним, бо процесор конкретної плати підтримує unaligned load. Правило C і можливості машинної інструкції – різні рівні: компілятор може оптимізувати коректний `memcpy`, але це не гарантує, що ручне розіменування misaligned вказівника є коректним або швидшим.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

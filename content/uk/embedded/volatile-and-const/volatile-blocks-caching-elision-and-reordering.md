---
id: emb-volconst-0002
title: "Як `volatile` впливає на доступи, які оптимізує компілятор?"
description: "volatile робить доступи до позначеного об’єкта спостережуваними за правилами реалізації, але не є загальним бар’єром порядку."
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

**`volatile` вимагає враховувати volatile-доступи за правилами конкретної реалізації C, тому компілятор зазвичай не може кешувати їх як звичайні значення або прибирати їх**.

Без цього компілятор може повторно використати попереднє значення звичайного об’єкта або прибрати звичайний запис, якщо програма цього не спостерігає. Однак `volatile` не забороняє будь-яке переупорядкування: воно не впорядковує звичайні non-volatile-доступи відносно volatile і навіть volatile-доступи можуть мати обмеження між sequence points.[^iso-c-n1570] [^gcc-volatile]

Правило: для точного порядку периферійних операцій звіряйся з документацією компілятора та використовуй потрібний compiler або hardware barrier.[^gcc-volatile]

## Detailed explanation

`volatile` впливає на те, як компілятор трактує доступи до позначеного об’єкта; це не перемикач, який вимикає всі оптимізації навколо нього. Стандарт C залишає визначення конкретного volatile-доступу реалізації, а документація GCC окремо зазначає, що volatile-доступи не є загальним бар’єром для звичайних об’єктів.[^iso-c-n1570] [^gcc-volatile]

Найочевидніше це видно в циклі опитування. Якщо зовнішня подія змінює об’єкт, який код читає як volatile, кожне читання спостерігається згідно з реалізацією, і цикл може побачити нове значення. Для memory-mapped регістра не можна прибрати запис лише тому, що програма більше не читає це значення: апаратна дія є причиною самого доступу. Водночас конкретні регістри можуть мати правила «write-one-to-clear», ширину доступу чи заборону read-modify-write, які визначаються документацією MCU, а не самим C.[^iso-c-n1570]

Обережно з фразою «volatile блокує переупорядкування». GCC гарантує обмеження щодо volatile-доступів відповідно до своєї документації, але прямо попереджає, що non-volatile доступи не впорядковані відносно volatile. Отже, запис даних у буфер перед записом volatile-прапорця може потребувати окремого бар’єра, особливо для DMA або іншого агента, який бачить пам’ять незалежно від CPU.[^gcc-volatile]

Приклад: команда «налаштувати DMA descriptor, потім встановити start bit» має дві різні вимоги. volatile-звернення до регістра забезпечує доступ до регістра, а видимість попередніх змін у descriptor може вимагати compiler barrier і/або cache maintenance та hardware barrier відповідно до архітектури.

**Типова помилка:** вважати, що три оптимізації завжди заблоковані однаково. Розрізняй повторний доступ до volatile-об’єкта, порядок звичайної пам’яті та порядок, який бачить пристрій.

## Sources

<!-- generated from frontmatter -->

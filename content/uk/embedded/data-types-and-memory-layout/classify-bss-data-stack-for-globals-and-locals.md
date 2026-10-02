---
id: emb-dtypes-0028
title: "Що буде у `.bss`, `.data`, stack для: `int g1; int g2 = 5; void f(){int l=3;}`?"
description: "Неініціалізована глобальна йде у .bss, ініціалізована - у .data, а локальна змінна функції - на стек."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`int g1;` за типовою embedded linker convention розміщується у **.bss** (має значення 0 до виконання програми; у завантажувальному образі зазвичай не зберігають нульові байти).

`int g2 = 5;` зазвичай розміщується у **.data** в RAM, з початковим значенням в образі завантаження, часто у Flash.

`int l = 3;` має automatic storage duration; у типовій реалізації зберігається на **stack**, хоча компілятор може тримати її в регістрі або оптимізувати.

Машинний код `f()` зазвичай розміщується у `.text`, яке на багатьох embedded-платформах відображене у Flash; мова C не задає ці назви секцій чи фізичну пам'ять.[^iso-c-n1570]

## Detailed explanation

У C важливо відрізняти тривалість зберігання об'єкта від секції у linker map. Глобальні змінні мають static storage duration: якщо їх явно не ініціалізовано, стандарт задає нульове початкове значення. Типовий embedded linker розміщує такі об'єкти у `.bss`, а startup code забезпечує нульове заповнення відповідної RAM області перед `main`.[^iso-c-n1570]

Для глобального `g2` явний ініціалізатор задає значення 5. Часто runtime-представлення лежить у RAM секції `.data`, а початкові байти входять до образу програми у Flash; startup code копіює їх перед запуском C-коду. Це домовленість toolchain та linker script, а не правило мови, що будь-яка `.data` має бути саме у Flash або завжди копіюватися таким способом.[^iso-c-n1570]

Локальна змінна `l` має automatic storage duration, бо оголошена у блоці без `static`. На звичайній ABI її місце часто резервується у stack frame виклику `f`, а ініціалізатор виконується щоразу при вході у блок. Але стандарт C не вимагає фізичного stack slot: оптимізатор може використати регістр або взагалі прибрати змінну, якщо її значення не спостерігається.[^iso-c-n1570]

**Приклад:** після startup-коду `g1` читається як нуль, а `g2` як п'ять; кожен виклик `f` створює нове абстрактне значення `l`, яке починається з трьох. У debugger адреса `l` може змінюватися між викликами, бути відсутньою або позначатися як optimized out – це не змінює її мовної тривалості зберігання.[^iso-c-n1570]

**Типова помилка:** трактувати `.bss`, `.data`, `.text` і stack як вимоги стандарту C. Це поширені імена й рішення платформи; для конкретного образу дивись linker script, map file і startup code.

## Sources

<!-- generated from frontmatter -->

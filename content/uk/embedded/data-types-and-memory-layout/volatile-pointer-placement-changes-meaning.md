---
id: emb-dtypes-0046
title: "Що не так: `volatile int *reg` vs `int * volatile reg` - яка різниця?"
description: "volatile int *reg кваліфікує дані, на які вказує reg, а int * volatile reg кваліфікує сам вказівник."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

`volatile int *reg` - вказівник на `volatile int`, а `int * volatile reg` - volatile сам вказівник; для регістра зазвичай кваліфікують тип об’єкта. `volatile` вимагає враховувати доступи до об’єкта за правилами abstract machine, але саме по собі не гарантує фізичний bus access для кожного виразу, atomicity чи синхронізацію.[^iso-c-n1570]

Наприклад, `volatile uint32_t * const GPIOA` означає незмінний вказівник на volatile об’єкт; коректний тип і доступи залежать від карти регістрів конкретного MCU.[^iso-c-n1570]

## Detailed explanation

`volatile int *reg` є вказівником на volatile-об’єкт типу `int`, тоді як `int * volatile reg` є volatile-об’єктом-вказівником на звичайний `int`. Розташування кваліфікатора змінює тип різного рівня: у першому оголошенні кваліфікований тип даних після розіменування, у другому – сам об’єкт `reg`.[^iso-c-n1570]

Це важливо для memory-mapped I/O. Коли апаратне забезпечення може змінювати регістр поза звичайним потоком виконання, доступ до нього описують через volatile-qualified lvalue, щоб компілятор враховував цей доступ згідно з абстрактною машиною C. Кваліфікований лише вказівник не робить volatile дані, на які він вказує; компілятор може оптимізувати звичайні читання цих даних як звичайні об’єкти.[^iso-c-n1570]

Оголошення `volatile uint32_t * const GPIOA` фіксує адресу самого вказівника, а volatile-кваліфікатор стосується об’єкта за цією адресою. Реальний регістр зазвичай описують також точним розміром, адресою та дозволеними операціями з reference manual пристрою. Не можна механічно вважати, що будь-який `volatile`-доступ дорівнює одному фізичному циклу шини: конкретна реалізація та апаратний інтерфейс визначають, як доступ стає спостережним.[^iso-c-n1570]

Для звичайного RAM volatile не є механізмом потокової синхронізації: воно не робить складену операцію атомарною і не замінює mutex чи atomic type. Якщо потрібен спільний лічильник між ISR і основним кодом, перевіряють ширину операції, atomicity для цього MCU та правила доступу до спільного стану окремо.[^iso-c-n1570]

Приклад читання: у `volatile int *reg` volatile належить значенню `*reg`; у `int * volatile reg` volatile належить змінній `reg`, яка зберігає адресу. Типова помилка – перенести кваліфікатор до вказівника, очікуючи, що це змінить властивості розіменованого об’єкта.

**Типові помилки:**
- Називати `volatile` гарантією atomicity або повного memory barrier.
- Вважати, що кваліфікатор вказівника автоматично кваліфікує цільовий об’єкт.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

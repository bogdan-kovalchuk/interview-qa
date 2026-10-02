---
id: emb-dtypes-0033
title: "Що зберігається у stack frame при виклику функції?"
description: "Stack frame містить збережені регістри, адресу повернення, локальні змінні та вирівнювальний padding."
track: embedded
section: data-types-and-memory-layout
level: middle
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
  - source_id: arm-aapcs32
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
    accessed: 2026-10-04
    kind: spec
    version: "AAPCS32"
    applicability: "Описує стек і правила вирівнювання для Arm 32-bit ABI; не задає універсальний frame."
  - source_id: armv7m
    title: "Armv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
    accessed: 2026-10-04
    kind: official
    version: "Armv7-M"
    applicability: "Винятки Armv7-M; не охоплює однаково всі Cortex-M покоління."
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

Склад stack frame залежить від ABI, компілятора й оптимізації: він може містити збережені регістри, адресу повернення, локальні дані та padding, але не має фіксованого універсального переліку. На Cortex-M під час exception апаратура зберігає базовий frame з R0–R3, R12, LR, PC та xPSR; ядра з FPU можуть використовувати розширений frame і lazy stacking.[^armv7m]

## Detailed explanation

Stack frame – це частина стекової пам’яті, яку функція використовує під час виконання. Це не універсальний перелік полів: ABI визначає правила виклику, збереження регістрів і вирівнювання, а компілятор разом з оптимізатором визначає фактичний пролог та розміщення даних.[^arm-aapcs32]

У frame можуть потрапити локальні об’єкти, аргументи, що не помістилися в регістри, spill-и тимчасових значень, збережені callee-saved регістри та місце для вирівнювання. Проте локальна змінна може весь час жити в регістрі або зникнути після оптимізації. Leaf function може не зберігати адресу повернення у стеку, якщо вона лишається в LR. Тому різні рівні оптимізації дають різні stack frames для того самого коду.

За AAPCS32 SP має бути вирівняний на 8 байтів на межі публічного виклику. Це обмеження ABI, а не правило про однаковий розмір кожного frame.[^arm-aapcs32]

Під час exception на Cortex-M апаратно зберігається базовий набір регістрів на активному стеку. Вкладені exception збільшують його використання, але оцінка також має врахувати локальні дані ISR, викликані функції та, на відповідних ядрах, збереження floating-point контексту.[^armv7m]

**Типова помилка:** рахувати стек як фіксовану суму адреси повернення і всіх оголошених локальних змінних. Для оцінки перевіряйте ABI, прапорці оптимізації, звіти stack usage та найглибший шлях викликів. Для прикладу, якщо функція викликає іншу, її активні дані залишаються потрібними, доки вкладений виклик не повернеться; рекурсія повторює це споживання для кожного рівня. Резерв стека тому визначають за максимальною глибиною одночасно активних викликів, а не загальною кількістю функцій у програмі.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

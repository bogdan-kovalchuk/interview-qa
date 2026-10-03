---
id: emb-dtypes-0101
title: "Що таке EABI і чому ABI важливий при змішуванні object files, libraries і compiler flags?"
description: "EABI фіксує calling convention, layout типів, alignment і floating-point ABI, тому всі firmware objects і libraries мають узгоджуватися."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
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
  - source_id: arm-aapcs32
    title: "Arm ABI: Procedure Call Standard for the Arm Architecture"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
    accessed: 2026-10-04
    kind: spec
    version: "2025Q4"
    applicability: "Визначення EABI, контракт викликів, типи й варіанти передачі floating-point для AArch32; не описує ABI інших архітектур."
---

## Short answer

**EABI** – ABI для embedded-середовища; конкретна родина угод визначає формат об’єктів, виклики й передавання даних. Для Arm, наприклад, AAPCS32 задає аргументи функцій, збереження регістрів і варіанти передачі floating-point.[^arm-aapcs32] Soft-float і hard-float можуть мати несумісні calling convention, тож linker або runtime може виявити помилку при змішуванні таких модулів.[^arm-aapcs32] Сумісним має бути зовнішній контракт модулів, а не обов’язково кожен локальний прапорець компілятора.

## Detailed explanation

ABI – це бінарний контракт, за яким окремо скомпільовані об’єктні файли можуть взаємодіяти в одному виконуваному образі. Він ширший за calling convention: правила можуть охоплювати представлення типів і вирівнювання, передачу аргументів та результатів, збереження регістрів, розміщення секцій і домовленості runtime. EABI означає варіант ABI для embedded або freestanding-середовища, але не є одним універсальним документом для всіх MCU. Наприклад, Arm AAPCS32 є процедурним стандартом викликів у межах Arm ABI, а ELF і runtime описані окремими специфікаціями цієї родини.[^arm-aapcs32]

Практична сумісність залежить від межі між об’єктними файлами. Два модуля можуть використовувати різні оптимізації чи локальні прапорці й лишатися сумісними, якщо їхні публічні інтерфейси дотримуються однакового контракту. Натомість різний спосіб передавання floating-point аргументів може змінити, в яких регістрах функція очікує значення. Код викликача тоді передає аргумент одним способом, а callee читає його іншим; це не обов’язково виявиться під час компіляції окремих файлів. Toolchain може записати ABI attributes в object file та діагностувати частину конфліктів під час link, але такі перевірки не є повним доказом сумісності.[^arm-aapcs32]

Перевіряти слід саме target triple/architecture, ABI variant, FPU і floating-point calling convention, endianness, object format, C/C++ ABI, а також compiler runtime та бібліотеки. Назви `soft`, `softfp` і `hard` залежать від toolchain; не можна виводити однакову сумісність лише з того, що всі модулі зібрані для того самого ядра. ABI сумісність також не робить довільні версії бібліотек взаємозамінними, якщо відрізняються їхні API або runtime-вимоги.[^arm-aapcs32]

**Типові помилки:**

- Вважати, що слово EABI саме по собі означає один набір правил для всіх архітектур; з’ясуйте конкретну ABI specification і platform ABI.
- Вважати, що `volatile` або однакова ширина `int` гарантують binary compatibility; ці ознаки не задають calling convention.
- Ігнорувати ABI-атрибути prebuilt library; перевірте їх документацію та повідомлення linker, а не лише командний рядок власного модуля.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

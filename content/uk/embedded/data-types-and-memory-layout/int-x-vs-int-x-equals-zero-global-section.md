---
id: emb-dtypes-0031
title: "Чи є різниця між `int x;` і `int x = 0;` оголошеними глобально?"
description: "Обидва оголошення мають нульове значення до початку виконання; розміщення в секціях визначає toolchain."
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
  - source_id: arm-aapcs32
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
    accessed: 2026-10-04
    kind: spec
    version: "AAPCS32"
    applicability: "Описує категорії пам’яті процесу; не визначає linker script конкретного MCU."
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

Для об’єктів зі static storage duration обидва оголошення дають нульове значення до початку виконання програми. `int x;` зазвичай розміщують у `.bss`; явний `int x = 0;` також може бути розміщений там. Вибір секції визначає toolchain, а не синтаксис C, тому явний нуль не обов’язково витрачає більше Flash.[^iso-c-n1570]

## Detailed explanation

Для об’єкта зі static storage duration C гарантує початкове нульове значення, якщо initializer відсутній; явний initializer `= 0` задає те саме значення.[^iso-c-n1570]

Стандарт описує значення, але не секції linker script на кшталт `.bss` і `.data`. Toolchain зазвичай збирає нуль-ініціалізовані об’єкти в `.bss`: секція займає RAM під час роботи, а startup code очищає її перед викликом програми. Початкові ненульові дані типово зберігаються у Flash і копіюються до RAM. Оптимізатор може розпізнати явний нуль і вибрати `.bss`; точне розміщення треба перевіряти у linker script та map-файлі.

Твердження «`int x = 0;` завжди витрачає Flash, а `int x;` ніколи» хибне. Для global-змінної після startup доступне однакове нульове значення. Явна ініціалізація може покращити читабельність, але сама собою не примушує окрему секцію. Не переносіть цей висновок на локальні автоматичні змінні: без initializer читання до присвоєння не дає гарантованого нуля.

**Типові помилки:**

- Виводити розташування в пам’яті з синтаксису C, не перевіривши налаштування linker.
- Плутати нульове значення перед `main` із фізичним зберіганням нулів у Flash.

Для конкретної плати перевірте linker script та map-файл: вони показують секцію символу. Startup code визначає, як ці дані стають доступними до `main`.[^arm-aapcs32] Наприклад, карта пам’яті може показати `.bss` у RAM без відповідного діапазону у Flash image, оскільки початковий вміст цієї секції дорівнює нулю і формується під час запуску. Це типовий спосіб реалізації, а не вимога C. Отже, порівнюйте артефакти конкретної збірки.

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

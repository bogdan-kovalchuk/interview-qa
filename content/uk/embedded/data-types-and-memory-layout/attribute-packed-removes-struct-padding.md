---
id: emb-dtypes-0025
title: "Як `__attribute__((packed))` впливає на `struct { char a; int b; char c; };`?"
description: "__attribute__((packed)) прибирає padding, зменшуючи розмір struct, але може викликати misaligned access."
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
  - source_id: gcc-packed
    title: "GCC: Common Type Attributes (packed)"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Описує розміщення членів із packed у GCC; точний layout залежить від target та ABI."
  - source_id: arm-cortex-m0
    title: "Arm Cortex-M0 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/5ea6ce5e9931941038def8c1%3Ftoken%3D
    accessed: 2026-10-04
    kind: official
    version: "DUI 0497A"
    applicability: "Cortex-M0 не підтримує невирівняні доступи; це твердження стосується саме цього ядра."
---

## Short answer

`__attribute__((packed))` у GCC мінімізує вирівнювання членів і може прибрати padding, але це розширення компілятора. За поширених припущень ця структура зменшується з 12 до 6 байтів, а `int b` опиняється на offset 1; layout треба перевірити для цільової ABI. Такий невирівняний член може вимагати повільніших доступів або не підтримуватися апаратно: <span class="warn">Cortex-M0 генерує HardFault</span> на невирівняному доступі, а на інших ядрах поведінка залежить від інструкції та конфігурації.[^gcc-packed] [^arm-cortex-m0]

## Detailed explanation

У GCC `__attribute__((packed))` просить розмістити члени структури з мінімальним проміжком, зменшуючи padding; це розширення компілятора, а не стандартна властивість C.[^gcc-packed]

Для прикладу без packed і за поширених припущень `char` має розмір 1, а `int` – розмір і вирівнювання 4 байти. Тоді `a` має offset 0, `b` – offset 4, `c` – offset 8, а кінцеве вирівнювання дає розмір 12. За packed GCC зазвичай розмістить `b` на offset 1, `c` на offset 5, а розмір буде 6 байтів. Ці числа треба підтвердити для конкретних типів, target та compiler; атрибут не робить layout переносним між ABI.[^gcc-packed]

Зменшення padding означає, що `b` може мати адресу, не кратну вирівнюванню `int`. Компілятор знає про packed member і може згенерувати потрібні для target операції, але доступ може бути повільнішим або обмеженим апаратурою. На Cortex-M0 невирівняне завантаження чи збереження спричиняє `HardFault`; для інших ядер поведінка залежить від інструкції, конфігурації та шини, тож твердження про всі M3/M4 як просто «повільніші» надто широке.[^arm-cortex-m0]

Packed-структури можуть бути корисні для опису зовнішнього бінарного формату, але не слід без перевірки трактувати довільний буфер як таку структуру або передавати адресу невирівняного члена як звичайний `int *`. Явне читання і запис байтів часто безпечніші й чіткіше описують endian та довжину поля.

**Типові помилки:**

- Вважати, що packed гарантує швидший чи безпечний доступ на будь-якому MCU.
- Вважати конкретні offsets і `sizeof` стандартом C.

**Приклад:**

```text
ordinary (assumed ABI): a@0, b@4, c@8, sizeof = 12
GCC packed (same field sizes): a@0, b@1, c@5, sizeof = 6
```

Перевіряйте фактичні offsets та згенерований код, а на цільовому пристрої – вимоги до невирівняних операцій. Застосовуйте packed лише там, де сумісність формату справді цього вимагає, і відокремлюйте декодування байтів від звичайної арифметики над вирівняними об’єктами.[^gcc-packed] [^arm-cortex-m0]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

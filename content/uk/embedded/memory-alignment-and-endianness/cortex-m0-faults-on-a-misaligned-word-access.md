---
id: emb-align-0007
title: "Trap: що станеться при misaligned 32-бітному доступі на Cortex-M0?"
description: "Cortex-M0 піднімає HardFault для невирівняного halfword або word load/store."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-08
content_revision: 4
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: arm-cortex-m0-alignment
    title: "Arm Cortex-M0 Devices Generic User Guide: Address alignment"
    url: https://documentation-service.arm.com/static/5ea6ce5e9931941038def8c1
    accessed: 2026-09-08
    kind: official
    version: "DUI 0497A"
    applicability: "Вимоги Cortex-M0 до вирівнювання та HardFault для невирівняного доступу до пам'яті."
  - source_id: learncpp-object-sizes
    title: "LearnCpp: Розміри об'єктів і оператор sizeof"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додатковий контекст про багатобайтові об'єкти й залежні від реалізації розміри типів."
  - source_id: acode-next-cpp
    title: "aCode: Кінець? Що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додатковий український маршрут вивчення C++; не є документацією processor."
---

## Short answer

<span class="warn">HardFault.</span>

Cortex-M0 не підтримує unaligned memory access: для halfword потрібна halfword-aligned адреса, а для word – word-aligned адреса. Load або store з порушенням цієї вимоги піднімає HardFault.

Не узагальнюй цю відповідь на кожен Cortex-M або іншу ISA. Байти за довільним offset копіюй через `memcpy` у вирівняний об'єкт, а потім декодуй byte order.[^embeddedinterviewlab]

## Detailed explanation

Arm визначає aligned word access як доступ за word-aligned адресою, а aligned halfword access – за halfword-aligned адресою. Byte access завжди вирівняний. У документації прямо сказано, що Cortex-M0 не підтримує unaligned access і піднімає HardFault за спроби такої memory operation.[^arm-cortex-m0-alignment]

Це окремо від правила C. Перетворення `uint8_t *` на `uint32_t *` може дати неправильно вирівняний pointer; його використання має undefined behavior у C навіть на processor, який підтримує частину unaligned instructions.[^iso-c-n1570]

## Symptom

Device переходить у `HardFault_Handler` на проблемному load або store. Cortex-M0 має менше configurable fault-status registers, ніж старші Cortex-M, тому діагностику зазвичай починають зі stacked PC, стану registers, faulting instruction та обчисленої нею ефективної адреси.

## Why it happens

Compiler генерує halfword або word instruction, бо тип виразу обіцяє належне вирівнювання. Якщо фактична адреса порушує цю обіцянку, Cortex-M0 не може розкласти instruction на підтримувані unaligned accesses і піднімає fault.

Типовий тригер – таке читання packed frame:

```c
uint32_t value = *(const uint32_t *)&frame[1];
```

Cast змінює тип pointer, але не вирівнювання `frame + 1`.

## How to avoid

Скопіюй representation у вирівняний storage, а потім інтерпретуй його byte order:

```c
uint32_t value;
memcpy(&value, &frame[1], sizeof value);
```

Для protocol явні shifts із байтів часто зрозуміліші, бо `memcpy` зберігає host byte order, а не конвертує його. Увімкни alignment warnings, не ігноруй packed-member warnings і дотримуйся width та alignment із device reference manual для DMA/MMIO.

## Sources

<!-- generated from frontmatter -->

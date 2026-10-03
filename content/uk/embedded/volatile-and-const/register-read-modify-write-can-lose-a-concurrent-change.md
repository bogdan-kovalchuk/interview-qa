---
id: emb-volconst-0037
title: "Чому read-modify-write для volatile register може бути небезпечним?"
description: "Операція не атомарна: це читання register, модифікація в CPU, потім запис назад."
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
  - source_id: stm32-bsrr
    title: "STMicroelectronics STM32L1 reference manual, GPIO bitwise handling"
    url: https://www.st.com/resource/en/reference_manual/cd00240193.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0038"
    applicability: "Описує BSRR як атомарний set/reset для GPIO ODR саме на STM32L1; інші MCU та їхні регістри можуть мати іншу поведінку."
---

## Question code

```c
GPIOA_ODR |= (1u << pin);
```

## Short answer

Операція <span class="warn">не атомарна</span>: це читання register, модифікація в CPU, потім запис назад.

Якщо hardware або ISR змінить інші біти між read і write, фінальний запис може перетерти ці зміни. Наприклад, STM32 GPIO має BSRR, який змінює вибрані біти ODR одним записом; це властивість конкретної периферії, а не будь-якого register.[^stm32-bsrr]

Захист: використовуй документовані set/clear registers, де вони є; інакше захисти RMW від конкурентного доступу, наприклад critical section для ISR. `volatile` не робить послідовність атомарною.[^stm32-bsrr]

## Detailed explanation

Read-modify-write (RMW) – це послідовність із трьох дій: прочитати register, змінити значення в CPU, записати результат назад. Вираз `GPIOA_ODR |= mask` зазвичай потребує саме такого циклу, хоча точні інструкції залежать від compiler та архітектури. Кваліфікатор `volatile` вимагає відповідних volatile-доступів за правилами реалізації, але не зливає кілька кроків у неподільну операцію.

Проблема виникає, коли між читанням і записом інший учасник змінює register. Наприклад, ISR встановив біт 2 після того, як основний код прочитав старе значення для встановлення біта 0. Запис основного коду поверне старе значення з бітом 0 і може стерти новий біт 2. Такий самий сценарій можливий, якщо апаратний блок сам оновлює статусні біти. Наслідок часто виглядає як рідкісна втрата події чи несподіваний стан GPIO.

Для STM32 GPIO register `BSRR` задає set/reset окремих бітів ODR одним записом, без читання ODR та зворотного запису; це зменшує вікно гонки саме для цієї операції. BSRR не блокує ODR і не робить інші регістри атомарними. Для інших MCU шукай у reference manual операції set/clear, write-one-to-clear або атомарні інструкції, якщо вони підтримуються.[^stm32-bsrr]

**Як уникнути помилки:**

- Не використовуй RMW для register із побічними ефектами без перевірки його семантики.
- Застосовуй спеціальний hardware register, якщо виробник його надає.
- Якщо RMW неминучий і конкурент – ISR того самого CPU, виконай коротку critical section за правилами платформи.

Не припускай, що C atomic API можна застосувати до будь-якого MMIO-регістра: апаратна підтримка, ширина доступу та дозволені операції визначаються платформою.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

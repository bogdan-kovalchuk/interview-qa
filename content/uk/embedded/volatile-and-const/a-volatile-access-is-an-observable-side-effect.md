---
id: emb-volconst-0035
title: "Чи є читання volatile-об’єкта side effect?"
description: "Так, volatile access вважається observable side effect для абстрактної машини C."
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
---

## Short answer

**Так, доступ через lvalue з `volatile` є side effect і має виконуватися за правилами абстрактної машини C.**[^iso-c-n1570]

Тому компілятор не може просто прибрати volatile-читання hardware register як «невикористаний результат». На пристрої саме читання може очищати flag, acknowledge interrupt або запускати bus transaction; конкретне значення access визначає реалізація.

Embedded-правило: якщо read-to-clear або read-has-side-effect register описаний без `volatile`, оптимізатор може зламати протокол периферії. `volatile` не забезпечує atomicity, синхронізацію між потоками чи універсальний memory barrier.[^iso-c-n1570]

## Detailed explanation

Доступ через lvalue з типом, кваліфікованим як `volatile`, має особливий контракт із компілятором: абстрактна машина C розглядає такий доступ як side effect і вимагає оцінювати його згідно зі своїми правилами. Через це volatile-читання не можна безумовно вилучити лише тому, що його повернене значення не використовується.[^iso-c-n1570]

У MCU регістр може мати побічний ефект читання: наприклад, читання повертає стан прапорця й водночас очищає його. Якщо програміст читає такий регістр через неvolatile lvalue, компілятор може кешувати значення або вилучати повторні читання, оскільки звичайна пам’ять не змінюється сама по собі з погляду програми. Кваліфікатор у визначенні регістру повідомляє компілятору, що звернення має бути збережене відповідно до volatile-семантики.[^iso-c-n1570]

Це не визначає, що саме є одним доступом: стандарт залишає цю деталь implementation-defined. Також `volatile` не робить операцію атомарною, не захищає від гонок між потоками чи ISR і не є повною заміною compiler або CPU barrier. Для синхронізації потрібні атоміки, критичні секції чи платформні примітиви; для порядку доступу до периферії слід виконувати вимоги документації MCU та compiler.[^iso-c-n1570]

Приклад:

```c
#define STATUS (*(volatile uint32_t *)STATUS_ADDR)
uint32_t flags = STATUS; // читання має залишитися volatile access
```

**Типова помилка:** вважати, що `volatile` перетворює будь-яку змінну на thread-safe. Його призначення тут – змусити реалізацію враховувати конкретні доступи, наприклад до memory-mapped register; воно не задає ні блокування, ні порядок між потоками.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

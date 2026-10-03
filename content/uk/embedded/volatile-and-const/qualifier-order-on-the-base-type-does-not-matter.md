---
id: emb-volconst-0057
title: "Trap: чи однакові `const volatile uint32_t *` і `volatile const uint32_t *`?"
description: "Так, для pointed-to base type порядок const і volatile не змінює значення."
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
---

## Short answer

**Так, `const volatile uint32_t *` і `volatile const uint32_t *` мають однаковий тип.**

Обидва типи означають pointer to const volatile `uint32_t`. Дані за pointer не можна записувати через цей lvalue, але читання має бути volatile. Важливо не плутати це з `const volatile uint32_t * const`, де додатковий `const` після `*` захищає сам pointer.

Правило: порядок cv-qualifiers на одному рівні типу не змінює значення; важливо, до якого рівня pointer chain вони застосовані.[^iso-c-n1570]

## Detailed explanation

`const volatile uint32_t *p` і `volatile const uint32_t *p` оголошують pointer на той самий кваліфікований тип: `uint32_t` одночасно має `const` і `volatile`. C дозволяє кілька type qualifiers для одного типу, а їхній порядок у списку не змінює тип.[^iso-c-n1570]

Кваліфікатори діють на об’єкт, до якого застосовано declarator. У цих оголошеннях вони стоять до `*`, отже кваліфікують pointed-to integer. Читання `*p` є volatile access; присвоєння `*p = 3` заборонене, бо lvalue також const-qualified. Точна семантика volatile access залежить від реалізації C та ABI пристрою.[^iso-c-n1570]

`const volatile uint32_t * const p` додає qualifier після `*`, тож він стосується самого pointer: його не можна перенаправити, а об’єкт за адресою лишається const volatile. Натомість `uint32_t * const p` має незмінний pointer на звичайний змінюваний integer. Позиція відносно зірочки визначає рівень типу.[^iso-c-n1570]

Приклад читання:

```c
volatile const uint32_t *status = (volatile const uint32_t *)0x40000000u;
uint32_t value = *status; // читання volatile-qualified об’єкта
```

Це лише ілюстрація типів: адреса та ширина register мають відповідати документації MCU. Не слід виводити атомарність, memory barrier чи безпечність адреси з qualifier.[^iso-c-n1570]

**Типова помилка:** думати, що другий qualifier змінив значення. Знайди `*`, визнач pointed-to object, а тоді окремо прочитай qualifiers до і після зірочки.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

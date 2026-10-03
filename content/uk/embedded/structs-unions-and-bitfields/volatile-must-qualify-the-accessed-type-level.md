---
id: emb-structs-0046
title: "Чому `volatile` на struct pointer і `volatile` на fields не завжди одне й те саме?"
description: "Кваліфікатор має застосовуватися до того рівня типу, через який відбувається access."
track: embedded
section: structs-unions-and-bitfields
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

**`volatile` має кваліфікувати об’єкт, доступ до якого виконується.** Якщо pointer має тип «pointer to volatile struct», доступ до його members через `->` також є volatile-qualified.[^iso-c-n1570]

`volatile GPIO_TypeDef *GPIOA` кваліфікує об’єкт, на який вказує pointer, а `GPIO_TypeDef * volatile GPIOA` – сам pointer. Доступ через non-volatile alias не має цих властивостей, а `volatile` не забезпечує atomicity чи синхронізацію потоків.[^iso-c-n1570]

Для memory-mapped registers тип доступу має відповідати контракту платформи; перевіряй визначення типів і macros у документації SDK.[^iso-c-n1570]

## Detailed explanation

У C `volatile` має бути частиною типу lvalue, через який програма читає або записує регістр; кваліфікація структури через pointer поширюється на тип member-а, вибраного оператором `->`.[^iso-c-n1570]

Наприклад, `volatile struct Registers *regs` означає pointer на volatile-qualified структуру. Вираз `regs->status` має volatile-qualified тип, тож компілятор трактує цей доступ відповідно до правил абстрактної машини. Натомість `struct Registers * volatile regs` робить volatile саму змінну-pointer: компілятор має враховувати її читання або запис, але це не кваліфікує автоматично об’єкт, на який вона вказує. Місце `volatile` у декларації тому змінює конкретний тип, а не просто «вмикає volatile для всього поруч».[^iso-c-n1570]

На практиці визначення CMSIS часто кваліфікують окремі поля периферійної структури як `__I`, `__O` чи `__IO`, а API конкретного MCU визначає дозволені способи доступу. В обох схемах важливо користуватися оголошеним типом, не відкидати qualifier через cast і звірятися з документацією виробника: сам стандарт C не визначає ширину транзакції периферійного регістра чи всі апаратні побічні ефекти.[^iso-c-n1570]

**Приклад:**

```c
struct Registers { uint32_t status; };
volatile struct Registers *regs = (volatile struct Registers *)0x40000000u;
uint32_t value = regs->status;
```

Останній рядок читає volatile-qualified member через цей pointer. Це не означає, що доступ атомарний, що апаратний регістр підтримує саме такий розмір читання або що `volatile` синхронізує потоки. Для таких властивостей потрібні гарантії ISA, периферійної специфікації та відповідних atomic/critical-section примітивів.[^iso-c-n1570]

Типова помилка – додати `volatile` до pointer-об’єкта й вважати pointee volatile, або зробити cast до звичайного pointer і продовжити читання через нього. Перевіряй тип на стороні об’єкта, до якого звертаєшся, та залишай qualifier у всьому register access API.

## Sources

<!-- generated from frontmatter -->

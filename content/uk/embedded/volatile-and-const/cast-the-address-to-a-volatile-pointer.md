---
id: emb-volconst-0008
title: "Як правильно оголосити memory-mapped 32-bit register за адресою `0x40020014`?"
description: "Типовий варіант: #define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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

Типовий варіант: `#define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)`.

Тут `volatile uint32_t *` означає pointer to volatile 32-bit data. Розіменування дає volatile lvalue, доступ до якого зберігає визначену реалізацією семантику volatile; відповідність фактичному bus access залежить від MCU та compiler.[^iso-c-n1570]

Це типова форма для memory-mapped register, але адресу й допустиму ширину доступу треба звірити з документацією MCU.[^iso-c-n1570]

## Detailed explanation

Щоб оголосити memory-mapped register, потрібен вказівник на volatile-об’єкт і його розіменування. Вираз `volatile uint32_t *` має тип «вказівник на volatile `uint32_t`», а `*(volatile uint32_t *)address` є lvalue, через який читають або записують цей об’єкт. Наприклад: `#define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)`. Кваліфікація стосується даних за адресою, а не змінної-вказівника.[^iso-c-n1570]

У стандарті C `volatile` означає, що реалізація повинна зберігати семантику volatile-об’єкта за правилами абстрактної машини; стандарт також залишає визначення самого доступу реалізації. Тому цей запис не є універсальною гарантією електричного транзакту на шині. Embedded-компілятор та платформа визначають, як такий volatile access перетворюється на інструкції, а документація MCU визначає дозволені адреси, ширини та side effects.[^iso-c-n1570]

Перед використанням перевірте, що `0x40020014` справді є адресою потрібного регістра на конкретному MCU, вирівнювання відповідає `uint32_t`, а регістр підтримує 32-бітний доступ. Якщо регістр має окремі set/clear alias або небезпечну read-modify-write семантику, звичайне `|=` може бути неправильним способом змінити біт. Для таких деталей потрібен reference manual, а не лише синтаксис C.

**Приклад:**

```c
#define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)
GPIOA_ODR = 1u;
```

Фрагмент ілюструє форму виразу, але адресу не можна переносити між MCU без перевірки. У реальному проєкті зазвичай краще використовувати vendor header з уже описаною мапою регістрів і кваліфікованими полями; це зменшує ризик хибної адреси чи типу.

**Типова помилка:** привести адресу до `volatile uint32_t`, а не до `volatile uint32_t *`. Перше не створює вказівник і не дає коректного розіменування; зірочка в типі є суттєвою частиною оголошення.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

---
id: emb-volconst-0045
title: "Чому peripheral register struct fields оголошують як `volatile`?"
description: "Бо кожне поле struct overlay представляє hardware register, а не звичайне RAM-поле."
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

**Бо кожне поле struct overlay представляє hardware register, а не звичайне RAM-поле.**

Коли код звертається до поля, оголошеного volatile, реалізація має зберегти відповідний volatile access згідно з правилами C. Але точне визначення access є implementation-defined; `volatile` саме по собі не гарантує атомарності, ширини bus transaction чи потрібного порядку апаратних операцій.[^iso-c-n1570]

Правило: у register overlay кваліфікуй доступ до memory-mapped register як `volatile`, а адресу, розкладку полів, ширину та побічні ефекти звіряй із документацією MCU.[^iso-c-n1570]

## Detailed explanation

Поля register overlay позначають `volatile`, бо object за відповідною адресою може змінюватися незалежно від звичайного потоку C-коду, наприклад через peripheral hardware або interrupt. Кваліфікатор вимагає, щоб реалізація враховувала доступи згідно з abstract machine; стандарт прямо допускає використання `volatile` для memory-mapped I/O, але визначення того, що саме є access, лишає реалізації.[^iso-c-n1570]

Типова структура відображає адреси регістрів як поля C struct, а pointer на неї формується за базовою адресою peripheral. `GPIOA->ODR = value` тоді позначає запис у відповідне volatile-поле, а читання `GPIOA->IDR` – доступ до поля, яке може змінитися через зовнішній стан pin-а. Без `volatile` компілятор може оптимізувати звичайні RAM-доступи, виходячи з того, що значення не змінюється без видимого запису програми; це припущення не годиться для peripheral registers.[^iso-c-n1570]

**Приклад:**

```c
typedef struct {
    volatile uint32_t MODER;
    volatile uint32_t IDR;
    volatile uint32_t ODR;
} gpio_registers_t;

#define GPIOA ((gpio_registers_t *)GPIOA_BASE)
```

Цей приклад показує лише ідею доступу. Реальна структура повинна точно відповідати register map виробника: порядок, offsets, reserved regions і допустимі ширини запису не можна вивести з C-коду. Деякі регістри очищуються записом одиниці, мають read-to-clear semantics або забороняють read-modify-write; для них звичайне `|=` може бути хибним навіть за наявності `volatile`. Такі правила визначає reference manual MCU.[^iso-c-n1570]

Не покладайся на `volatile` як на загальну memory barrier, mutex чи гарантію атомарності. Воно саме по собі не забезпечує узгодження кількох полів між ISR та main і не гарантує, що bus виконає доступ потрібною периферії шириною. Для цього потрібні вимоги конкретного пристрою, компілятора та архітектури. Типова помилка – оголосити весь struct volatile і вважати, що цим уже забезпечено правильні offsets та безпечні операції; перевіряй обидва аспекти окремо.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

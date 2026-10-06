---
id: emb-patterns-0038
title: "Чому function-pointer FSM table роблять `static const`?"
description: "const робить таблицю read-only: її кладуть у .rodata (зазвичай Flash), не витрачаючи RAM, а запис у неї не компілюється."
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Підтверджує, що присвоєння const-об’єкту порушує constraint (6.5.16, 6.3.2.1), що зміна об’єкта, визначеного як const, через не-const lvalue є undefined behavior (6.7.3, пункт 6), і що адреса функції є address constant для static-ініціалізатора (6.6); не визначає, у якій пам’яті лежать дані."
  - source_id: gcc-gccint-sections
    title: "GCC 16.1.0 Internals: Defining the Output Assembler Language, Sections"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gccint/Sections.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Підтверджує, що типова реалізація вибору секції в GCC кладе read-only змінні в readonly_data_section (на практиці .rodata); конкретний лінкер-скрипт вирішує, у якій пам’яті ця секція лежить."
  - source_id: gcc-named-address-spaces
    title: "GCC 16.1.0: Named Address Spaces (AVR Named Address Spaces)"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Named-Address-Spaces.html#AVR-Named-Address-Spaces
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Показує, що на AVR поза avrtiny/avrxmega3 навіть read-only дані за замовчуванням лежать у RAM, а для Flash потрібні `__flash` або `progmem`; стосується лише AVR."
  - source_id: ld-output-section-lma
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Пояснює, що секція може мати різні адреси завантаження (LMA, ROM-образ) і виконання (VMA), а ініціалізовані дані копіюють з ROM у RAM під час старту; це механізм, через який змінна таблиця займає і Flash, і RAM."
---

## Short answer

**`static const` робить таблицю read-only: компілятор кладе її в `.rodata`, а лінкер-скрипт зазвичай розміщує `.rodata` у Flash, тож таблиця не займає RAM.**[^gcc-gccint-sections]

Присвоєння елементу такої таблиці не скомпілюється, а зміна через відкинутий `const` – undefined behavior.[^iso-c-n1570] Розміщення залежить від тулчейна: на AVR без `__flash` чи `PROGMEM` `const`-дані лежать у RAM.[^gcc-named-address-spaces]

Правило: незмінні dispatch/handler таблиці роби `static const`.

## Detailed explanation

Таблиця переходів FSM – масив вказівників на функції, наприклад `static const handler_t handlers[] = { on_idle, on_busy };`. Адреса функції є address constant, тож її дозволено в ініціалізаторі об’єкта зі static storage duration, і вміст таблиці повністю відомий під час збірки.[^iso-c-n1570] Це дозволяє позначити її `const`: об’єкт, визначений з const-кваліфікатором, компілятор вважає read-only, і типовий вибір секції в GCC кладе такі змінні в окрему read-only секцію даних, тобто `.rodata`.[^gcc-gccint-sections]

Різниця для пам’яті випливає з того, як лінкер працює з даними. Звичайна ініціалізована змінна живе в `.data`: початкові значення зберігаються в образі у ROM (адреса завантаження, LMA), а під час старту startup-код копіює їх у RAM за адресою виконання (VMA).[^ld-output-section-lma] Отже, змінна таблиця займає місце і у Flash, і в RAM. Таблиця станів 8 на 8 з 32-бітними вказівниками – це 64 * 4 = 256 байтів RAM. З `const` дані лишаються в `.rodata`, а те, у якій пам’яті опиниться ця секція, вирішує лінкер-скрипт; у типових скриптах для мікроконтролерів це Flash. Слово `static` тут стосується лише видимості (internal linkage): таблицю не побачать інші translation units, але в Flash її кладе саме `const`, а не `static`.

Захист від випадкового перезапису має два рівні. Компілятор відхиляє присвоєння елементу `const`-таблиці, бо ліва частина присвоєння має бути modifiable lvalue, а const-кваліфікований тип таким не є.[^iso-c-n1570] Якщо ж зняти `const` приведенням типу й змінити об’єкт, визначений як const, це undefined behavior.[^iso-c-n1570] Апаратний захист з’являється лише якщо таблиця справді у Flash: випадковий запис у RAM (вихід за межі масиву, переповнення стека) її зазвичай не зачепить, бо звичайна інструкція запису не змінює Flash. Але мова цього не гарантує: розміщення залежить від тулчейна й лінкер-скрипта. Для AVR поза `avrtiny` та `avrxmega3` навіть read-only дані за замовчуванням потрапляють у RAM, а для Flash потрібні `__flash` або `progmem` та читання через `LPM`; тож перевіряйте map file.[^gcc-named-address-spaces]

Приклад ілюстративний:

```c
typedef void (*handler_t)(void);
static void on_idle(void) { /* ... */ }
static void on_busy(void) { /* ... */ }

static const handler_t handlers[] = { on_idle, on_busy };
/* handlers[0] = on_busy;  <- помилка компіляції: елемент const */
```

**Типові помилки:**

- Вважати, що `static` кладе таблицю у Flash: це робить `const` разом із лінкер-скриптом.
- Не перевірити map file і припустити Flash, наприклад на AVR, де `const`-дані за замовчуванням лежать у RAM.
- Знімати `const` приведенням, щоб «підправити» елемент таблиці в runtime.
- Індексувати таблицю зовнішнім значенням без перевірки меж.

## Sources

<!-- generated from frontmatter -->

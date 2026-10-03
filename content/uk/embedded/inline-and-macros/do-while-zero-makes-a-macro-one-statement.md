---
id: emb-macros-0010
title: "Навіщо statement-макрос обгортають у `do { ... } while(0)`?"
description: "Щоб макрос із кількох інструкцій поводився як один statement і коректно працював з if/else та крапкою з комою."
track: embedded
section: inline-and-macros
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

## Question code

```c
#define LOG_ERR(m) do { \
    uart_puts("[ERR] "); \
    uart_puts(m); \
} while (0)
```

## Short answer

**Щоб макрос із кількох інструкцій поводився як один statement** і коректно працював з `if/else` та крапкою з комою.

`do { ... } while(0)` утворює єдиний блок, який вимагає `;` у кінці виклику, тому `if (c) LOG_ERR(x); else ...` компілюється правильно.

Для statement-макросу з кількох дій ця ідіома зберігає очікувану структуру `if/else`; зворотна скісна риска в кінці рядка продовжує директиву препроцесора.[^iso-c-n1570]

## Detailed explanation

`do { ... } while (0)` дає multi-statement макросу синтаксичну форму одного циклічного statement, тіло якого виконується рівно один раз. Крапка з комою після `while (0)` належить конструкції `do-while`, а крапка з комою після виклику макросу завершує statement у коді користувача.[^iso-c-n1570]

Препроцесор спершу підставляє replacement list макросу, після чого компілятор розбирає звичайний C-код. Без обгортки макрос із двох викликів функцій розгорнеться у два окремі statements. У контексті `if (condition) LOG_ERR(message); else recover();` перший statement стане тілом `if`, а другий виявиться між `if` та `else`; `else` уже не матиме відповідного `if`. Блок у `do` групує обидва виклики в один statement і зберігає очікуване підпорядкування.[^iso-c-n1570]

Умова `0` означає, що тіло циклу не повторюється. На відміну від простого блоку `{ ... }`, який після макросу має додаткову крапку з комою і в певному контексті стає порожнім statement, `do-while` природно приймається там, де граматика очікує один statement. Це стосується `if/else`, циклів і місць, де виклик макросу завершується `;`.[^iso-c-n1570]

Приклад:

```c
#define LOG_ERR(message) do { \
    uart_puts("[ERR] "); \
    uart_puts(message); \
} while (0)

if (has_error)
    LOG_ERR(text);
else
    recover();
```

Тут `else` належить потрібному `if`, а обидва виклики всередині макросу виконуються тільки коли `has_error` істинне. Для функції, що може замінити макрос, функція зазвичай дає кращі типи та менше пасток; ідіома потрібна саме коли потрібен statement-макрос із кількох дій.[^iso-c-n1570]

**Типові помилки:**

- Додавати крапку з комою в кінець самого `#define`, змушуючи caller отримати зайвий порожній statement.
- Забути зворотну скісну риску продовження рядка або залишити після неї пробіли.
- Вважати конструкцію звичайним циклом із повтореннями; умова `0` гарантує одноразове виконання.

## Sources

<!-- generated from frontmatter -->

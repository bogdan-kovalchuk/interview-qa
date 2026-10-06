---
id: emb-patterns-0040
title: "Trap: що буде, якщо в state machine не перевірити індекс стану перед `handlers[state]`?"
description: "Невалідний/пошкоджений стан -> out-of-bounds read таблиці й indirect call за випадковою адресою (ймовірний HardFault)."
track: embedded
section: common-code-patterns
level: junior
type: pitfall
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
    applicability: "Підтверджує, що вихід індексу за межі масиву (6.5.6 п. 8, Annex J.2) і виклик через вказівник на функцію несумісного типу (6.5.2.2 п. 9) є undefined behavior; нічого не каже про поведінку конкретного процесора."
  - source_id: tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (SPMS376E)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
    accessed: 2026-10-06
    kind: official
    version: "SPMS376E"
    applicability: "Для ядра Cortex-M4F: bus error на instruction fetch, перехід у XN-регіон і спроба виконати код зі скинутим Thumb-бітом дають fault, а fault без ввімкненого обробника ескалює в HardFault. Розділ 2.6 Fault Handling. Для інших ядер і чипів деталі відрізняються; адреса на справжній код fault не викликає."
---

## Short answer

<span class="warn">Невалідний/пошкоджений стан -> out-of-bounds read таблиці й indirect call за випадковою адресою</span> (undefined behavior: на Cortex-M це ймовірний fault, зокрема HardFault, але не гарантований).[^iso-c-n1570]

Дані стають control flow, тож стан із зовнішнього входу чи corruption напряму керує тим, яку функцію викличуть, а якщо прочитане значення випадково вказує на реальний код, fault не станеться взагалі.[^tm4c123-datasheet]

Захист (для беззнакового `state`): `if (state < ARRAY_SIZE(handlers) && handlers[state]) handlers[state](evt); else on_error();`

## Detailed explanation

У C вираз `handlers[state]` означає `*(handlers + state)`. Якщо індекс виводить результат за межі масиву, далі ніж на один елемент за останнім, то вже саме обчислення вказівника є undefined behavior – ще до того, як щось прочитано.[^iso-c-n1570] На практиці компілятор просто завантажує слово за адресою `handlers + state*sizeof(handler_t)`: це може бути наступна константа у flash, літерал-пул або дані іншого модуля. Це слово далі використовується як адреса функції, а якщо за нею немає функції сумісного типу, поведінка знову undefined.[^iso-c-n1570]

Що станеться на залозі, залежить від самого значення. На Cortex-M слово потрапляє в PC через `BLX` або `BX`: якщо молодший біт нульовий, процесор намагається вийти зі стану Thumb і отримує usage fault; адреса, якої немає в пам’яті, дає bus fault на instruction fetch; перехід у регіон, позначений як XN (execute never), теж дає fault.[^tm4c123-datasheet] Якщо обробник такого fault не ввімкнено, він ескалює в HardFault.[^tm4c123-datasheet] Тому «ймовірний HardFault» – чесне формулювання, але не гарантія: коли випадкове значення непарне й вказує на виконуваний код, fault не буде, і прошивка мовчки викличе не той handler.

Невалідний стан береться з реальних джерел: пошкодження RAM через stack overflow чи вихід за межі сусіднього буфера, неініціалізована змінна, поле з пакета або команда з UART. Якщо `state` має знаковий тип, перевірка `state < N` пропускає від’ємні значення, тому індекс краще тримати беззнаковим або перевіряти обидві межі. Саму таблицю корисно робити `static const`: тоді вона зазвичай лежить у flash, і її не зіпсує та сама corruption.

```c
typedef void (*handler_t)(event_t);
static const handler_t handlers[STATE_COUNT] = { on_idle, on_busy, on_done };

void dispatch(uint32_t state, event_t evt)
{
    if (state < STATE_COUNT && handlers[state] != NULL) {
        handlers[state](evt);
    } else {
        on_error(state);   /* залогувати, перейти в безпечний стан */
    }
}
```

**Типові помилки:**

- Перевіряти лише `handlers[state] != NULL`: ця перевірка сама читає елемент за межами таблиці.
- Писати `state <= STATE_COUNT` замість `<`: індекс `STATE_COUNT` уже за межами масиву.
- Вважати HardFault «захистом»: для частини значень fault не станеться, а виконається чужий код.
- Мовчки ігнорувати помилковий стан у `else` замість переходу в безпечний режим або reset.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

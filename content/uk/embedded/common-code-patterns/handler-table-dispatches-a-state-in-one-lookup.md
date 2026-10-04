---
id: emb-patterns-0004
title: "Як виглядає state machine на function-pointer table?"
description: "Масив вказівників на handler-и, індексований станом; диспетчеризація – один lookup, O(1)."
track: embedded
section: common-code-patterns
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

## Question code

```c
typedef void (*handler_t)(oven_event_t e);
static const handler_t handlers[] = {
  [STATE_IDLE]    = on_idle,
  [STATE_HEATING] = on_heating,
  [STATE_ERROR]   = on_error,
};
handlers[*state](evt);
```

## Short answer

**Масив вказівників на handler-и може вибрати функцію за індексом стану за один lookup.**

Переваги: окрема функція на стан полегшує ізоляцію логіки. Ініціалізована `static const` таблиця зазвичай розміщується в read-only секції, але фізичний сегмент залежить від toolchain і linker script.[^iso-c-n1570]

Правило: масштабовано для багатьох станів, але важче читати в дебагері.[^embeddedinterviewlab]

## Detailed explanation

Function-pointer table зберігає адресу функції-обробника для кожного значення стану. Якщо значення `enum` використані як індекси щільного масиву, диспетчер читає елемент за цим індексом і викликає відповідний handler. Такий прямий індексний доступ має сталу кількість операцій відносно числа записів таблиці, але це не означає, що вся обробка події має сталу тривалість.[^iso-c-n1570]

У наведеному коді designated initializers пов’язують імена станів із функціями, що робить відповідність зрозумілішою за позиційний список. Тип кожного handler-а має збігатися з `handler_t`; компілятор перевіряє сумісність типу вказівника на функцію. Перед індексацією перевірте, що `*state` лежить у межах таблиці та відповідає заповненому елементу. Інакше можна викликати нульовий або неправильний вказівник.

Масив handler-ів зручний, коли обробка локальна для стану. Якщо перехід залежить від пари state/event, функція все одно мусить розрізняти події або може знадобитися двовимірна таблиця. Це змінює компроміс між явністю і розміром даних. Таблиця не прибирає потреби описати, що робити з невідомим станом, відсутнім handler-ом чи недозволеною подією.

Ключове слово `static` надає таблиці внутрішнє зв’язування на рівні файла, а `const` забороняє змінювати елементи через це ім’я. Воно саме по собі не обіцяє, що байти опиняться саме у Flash: розміщення read-only секцій визначає linker script і платформа. Так само function pointer не є автоматично швидшим за `switch`; виміряйте цільову збірку, якщо це важливо.[^iso-c-n1570]

**Типові помилки:**

- Індексувати таблицю неперевіреним значенням стану.
- Припускати, що `const` гарантує фізичне розміщення у Flash на кожному MCU.
- Вважати один lookup доказом сталої тривалості всього handler-а.

## Sources

<!-- generated from frontmatter -->

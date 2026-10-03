---
id: emb-fnptr-0042
title: "Чому `std::function` не завжди підходить для embedded callback API?"
description: "std::function зручний, але може мати overhead і потенційні allocation-и."
track: embedded
section: function-pointers-and-callbacks
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
  - source_id: cppreference-function
    title: "cppreference: std::function constructor"
    url: https://en.cppreference.com/w/cpp/utility/functional/function
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Описує type erasure та гарантію small-object optimization для function pointer і reference_wrapper; інші allocation details залежать від реалізації."
---

## Short answer

**`std::function` зручний, але може мати overhead і потенційні allocation-и.**

Він стирає тип callable і може зберігати lambdas/functors, але це збільшує code size, може тягнути exceptions/RTTI залежно від toolchain і іноді використовує heap, якщо callable не вміщається в small buffer optimization.

Embedded-правило: у low-level drivers частіше використовують `function pointer + void *ctx`; у application layer `std::function` можливий, якщо політика проекту дозволяє.[^cppreference-function]

## Detailed explanation

`std::function` зберігає callable через type erasure, що спрощує API, але додає непрямий виклик і може вимагати динамічної пам’яті.[^cppreference-function]

Звичайний template або function pointer зберігає конкретний тип callable у типі самої змінної чи API. Натомість `std::function<R(Args...)>` надає єдиний тип-обгортку для функцій, lambda expressions і functor-ів із сумісною сигнатурою. Усередині обгортка зберігає ціль та операцію її виклику. Це зручно для гнучких черг подій, але зазвичай означає додаткову непряму диспетчеризацію та більший код.[^cppreference-function]

Стандарт гарантує відсутність dynamic allocation для деяких малих цілей, зокрема function pointer; для довільного callable такого загального гарантування немає. Реалізація може зберігати невеликі об’єкти у внутрішньому буфері, а більші розміщувати окремо. Поріг і деталі оптимізації залежать від реалізації, тому захоплена lambda може виділити пам’ять у одній конфігурації та ні в іншій.[^cppreference-function]

Для firmware це має значення, якщо callback створюється у критичному за часом шляху, heap заборонений або потрібна передбачувана затримка. Сам факт використання `std::function` не доводить, що буде allocation: виміряйте конкретну реалізацію та callable. Низькорівневий драйвер часто використовує function pointer разом із `void *context`, де розмір і життєвий цикл явні; application layer може обрати `std::function`, якщо вимоги до ресурсів це дозволяють.[^cppreference-function]

**Типові помилки:**

- вважати, що кожен `std::function` обов’язково виділяє пам’ять;
- припускати, що жодна lambda не виділить пам’ять;
- оцінювати придатність лише за синтаксисом, не перевіривши latency, heap policy та розмір прошивки.

## Sources

<!-- generated from frontmatter -->

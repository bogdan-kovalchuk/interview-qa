---
id: emb-fnptr-0044
title: "Що таке state machine на function pointers?"
description: "Це таблиця state handlers або transition handlers, де поточний state вибирає функцію для обробки event-а."
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
  - source_id: cppreference-pointer
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Описує типи вказівників на функції, потрібні для таблиці handler-ів; вибір моделі state machine є архітектурним рішенням."
---

## Short answer

**Це таблиця state handlers або transition handlers**, де поточний state вибирає функцію для обробки event-а.

Наприклад: `state = handlers[state](ctx, event);`. Це робить кожен state окремою функцією і зменшує великий nested `switch`. Для embedded protocol stacks це часто читабельно і тестовано по state handler-ах.

Правило: state enum має бути bounds-checked перед індексом у handler table.[^cppreference-pointer]

## Detailed explanation

State machine на function pointers зберігає обробники станів у таблиці, а поточний стан обирає функцію для наступної події.[^cppreference-pointer]

Замість одного довгого `switch` програма може мати масив handler-ів із сумісною сигнатурою, наприклад `State (*)(Context *, Event)`. Кожен handler описує реакцію на event у конкретному стані та може повернути наступний стан. Інший поширений варіант зберігає в таблиці явні переходи або handler-и дій; важливо, щоб модель стану й переходу залишалася зрозумілою, а не була прихована у довільних побічних ефектах.

Таблиця полегшує ізольоване тестування поведінки станів і дозволяє компактно додавати стани. Водночас це не автоматично безпечніше за `switch`: індекс таблиці треба перевірити. Значення enum може бути некоректним через пошкоджені дані, помилку перетворення або зовнішній input. Перевірка меж і визначений fallback не дають прочитати пам’ять за межами таблиці. Якщо таблиця має пропуски, явно позначте їх як недопустимі, а не викликайте нульовий вказівник.

Приклад: для станів `Idle`, `Receiving` і `Done` таблиця містить по handler-у. Після отримання байта код перевіряє, що числовий індекс відповідає одному з трьох записів, викликає обробник із контекстом та подією, а результат зберігає як новий стан. Сам handler може перевірити довжину пакета чи контрольну суму й повернути `Done` лише після завершення умов протоколу.

**Типові помилки:**

- індексувати таблицю довільним значенням enum без перевірки;
- змішати порядок значень enum і записів таблиці;
- не визначити реакцію на неочікувану подію або недопустимий стан.

## Sources

<!-- generated from frontmatter -->

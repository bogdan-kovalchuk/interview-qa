---
id: emb-fnptr-0054
title: "Чи можна порівнювати function pointers?"
description: "Так, function pointers одного сумісного типу можна порівнювати на рівність/нерівність."
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
---

## Short answer

**Так, function pointers одного сумісного типу можна порівнювати на рівність/нерівність.**

Це корисно для перевірки `cb != NULL` або для визначення, чи зареєстрований default handler. Але ordering comparison типу `<` не має змісту для function pointers.

Правило: використовуй function pointer comparison лише для equality checks, не для сортування або range checks адрес коду.[^iso-c-n1570]

## Detailed explanation

Так, function pointers сумісних типів можна порівнювати на рівність і нерівність; результат стосується того, чи позначають вони ту саму функцію або чи є обидва null pointers. Це визначено правилами equality operators у C, а не фізичним розташуванням машинного коду.[^iso-c-n1570]

Такий тест корисний для перевірки, чи зареєстровано callback: `if (cb != NULL)` відокремлює відсутній handler від вказівника на функцію. Також можна порівняти callback з конкретною відомою функцією, якщо типи сумісні. Рівність тут означає рівність значень function pointers за правилами мови, а не однаковість тексту вихідного коду чи конкретної адреси після оптимізації.[^iso-c-n1570]

Не плутай equality operators `==` і `!=` з relational operators `<`, `>` та їхніми варіантами. Обмеження relational operators C дозволяють вказівники на сумісні типи об’єктів, але не на функції. Тому спроба впорядкувати function pointers є constraint violation, а не спосіб знайти функцію, що розташована «раніше» у Flash. Розкладка коду може змінюватися під час link і не є переносним порядком для логіки програми.[^iso-c-n1570]

Приклад: таблиця callback-ів може містити `NULL` до ініціалізації. Перевірка `cb == NULL` безпечно визначає цей стан; викликати `cb()` до перевірки не можна, якщо значення ще може бути null. Для двох конкретних handlers допустимо порівняти `cb == on_rx`, коли сигнатури сумісні, але не порівнювати їх для сортування.

**Типові помилки:**

- Використовувати `<` для порівняння адрес функцій або визначати пріоритет callback-а за їхнім розташуванням.
- Порівнювати значення різних несумісних function pointer types без явного коректного приведення та розуміння наслідків виклику.
- Вважати будь-який неперевірений function pointer безпечним для виклику.

Для вибору callback-а використовуй явний enum, індекс або таблицю реєстрації. Equality перевіряє ідентичність значення вказівника; воно не замінює механізм пріоритету чи маршрутизації подій.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

---
id: emb-patterns-0019
title: "Чому в багатьох API `ERR_OK` дорівнює 0?"
description: "Щоб 0 означав успіх, а будь-яке ненульове значення – помилку (truthiness)."
track: embedded
section: common-code-patterns
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

**Щоб `0` означав успіх, а будь-яке ненульове значення – помилку** (truthiness).

Тоді `if (result) { handle_error(); }` і `if (sensor_read(...) != ERR_OK)` працюють природно. Це типова конвенція HAL (hardware abstraction layer) і багатьох POSIX-подібних API (application programming interface): 0 = success, non-zero/negative value = error.

Правило: у enum помилок `ERR_OK = 0` на першому місці; реальні коди – ненульові.[^iso-c-n1570]

## Detailed explanation

У багатьох C API нуль означає успішне виконання, а ненульові коди позначають різні помилки. Це домовленість інтерфейсу, а не правило мови C: `enum` дозволяє призначити `ERR_OK` будь-яке ціле значення, і конкретна бібліотека визначає власні коди. Тому назва `ERR_OK` сама по собі не доводить, що значення дорівнює нулю; перевіряй документацію API або явне присвоєння в оголошенні.[^iso-c-n1570]

Коли успіх має значення нуль, вираз `if (result)` у C входить у гілку для будь-якого ненульового результату. Це дає зручний короткий тест помилки, але не розрізняє причини: для цього код потрібно порівняти з конкретними значеннями, наприклад `ERR_TIMEOUT` чи `ERR_CRC`. Явне `result != ERR_OK` часто читабельніше, особливо якщо набір кодів може змінитися.

**Приклад:**

```c
typedef enum { ERR_OK = 0, ERR_TIMEOUT, ERR_CRC } err_t;
err_t result = sensor_read();
if (result != ERR_OK) {
    log_error(result);
}
```

Оскільки перший перелічувач дорівнює нулю, наступні автоматично отримують послідовні значення, якщо не вказано інше. Це лише спосіб оголосити константи; він не забезпечує, що стороння функція справді повертає їх за задокументованим контрактом.[^iso-c-n1570]

**Типові помилки:**

- Вважати, що будь-який API зобов’язаний використовувати нуль для успіху. Деякі API повертають кількість байтів, індекс або окремий статус.
- Вважати, що будь-яке ненульове значення в усіх системах є помилкою: у деяких контрактах ненульове значення може бути успішним результатом.
- Перевірити лише truthiness там, де треба окремо обробити timeout і пошкоджені дані.

## Sources

<!-- generated from frontmatter -->

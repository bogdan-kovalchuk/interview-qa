---
id: emb-align-0032
title: "Як правильно надіслати дані між двома різними MCU?"
description: "Визначити явний wire-формат і серіалізувати поле за полем з явним byte order."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 4
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

**Визначити явний wire-формат і серіалізувати поле за полем з явним byte order.**

Формат визначає поля, ширини, byte order, signedness, версію та перевірку довжини. Не передавай struct як сирі байти між різними ABI: padding, alignment і представлення типів можуть різнитися. `htonl`/`htons` стосуються 32- і 16-бітних чисел у network byte order, а не є загальним encoder.[^iso-c-n1570]

Явна специфікація та відповідні encoder/decoder прибирають залежність формату від layout конкретної структури; переносимість обмежена типами й правилами, які формат визначає.[^iso-c-n1570]

## Detailed explanation

Щоб дві MCU обмінювалися даними, вони мають погодити wire format – послідовність байтів і значення кожного поля. Визначають ширину чисел, byte order, signed representation, кодування тексту чи floating-point, межі повідомлення та реакцію на некоректні поля. Стандартизований формат, наприклад CBOR, задає data model та encoding; власний протокол мусить описати ці деталі сам.[^iso-c-n1570]

Не покладайся на raw `memcpy` структури: різні збірки можуть мати різні padding, alignment, endianness або представлення типів. Навіть однаковий компілятор не гарантує сумісності між ABI чи версіями формату. Encoder має записувати поле в узгоджене місце, а decoder – перевірити довжину перед читанням і відновити значення за правилами протоколу.[^iso-c-n1570]

Наприклад, протокол може визначити `temperature` як signed 16-bit integer у big-endian зі scale 0.01 градуса. Encoder записує старший, а потім молодший byte; decoder перевіряє, що є обидва байти, і відновлює значення з урахуванням масштабу та знаковості. Це специфікація протоколу, а не layout C-структури.[^iso-c-n1570]

`htons` і `htonl` перетворюють відповідно 16- та 32-бітні значення між host byte order і network byte order у системах із відповідними API. Для іншої ширини чи формату потрібна окрема логіка; ці функції не визначають framing, версіювання чи валідацію повідомлень.[^iso-c-n1570]

**Типові помилки:**
- Передавати `sizeof(struct)` байтів і припускати, що інша MCU має такий самий layout.
- Вважати byte order єдиною різницею між двома ABI.
- Декодувати до перевірки довжини та допустимих значень полів.

Серіалізуй і десеріалізуй поле за полем, тестуй відомі byte vectors на обох MCU і тримай формат незалежним від внутрішніх структур програми. Для сумісності через зміну формату визнач правила версіювання або розширення.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

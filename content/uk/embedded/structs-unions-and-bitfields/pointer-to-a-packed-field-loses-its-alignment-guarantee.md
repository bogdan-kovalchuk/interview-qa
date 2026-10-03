---
id: emb-structs-0013
title: "Чому pointer на packed поле може бути небезпечним?"
description: "&pkt.value може бути невирівняною адресою для вказівника на uint32_t."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: gcc-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Документація GCC для розширень атрибутів і їхніх обмежень."
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
struct __attribute__((packed)) P {
    uint8_t tag;
    uint32_t value;
};

uint32_t *p = &pkt.value;
```

## Short answer

<span class="warn">`&pkt.value` може бути unaligned address для `uint32_t *`.</span>

Звичайний `uint32_t *` несе припущення, що адреса достатньо вирівняна для `uint32_t`. Якщо поле packed, це припущення може бути хибним. Розіменування такого pointer може бути undefined behaviour або fault на MCU.

Захист: не бери pointer на packed multi-byte fields; використовуй `memcpy(&tmp, &pkt.value, sizeof tmp)` або byte parser.[^gcc-attributes]

## Detailed explanation

Взяття адреси packed-поля може створити вказівник, адреса якого не відповідає звичайному alignment типу поля. У прикладі `tag` має один байт, тому `value` може починатися за offset 1; звичайний `uint32_t *` за контрактом типу призначений для адреси, належно вирівняної для `uint32_t`. GCC окремо попереджає, що адреса packed member зазвичай дає unaligned pointer.[^gcc-attributes]

Це небезпечно навіть тоді, коли сам доступ через `pkt.value` компілятор уміє згенерувати безпечно: при взятті адреси інформація про packed-контекст може загубитися. Якщо передати `p` функції, яка читає `*p`, функція може скомпілювати звичайне вирівняне завантаження. За правилами C перетворення покажчика на тип із вимогою alignment, коли результат не вирівняний, має undefined behaviour; на MCU це може також завершитися fault.[^gcc-attributes]

**Приклад:**

Для читання поля скопіюйте його байти в локальний `uint32_t` за допомогою `memcpy(&tmp, &pkt.value, sizeof tmp)`, а потім окремо врахуйте byte order формату. Або передайте байтовий буфер і offset спеціалізованому parser-у. Не маскуйте проблему cast-ом до `uint32_t *`: cast не змінює адресу й не робить її вирівняною.[^gcc-attributes]

**Типові помилки:**

- Вважати, що `&pkt.value` завжди вирівняна лише тому, що тип поля – `uint32_t`.
- Передавати адресу поля у звичайну функцію для `uint32_t *`.
- Плутати коректність доступу, згенерованого для packed member, з коректністю окремого pointer type.

Компілятор може діагностувати таке взяття адреси; не вимикайте відповідне попередження без обґрунтування. Якщо API потребує pointer, передавайте адресу вирівняної локальної копії й копіюйте результат назад лише коли це безпечно для формату. Перевірте розмір поля й межі вихідного буфера окремо: правильне вирівнювання не є перевіркою меж.[^gcc-attributes]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

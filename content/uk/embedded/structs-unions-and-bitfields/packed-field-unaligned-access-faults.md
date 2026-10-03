---
id: emb-structs-0012
title: "Trap: чому `__attribute__((packed))` може спричинити HardFault?"
description: "Бо multi-byte поле може стати невирівняним."
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

## Short answer

<span class="warn">Бо multi-byte поле може стати невирівняним.</span>

Якщо `uint32_t value` у packed struct лежить на offset 1, доступ до нього може згенерувати unaligned load/store. На Cortex-M це залежить від ядра, налаштувань і типу інструкції: іноді працює повільніше, іноді дає UsageFault/HardFault, особливо для певних halfword/word або peripheral accesses.

Захист: для packed protocol data читай поля через `memcpy` у вирівняну локальну змінну або парсь байти явно.[^gcc-attributes]

## Detailed explanation

`__attribute__((packed))` може розмістити багатобайтове поле за адресою, яка не відповідає alignment його типу. Наприклад, після однобайтового `tag` поле `uint32_t value` може мати offset 1. Це не означає, що кожен такий доступ обов’язково впаде: наслідок залежить від ISA, конкретної інструкції, налаштувань ядра та області пам’яті.[^gcc-attributes]

Деякі процесори виконують частину unaligned load/store повільніше або кількома операціями; інші інструкції чи доступи до Device-пам’яті можуть вимагати alignment і викликати exception. Для Cortex-M результат залежить від моделі ядра, конфігурації та виду операції, тому твердження «packed завжди спричиняє HardFault» так само хибне, як і «unaligned access завжди безпечний». Перевіряйте programmer’s manual і налаштування цільового MCU.[^gcc-attributes]

**Приклад:**

Коли дані приходять із мережі або збережені у щільному binary format, скопіюйте байти поля в локальний правильно вирівняний об’єкт через `memcpy`, а потім застосуйте потрібне перетворення byte order. Інший варіант – скласти число з окремих байтів. Переконайтеся, що довжина буфера достатня; `memcpy` не перевіряє межі й не виправляє endianness автоматично.[^gcc-attributes]

Проблема може бути оманливою: на одному compiler/MCU тест проходить, але інша оптимізація генерує іншу послідовність доступу, або помилка виникає лише при ввімкненому trap для unaligned operation. Неправильне вирівнювання також може спричинити штраф продуктивності без fault.

**Типові помилки:**

- Діагностувати кожен HardFault як наслідок packed поля без аналізу fault status та адреси.
- Передавати адресу такого поля функції, яка очікує звичайний вирівняний `uint32_t *`.
- Вважати, що `memcpy` виконує endian conversion або перевіряє вхідний буфер.

У коді, який мусить працювати на кількох ядрах, краще парсити wire format явно або перевіряти властивості кожної цілі. Для register access не застосовуйте packed як спосіб обійти вимоги peripheral щодо ширини та alignment доступів.[^gcc-attributes]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

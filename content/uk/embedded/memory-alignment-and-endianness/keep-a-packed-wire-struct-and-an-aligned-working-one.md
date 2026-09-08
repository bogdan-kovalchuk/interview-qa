---
id: emb-align-0010
title: "Який рекомендований патерн роботи з packed wire-форматом?"
description: "Тримай дві структури: packed для дроту і звичайну вирівняну для обробки."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-08
content_revision: 4
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: gcc-type-attributes
    title: "Common Type Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Type-Attributes.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Документує атрибут типу packed у GCC та його вплив на розташування членів."
  - source_id: learncpp-struct-miscellany
    title: "Struct miscellany"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткове пояснення padding у структурах і порядку членів."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткова українська дорожня карта подальшого вивчення C і C++; не є нормативним джерелом правил wire-формату."
---

## Short answer

**Відокремлюй зовнішнє байтове представлення від звичайного вирівняного типу, з яким працює програма.**

```c
struct __attribute__((packed)) WireReading {
    uint8_t timestamp_le[4];
    uint8_t value_le[2];
    uint8_t id;
};

struct Reading {
    uint32_t timestamp;
    uint16_t value;
    uint8_t id;
};
```

Декодуй кожне байтове поле у вирівняний об'єкт, явно застосовуючи порядок байтів формату. Далі працюй із вирівняним об'єктом.

Правило: packed-тип описує розташування у сховищі, але сам собою не визначає серіалізацію, порядок байтів або безпечний native-доступ.[^embeddedinterviewlab]

## Detailed explanation

Два представлення мають різні завдання:

- `WireReading` відповідає зовнішньому запису із семи байтів. Багатобайтові значення в ньому є масивами байтів, тому читання запису не створює невирівняний lvalue типу `uint16_t` або `uint32_t`.
- `Reading` зберігає native-цілі числа з вирівнюванням і порядком байтів цільової платформи. Решта програми має працювати саме з цим типом.

Для little-endian wire-формату декодування може бути явним:

```c
static uint16_t load_le16(const uint8_t p[2]) {
    return (uint16_t)p[0] | ((uint16_t)p[1] << 8);
}

static uint32_t load_le32(const uint8_t p[4]) {
    return (uint32_t)p[0]
         | ((uint32_t)p[1] << 8)
         | ((uint32_t)p[2] << 16)
         | ((uint32_t)p[3] << 24);
}

static struct Reading decode(const struct WireReading *wire) {
    return (struct Reading) {
        .timestamp = load_le32(wire->timestamp_le),
        .value = load_le16(wire->value_le),
        .id = wire->id,
    };
}
```

Таке перетворення на межі робить alignment і endianness явними та придатними до тестування. Якщо packed-структура натомість містить native багатобайтові члени, вони можуть опинитися за адресами, непридатними для звичайного типізованого доступу; GCC також попереджає, що взяття адреси такого поля може створити некоректний вказівник.[^gcc-type-attributes] Packing прибирає певний padding, але не перетворює повне об'єктне представлення компілятора на переносний протокол.

Для фіксованого формату перевіряй його розмір і offsets під час компіляції, тестуй відомі байтові вектори та виконуй зворотне перетворення під час кодування. Матеріал про struct padding пояснює, чому вирівняний робочий тип може бути більшим за wire-запис,[^learncpp-struct-miscellany] а дорожня карта aCode допомагає розмістити цю системну тему в ширшому плані вивчення C і C++.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->

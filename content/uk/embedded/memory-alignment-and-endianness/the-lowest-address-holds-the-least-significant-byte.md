---
id: emb-align-0035
title: "Що виведе цей код на little-endian машині?"
description: "На little-endian молодший байт 0x44 лежить за найнижчою адресою, тож код виведе 44; на big-endian – 11."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
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

## Question code

```c
uint32_t w = 0x11223344;
uint8_t *p = (uint8_t*)&w;
printf("%02X", (unsigned)p[0]);
```

## Short answer

На little-endian код виведе `44`: байт із молодшими значущими бітами `0x44` лежить за найнижчою адресою, тож `p[0]` читає саме його. На big-endian вивід був би `11`; огляд байтів об’єкта через `uint8_t*` дозволений, бо це character type.[^iso-c-n1570]

## Detailed explanation

Endianness описує порядок байтів у багатобайтовому числовому значенні. На little-endian реалізації байт із молодшими значущими бітами розміщено за нижчою адресою; на big-endian порядок зворотний. Це властивість представлення конкретної реалізації, а не порядок, який C вимагає для всіх машин.[^iso-c-n1570]

У прикладі `w` має значення `0x11223344`, а через `uint8_t*` код на звичній платформі оглядає байти його object representation. За 8-бітних байтів little-endian `p[0]` дорівнює `0x44`, тоді як big-endian дасть `0x11`. Інші байти в першому випадку йдуть як `33`, `22`, `11`, а в другому – як `11`, `22`, `33`, `44`.[^iso-c-n1570]

Стандарт C дозволяє оглядати object representation через character type; на поширених реалізаціях `uint8_t` є псевдонімом `unsigned char`. Приведення `(unsigned)` у виклику `printf` потрібне тому, що після integer promotion `p[0]` має тип `int`, а `%X` очікує `unsigned int`; без нього тип аргументу не відповідав би специфікатору.[^iso-c-n1570]

**Приклад:**

Для читання протоколу не слід покладатися на те, що байти в пам’яті хоста вже мають потрібний wire order. Якщо формат задає big-endian, значення можна скласти явно: `value = ((uint32_t)b0 << 24) | ((uint32_t)b1 << 16) | ((uint32_t)b2 << 8) | b3`. Тоді результат не залежить від розкладки локального `uint32_t`; також треба перевірити, що в буфері є всі чотири байти.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

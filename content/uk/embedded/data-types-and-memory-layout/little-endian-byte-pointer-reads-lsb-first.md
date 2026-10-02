---
id: emb-dtypes-0090
title: "Що виведе на little-endian? `uint32_t x = 0xDEADBEEF; uint8_t *p = (uint8_t*)&x; printf(\"%02X\", p[0]);`"
description: "На little-endian молодший байт лежить за найменшою адресою, тож p[0] дає EF."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

На little-endian системі `0xDEADBEEF` зберігається байтами від молодшого до старшого, тому `p[0]` дорівнює `0xEF`. Це залежить від порядку байтів цільової платформи. Для огляду object representation стандарт C дозволяє доступ через `unsigned char*`; не кожна реалізація зобов’язана визначати `uint8_t`, і якщо він існує, не слід припускати без перевірки, що це character type.[^iso-c-n1570]

## Detailed explanation

Endianness описує порядок байтів багатобайтового значення в пам’яті. У little-endian найменш значущий байт лежить за найменшою адресою; у big-endian першим за адресою буде найстарший байт. Порядок бітів усередині окремого байта цим терміном не задається.

Для `uint32_t x = 0xDEADBEEF` байти значення мають значення `DE`, `AD`, `BE`, `EF`. На little-endian адреси зростають у напрямку від `EF` до `DE`, отже читання першого байта дає `0xEF`. На big-endian перший байт буде `0xDE`. Типізований доступ до `x` як до `uint32_t` повертає саме числове значення незалежно від порядку байтів; різниця проявляється, коли програма оглядає його представлення в пам’яті.[^iso-c-n1570]

Для доступу до байтів object representation у C стандарт гарантує спеціальний aliasing дозвіл для character types, зокрема `unsigned char`. `uint8_t` є необов’язковим typedef: він існує лише коли реалізація має ціле типу рівно 8 біт без padding. Хоча на поширених MCU це часто псевдонім `unsigned char`, сам факт наявності `uint8_t` не слід перетворювати на загальне твердження про character aliasing.[^iso-c-n1570]

Приклад для заданого little-endian target: байтова послідовність буде `[EF][BE][AD][DE]`, тому індекси 0–3 читають саме ці значення. Це не спосіб серіалізації переносимого формату: для файлу чи мережі явно кодуйте байти в потрібному порядку, а не записуйте пам’ять структури напряму.

Для практичної перевірки порядок байтів можна виявити, записавши значення 1 у багатобайтове ціле та оглянувши його через `unsigned char*`. Такий тест повідомляє про конкретний target, але його результат не можна зашивати як універсальне припущення для іншого MCU, симулятора чи протоколу. Навіть на одному процесорі зовнішній формат має власний визначений порядок.

**Типова помилка:** вважати, що little-endian визначає порядок байтів у протоколі або що всі MCU використовують його. Порядок треба встановити контрактом формату чи перевірити для конкретної цілі.[^iso-c-n1570]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

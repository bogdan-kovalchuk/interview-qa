---
id: emb-volconst-0029
title: "Що означає MISRA-підхід до `const` для pointer parameters?"
description: "Pointer parameter має вказувати на const-qualified type, якщо функція не змінює pointed-to object."
track: embedded
section: volatile-and-const
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
  - source_id: mathworks-misra-813
    title: "MISRA C:2012 Rule 8.13 – A pointer should point to a const-qualified type whenever possible"
    url: https://www.mathworks.com/help/bugfinder/ref/misrac2012rule8.13.html
    accessed: 2026-10-04
    kind: community
    version: "R2026b"
    applicability: "Переказує текст, rationale та статус Rule 8.13 як advisory; це документація інструмента, а не повний нормативний текст MISRA."
---

## Short answer

**За MISRA C:2012 Rule 8.13 pointer слід спрямовувати на const-qualified type, коли це можливо; це advisory recommendation.**

Це рекомендація, а не обов’язкова вимога: вона спонукає не надавати функції зайве право змінювати об’єкт і дає static analyzer змогу виявляти pointer parameters, які можна кваліфікувати як `const`.[^mathworks-misra-813]

Практичне правило: для parser, який лише читає frame, обери `void parse(const uint8_t *frame, size_t len)`. Застосовуй виняток, коли функції справді потрібно змінювати об’єкт або є інша обґрунтована причина.[^mathworks-misra-813] [^iso-c-n1570]

## Detailed explanation

MISRA C:2012 Rule 8.13 рекомендує, щоб pointer вказував на `const`-qualified type, коли це можливо. Її формулювання – «should», а категорія правила – advisory, отже це рекомендація щодо якості коду, а не безумовна вимога стандарту мови C чи обов’язкова MISRA rule.[^mathworks-misra-813]

Кваліфікатор стосується pointed-to type, а не самого pointer. У `const uint8_t *frame` функція не може записувати байти через `frame`, хоча може змінити локальне значення pointer. У `uint8_t * const frame` pointer незмінний, але байти за адресою можна змінювати. Для read-only аргументу потрібна перша форма. Це дає компілятору змогу відхилити випадкове присвоєння через цей pointer і дозволяє передати як const, так і mutable object функції, що його лише читає.[^iso-c-n1570]

Рекомендація допомагає зробити межу API видимою. Наприклад, парсер кадру зазвичай не повинен змінювати вхідні байти, тому `parse(const uint8_t *frame, size_t len)` точно описує його поведінку. Аналізатор може виявити параметр без `const`, якщо функція його не змінює; однак аналіз залежить від інструмента та його налаштувань. Сам факт відсутності `const` не доводить помилку: функція, яка редагує буфер на місці, має приймати writable pointer.[^mathworks-misra-813]

Приклад: `void checksum(const uint8_t *data, size_t len)` може обчислити checksum, не змінюючи дані. `void normalize(uint8_t *data, size_t len)` може змінити елементи, тому `const` на pointed-to type тут завадив би потрібній поведінці. Не плутай це з top-level `const` на параметрі pointer: його зміна не змінює тип функції для caller і не захищає об’єкт, на який той вказує.[^iso-c-n1570]

**Типова помилка:** називати Rule 8.13 обов’язковою вимогою MISRA або ставити `const` на pointer замість pointed-to type. Перевіряй фактичні записи у функції та формулюй qualifier так, щоб він відповідав контракту.[^mathworks-misra-813]

## Sources

<!-- generated from frontmatter -->

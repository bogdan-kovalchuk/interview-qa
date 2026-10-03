---
id: emb-dtypes-0109
title: "Як union представлений у пам’яті і які обмеження має type punning через union?"
description: "У union всі members починаються з одного offset, а розмір і alignment визначаються найбільшим member. Запис в один member перезаписує ті самі байти. Для переносимої інтерпретації байтів краще використовувати memcpy."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
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
  - source_id: cpp-draft-union
    title: "C++ working draft: Unions"
    url: https://eel.is/c++draft/class.union
    accessed: 2026-10-04
    kind: spec
    version: null
    applicability: "Визначає активний member union та обмеження його lifetime у C++; не описує правила C."
---

## Short answer

У **union** всі members починаються з одного offset, а розмір і alignment визначаються його вимогами до членів та реалізацією. Запис в один member робить його активним; читання іншого має різні наслідки за правилами C і C++, зокрема правилами effective type та lifetime.[^iso-c-n1570][^cpp-draft-union] <span class="warn">Для переносимої інтерпретації байтів краще використовувати `memcpy`</span>, а не вважати, що union type punning однаково працює в C і C++.

## Detailed explanation

`union` надає спільне сховище для різних members: кожен member починається з однакової адреси, а розмір union достатній для найбільшого member із потрібним вирівнюванням. Реальна величина `sizeof` може включати padding, щоб масив таких union-об’єктів зберігав коректне вирівнювання. Це описує розміщення, але не означає, що всі члени одночасно містять незалежні значення.[^iso-c-n1570]

У типовому варіанті використання програма записує один member і трактує саме його як активний варіант. Якщо записати інший, ті самі байти використовуються новим значенням. Читання попереднього member не є загальним переносимим способом конвертації представлень. У C результат читання іншого member має правила про інтерпретацію object representation та може залежати від реалізації; у C++ читання неактивного member обмежене object lifetime, з окремими винятками, зокрема для common initial sequence standard-layout структур.[^iso-c-n1570][^cpp-draft-union]

Ця різниця важлива для firmware, де часто потрібно розкласти float на байти або подивитися на raw register value. Union punning може бути підтриманий конкретним компілятором як розширення чи гарантований ABI-прийом, але це треба документувати й перевіряти для конкретної toolchain/мовного режиму. Він не вирішує endianness: порядок байтів як і раніше задає платформа, а не сам union.[^cpp-draft-union]

Для переносимого копіювання object representation між сумісними об’єктами використовують `memcpy`, а протокольні значення декодують окремо за форматом. Наприклад, копіювання байтів у `uint32_t` усуває проблему alignment джерела, але не перетворює little-endian байти на числове значення в big-endian системі. Треба явно перевірити довжину, типове представлення та потрібний byte order.[^iso-c-n1570]

Приклад: `union { uint32_t word; uint8_t bytes[4]; }` дає доступ до спільних чотирьох байтів, але порядок `bytes[0]` для заданого `word` відрізняється залежно від endianness. Тому така конструкція може бути корисна у platform-specific коді, але не є серіалізатором протоколу.

**Типові помилки:**
- Вважати, що union автоматично конвертує значення між типами.
- Переносити правила union з C на C++ без перевірки стандарту.
- Вважати `sizeof(union)` рівним сумі розмірів усіх members або використовувати union як переносимий wire-format parser.[^iso-c-n1570]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

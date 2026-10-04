---
id: emb-align-0025
title: "Що повертає `_Alignof(T)` (C11) / `alignof(T)`?"
description: "Вимогу вирівнювання типу в байтах."
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

**Вимогу вирівнювання типу в байтах.**

Значення для `uint32_t` і `double` залежать від реалізації; часто наведені числа 4 і 8 не є гарантією стандарту. Це compile-time властивість, корисна для перевірок layout і власних allocators.

Правило: у C11 – `_Alignof` (макрос `alignof` у `<stdalign.h>`); у C++ – `alignof` вбудований.[^iso-c-n1570]

## Detailed explanation

`_Alignof(T)` у C повертає вимогу вирівнювання типу `T` як значення типу `size_t`; це властивість реалізації, а не обіцянка певного числа байтів для всіх платформ.[^iso-c-n1570]

Об’єкт має розташовуватися за адресою, що задовольняє вимоги його типу. Компілятор використовує ці вимоги, зокрема, щоб визначати layout структур і розміщення об’єктів. Оператор `_Alignof` дає програмі змогу дізнатися вимогу для повного типу під час компіляції; він не вимірює фактичну адресу змінної.[^iso-c-n1570]

Для `uint32_t` значення 4 поширене на звичних MCU ABI, але сам факт, що тип має 32 біти, не встановлює його alignment стандартом. Так само 8 для `double` – поширений приклад, не гарантія. Перевіряйте цільову реалізацію, коли layout має значення.

Приклад перевірки компілятором:

```c
_Static_assert(_Alignof(uint32_t) <= 8, "unexpected alignment");
```

**Типові помилки:**

- Вважати, що alignment дорівнює `sizeof(T)`.
- Вважати наведені для однієї ABI числа універсальними.

Власний allocator має забезпечити адресу, кратну вимозі alignment типу, а не просто достатньо великий розмір блока. У C11 стандартні alignment є фундаментальними; extended alignment можуть підтримуватися лише окремими реалізаціями, тому переносний код має враховувати можливості цільового компілятора.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

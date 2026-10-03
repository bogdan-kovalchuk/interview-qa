---
id: emb-volconst-0031
title: "Чим відрізняються `const char *p = \"OK\"` і `char p[] = \"OK\"`?"
description: "const char p вказує на read-only string literal, а char p[] створює mutable array з копією символів."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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

**`const char *p` вказує на read-only string literal, а `char p[]` створює mutable array з копією символів.**

У першому випадку `p[0] = 'N'` заборонено типом. У другому випадку масив містить `'O'`, `'K'`, `'\0'` у власному storage, і `p[0] = 'N'` дозволено.

Embedded-наслідок: literal може жити у Flash, а mutable array зазвичай потребує RAM.[^iso-c-n1570]

## Detailed explanation

`const char *p = "OK"` створює вказівник на перший символ string literal, тоді як `char p[] = "OK"` створює окремий масив із трьох `char`: `O`, `K` і завершального `\0`. У першому оголошенні `const` обмежує зміну символів через `p`; у другому елементи масиву змінювані. Сам вказівник `p` у першому випадку не є `const` і може бути спрямований на інше місце, якщо його оголошено у змінюваному контексті.[^iso-c-n1570]

Ці оголошення відрізняються типом об’єкта, а не лише способом запису адреси. Рядковий літерал у C має масивний тип символів, але спроба змінити його вміст має undefined behavior. Під час ініціалізації масиву символів його елементи отримують копію символів літерала, включно з нульовим термінатором, тож запис у `p[0]` змінює саме масив. Оголошення масиву одночасно задає власне сховище для його елементів.[^iso-c-n1570]

У вбудованій системі компілятор і компонувальник можуть розмістити незмінний literal у Flash, тоді як змінюваний масив із автоматичною тривалістю зберігання зазвичай потребує RAM і початкового копіювання. Точне розміщення залежить від тривалості зберігання об’єкта, ABI та linker script, тому не можна виводити адресу або фізичну пам’ять лише з типу вказівника. Для довготривалих рядків у RAM можна оголосити масив із `static`; для даних, які не змінюються, варто лишати доступ через `const`.[^iso-c-n1570]

Приклад:

```c
const char *p = "OK";  // p[0] = 'N' не дозволено
char copy[] = "OK";   // copy[0] = 'N' дозволено
```

**Типова помилка:** вважати, що `const char *p` означає незмінний сам вказівник. `const` стосується символів, на які він указує; запис `p = other` може бути дозволений, а `p[0] = 'N'` – ні.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

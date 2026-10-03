---
id: emb-volconst-0030
title: "Trap: що небезпечно в `char *p = \"OK\"; p[0] = 'N';`?"
description: "Запис у string literal має undefined behavior."
track: embedded
section: volatile-and-const
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

<span class="warn">Запис у string literal має undefined behavior.</span>

У C string literal ініціалізує масив із static storage duration, і спроба змінити цей масив має undefined behavior. Його фізичне розміщення залежить від реалізації; на MCU запис може спричинити fault, але це не гарантований симптом.

Використовуй `const char *p = "OK";` для доступу лише для читання або mutable array `char p[] = "OK";`, якщо потрібно змінювати символи.[^iso-c-n1570]

## Detailed explanation

Запис у string literal не є способом змінити текст на місці: у C така операція має undefined behavior. У декларації `char *p = "OK";` сам pointer має тип pointer to `char`, але це не змінює властивостей масиву, створеного string literal. C дозволяє таку ініціалізацію pointer, однак стандарт визначає, що спроба модифікувати масив literal дає undefined behavior.[^iso-c-n1570]

Це важлива відмінність між типом pointer і доступом до об’єкта. У прикладі `p[0] = 'N'` вираз індексації еквівалентний доступу до першого елемента масиву literal для запису. Компілятор може попередити про таке використання, а реалізація може розмістити literal у пам’яті, доступній лише для читання; тоді на MCU можливий fault. Проте ні попередження, ні fault не є умовою стандарту: після undefined behavior результат не визначений.[^iso-c-n1570]

Щоб зберегти незмінний текст, оголоси pointer як `const char *p = "OK";`. Це фіксує read-only намір у типі та не дозволяє записувати символ через `p`. Якщо потрібна власна змінювана копія, оголоси масив: `char p[] = "OK";`. У цьому разі елементи масиву ініціалізуються символами та завершальним нульовим байтом, і запис у його межах дозволений.[^iso-c-n1570]

Приклад: `char p[] = "OK"; p[0] = 'N';` змінює перший елемент власного масиву, тож після операції рядок містить `NK`. Натомість додавання `const` до pointer як у `char * const p` заборонило б перепризначити сам pointer, але не зробило б запис у literal коректним. Важливо кваліфікувати pointed-to type: `const char *p`.[^iso-c-n1570]

**Типова помилка:** прибрати попередження cast-ом або покладатися на те, що конкретна плата дозволяє запис у секцію literal. Не обходь діагностику; обери `const char *` для читання або окремий змінюваний масив для редагування.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

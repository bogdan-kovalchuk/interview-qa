---
id: emb-volconst-0040
title: "Що таке top-level і low-level `const` у pointer type?"
description: "Top-level const кваліфікує сам об’єкт pointer, low-level const кваліфікує pointed-to data."
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
---

## Short answer

**Top-level `const` кваліфікує сам об’єкт pointer, low-level `const` кваліфікує pointed-to data.**

У `int * const p` top-level const: `p` не можна переназначити. У `const int *p` low-level const: через `p` не можна змінити `*p`. Для API важливіше low-level const, бо воно описує, що функція робить із даними caller-а.

Правило: `const` після `*` кваліфікує pointer, а `const` перед base type кваліфікує pointed-to data.[^iso-c-n1570]

## Detailed explanation

У декларації `int * const p` top-level `const` кваліфікує сам pointer, а в `const int *p` low-level `const` кваліфікує об’єкт, на який він вказує. Розташування `const` відносно `*` допомагає прочитати, який саме рівень типу обмежений: після зірочки – pointer, перед базовим типом – pointed-to object.[^iso-c-n1570]

Це дає різні дозволи. Для `int * const p = &value` можна виконати `*p = 7`, якщо `value` є змінним `int`, але не можна присвоїти `p` іншу адресу. Для `const int *p = &value` можна змінювати сам `p`, проте запис `*p = 7` заборонений через цей вираз. Комбінований тип `const int * const p` забороняє обидві дії через `p`.

Low-level `const` часто використовують у параметрах функцій, щоб показати, що реалізація не змінює дані через цей pointer, наприклад `void print(const char *text)`. Це обмеження доступу через конкретний вираз, а не доказ, що об’єкт ніде не зміниться: інший non-const pointer може змінити змінний об’єкт. Якщо ж сам об’єкт оголошено const, спроба змінити його через cast має undefined behaviour за правилами C.[^iso-c-n1570]

**Типові помилки:**

- Читати `const int *p` так, ніби сам pointer є const.
- Вважати, що `int * const p` забороняє змінювати ціле число.
- Вважати, що cast знімає обмеження з об’єкта, який справді оголошений const.

Практичне читання зліва направо: тип даних, потім pointer та його власні qualifiers. У вкладених типах перевіряй кожен рівень окремо, бо `const int **` і `int * const *` мають різні правила сумісності й присвоювання.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

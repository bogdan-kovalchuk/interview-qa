---
id: emb-volconst-0019
title: "Як прочитати декларацію `const int *p`?"
description: "p є pointer to const int."
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

**`p` є pointer to const `int`**.

`p` можна перенаправити на інший `int`, але не можна виконати `*p = 5`. Важливо: сам об’єкт не обов’язково фізично immutable; просто через цей pointer він доступний тільки для читання.

Правило: читай від імені змінної вправо і вліво: `p` is pointer to const int.[^iso-c-n1570]

## Detailed explanation

Декларацію `const int *p` читають від імені `p`: це pointer на `const int`. Ім’я спершу пов’язане з найближчим до нього оператором `*`, який означає pointer, а кваліфікатор `const` у типі `int` забороняє зміну цільового об’єкта через розіменування цього pointer. Тому `p = other` може бути коректним, якщо типи сумісні, а `*p = 5` відхиляється як запис через const-qualified lvalue.[^iso-c-n1570]

Фраза «pointer to const» описує дозволений доступ, а не обов’язково властивість самої пам’яті. Наприклад, змінну `int value` можна передати функції як `const int *`, хоча код, що має доступ до `value` через його звичайне ім’я, може продовжувати її змінювати. Отже, `const` допомагає реалізації функції не змінити аргумент випадково і дає компілятору змогу перевірити цей намір, але не є механізмом синхронізації між перериванням, задачею чи іншим потоком.[^iso-c-n1570]

Правило читання «від імені вправо, потім вліво» є мнемонікою, а не універсальним парсером для довільних декларацій C. Для простих pointer-декларацій воно працює добре: у `const int *p` рух від `p` зустрічає `*`, отже маємо pointer, а далі базовий тип `int` має `const`. У складних деклараціях з дужками, масивами та функціями потрібно враховувати пріоритет declarator syntax; не можна механічно читати всі символи в одному напрямку.[^iso-c-n1570]

**Приклад:** нехай `int value = 3; const int *p = &value;`. Вираз `p = &other_value` може перенаправити pointer, а `*p = 5` заборонено. Якщо інший код виконає `value = 4`, читання `*p` дасть оновлене значення, бо сам `value` не обов’язково оголошений const.

**Типові помилки:**
- плутати `const int *p` з `int * const p`;
- називати цільовий об’єкт фізично незмінним;
- застосовувати мнемоніку без урахування дужок у складному declarator.

## Sources

<!-- generated from frontmatter -->

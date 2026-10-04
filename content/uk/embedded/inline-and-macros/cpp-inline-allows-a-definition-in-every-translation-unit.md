---
id: emb-macros-0048
title: "Чим відрізняється семантика `inline` у C і C++?"
description: "У C++ inline-функція може мати визначення в кількох translation units (TU) через header без порушення ODR (One Definition Rule) – лінкер зливає копії; це штатний спосіб класти функції в header."
track: embedded
section: inline-and-macros
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
  - source_id: cppreference-inline
    title: "cppreference: inline specifier"
    url: https://en.cppreference.com/w/cpp/language/inline
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Специфікатор inline у C++: inline-функція з external linkage може мати по одному визначенню в кожній translation unit за умови узгоджених визначень."
---

## Short answer

У C++ `inline`-функція може мати визначення в кількох translation units (TU) через header, якщо визначення відповідають вимогам ODR (One Definition Rule); це штатний спосіб визначати функції в header.[^cppreference-inline][^embeddedinterviewlab]

У C (C99+) правила складніші: чистий `inline` дає лише inline-визначення без external symbol, тому потрібен `extern` у одному TU або, простіше, `static inline`.

Правило: у C для header-функцій часто використовують `static inline`; у C++ `inline` дозволяє множинні визначення за умов ODR.[^iso-c-n1570]

## Detailed explanation

У C++ функція з `inline` може мати визначення в кількох translation units (TU), тому її часто визначають у header, який включають різні `.cpp` файли. Це дозволено правилами ODR (One Definition Rule), лише якщо виконані умови для множинних визначень; зокрема, вони мають відповідати одна одній. Лінкер не перетворює довільні різні тіла на коректне єдине визначення.[^cppreference-inline][^embeddedinterviewlab]

Слово `inline` не означає, що тіло обов’язково буде вставлено в місце виклику. Це мовна властивість визначення; оптимізатор окремо вирішує, чи робити таку підстановку. Отже, ключове слово може бути потрібне для розміщення визначення в заголовку, навіть якщо генерація машинного коду залишає звичайний виклик.[^embeddedinterviewlab]

C має іншу модель. У C99 і новіших стандартах `inline` із зовнішнім компонуванням пов’язаний із правилами external definition, тоді як `static inline` створює внутрішньо зв’язану функцію окремо для кожного TU. Саме тому `static inline` поширений для малих функцій у C headers. Результат треба співвідносити з режимом стандарту, заданим компілятору: GNU-режими можуть мати свої історичні правила inline.[^iso-c-n1570]

**Типові помилки:**

- Казати, що лінкер зливає копії без згадки про однаковість і вимоги ODR.
- Плутати множинні визначення в C++ з оптимізацією підстановки.
- Переносити рекомендацію `static inline` для C у C++ без розгляду компонування.

**Приклад:** спільний C++ header може визначати `inline` helper, який включено у `a.cpp` та `b.cpp`; це коректно за умови узгоджених визначень. Якщо умовна компіляція змінює тіло лише в одному TU, програма вже не відповідає припущенню про одне визначення. У C окремі TU з `static inline` мають власні внутрішні визначення, тож не потребують спільного зовнішнього символу.[^embeddedinterviewlab] [^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

---
id: emb-macros-0019
title: "Що рекомендує MISRA C Directive 4.9 щодо function-like макросів?"
description: "MISRA C Directive 4.9 рекомендує функцію замість function-like макросу, коли вони взаємозамінні."
track: embedded
section: inline-and-macros
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
  - source_id: misra-c2012-amd3-dir49
    title: "MISRA C:2012 Amendment 3"
    url: https://misra.org.uk/app/uploads/2022/12/MISRA-C-2012-AMD3.pdf
    accessed: 2026-10-04
    kind: spec
    version: "2012 Amendment 3"
    applicability: "На сторінці 11 уточнює виняток Directive 4.9 для function-like macros із _Generic; повний текст директиви міститься в основному документі MISRA C:2012."
  - source_id: gcc-cpp-overview
    title: "GCC CPP: Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Пояснює призначення препроцесора і підстановку макросів перед компіляцією; не є рекомендацією MISRA."
---

## Short answer

**MISRA C Directive 4.9 рекомендує функцію замість function-like макросу**, коли ці варіанти взаємозамінні.

Це директива з категорією Required, але вона не забороняє макроси безумовно; Amendment 3 уточнює виняток для макросів із `_Generic`.[^misra-c2012-amd3-dir49]

Практично перевіряй, чи може функція виконати ту саму роль без втрати потрібної поведінки; `static inline` може бути кандидатом, але директива не наказує саме цей механізм.[^misra-c2012-amd3-dir49]

## Detailed explanation

MISRA C Directive 4.9 рекомендує застосовувати функцію замість function-like macro, якщо обидва механізми взаємозамінні. Це саме директива, а не Rule 4.9, і вона формулює перевагу, а не загальну заборону макросів. Категорія Required означає вимогу дотримуватися директиви в межах відповідності MISRA, водночас оцінюючи чи справді два механізми взаємозамінні.[^misra-c2012-amd3-dir49]

Звичайна функція має оголошений тип параметрів, її аргументи обчислюються за правилами C, а debugger може показати виклик як функцію. Макрос натомість виконується препроцесором як підстановка токенів перед компіляцією. Через це function-like macro може повторно використати аргумент, підставити його в несподіваний синтаксичний контекст або приховати місце помилки у розгорнутому тексті. Такі відмінності пояснюють, чому функція є кращим вибором для звичайної поведінки, коли вона підходить.[^gcc-cpp-overview]

Directive 4.9 не означає, що кожен макрос треба механічно переписати на функцію. Наприклад, функція не може керувати `#if` та `#ifdef`, а compile-time формування токенів та окремі generic patterns можуть вимагати макросу. Amendment 3 прямо додає виняток, коли function-like macro потрібен для `_Generic`, бо в типовому випадку цей selection не можна замінити функцією.[^misra-c2012-amd3-dir49]

Приклад рішення: арифметичний `MAX(a, b)` краще розглянути як типізовану функцію або `static inline` реалізацію з чіткою політикою типів. Макрос `LOG_IF_ENABLED(...)`, що прибирається умовною компіляцією, не взаємозамінний із звичайним викликом у тих самих build modes. Вибір має враховувати мову, toolchain і вимоги проєкту, а відповідність MISRA визначається застосованою редакцією настанов та прийнятими відхиленнями.

**Типові помилки:**

- Називати Directive 4.9 правилом або трактувати її як абсолютну заборону.
- Стверджувати, що MISRA завжди вимагає саме `static inline`.
- Замінювати макрос без перевірки compile-time поведінки та сумісності типів.

## Sources

<!-- generated from frontmatter -->

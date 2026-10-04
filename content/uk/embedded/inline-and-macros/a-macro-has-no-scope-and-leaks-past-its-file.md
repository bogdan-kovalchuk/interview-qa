---
id: emb-macros-0035
title: "Trap: як макрос із header впливає на код, що його включає?"
description: "Після #define макрос замінює токени далі в тій самій translation unit, зокрема в заголовках, включених пізніше; окремо скомпільований файл визначення не успадковує."
track: embedded
section: inline-and-macros
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
  - source_id: gcc-cpp-macro-processing
    title: "GCC CPP: Object-like Macros and Undefining and Redefining Macros"
    url: https://gcc.gnu.org/onlinedocs/cpp/Object-like-Macros.html
    accessed: 2026-10-04
    kind: official
    version: current
    applicability: "Послідовне препроцесування, розгортання макросів і #undef у GNU CPP; описує типовий C preprocessor workflow."
---

## Short answer

<span class="warn">Макрос не має блокової чи файлової області видимості</span>: після `#define` препроцесор замінює його ім’я далі в поточній translation unit, зокрема в заголовках, включених після визначення. Окремо скомпільований `.c`-файл не успадковує визначення автоматично.[^gcc-cpp-macro-processing]

Наприклад, `#define max(a,b) ...` у header може зіпсувати `std::max` або поле `obj.max` у translation unit, що включає цей header.[^gcc-cpp-macro-processing]

Для зменшення конфліктів використовуй помітні UPPER_CASE імена з префіксом проєкту; коли макрос більше не потрібен у цій translation unit, його можна скасувати через `#undef`.[^gcc-cpp-macro-processing]

## Detailed explanation

Макрос у C – це директива препроцесора, яка визначає текстову заміну, а не оголошення зі звичайною областю видимості C. Препроцесор читає джерело послідовно: після рядка `#define NAME ...` подальші входження `NAME` розглядаються як макрос, поки його не скасовано через `#undef` або поки не завершено обробку translation unit.[^gcc-cpp-macro-processing]

У C `#include` обробляється як включення вмісту заголовка в поточну послідовність препроцесування. Тому макрос із заголовка впливає на код нижче місця включення та на інші заголовки, які обробляються після нього. Це не означає, що макрос магічно переходить до будь-якого іншого файлу проєкту: незалежно скомпільована одиниця трансляції має власний процес препроцесування і повинна окремо включити заголовок із визначенням.[^gcc-cpp-macro-processing]

Небезпека виникає через суто токенну заміну: препроцесор не розуміє, що `max` задумано як ім’я поля, функції або шаблону. Тож короткий макрос `max` може змінити синтаксис непов’язаного коду. Великі літери допомагають упізнати макрос, а префікс зменшує шанс колізії; ці домовленості не створюють ізоляції.[^gcc-cpp-macro-processing]

Приклад: якщо header визначає `PROJECT_MAX(a, b)`, а потім включає іншу бібліотеку, заміна діє і під час препроцесування цієї бібліотеки в тому самому translation unit. Якщо макрос потрібен лише всередині заголовка, заголовок може скасувати його після внутрішнього використання за допомогою `#undef`, але таке рішення має узгоджуватися з очікуваннями споживачів header.[^gcc-cpp-macro-processing]

**Типова помилка:** називати макрос локальним «для файлу», маючи на увазі лише файл із `#define`. Перевіряй ланцюжок `#include` і порядок включення. Для діагностики переглянь препроцесований вихід або скасуй визначення після останнього потрібного використання.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

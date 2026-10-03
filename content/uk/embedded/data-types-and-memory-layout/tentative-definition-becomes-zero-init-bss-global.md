---
id: emb-dtypes-0094
title: "Що таке tentative definition у C і де вона розміщується?"
description: "У C tentative definition на рівні файлу стає визначенням із нульовою ініціалізацією, якщо в translation unit немає іншого визначення."
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: gcc-codegen-options
    title: "GCC: Options for Code Generation Conventions"
    url: https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Документує різницю між -fcommon та -fno-common у GCC для глобальних tentative definitions; поведінка специфічна для GCC."
  - source_id: cpp-basic-def
    title: "C++ draft: Declarations and definitions"
    url: https://eel.is/c++draft/basic.def
    accessed: 2026-10-04
    kind: spec
    version: "current working draft"
    applicability: "Підтримує розрізнення declaration/definition у C++; не описує правила мови C."
---

## Short answer

**Tentative definition** – оголошення об’єкта у file scope без ініціалізатора і без `extern`, наприклад `int x;`. Якщо в межах цього translation unit немає звичайного визначення того самого ідентифікатора, C трактує її як визначення з нульовою ініціалізацією; розміщення в `.bss` не гарантується стандартом.[^iso-c-n1570]

У GCC розміщення в common block залежить від `-fcommon`; з `-fno-common` однакові визначення з кількох файлів можуть завершитися помилкою компонування. У C++ немає поняття tentative definition.[^gcc-codegen-options] [^cpp-basic-def]
## Detailed explanation

У C оголошення `int count;` на рівні файлу без `extern` є tentative definition. Воно заявляє об’єкт із зовнішнім зв’язуванням, але остаточне правило застосовується наприкінці translation unit: якщо там немає іншого, не tentative, визначення `count`, програма поводиться так, ніби є визначення з нульовим ініціалізатором. Якщо в тому самому файлі також є `int count = 5;`, цей зовнішній definition задовольняє tentative declaration; це не дві окремі змінні.[^iso-c-n1570]

Стандарт C описує семантику оголошень, але не вимагає, щоб zero-initialized об’єкт лежав саме в секції з назвою `.bss`. Таке розміщення є звичною домовленістю ABI та toolchain: initialized data часто має `.data`, а нульові глобальні – `.bss`, яку startup code очищає перед використанням програми. Інші формати об’єктів і компонувальники можуть застосовувати інші секції чи механізми.[^iso-c-n1570]

Обережно з розміщенням `int count;` у header, включеному до кількох C-файлів. Кожен translation unit отримає свою tentative definition, а поведінка компонування залежатиме від параметрів компілятора й ABI. Наприклад, GCC з `-fcommon` кладе такі глобальні в common block і дозволяє лінкеру звести їх, тоді як `-fno-common` створює звичайні визначення, дублікати яких спричиняють помилку. Заголовок має містити `extern int count;`, а єдине визначення – бути в одному `.c` файлі.[^gcc-codegen-options]

Це правило належить C і не переноситься механічно на C++. У C++ оголошення змінної на рівні простору імен без initializer зазвичай є визначенням, тому заголовковий `int count;` може порушити ODR при включенні в кілька translation units. Використовуйте `extern` для декларації, а визначення розміщуйте окремо або застосовуйте відповідну модель inline variables у сучасному C++.[^cpp-basic-def]

**Типова помилка:** вважати `.bss` частиною визначення мови або припускати, що однакові `int x;` у різних файлах завжди автоматично зливаються. Для C перевіряйте режим компілятора, а в переносному коді розділяйте декларацію та одне визначення.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

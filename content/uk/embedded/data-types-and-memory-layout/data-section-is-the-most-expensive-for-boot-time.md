---
id: emb-dtypes-0062
title: "Які дані startup code зазвичай копіює з Flash у RAM перед `main()`?"
description: "Startup code зазвичай копіює початкові значення `.data` з Flash у RAM перед main()."
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
  - source_id: gnu-ld-lma
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Описує LMA/VMA та приклад runtime-копіювання даних і очищення bss; конкретну ініціалізацію визначає платформа."
---

## Short answer

Startup code зазвичай копіює початкові байти `.data` з Flash у RAM перед `main()`, якщо секція має різні load і run addresses. Час залежить від розміру секції та пам’яті, тому `.data` не є універсально найдорожчою частиною старту.[^gnu-ld-lma]

`.bss` часто очищають у RAM, а розміщення `.text`, `.rodata` та інших секцій задає linker script і платформа.[^gnu-ld-lma]

## Detailed explanation

У типовій embedded конфігурації змінювані об’єкти зі статичною тривалістю зберігання, що мають ненульові початкові значення, потребують копії в RAM. Linker зберігає початкові байти в образі Flash за load memory address (LMA), тоді як код звертається до адреси виконання в RAM – virtual memory address (VMA). Startup routine копіює байти між цими адресами до виклику `main()`.[^gnu-ld-lma]

Вартість залежить від розміру `.data`, швидкості читання Flash і запису RAM та реалізації копіювання. Велика `.data` може подовжити старт, але інші операції – налаштування clock, перевірка образу чи калібрування – можуть коштувати більше. Linker script може задати інше розміщення, а startup code залежить від конкретної платформи.[^gnu-ld-lma]

Для `.bss` типовий крок – записати нулі в її діапазон RAM. `.text` зазвичай виконується з пам’яті коду, а `.rodata` часто залишається у Flash; це поширена схема, а не вимога C. Перевірте linker script і startup routine, перш ніж припускати, що секція не копіюється.[^gnu-ld-lma]

**Приклад оцінки:** якщо startup копіює 1200 байтів, час копіювання за незмінних тактування й реалізації зростатиме разом із розміром. Для фактичного висновку перевірте map-файл і виміряйте старт на цільовій платі. Незмінна таблиця може бути розміщена у read-only memory, якщо target читає дані звідти; саме `const` не гарантує конкретної секції без перевірки toolchain та linker script.[^gnu-ld-lma]

Розділення адрес потрібне, бо після старту процесор має бачити змінні за RAM-адресами, хоча їхні початкові байти зберігаються в образі прошивки. Linker script передає startup code межі й адреси областей, але реалізація може копіювати кілька секцій, очищати додаткову пам’ять або виконувати перевірки до `main()`.[^gnu-ld-lma]

Не робіть висновок про час запуску лише з розміру `.data`: виміряйте шлях від reset до потрібної контрольної точки й окремо перевірте копіювання, налаштування clock та інші ранні кроки. Це допомагає відрізнити витрати перенесення даних від повільного старту периферії чи верифікації образу.[^gnu-ld-lma]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

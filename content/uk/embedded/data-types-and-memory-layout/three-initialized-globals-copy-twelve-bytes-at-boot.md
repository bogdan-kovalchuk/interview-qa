---
id: emb-dtypes-0085
title: "Скільки байт скопіює startup code для (глобальні)? `int a=1; int b=2; int c=3;`"
description: "Усі три - ініціалізовані глобальні у .data, тож startup code копіює 12 байт (3 * sizeof(int)) з Flash у RAM."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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
    title: "GNU ld manual: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Пояснює LMA/VMA і приклад startup-копіювання ініціалізованих даних; сам linker script визначає набір байтів секції."
---

## Short answer

Точна кількість залежить від ABI та складу `.data`; за 32-бітного `int` і лише цих трьох об’єктів їхні значення займають 12 байтів.[^iso-c-n1570] [^gnu-ld-lma]

У типовій bare-metal схемі значення копіюються з LMA у Flash до VMA в RAM, але startup code переносить налаштований linker script діапазон `.data`, а не обов’язково саме ці змінні чи рівно 12 байтів.[^gnu-ld-lma]

Нульові ініціалізатори часто розміщують у `.bss`, але це рішення toolchain, а не гарантія C.[^gnu-ld-lma]

## Detailed explanation

У фрагменті є три об’єкти з початковими значеннями, але мова C не задає універсальну кількість байтів, яку скопіює startup code. `sizeof(int)` залежить від ABI, а linker script визначає розташування й межі секцій. Отже, за припущення, що `int` має 4 байти, усі три об’єкти залишилися в `.data`, а інших даних у копійованому діапазоні немає, їхні значення займають 12 байтів. Без цих припущень відповідь «12» не випливає з тексту програми.[^iso-c-n1570] [^gnu-ld-lma]

У типовому linker layout для bare-metal `.data` має VMA у RAM, де змінні читаються та змінюються під час виконання, і LMA у Flash, де зберігаються початкові байти. Startup routine копіює діапазон секції з LMA до VMA до виклику `main()`. Розмір копії зазвичай обчислюють як різницю між кінцевою і початковою адресами RAM-діапазону. Ці символи й діапазони походять із linker script, а не є вбудованою вимогою C.[^gnu-ld-lma]

Також важливо розрізняти розмір значень і розмір усієї копії. Змінні можуть бути вилучені оптимізацією або розміщені в іншій секції; `.data` може містити й інші об’єкти, а між ними можуть виникати пропуски через alignment. Натомість нульові ініціалізатори часто потрапляють у `.bss`: у файлі образу можна зберегти лише опис нульового RAM-діапазону, а startup code занулить його. Це поширена схема GNU toolchain, але точну поведінку треба перевіряти в ELF та linker script цільової збірки.[^gnu-ld-lma]

Для конкретного target подивись `sizeof(int)` у компіляторі, таблицю секцій ELF через `objdump -h` і символи меж через `nm`. Якщо `.data` займає 12 байтів, саме стільки байтів зазвичай копіюється для всієї секції, але не обов’язково вони належать лише трьом оголошеним змінним. Висновок про 12 байтів потребує явних умов щодо ABI, оптимізації та складу секції.[^gnu-ld-lma]

Ініціалізатор у вихідному коді також не обіцяє конкретне байтове представлення. Порядок байтів, ширина `int` і можливе вирівнювання визначаються реалізацією; наведену послідовність байтів не можна переносити на big-endian або іншу ABI-конфігурацію. Питання про фактичну копію найкраще розв’язувати за артефактами саме тієї збірки, яку прошивають на пристрій.[^iso-c-n1570] [^gnu-ld-lma]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

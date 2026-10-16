---
id: emb-volconst-0024
title: "Чому `const` важливий для embedded не лише як захист від запису?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gnu-ld-linker-scripts
    title: "GNU ld manual: Linker Scripts"
    url: https://sourceware.org/binutils/docs/ld.html
---

## Short answer

**`const` забороняє зміну через цей lvalue; linker script визначає розміщення у Flash**.

У типовій embedded-конфігурації linker script може розмістити read-only дані у Flash/ROM, а змінювані ініціалізовані дані скопіювати з Flash у RAM під час старту. Це залежить від системи, а не є гарантією C.[^gnu-ld-linker-scripts]

`const` для незмінних calibration tables, strings, protocol descriptors, CRC tables і LUT задає read-only доступ і може заощадити RAM. Перевіряйте map-файл: декларація сама не гарантує ні `.rodata`, ні Flash.[^iso-c-n1570] [^gnu-ld-linker-scripts]

## Detailed explanation

`const` у C обмежує зміну об’єкта через lvalue з кваліфікованим типом, але стандарт мови не описує Flash, SRAM, ELF-секції чи startup code. Це розмежування важливе в embedded: правило типів компілятор перевіряє, а використання пам’яті визначає ABI й конфігурація інструментів.[^iso-c-n1570]

У типовому проєкті компілятор формує окремі input sections для константних і змінюваних даних. GNU linker script зіставляє input sections із output sections і memory regions, тому конфігурація може спрямувати read-only дані до ROM/Flash. Імена `.rodata` та `.data` поширені, але точні шаблони й адреси задає конкретний linker script.[^gnu-ld-linker-scripts]

Ініціалізована змінювана глобальна змінна часто має runtime-адресу в RAM і load image у Flash: startup code копіює початкові байти перед викликом `main`. Read-only таблиця, якщо linker розмістив її в доступній для читання пам’яті програми, може лишатися у Flash і не витрачати SRAM на копію. Проте це залежить від архітектури: деякі MCU не дають звичайного доступу до Flash, або компілятор/скрипт спеціально копіює дані.[^gnu-ld-linker-scripts]

Приклад: LUT із 256 елементів `uint16_t` займає `256 * 2 = 512` байтів за умови, що `uint16_t` визначено і кожен елемент має 2 байти. Якщо вона справді читається напряму з Flash, ці 512 байтів не займають SRAM; перевірте linker map та секційні адреси, а не робіть висновок лише з ключового слова. Типова помилка – вважати, що `const` автоматично означає Flash: воно гарантує обмеження запису через тип, не фізичне розміщення.[^iso-c-n1570] [^gnu-ld-linker-scripts]

---
id: emb-dtypes-0065
title: "Як виглядає типовий layout секцій у `.elf` файлі для Cortex-M?"
description: "Flash тримає .text, .rodata і LMA .data, а RAM тримає VMA .data, .bss, heap і stack."
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
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Описує LMA/VMA та приклад runtime-копіювання; linker script конкретного target визначає фактичне розміщення."
  - source_id: gnu-ld-script
    title: "GNU ld: Linker Scripts"
    url: https://www.sourceware.org/binutils/docs/ld/Scripts.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Пояснює роль linker script у відображенні секцій і компонуванні; не задає універсальний layout усіх ELF."
---

## Short answer

**Flash (типово)**: `[.text][.rodata][.data LMA]`
**RAM (типово)**: `[.data VMA][.bss][heap]...[stack]`

LMA (Load Memory Address) – звідки завантажують байти; VMA (Virtual Memory Address) – адреса секції під час виконання. Для `.data` вони часто вказують відповідно на Flash і RAM, а startup code копіює дані між ними.

Перевірка: `arm-none-eabi-objdump -h firmware.elf` або `arm-none-eabi-size firmware.elf`[^gnu-ld-lma]

## Detailed explanation

Linker script визначає, як input sections потрапляють у output sections і які адреси їм призначити. У типовому bare-metal Cortex-M образі `.text` містить інструкції, `.rodata` – сталі дані; обидві секції зазвичай доступні у Flash. Змінювана ініціалізована `.data` має початкову копію в образі Flash, але адресу виконання в RAM.[^gnu-ld-lma]

Для секції розрізняють virtual memory address (VMA), тобто адресу під час виконання, і load memory address (LMA), звідки секцію завантажують. Директиви `AT` та `AT>` у linker script можуть призначити різні адреси. Startup code використовує символи linker-а, щоб скопіювати `.data` з LMA до VMA до запуску C-коду; типова ініціалізація також очищує `.bss` у RAM.[^gnu-ld-lma]

Це не фіксований формат усіх ELF-файлів. Назви й розміщення залежать від linker script, ABI, завантажувача та target. Heap і stack – runtime області RAM, їхні межі часто задають linker symbols або startup code; вони не обов’язково є ELF-секціями й не завжди ростуть назустріч одне одному.[^gnu-ld-script]

**Приклад перевірки:** `arm-none-eabi-objdump -h firmware.elf` показує секції, розміри та адреси. Зіставте `.data` з linker script і startup symbols, перш ніж робити висновок, що LMA у Flash, а VMA у RAM. У GNU ld директиви `AT` або `AT>` задають LMA для output section; без них linker виводить адресу за власними правилами. Назва секції сама по собі не показує фізичне розташування байтів.[^gnu-ld-lma]

Та сама секція може мати різні адреси завантаження й виконання, але не кожне середовище потребує такого поділу: якщо код виконується безпосередньо з місця зберігання або завантажувач розміщує образ інакше, схема зміниться. Тому перевіряйте фактичний ELF і конфігурацію обраного toolchain, а не переносіть схему Cortex-M на всі ELF-файли.[^gnu-ld-script]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

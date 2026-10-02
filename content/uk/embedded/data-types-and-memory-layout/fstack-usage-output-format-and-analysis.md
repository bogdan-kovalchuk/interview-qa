---
id: emb-dtypes-0067
title: "Що означає `-fstack-usage` у GCC і як читати його output?"
description: "GCC -fstack-usage записує для кожної функції її stack usage у .su файл поруч із відповідним output object."
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
  - source_id: gcc-stack-usage
    title: "GCC: Developer Options, -fstack-usage"
    url: https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Визначає формат рядків .su і значення static, dynamic, bounded; точність стосується функційного stack usage, не сумарного worst-case call chain."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

GCC прапорцем `-fstack-usage` записує stack usage функцій у `.su` файл з іменем від `auxname`, зазвичай basename source або object output.[^gcc-stack-usage] Кожен tab-separated рядок містить ім’я функції з source location, mangled name, байти та qualifier: `static` – фіксований frame, `dynamic` – зміни stack під час роботи, `dynamic,bounded` – відома верхня межа.[^gcc-stack-usage]

Без `bounded` кількість байтів не охоплює необмежену частину. Аналізуй звіт із call graph, бо найбільший frame не дорівнює піку вкладених викликів; врахуй interrupts, recursion, RTOS stacks і бібліотеки, а `-Wstack-usage=256` сприймай як поріг попередження, не гарантію достатнього stack.[^gcc-stack-usage]

## Detailed explanation

Прапорець `-fstack-usage` створює звіт під час компіляції одиниці трансляції. Ім’я `.su` походить від `auxname`, тобто object output або source file, тому це не обов’язково окремий файл на кожен `.o`.[^gcc-stack-usage]

Рядки мають tab-separated поля: ім’я функції з source location, mangled name, байти та qualifier. У C++ mangled name розрізняє overload-и; bytes тлумачать разом із qualifier як відому частину frame.[^gcc-stack-usage]

`static` означає, що GCC бачить фіксований обсяг frame. `dynamic` означає додаткові зміни stack під час роботи функції, наприклад через variable-length array чи інші механізми. Якщо також є `bounded`, компілятор має межу для цих змін, а число є верхньою межею використання функції. Без `bounded` число охоплює лише відому частину, отже його не можна трактувати як максимум.[^gcc-stack-usage] Реальні записи залежать від optimization flags і target ABI, тому звіт треба отримувати для конфігурації firmware, яку планують випускати, а не лише для debug build.

Приклад: функція з frame 48 байтів, що викликає функцію з frame 80 байтів, може потребувати близько 128 байтів плюс збережені регістри й ABI overhead. Один `.su` не підсумовує call chain, тому для RTOS врахуй вкладення, interrupts, бібліотеки й запас та звір оцінку runtime watermark на пристрої. `-Wstack-usage=N` допомагає знайти великі функції, але не замінює вимірювання. Результат залежить від optimization flags, отже debug звіт може не відповідати release firmware.[^gcc-stack-usage]

Interrupt handler може вкладатися в задачу у найглибшій точці call chain, тому вимірюй сумарний контекст. Звіт слід отримувати з тими optimization flags і ABI, які використовує release firmware.[^gcc-stack-usage]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

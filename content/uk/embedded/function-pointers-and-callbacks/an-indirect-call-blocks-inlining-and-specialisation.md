---
id: emb-fnptr-0056
title: "Чому function pointers впливають на оптимізацію?"
description: "Indirect call важче оптимізувати, ніж direct call."
track: embedded
section: function-pointers-and-callbacks
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
  - source_id: gcc-indirect-calls
    title: "GCC manual: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Документує оптимізації GCC для indirect calls і умови їх застосування; не гарантує однакових можливостей в інших компіляторах."
---

## Short answer

**Indirect call важче оптимізувати, ніж direct call.**

Компілятор може не знати точну callee функцію, тому зазвичай не може inline-ити виклик або виконати оптимізації, залежні від конкретного тіла. Аналіз видимих значень і LTO іноді дають змогу визначити кандидата й перетворити виклик, але це залежить від програми та toolchain.[^gcc-indirect-calls]

Embedded-висновок: function pointers дають гнучкість, але непрямий виклик може мати додаткову вартість; у hot paths перевіряй згенерований assembly і вимірювання.[^gcc-indirect-calls]

## Detailed explanation

Indirect call використовує function pointer, щоб під час виконання визначити адресу функції, тоді як direct call уже називає конкретну функцію.[^gcc-indirect-calls]

Для direct call компілятор бачить callee і може оцінити її тіло в місці виклику. Це створює нагоду для inlining, поширення констант з аргументів, видалення недосяжних гілок і кращого аналізу call graph. Саме можливість аналізу, а не заборона стандарту, пояснює різницю: стандарт C не вимагає конкретних оптимізацій.[^gcc-indirect-calls]

У випадку `callback()` значення callback може надійти з реєстрації, таблиці або іншого модуля. Якщо компілятор не може звузити набір можливих цілей, він мусить залишити непрямий виклик і не може застосувати до невідомого тіла всі оптимізації, які можливі для однієї відомої функції. Проте це не означає, що function pointer завжди повільний: процесор, ABI, розмір таблиці та частота виконання впливають на фактичну вартість.

GCC описує speculative indirect-call перетворення та devirtualization, які за певних умов можуть створити перевірку й direct-call гілку або виявити ціль. LTO дає змогу бачити більше одиниць трансляції, але теж не гарантує, що динамічне значення стане відомим.[^gcc-indirect-calls]

Приклад: якщо dispatch table фактично має лише одну доступну ціль і це видно оптимізатору, він може спростити виклик. Якщо таблиця змінюється під час виконання або її заповнює інший модуль, такий висновок може бути неможливим. Порівнюй assembly і часові вимірювання саме для production flags та цільового MCU.

**Типова помилка:** стверджувати, що function pointers забороняють inline або неодмінно збільшують latency. Точніше сказати, що невідома ціль обмежує деякі оптимізації, а результат залежить від того, що compiler може довести.

## Sources

<!-- generated from frontmatter -->

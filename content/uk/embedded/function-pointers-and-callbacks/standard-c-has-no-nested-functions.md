---
id: emb-fnptr-0036
title: "Trap: чи можна зробити callback звичайною nested function у стандартному C?"
description: "Ні. Standard C не має nested functions."
track: embedded
section: function-pointers-and-callbacks
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
  - source_id: gcc-nested-functions
    title: "GCC documentation: Nested Functions"
    url: https://gcc.gnu.org/onlinedocs/gcc/Nested-Functions.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Документує GNU C як розширення, trampolines і обмеження часу життя адреси; не описує ISO C."
---

## Short answer

<span class="warn">Ні. ISO C не визначає nested functions; GCC надає їх як GNU C extension.</span> [^iso-c-n1570] [^gcc-nested-functions]

GCC реалізує взяття адреси такої функції через trampolines; адреса також стає небезпечною після виходу з функції, що містить її визначення.[^gcc-nested-functions]

Захист: використовуй file-scope `static` function і `void *context`; тоді стандартний callback не залежить від GNU extension.[^iso-c-n1570]

## Detailed explanation

ISO C визначає функції як file-scope definitions, а compound statement усередині функції може містити декларації, але не визначення іншої функції. Тому визначення функції всередині тіла іншої функції не є конструкцією стандартної мови C; код із нею треба вважати залежним від конкретного compiler extension.[^iso-c-n1570]

GCC підтримує nested functions у режимі GNU C. Така функція бачить імена з зовнішнього блоку, а її адреса може передаватися далі; GCC описує реалізацію адреси через trampoline. Виклик після завершення зовнішньої функції небезпечний, бо потрібне середовище зовнішнього виклику вже не існує.[^gcc-nested-functions]

**Як проявляється пастка:** приклад збирається з GNU-розширеннями на одному компіляторі, але не компілюється як strict ISO C або на іншому toolchain. Навіть у GCC збережений callback не можна безпечно викликати після повернення з функції, яка містила nested function.[^gcc-nested-functions]

Для portable callback оголоси функцію на file scope і передай дані окремим context pointer, якщо API це підтримує. Об’єкт контексту має жити щонайменше стільки, скільки callback може його використовувати; це правило часу життя залишається важливим і для звичайної функції.[^iso-c-n1570]

Приклад:

```c
struct state { int value; };
static void callback(void *context) {
    struct state *s = context;
    s->value += 1;
}
```

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

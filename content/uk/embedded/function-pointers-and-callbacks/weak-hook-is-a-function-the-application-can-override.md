---
id: emb-fnptr-0052
title: "Що таке weak callback hook у embedded firmware?"
description: "Weak hook – це weak function, яку application може перевизначити сильною реалізацією."
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
  - source_id: gcc-weak-attribute
    title: "GCC: Common Function Attributes – weak"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "GCC current documentation"
    applicability: "Описує GNU weak attribute і можливість override для підтримуваних ELF/a.out toolchain; це розширення компілятора, не гарантія ISO C."
---

## Short answer

**Weak hook** – це функція зі слабким символом, який application може перевизначити сильною реалізацією у toolchain, що підтримує цю linker semantics.[^gcc-weak-attribute]

У GCC на підтримуваних ELF або a.out targets оголошення з `__attribute__((weak))` створює weak symbol; сильне визначення того самого символу може його перевизначити під час link.[^gcc-weak-attribute]

Це GNU/toolchain-specific механізм, а не властивість стандарту C. Він зручний для startup defaults; для кількох runtime-інстансів зазвичай потрібна явна реєстрація callback разом із context.

## Detailed explanation

Weak hook – це зовнішня функція, оголошена weak за правилами конкретного compiler і linker. Коли програма містить лише weak default implementation, посилання на символ може вести до неї; якщо application надає сумісне strong definition, toolchain може обрати його під час link. У GCC атрибут `weak` створює weak symbol, призначений, зокрема, для перевизначення у user code, але підтримка залежить від object format і toolchain.[^gcc-weak-attribute]

Такий механізм часто використовують у startup code: бібліотека задає default handler, а firmware додає функцію з тим самим зовнішнім ім’ям. Якщо application не визначає override, default handler залишається доступним. Треба звірити точні правила конкретного linker-а, включно з тим, як він обробляє дублікати, бібліотеки та секції; саме слово `weak` у вихідному коді не створює універсальної гарантії мови C.[^gcc-weak-attribute]

Важливо розрізняти weak hook і function pointer registration. Hook – це один символ із фіксованим ім’ям на рівні програми. Реєстрація ж може змінювати callback під час виконання і зберігати додатковий вказівник на стан пристрою. Тому hook зручний як extension point для глобальної поведінки, наприклад default interrupt handler, але сам по собі не вибирає між двома UART або таймерами.

Приклад: startup library оголошує `SysTick_Handler` weak, а application визначає strong-функцію з таким самим ім’ям і сумісною сигнатурою. Під час link має перемогти application definition у підтримуваному toolchain; перевірити це можна таблицею символів і map-файлом зібраного ELF.

**Типові помилки:**

- Вважати `__attribute__((weak))` переносимим синтаксисом стандарту C.
- Визначати override з несумісною сигнатурою або C++ name mangling, через що назви символів можуть не збігтися.
- Використовувати один global hook як механізм вибору конкретного екземпляра периферії.

Для переносимого чи багатоекземплярного driver-а краще визначити явний API реєстрації і передавати `context` окремим аргументом. Weak hook залишай там, де проект контролює toolchain і справді потрібна одна глобальна точка розширення.[^gcc-weak-attribute]

## Sources

<!-- generated from frontmatter -->

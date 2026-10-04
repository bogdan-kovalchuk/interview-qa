---
id: emb-patterns-0029
title: "Коли обирати enum+switch, а коли function-pointer table для FSM?"
description: "enum+switch – приблизно до восьми станів, важлива простота дебагу і warning на пропущені case."
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  en: 4
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
  - source_id: gcc-warning-options
    title: "GCC 16.1.0: Warning Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Warning-Options.html
    accessed: 2026-10-04
    kind: official
    version: "16.1.0"
    applicability: "Документує -Wswitch та -Wswitch-enum для пропущених enum cases; нічого не гарантує про швидкість switch чи таблиць."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**enum+switch** зручний, коли переходи краще читати явно; конкретний компілятор може попередити про пропущені `enum` cases за відповідного warning-прапорця.[^gcc-warning-options]

Function-pointer table може зменшити повторюваний dispatch-код, але сама по собі не гарантує `O(1)` чи кращої швидкодії; індекс треба перевіряти.

Обирай за читабельністю та вимірюваннями на цільовій платформі, а не за фіксованою кількістю станів.[^iso-c-n1570]

## Detailed explanation

`enum` разом із `switch` зручно описує скінченний автомат, коли переходи та дії важливо бачити явно в одному місці. Function-pointer table зберігає handler для кожного індексу чи стану, що може скоротити повторюваний dispatch-код, коли набір обробників великий або формується конфігурацією. Універсальної межі на кшталт «до восьми станів» немає: вибір залежить від читабельності, пам’яті, вимог часу та можливостей компілятора.[^iso-c-n1570]

Не слід обіцяти, що `switch` повільний, а таблиця завжди має O(1) час. Компілятор може реалізувати `switch` ланцюжком переходів, jump table або іншою інструкцією; рішення залежить від розподілу case labels і цільової архітектури. Перевага явного `switch` – компілятор часто може попередити про пропущені enum cases, якщо немає `default` і ввімкнені відповідні warnings. Таблиця handler-ів натомість потребує безпечної перевірки індексу та визначеної поведінки для порожнього entry.

Приклад демонструє лише структуру вибору, а не гарантію продуктивності:

```c
switch (state) {
case IDLE:  handle_idle(); break;
case BUSY:  handle_busy(); break;
default:    handle_invalid_state(); break;
}
```

**Типові помилки:**

- Вибирати таблицю лише через припущення про швидкість без вимірювання на target.
- Індексувати таблицю зовнішнім значенням без bounds check.
- Використовувати `default` так, що новий enum case маскується від compiler warning.

Для невеликого FSM почніть із найчитабельнішого варіанта, потім перевірте map file, розмір коду та latency, якщо це справді обмеження.

## Sources

<!-- generated from frontmatter -->

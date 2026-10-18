---
id: emb-cppfound-0059
title: "Чи можна порівнювати вказівники (`<`, `>`) і коли це визначена поведінка?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Порівняння `==` та `!=` – завжди **визначено** між будь-якими двома вказівниками одного типу.

Порівняння `<`, `>`, `<=`, `>=` – **визначено лише** якщо обидва вказівники вказують на **один і той самий масив** (або структуру). Порівняння вказівників різних об'єктів -> <span class="warn">undefined behavior (UB) за стандартом</span>.

Практика: більшість платформ дають коректну відповідь навіть для різних об'єктів, але не покладайся на це у portable коді.[^embeddedinterviewlab]

## Detailed explanation

TODO

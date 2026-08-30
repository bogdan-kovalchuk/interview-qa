---
id: emb-dtypes-0047
title: "Що таке signed integer overflow у C і яка його поведінка за стандартом?"
description: "Вихід signed int за межі діапазону - undefined behavior за стандартом C, а не гарантований wraparound."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Вихід за межі `INT_MIN..INT_MAX` - <span class="warn">undefined behavior</span> за стандартом C (§6.5).

Компілятор може:
1. Зробити wraparound до `INT_MIN` (типово two's complement);
2. Видалити умовний код як "завжди false";
3. Нескінченний цикл: `for(int i=0; i < i+1; i++)` - UB, компілятор може оптимізувати.

Для визначеного wraparound: `uint32_t`. Перевірка: `if(x <= INT_MAX - y) x += y;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

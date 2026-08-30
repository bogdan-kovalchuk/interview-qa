---
id: emb-cemb-0025
title: "Які варіанти використання `extern` знаєте?"
description: "`extern` оголошує ім'я, визначене в іншому translation unit; у C++ `extern \"C\"` вимикає name mangling для сумісності з C API."
track: embedded
section: c-in-embedded
level: junior
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
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<code>extern</code> оголошує ім'я, яке визначене в іншому translation unit: у header пишуть <code>extern int counter;</code>, а в одному <code>.c</code> файлі має бути визначення <code>int counter;</code>. Це дозволяє розділяти declaration і definition без дублювання глобальної змінної.<br><br>Також <code>extern</code> застосовують для функцій, хоча для звичайних функцій external linkage є типовим. У C++ є окремий випадок <code>extern "C"</code> – він вимикає C++ name mangling, щоб C++ код міг лінкуватися з C API або динамічною бібліотекою.[^dou-embedded-interview]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

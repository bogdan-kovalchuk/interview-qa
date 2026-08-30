---
id: emb-cemb-0020
title: "Як `static` впливає на глобальні та локальні змінні?"
description: "У локальної змінної `static` змінює час життя, а у глобальної змінної або функції обмежує linkage поточним файлом."
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

Для <span class="key">локальної змінної</span> <code>static</code> змінює час життя: змінна створюється один раз, живе до завершення програми й зберігає значення між викликами функції. Область видимості при цьому лишається локальною для блоку.<br><br>Для <span class="key">глобальної змінної</span> або функції <code>static</code> змінює linkage: ім'я видно тільки в поточному <code>.c</code>/<code>.cpp</code> файлі. Це називається internal linkage і допомагає уникати конфліктів імен між translation units.[^dou-embedded-interview]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

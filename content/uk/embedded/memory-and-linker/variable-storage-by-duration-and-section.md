---
id: emb-memlink-0009
title: "Де може зберігатися змінна?"
description: "Місце зберігання змінної залежить від storage duration і linker script: це можуть бути stack, heap, статична пам'ять, секції .data, .bss, .rodata або .text."
track: embedded
section: memory-and-linker
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? memory-and-linker; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Змінна може мати різне місце зберігання залежно від storage duration і linker script. Локальні автоматичні змінні зазвичай лежать на <span class="key">stack</span>, динамічні об'єкти з <code>malloc</code> – у <span class="key">heap</span>, глобальні та <code>static</code> – у статичній пам'яті.[^dou-embedded-interview]

Типові секції: <code>.data</code> – ініціалізовані глобальні/static змінні, копіюються з Flash у RAM; <code>.bss</code> – нульові або неініціалізовані global/static, зануляються startup-кодом; <code>.rodata</code> – константи; <code>.text</code> – машинний код. Компілятор також може тимчасово тримати значення в регістрах.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

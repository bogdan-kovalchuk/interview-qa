---
id: emb-build-0005
title: "Що буде, якщо у двох файлах зробити функцію з однаковим ім'ям і параметрами? На якому етапі виникне помилка?"
description: "Дві не-static функції з однаковим ім'ям в різних translation units компілюються окремо, але лінкер видасть multiple definition / duplicate symbol."
track: embedded
section: toolchain-and-build
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу toolchain-and-build; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Якщо у двох `.c`/`.cpp` файлах визначити не-`static` функцію з однаковим ім'ям і external linkage, компіляція окремих файлів може пройти успішно, бо кожен translation unit компілюється окремо.[^dou-embedded-interview]

Помилка зазвичай виникне на етапі **linking**: linker побачить два global symbols з однаковим іменем і видасть multiple definition / duplicate symbol. Якщо зробити функції `static`, кожна матиме internal linkage і конфлікту між файлами не буде. У C++ overload можливий тільки якщо сигнатури різні; однакова сигнатура все одно порушує ODR.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

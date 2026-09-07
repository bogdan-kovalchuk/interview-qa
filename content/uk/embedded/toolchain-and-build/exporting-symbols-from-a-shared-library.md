---
id: emb-build-0004
title: "Як експортувати/імпортувати функції з динамічної бібліотеки?"
description: "У Linux символи в .so видимі за замовчуванням і контролюються через visibility attribute, а Windows DLL потребує явних dllexport/dllimport."
track: embedded
section: toolchain-and-build
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу toolchain-and-build; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

У Linux/Unix функції з shared library зазвичай експортуються як символи в `.so`.[^dou-embedded-interview] Для C API достатньо не робити функцію `static`, зібрати з `-fPIC` і злинкувати `-shared`; видимість можна контролювати через `__attribute__((visibility("default")))` і linker version script.

У Windows DLL зазвичай використовують `__declspec(dllexport)` при збірці бібліотеки й `__declspec(dllimport)` у користувача або `.def` файл. Для C++ API часто додають `extern "C"` для стабільних C-символів або експортують C++ з урахуванням ABI конкретного компілятора.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

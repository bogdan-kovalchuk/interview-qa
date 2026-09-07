---
id: emb-memlink-0006
title: "Які проблеми можуть виникнути, якщо функція повертає вказівник на локальну змінну?"
description: "Локальна змінна знищується при виході з функції, тож повернений на неї вказівник стає dangling pointer, а доступ через нього – undefined behavior."
track: embedded
section: memory-and-linker
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-07
    kind: community
    version: null
    applicability: "Походження фрагмента коду й попередження GCC у цій відповіді; решту тверджень підтримує DOU-колода."
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? memory-and-linker; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Локальна змінна живе на **стеку** і знищується при виході з функції (SP змінюється).[^dou-embedded-interview] Повернений вказівник стає <span class="warn">dangling pointer</span> – вказує на вже недійсну пам'ять. Читання або запис через нього – <span class="warn">undefined behavior</span>: може повернути сміття, перезаписати інші змінні або спричинити crash.

```c
int* f(void) { int x = 42; return &x; }
```

Пам'ять може бути перезаписана наступним викликом функції, а GCC попереджає: `warning: function returns address of local variable [-Wreturn-local-addr]`.[^embeddedinterviewlab]

Правильні альтернативи: повертати значення (не вказівник); виділяти пам'ять через `malloc` (heap); використовувати `static` змінну (але не потокобезпечно); передавати буфер через параметр.

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

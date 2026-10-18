---
id: emb-memlink-0006
title: "Які проблеми можуть виникнути, якщо функція повертає вказівник на локальну змінну?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
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

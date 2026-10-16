---
id: emb-memlink-0007
title: "Які типи сегментів пам'яті ви знаєте?"
track: embedded
section: memory-and-linker
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

Типовий розподіл пам'яті C-програми:[^dou-embedded-interview]

- **.text** – машинний код функцій. Read-only. У MCU часто зберігається у Flash.
- **.rodata** – read-only дані, наприклад рядкові літерали й частина констант.
- **.data** – глобальні та статичні змінні з ненульовою ініціалізацією. Копіюється з Flash у RAM при старті.
- **.bss** – глобальні та статичні змінні без ініціалізації або з `= 0`. Заповнюється нулями startup-кодом;
- **Stack** – локальні змінні, аргументи, адреси повернення;
- **Heap** – динамічна пам'ять (`malloc`); На більшості архітектур stack росте вниз, а heap вгору, але це platform/ABI dependent, не правило стандарту C.

## Detailed explanation

TODO

---
id: emb-memlink-0009
title: "Де може зберігатися змінна?"
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

Змінна може мати різне місце зберігання залежно від storage duration і linker script. Локальні автоматичні змінні зазвичай лежать на **stack**, динамічні об'єкти з `malloc` – у **heap**, глобальні та `static` – у статичній пам'яті.[^dou-embedded-interview]

Типові секції: `.data` – ініціалізовані глобальні/static змінні, копіюються з Flash у RAM; `.bss` – нульові або неініціалізовані global/static, зануляються startup-кодом; `.rodata` – константи; `.text` – машинний код. Компілятор також може тимчасово тримати значення в регістрах.

## Detailed explanation

TODO

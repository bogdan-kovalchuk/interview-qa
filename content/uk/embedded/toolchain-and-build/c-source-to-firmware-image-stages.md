---
id: emb-build-0011
title: "Які етапи проходить C-файл від preprocessing до executable або firmware image?"
description: "C-файл проходить preprocessing, compilation, assembly, linking і, для firmware, перетворення у цільовий image."
track: embedded
section: toolchain-and-build
level: middle
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
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

Спершу preprocessing розкриває `#include`, `#define` і conditional compilation. Далі compiler генерує assembly або IR, assembler створює object file, linker об'єднує objects/libraries і розміщує sections. Для firmware часто ще виконують `objcopy` у `.hex`/`.bin` і генерують map-файл.[^dou-embedded-interview]

## Detailed explanation

C-файл проходить кілька етапів перед тим, як стати executable або firmware image.[^gcc-overall-options]

**1. Preprocessing** (`cpp` або `gcc -E`):
- Розкриває `#include` – вставляє вміст header files
- Розкриває `#define` – замінює macros на їх значення
- Обробляє `#ifdef`/`#ifndef`/`#endif` – conditional compilation
- Видаляє коментарі
- Результат: `.c` файл з усіма includes розкритими

**2. Compilation** (`cc1` або `gcc -S`):
- Парсить C code і будує AST (Abstract Syntax Tree)
- Виконує optimization (якщо вказано `-O1`, `-O2`, `-O3`)
- Генерує assembly code або LLVM IR
- Результат: `.s` файл (assembly) або `.ll` (IR)

**3. Assembly** (`as` або `gcc -c`):
- Конвертує assembly code у machine code
- Створює object file з symbols та relocation entries
- Результат: `.o` файл (object file)

**4. Linking** (`ld` або `gcc`):
- Об'єднує всі object files і libraries
- Вирішує symbol references (external symbols)
- Розміщує sections (.text, .data, .bss) згідно з linker script
- Генерує executable або firmware image
- Результат: `.elf` файл (executable) або `.axf` (ARM)

**5. Post-build** (для firmware):
- `objcopy -O ihex firmware.elf firmware.hex` – Intel HEX format
- `objcopy -O binary firmware.elf firmware.bin` – Raw binary
- `objdump -h firmware.elf` – Section sizes
- `size firmware.elf` – Text/data/bss sizes
- Генерація map file (`-Wl,-Map=firmware.map`)

Кожен етап можна виконати окремо для debugging або аналізу.

## Evaluation guide

### Expected signals
- Знає основні етапи: preprocessing, compilation, assembly, linking
- Розуміє, що робить кожен етап
- Може назвати інструменти для кожного етапу (cpp, cc1, as, ld)
- Знає про post-build кроки для firmware (objcopy, map file)

### Red flags
- Плутає compilation з linking
- Не знає, що preprocessing – окремий етап
- Не розуміє різницю між object file і executable
- Не знає, як отримати .hex/.bin з .elf

### Level-up follow-up
- Як подивитися проміжні файли (preprocessed, assembly)?
- Що таке relocation entries і навіщо вони потрібні?
- Як linker script впливає на розміщення sections?

## Sources

<!-- generated from frontmatter -->

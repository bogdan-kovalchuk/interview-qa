---
id: emb-build-0012
title: "Як отримати проміжні файли preprocessing, assembly і object file під час компіляції?"
description: "Прапорці GCC і Clang -E, -S та -c дозволяють окремо отримати preprocessing output, assembly і object file."
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

Для GCC/Clang: `-E` дає preprocessed output, `-S` – assembly, `-c` – object file без link. Для аналізу firmware корисні `objdump -d`, `readelf -S` і linker map. У CMake ці flags можна тимчасово додати до target або виконати compiler command з `compile_commands.json`.[^dou-embedded-interview]

## Detailed explanation

GCC і Clang надають flags для отримання проміжних файлів на кожному етапі компіляції.[^gcc-overall-options]

**Preprocessing** (`-E`):
```bash
gcc -E main.c -o main.preprocessed.c
```
Результат: файл з усіма `#include` розкритими, macros заміненими, коментарями видаленими. Корисно для debugging macros і conditional compilation.

**Assembly** (`-S`):
```bash
gcc -S main.c -o main.s
```
Результат: assembly файл. Корисно для аналізу generated code, перевірки optimization, debugging compiler issues.

**Object file** (`-c`):
```bash
gcc -c main.c -o main.o
```
Результат: object file без linking. Корисно для перевірки symbol visibility, compilation errors без linking.

**Аналіз firmware**:
```bash
objdump -d firmware.elf      # Disassembly
objdump -h firmware.elf      # Section headers
readelf -S firmware.elf      # Section details
readelf -s firmware.elf      # Symbol table
size firmware.elf            # Text/data/bss sizes
```

**Linker map file** генерується з `-Wl,-Map=firmware.map` і показує:
- Розміщення всіх sections у пам'яті
- Адреси всіх symbols
- Розмір кожної section
- Memory usage по regions (FLASH, RAM)

**У CMake** можна тимчасово додати flags до target:
```cmake
target_compile_options(firmware PRIVATE -save-temps)
```
Або виконати compiler command з `compile_commands.json`:
```bash
grep -A5 "main.c" compile_commands.json
# Copy the command and add -E/-S/-c
```

## Evaluation guide

### Expected signals
- Знає flags `-E`, `-S`, `-c` і що вони роблять
- Може назвати інструменти для аналізу firmware (objdump, readelf, size)
- Розуміє, що таке linker map file і навіщо він потрібен
- Знає, як отримати проміжні файли у CMake

### Red flags
- Не знає різниці між `-E`, `-S`, `-c`
- Не може назвати інструменти для аналізу firmware
- Не розуміє, що показує linker map file
- Не знає, як подивитися preprocessed output

### Level-up follow-up
- Як подивитися assembly для конкретного функції?
- Що таке `-save-temps` і коли його використовувати?
- Як аналізувати memory usage з map file?

## Sources

<!-- generated from frontmatter -->

---
id: emb-build-0012
title: "Як отримати проміжні файли preprocessing, assembly і object file під час компіляції?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
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

### Очікувані сигнали

- Знає flags `-E`, `-S`, `-c` і що вони роблять
- Може назвати інструменти для аналізу firmware (objdump, readelf, size)
- Розуміє, що таке linker map file і навіщо він потрібен
- Знає, як отримати проміжні файли у CMake

### Червоні прапорці

- Не знає різниці між `-E`, `-S`, `-c`
- Не може назвати інструменти для аналізу firmware
- Не розуміє, що показує linker map file
- Не знає, як подивитися preprocessed output

### Питання на підвищення рівня

- Як подивитися assembly для конкретного функції?
- Що таке `-save-temps` і коли його використовувати?
- Як аналізувати memory usage з map file?

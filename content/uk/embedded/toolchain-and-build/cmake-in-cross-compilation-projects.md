---
id: emb-build-0009
title: "Як працює CMake у cross-compilation проекті для MCU або Embedded Linux?"
description: "Практичне питання про embedded-розробку та її обмеження."
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

CMake спочатку configure-ить build graph: читає `CMakeLists.txt`, toolchain file, target flags і генерує Ninja/Make project. Потім build tool викликає cross-compiler, assembler, linker і post-build утиліти на кшталт `objcopy`. Важливо розділяти host tools, які запускаються на PC, і target binaries, які призначені для MCU або Linux target.[^dou-embedded-interview]

## Detailed explanation

CMake у cross-compilation проекті працює у два етапи: configure і build. На configure етапі CMake читає `CMakeLists.txt`, toolchain file і генерує build system (Ninja або Makefiles). На build етапі build tool викликає cross-compiler, assembler, linker і post-build утиліти.[^gcc-overall-options]

**Toolchain file** – це CMake script, який задає target platform:
```cmake
set(CMAKE_SYSTEM_NAME Generic)  # or Linux, bare-metal
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
```

CMake розрізняє **host tools** (які запускаються на PC під час build) і **target binaries** (які будуть виконуватися на MCU). Наприклад, code generator може бути host tool, який створює код для target.

**Configure крок**:
```bash
cmake -B build -G Ninja \
  -DCMAKE_TOOLCHAIN_FILE=arm-toolchain.cmake \
  -DCMAKE_BUILD_TYPE=Release
```

**Build крок**:
```bash
cmake --build build --target firmware.elf
```

CMake автоматично додає target flags з toolchain file до кожної команди компіляції. Linker script задається через `target_link_options()` або `CMAKE_EXE_LINKER_FLAGS`. Post-build кроки (objcopy у .hex/.bin) додаються через `add_custom_command()`.

## Evaluation guide

### Expected signals
- Розуміє різницю між host tools і target binaries
- Знає, що toolchain file задає cross-compiler і target flags
- Може пояснити configure і build етапи
- Розуміє роль sysroot і linker script

### Red flags
- Плутає host compiler з cross-compiler
- Не знає, що таке toolchain file
- Не розуміє, чому не можна просто змінити compiler на cross-compiler без toolchain file

### Level-up follow-up
- Як CMake обробляє find_package() у cross-compilation?
- Як задати different optimization levels для різних targets?
- Як інтегрувати code generator як host tool?

## Sources

<!-- generated from frontmatter -->


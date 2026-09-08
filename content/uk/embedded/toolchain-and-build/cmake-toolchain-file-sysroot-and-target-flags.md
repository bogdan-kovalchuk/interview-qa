---
id: emb-build-0010
title: "Що таке toolchain file у CMake і яку роль мають compiler, sysroot та target flags?"
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

**Toolchain file** задає CMake, що build іде не для host, а для target: `CMAKE_SYSTEM_NAME`, compilers, archiver, objcopy, sysroot і flags. `sysroot` дає headers/libraries target-системи, а target flags задають ABI, FPU, CPU core, linker script тощо. Без цього CMake може непомітно знайти host-бібліотеки й зібрати несумісний binary.[^dou-embedded-interview]

## Detailed explanation

**Toolchain file** у CMake – це CMake script, який каже build system, що ви будуєте для target platform, а не для host. Він задає cross-compiler, sysroot, і target-specific flags.[^gcc-overall-options]

**Основні змінні toolchain file**:
```cmake
set(CMAKE_SYSTEM_NAME Generic)  # Target OS (Generic for bare-metal)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
```

**Sysroot** (`CMAKE_SYSROOT`) – це директорія з headers і libraries target system. Коли cross-compiler шукає headers або libraries, він шукає їх у sysroot, а не на host system. Це запобігає випадковому використанню host libraries.

**Target flags** задаються через `CMAKE_C_FLAGS`, `CMAKE_CXX_FLAGS`, `CMAKE_ASM_FLAGS`:
```cmake
set(CMAKE_C_FLAGS "-mcpu=cortex-m4 -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16")
set(CMAKE_EXE_LINKER_FLAGS "-T${CMAKE_SOURCE_DIR}/linker.ld -specs=nosys.specs")
```

Ці flags включають:
- `-mcpu=cortex-m4` – CPU architecture
- `-mthumb` – Thumb instruction set
- `-mfloat-abi=hard` – Hardware FPU
- `-mfpu=fpv4-sp-d16` – FPU type
- `-T linker.ld` – Linker script
- `-specs=nosys.specs` – Syscall stubs для bare-metal

Без toolchain file CMake використовує host compiler і host libraries, що призводить до binary, який не працює на target MCU.

## Evaluation guide

### Expected signals
- Знає, що toolchain file задає cross-compiler і target flags
- Розуміє роль sysroot для ізоляції від host system
- Може пояснити основні target flags (CPU, FPU, linker script)
- Розуміє, чому не можна просто змінити compiler без toolchain file

### Red flags
- Не знає, що таке toolchain file
- Плутає sysroot з include directories
- Не розуміє різницю між host і target
- Не знає, де задаються linker script і CPU flags

### Level-up follow-up
- Як задати different flags для різних build types (Debug/Release)?
- Як інтегрувати toolchain file з CMake presets?
- Як обробляти different ABIs (soft-float vs hard-float)?

## Sources

<!-- generated from frontmatter -->


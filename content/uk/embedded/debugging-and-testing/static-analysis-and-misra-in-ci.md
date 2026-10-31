---
id: emb-testemb-0007
title: "Які static analysis tools доречні для C/C++ firmware і як інтегрувати MISRA/AUTOSAR checks у CI?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: gcc-warning-options
    title: "GCC manual: Options to Request or Suppress Warnings"
    url: https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html
  - source_id: clang-tidy-docs
    title: "Clang-Tidy documentation"
    url: https://clang.llvm.org/extra/clang-tidy/
  - source_id: cppcheck-manual
    title: "Cppcheck manual"
    url: https://cppcheck.sourceforge.io/manual.html
  - source_id: zephyr-sca
    title: "Zephyr Project documentation: Static Code Analysis (SCA)"
    url: https://docs.zephyrproject.org/latest/develop/sca/index.html
  - source_id: cmake-export-compile-commands
    title: "CMake documentation: CMAKE_EXPORT_COMPILE_COMMANDS"
    url: https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html
  - source_id: misra-compliance-2020
    title: "MISRA Compliance:2020 – Achieving compliance with MISRA Coding Guidelines"
    url: https://misra.org.uk/app/uploads/2021/06/MISRA-Compliance-2020.pdf
---

## Short answer

Для firmware доречні **clang-tidy**, `cppcheck`, compiler warnings, commercial analyzers на кшталт PC-lint/FlexeLint, Coverity, Polyspace або Klocwork. У CI запускають аналіз на кожен target/config, фіксують rule set, suppressions і baseline, а MISRA/AUTOSAR deviation оформлюють явно. <span class="warn">Важливо аналізувати той самий code path, include dirs і defines, що й cross-build.</span>[^dou-embedded-interview]

## Detailed explanation

Static analysis для firmware будують шарами: кожен шар дешевший або глибший за попередній, і жоден не покриває все. Друга половина питання важливіша за перелік інструментів: аналіз має дивитися на той самий код, що потрапляє у прошивку, а результати мають бути керованими – з baseline, задокументованими відхиленнями і зрозумілим правилом, коли CI падає.

### Шари інструментів

- **Попередження компілятора** для кожної цілі збірки, у CI часто з `-Werror`. Найдешевший шар: у GCC `-Wall` вмикає, зокрема, `-Wswitch`, `-Wmaybe-uninitialized`, `-Wsequence-point` і `-Wunused-variable`, а неявні перетворення, що можуть змінити значення, ловить окремий `-Wconversion`, який до `-Wall` не входить.[^gcc-warning-options]
- **clang-tidy** – linter на базі Clang з групами перевірок `bugprone`, `cert`, `cppcoreguidelines`, `misc`, `readability` та іншими; окремої групи MISRA в переліку немає.[^clang-tidy-docs]
- **Cppcheck** – відкритий аналізатор з addon `misra`. Документація прямо попереджає, що відкритий Cppcheck покриває правила MISRA лише частково і не містить текстів правил: їх треба взяти з офіційного документа MISRA.[^cppcheck-manual]
- **Комерційні аналізатори** (Coverity, Polyspace, ECLAIR, Parasoft C/C++test, IAR C-STAT, PC-lint Plus, Klocwork) – глибший міжмодульний аналіз і звіти відповідності стандартам. Zephyr, наприклад, підключає низку з них через свою систему static code analysis.[^zephyr-sca]

MISRA Compliance:2020 радить обирати інструмент, здатний аналізувати всю програму, а не лише окремий файл, і зазначає, що для повнішого покриття може знадобитися більше одного інструмента.[^misra-compliance-2020]

### Аналізувати те, що реально компілюється

Firmware насичений `#ifdef`, board-specific include-шляхами і макросами з toolchain. Аналізатор, запущений з іншими defines, перевіряє інший код. Тому джерелом істини роблять compilation database: CMake з `CMAKE_EXPORT_COMPILE_COMMANDS` генерує `compile_commands.json` з точними командами компілятора для кожної одиниці трансляції (для Makefile- і Ninja-генераторів).[^cmake-export-compile-commands] clang-tidy читає цю базу через `-p <build-dir>`,[^clang-tidy-docs] Cppcheck – через `--project=compile_commands.json`; у цьому режимі він за замовчуванням перевіряє одну конфігурацію, узгоджену з компіляцією, а більше – лише з `--force` або `--max-configs`. Без бази компіляції й без `-D` Cppcheck сам перебирає комбінації defines, а з `-D` аналізує лише конфігурації, де цей символ визначено.[^cppcheck-manual] У Zephyr аналізатор обирають параметром збірки `ZEPHYR_SCA_VARIANT`; підтримка вбудована в ту саму CMake-збірку, а інструмент, якому треба бачити команди компіляції й лінкування, обгортає їх через `CMAKE_<LANG>_COMPILER_LAUNCHER` і `CMAKE_<LANG>_LINKER_LAUNCHER`.[^zephyr-sca]

```sh
cmake -B build-board-a -DCMAKE_TOOLCHAIN_FILE=cmake/arm-gcc.cmake \
      -DBOARD_CONFIG=board_a -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
clang-tidy -p build-board-a -checks='-*,bugprone-*,cert-*' --warnings-as-errors='*' src/*.c
cppcheck --project=build-board-a/compile_commands.json --addon=misra.json --inline-suppr
```

`--warnings-as-errors` лише підвищує до помилок перевірки, уже вибрані через `-checks`, і сам нових не вмикає.[^clang-tidy-docs] Ці кроки повторюють для кожного елемента матриці target/config: дефект у гілці `#ifdef BOARD_B` не побачить аналіз збірки для плати A. Практична деталь: clang-tidy розбирає код фронтендом Clang, тож специфічні прапорці GCC-кросс-тулчейну іноді доводиться відфільтрувати з бази.

### MISRA як процес, а не прапорець

MISRA Compliance:2020 ділить правила на категорії: Mandatory – порушення не дозволене ніколи; Required – дозволене лише через оформлене відхилення (deviation); Advisory – порушення фіксують, але deviation не обов’язковий. На старті проєкту узгоджують guideline re-categorization plan: Required можна підняти до Mandatory, Advisory – до Required, Mandatory або Disapplied, але не навпаки. Deviation record містить порушене правило, обставини, причину, контекст і запобіжні заходи, а також перелік місць у коді, де відхилення застосовано. На завершення складають guideline compliance summary зі статусом відповідності кожному правилу.[^misra-compliance-2020] Той самий документ нагадує, що IEC 61508, ISO 26262 і DO-178 у певних випадках вимагають кваліфікації компіляторів і аналізаторів.[^misra-compliance-2020]

Для C++ використовують окремі набори правил (MISRA C++ або AUTOSAR C++14), але схема та сама: зафіксований rule set, відхилення з обґрунтуванням, звіт.

### Як це виглядає в CI

1. Версії аналізаторів і конфігурацію правил фіксують у репозиторії, щоб результат не змінювався від оновлення образу CI.
2. Для існуючого коду знімають baseline; CI падає лише на нові знахідки, а старі розбирають планово.
3. Пригнічення робиться точково і з посиланням на deviation: `// NOLINT(check-name)` у clang-tidy[^clang-tidy-docs] або inline suppression у Cppcheck.[^cppcheck-manual] Масове вимкнення правила для всього проєкту – окреме рішення, задокументоване в плані.
4. Сторонній код (vendor HAL, RTOS) виділяють окремо: MISRA Compliance допускає для такого adopted code окремий, менш суворий план, бо його не змінюють.[^misra-compliance-2020]
5. Звіти зберігають як артефакти збірки, щоб compliance summary релізу спирався на конкретний запуск.

### Межі

Частина правил undecidable: якщо порушення залежить від значень під час виконання чи досяжності коду, інструмент у загальному випадку може відповісти лише «можливо», і відсутність diagnostic не означає відповідності.[^misra-compliance-2020] Тому static analysis не замінює review і тести, а звільняє їх від механічних перевірок.

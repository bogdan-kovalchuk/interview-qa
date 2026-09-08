---
id: emb-build-0004
title: "Як експортувати/імпортувати функції з динамічної бібліотеки?"
description: "У Linux символи в .so видимі за замовчуванням і контролюються через visibility attribute, а Windows DLL потребує явних dllexport/dllimport."
track: embedded
section: toolchain-and-build
level: junior
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

У Linux/Unix функції з shared library зазвичай експортуються як символи в `.so`.[^dou-embedded-interview] Для C API достатньо не робити функцію `static`, зібрати з `-fPIC` і злинкувати `-shared`; видимість можна контролювати через `__attribute__((visibility("default")))` і linker version script.

У Windows DLL зазвичай використовують `__declspec(dllexport)` при збірці бібліотеки й `__declspec(dllimport)` у користувача або `.def` файл. Для C++ API часто додають `extern "C"` для стабільних C-символів або експортують C++ з урахуванням ABI конкретного компілятора.

## Detailed explanation

У Linux/Unix shared library (`.so`) експортує символи через dynamic symbol table. Коли компілятор будує `.so`, він додає всі non-static global символи в таблицю експорту за замовчуванням. Для C API достатньо оголосити функцію без `static` ключового слова, скомпілювати з `-fPIC` (position-independent code) і злінкувати з `-shared`.[^gcc-overall-options]

Для контролю видимості використовують `__attribute__((visibility("default")))` для явного експорту або `__attribute__((visibility("hidden")))` для приховування символів. Linker version script (`.map` файл) дозволяє точно контролювати, які символи експортуються:

```
LIBMYLIB_1.0 {
    global:
        my_public_function;
        my_other_function;
    local:
        *;
};
```

У Windows DLL механізм інший. `__declspec(dllexport)` при збірці бібліотеки додає символ до export table. `__declspec(dllimport)` на стороні користувача каже компілятору, що функція знаходиться в DLL і потрібно використовувати indirect call через import address table (IAT). Альтернатива – `.def` файл з `EXPORTS` секцією, який не потребує модифікації вихідного коду.

Для C++ API додають `extern "C"` для запобігання name mangling і забезпечення стабільного ABI. Без цього C++ compiler mangling names (додає тип інформації до імені функції), що ускладнює бінарну сумісність між компіляторами.

У embedded Linux зазвичай використовують shared libraries для зменшення розміру firmware (кілька програм можуть використовувати одну бібліотеку) і для оновлення бібліотек без перекомпіляції всього додатку. У bare-metal MCU зазвичай використовують static linking, бо немає OS для завантаження shared libraries у runtime.


## Sources

<!-- generated from frontmatter -->

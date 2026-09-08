---
id: emb-build-0008
title: "Як відрізняються статична і динамічна бібліотека на етапах build та link?"
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

**Static library** (`.a`/`.lib`) копіюється linker-ом у firmware або executable тільки потрібними object files. **Dynamic library** (`.so`/`.dll`) підвантажується loader-ом у runtime і лишається окремим артефактом. Для bare-metal MCU зазвичай використовують static linking; Embedded Linux часто підтримує обидва варіанти.[^dou-embedded-interview]

## Detailed explanation

**Static library** (`.a` на Linux/macOS, `.lib` на Windows) – це архів object files. Коли linker обробляє static library, він витягує тільки ті object files, які потрібні для вирішення поточних symbol references. Невикористані object files не потрапляють у фінальний executable або firmware. Це означає, що розмір бінарника залежить тільки від реально використаного коду бібліотеки.[^gcc-overall-options]

Статичне лінкування відбувається на етапі build. Linker копіює потрібний код з `.a`/`.lib` у executable. Після цього бібліотека не потрібна для запуску програми – весь код вже всередині бінарника.

**Dynamic library** (`.so` на Linux, `.dll` на Windows, `.dylib` на macOS) – це окремий бінарний артефакт, який завантажується loader-ом оперційної системи у runtime. Коли програма запускається, OS знаходить потрібні shared libraries, завантажує їх у пам'ять і вирішує symbol references через dynamic linker. Програма може використовувати одну копію бібліотеки в пам'яті, навіть якщо кілька програм її використовують.

Для bare-metal MCU зазвичай використовують static linking, бо:
- Немає OS для завантаження shared libraries
- Flash пам'ять обмежена, і static linking дозволяє точно контролювати розмір firmware
- Немає dynamic linker для вирішення символів у runtime
- Firmware зазвичай monolithic – один бінарний образ

Embedded Linux часто підтримує обидва варіанти:
- Static linking для критичних до продуктивності компонентів (менше overhead, немає dynamic linking у runtime)
- Dynamic linking для бібліотек загального використання (libc, libpthread), щоб зменшити розмір firmware і дозволити оновлення бібліотек без перекомпіляції всіх програм


## Evaluation guide

### Expected signals

- Розрізняє static і dynamic libraries за способом лінкування та завантаження
- Розуміє, що static linking копіює код у бінарник, а dynamic linking завантажує бібліотеку у runtime
- Знає, що bare-metal MCU зазвичай використовують static linking через відсутність OS
- Розуміє компроміс між розміром firmware, продуктивністю та гнучкістю оновлень

### Red flags

- Плутає static library з static linking (це різні речі)
- Не знає різниці між `.a`/`.lib` та `.so`/`.dll`
- Вважає, що dynamic libraries завжди кращі за static
- Не розуміє, чому bare-metal MCU не використовують dynamic linking

### Level-up follow-up

- Як static linker вирішує, які object files витягувати з архіву?
- Які накладні витрати має dynamic linking у runtime?
- Як оновити shared library на embedded Linux пристрої в production?


## Sources

<!-- generated from frontmatter -->


---
id: emb-dtypes-0066
title: "Trap: `double` у embedded без FPU - у чому небезпека?"
description: "Без апаратної підтримки потрібної точності операції double компілятор може згенерувати виклики software floating-point routines; вартість залежить від MCU, компілятора й операції."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: gcc-arm-options
    title: "GCC: ARM Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Пояснює генерацію коду й сумісність ABI для ARM режимів soft, softfp і hard; не визначає кількість тактів для конкретного MCU."
  - source_id: arm-cortex-m4
    title: "Arm Cortex-M4 Processor Technical Reference Manual"
    url: https://documentation-service.arm.com/static/5fce431be167456a35b36ade
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує single-precision регістри та операції FPU Cortex-M4; наявність FPU залежить від реалізації Cortex-M4."
  - source_id: arm-cortex-m7
    title: "Arm Cortex-M7 Processor Technical Reference Manual"
    url: https://documentation-service.arm.com/static/5e906b038259fe2368e2a7bb
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує optional double-precision операції у конфігураціях FPU Cortex-M7; перевіряй конкретну реалізацію."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

На MCU без FPU для відповідної точності компілятор може реалізувати арифметику `double` програмними підпрограмами, що збільшує час виконання та іноді розмір коду; величину треба виміряти для цільової збірки.[^gcc-arm-options] `double` не означає універсально 8 байтів, а наявність FPU не гарантує прискорення: Cortex-M4F має single-precision FPU, тоді як конфігурація Cortex-M7 може мати single- або double-precision FPU.[^arm-cortex-m4][^arm-cortex-m7]

Вибір `float` чи `double` залежить від точності, діапазону й часу; перевіряй інструкції та вимірюй критичний шлях. GCC `-mfloat-abi` і `-mfpu` мають відповідати MCU та всім об’єктним файлам; `hard` і `soft` ABI несумісні.[^gcc-arm-options]

## Detailed explanation

Software floating-point реалізація означає, що потрібна операція виконується послідовністю звичайних інструкцій або викликом бібліотеки, а не відповідною інструкцією FPU. Наслідком може бути довший шлях виконання, додатковий код бібліотеки та використання регістрів чи stack; конкретна вартість різниться для додавання, ділення й перетворень, а оптимізатор може спростити операцію, якщо її результат відомий наперед.[^gcc-arm-options]

Не можна визначити ціну лише за назвою типу або ядра. Cortex-M0/M0+/M3 не мають FPU, але MCU може не мати його або збірка може його не використовувати. Cortex-M4F прискорює single precision, а деякі Cortex-M7 мають double precision; розмір `double` залежить від реалізації C.[^arm-cortex-m4][^arm-cortex-m7][^iso-c-n1570]

На реальному проєкті перевіряють disassembly та map-файл, а потім вимірюють worst-case execution time за тими самими оптимізаціями й ABI, що й у релізній збірці. Це виявляє library calls, але ще не доводить, що дедлайн буде порушено: для цього потрібне вимірювання повного шляху з перериваннями та планувальником. Порівнюй збірки на тих самих даних і частоті, інакше вимірювання не ізолює вплив типу.

**Типові помилки:**

- Вважати кожен Cortex-M4 чи M7 однаково обладнаним FPU; звіряй точну модель MCU та її конфігурацію.
- Вважати `float` автоматично найкращим вибором; спершу перевір вимоги до точності та числової стабільності.
- Встановити hard-float прапорці лише для частини залежностей; ABI має узгоджуватися в усіх об’єктних файлах.[^gcc-arm-options]

Для часових обмежень фіксуй compiler version, flags і частоту MCU разом із вимірюванням, щоб порівнювати збірки на однакових умовах. Окремо перевір підтримку бібліотеки runtime.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

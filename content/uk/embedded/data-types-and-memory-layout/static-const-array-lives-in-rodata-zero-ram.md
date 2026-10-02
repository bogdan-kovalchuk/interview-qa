---
id: emb-dtypes-0068
title: "Де зберігається у функції? `static const uint16_t lookup[] = {1, 2, 3};`"
description: "static const визначає тривалість зберігання та заборону змінювати масив через це lvalue; фактичне розміщення визначають компілятор і linker."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: gnu-ld-sections
    title: "GNU ld: SECTIONS Command"
    url: https://sourceware.org/binutils/docs/ld/SECTIONS.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Пояснює зіставлення input/output sections та розміщення; секція для C оголошення залежить від toolchain і linker script."
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

У локальному оголошенні `static` надає масиву static storage duration, а `const` забороняє змінювати його через це ім’я; жодне з ключових слів саме собою не гарантує секцію `.rodata` чи нульове використання RAM.[^iso-c-n1570] GCC і linker скеровують дані в секції та адреси за цільовою конфігурацією, тож це треба перевірити у map-файлі.[^gnu-ld-sections]

На типовій embedded linker-конфігурації незмінна таблиця може зберігатися у Flash, а writable initialized data копіюється з load image до RAM на старті. Конкретний результат залежить від compiler, linker script та адресного простору MCU.[^gnu-ld-sections]

## Detailed explanation

У функції `static const uint16_t lookup[] = {1, 2, 3};` оголошує локальну змінну зі static storage duration: існує один об’єкт протягом програми, а не новий масив у stack під час кожного виклику. `const` не дозволяє змінювати елементи через це ім’я.[^iso-c-n1570]

Ці властивості мови C не визначають фізичну пам’ять. Компілятор кладе об’єкт у секцію object file, а linker script зіставляє її з регіоном. Типовий MCU може розмістити read-only `.rodata` у Flash, але інший target може мати інший layout; перевір це у linker map і документації toolchain.[^gnu-ld-sections]

Writable static initialized array зазвичай потребує RAM для змін і початкового образу у nonvolatile memory; startup code копіює початкові байти до RAM. Натомість zero-initialized storage може бути відображена як `.bss` і очищатися на старті. Точна поведінка залежить від linker script і startup code, тому «static означає Flash» і «const означає zero RAM» не є мовними гарантіями.[^gnu-ld-sections]

**Приклад:**

```c
static const uint16_t lookup[] = {1, 2, 3};
```

Таблицю lookup доречно оголошувати `static const`, але перевір, чи firmware linker script розміщує її саме у Flash. Також перевір alignment і доступність читання з потрібного контексту.[^gnu-ld-sections]

## Sources

<!-- generated from frontmatter -->

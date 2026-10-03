---
id: emb-macros-0016
title: "Чим `#pragma once` відрізняється від класичного include guard?"
description: "#pragma once дає той самий захист одним рядком на початку файлу, без ризику зіткнення імен макросів-guard."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: gcc-once-headers
    title: "GCC: Once-Only Headers"
    url: https://gcc.gnu.org/onlinedocs/cpp/Once-Only-Headers.html
    accessed: 2026-10-04
    kind: official
    version: "GCC 16.1"
    applicability: "Документація GCC описує дію #pragma once у цьому toolchain і застерігає, що вона менш переносима за #ifndef."
  - source_id: msvc-once
    title: "Microsoft Learn: once pragma"
    url: https://learn.microsoft.com/en-us/cpp/preprocessor/once?view=msvc-170
    accessed: 2026-10-04
    kind: official
    version: "MSVC 170"
    applicability: "Документує поведінку та межі #pragma once у MSVC; не є твердженням про інші компілятори."
---

## Short answer

**`#pragma once` просить компілятор включити header не більш як один раз** у межах translation unit, без окремого макроса-guard.

Мінус: директива <span class="warn">не стандартизує саме таку поведінку в C або C++</span>, тож підтримка залежить від компілятора. Класичний `#ifndef` guard використовує стандартні conditional directives і має ширшу переносимість.

Перед вибором перевір підтримку та особливості шляхів включення в документації свого toolchain.[^gcc-once-headers] [^iso-c-n1570]

## Detailed explanation

`#pragma once` – це поширене розширення препроцесора, яке позначає header так, щоб цей компілятор не обробляв його повторно в тому самому translation unit. Воно досягає мети include guard, але спирається на те, як конкретний toolchain розпізнає повторне посилання на файл.[^gcc-once-headers]

Класичний include guard явно зберігає стан у макросі: `#ifndef`, `#define` і `#endif` є стандартними conditional directives мови C, а аналогічний шаблон підтримується препроцесорами C++. На відміну від них, конкретна дія `#pragma once` не визначена стандартом як одноразове включення; для нестандартних pragma реалізація може задавати власну поведінку або ігнорувати невідому директиву.[^iso-c-n1570]

Основна практична перевага `#pragma once` – коротший запис без імені макроса, отже немає колізії між двома guard-макросами. З іншого боку, його виявлення спирається на ідентифікацію того самого файлу. Aliased include paths або особливості файлової системи можуть ускладнити це визначення; конкретні обмеження залежать від компілятора. GCC прямо називає директиву менш переносимою альтернативою guard-у.[^gcc-once-headers]

**Приклад:**

```c
#pragma once
/* вміст header */
```

У проєкті з зафіксованим набором компіляторів така директива може бути зручною, якщо її поведінка документована та перевірена. Для бібліотеки, яка має збиратися різними або невідомими компіляторами, звичайний guard прозоріший для стандартного препроцесора. Не потрібно писати обидва механізми разом: обери один під вимоги переносимості проєкту.[^gcc-once-headers] [^msvc-once]

**Типові помилки:**

- Називати `#pragma once` стандартною директивою з однаковою гарантією в кожному компіляторі.
- Вважати, що захист обов’язково діє між різними translation units: кожен окремо компілюваний source file має власний прохід препроцесора.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

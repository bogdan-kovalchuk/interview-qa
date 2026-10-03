---
id: emb-structs-0040
title: "Trap: чому `memcmp(&a, &b, sizeof a)` поганий спосіб порівняти структури?"
description: "Бо padding bytes можуть відрізнятися, навіть якщо всі поля рівні."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
---

## Short answer

<span class="warn">Бо padding bytes можуть відрізнятися, навіть якщо всі поля рівні.</span> Padding не є частиною значень members, а стандарт C дозволяє йому набувати unspecified values під час запису значення структури. `memcmp` порівнює raw bytes, тому може виявити різницю представлень у структур з однаковими значеннями полів.

Захист: порівнюй поля явно або нормалізуй serialization format. Для security-sensitive output не виводь padding bytes назовні.[^iso-c-n1570]

## Detailed explanation

`memcmp(&a, &b, sizeof a)` порівнює перші `sizeof a` байтів двох object representations, а не значення members структури. Компілятор може вставити padding для alignment, і ці байти не є частиною логічного стану об’єкта. Стандарт C зазначає, що padding bytes структури набувають unspecified values під час запису значення; отже, рівні members не гарантують однакових байтів у padding.[^iso-c-n1570]

Наприклад, дві змінні можуть мати однакові `kind` і `count`, але padding міг отримати різні значення через окремі присвоєння чи різний код, який їх створив. Тоді `memcmp` поверне ненульове значення, хоча порівняння кожного потрібного поля показало б рівність. Водночас збіг байтів не завжди є достатнім визначенням семантичної рівності: тип може містити floating-point значення з кількома представленнями для того, що програма вважає еквівалентним.[^iso-c-n1570]

**Як проявляється помилка:** тест рівності нестабільно падає залежно від оптимізації, шляху ініціалізації або конкретної збірки. Це не доводить, що поля різні; тест перевіряє також padding та інші байти представлення. На іншій ABI зміниться і сам layout структури.[^iso-c-n1570]

**Типові помилки:**

- Вважати `sizeof` сумою розмірів members без padding.
- Обнуляти структури лише для того, щоб виправдати `memcmp`: це не робить порівняння значень переносимим для всіх типів і сценаріїв.
- Використовувати результат як доказ однаковості стану, не визначивши, що саме означає рівність.

Порівнюй members, які визначають семантику об’єкта, окремо. Для hash table чи протоколу створи канонічне кодування полів і хешуй або порівнюй саме його; не використовуй сирий layout структури як контракт.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

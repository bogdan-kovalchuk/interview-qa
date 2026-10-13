---
id: emb-tmplcx-0014
title: "Звідки береться code bloat від шаблонів?"
description: "Кожна унікальна інстанціація створює власні визначення використаних функцій, зазвичай з окремим кодом у Flash."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що специфікація шаблону функції чи member-функції інстанціюється, коли її визначення потрібне; неявна інстанціація класового шаблону інстанціює лише оголошення членів. Про розмір коду не йдеться."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-13
    kind: official
    version: "16.1.0"
    applicability: "Описує -fipa-icf: identical code folding для функцій, що зменшує розмір коду, краще працює з увімкненим LTO і за замовчуванням увімкнено на -O2. Не каже, які саме тіла злито в конкретній програмі."
---

## Short answer

<span class="warn">Кожна унікальна інстанціація створює власні визначення використаних функцій.</span>[^cpp-draft-temp-inst] У Flash такі визначення зазвичай займають окремий код; компілятор може злити лише функції з однаковим кодом (у GCC це `-fipa-icf`).[^gcc-optimize-options]

Приклад: `CircularBuffer<uint8_t,64>` і `CircularBuffer<uint16_t,64>` дають окремі набори методів, які програма викликає, і їхній код різний.

Правило: стеж за кількістю інстанціацій – на MCU з обмеженою Flash кожен новий тип може швидко збільшити прошивку.

## Detailed explanation

Специфікація шаблону функції інстанціюється тоді, коли потрібне її визначення. Member-функції класового шаблону так само інстанціюються лише за потреби, а неявна інстанціація класу створює лише оголошення членів.[^cpp-draft-temp-inst] Тому розмір коду залежить від того, скільки різних наборів аргументів використано і які їхні методи справді викликано, а не від повного списку методів класу.

Розглянемо `CircularBuffer<uint8_t,64>`, `CircularBuffer<uint16_t,64>` і `CircularBuffer<uint32_t,64>`. Якщо програма викликає `push` і `pop` для кожного з них, компілятор отримує три окремі набори визначень цих функцій. Їхній код різний: ширина елемента змінює інструкції завантаження та збереження, тому їх не можна злити. Це і є bloat: логіка однакова, а машинний код повторений для кожного типу.

Копії не завжди різні. Якщо два типи мають однакову ширину і однакову поведінку методів, машинний код може збігтися, і тоді GCC з `-fipa-icf` може злити такі функції. Цей прапорець за замовчуванням увімкнено на `-O2`, і він ефективніше працює з увімкненим LTO.[^gcc-optimize-options] Тому розмір треба міряти на збірці з потрібною оптимізацією, а не виводити з кількості шаблонних аргументів.

Перевірити це можна після збірки: `nm --size-sort -C` покаже розміри окремих символів, і буде видно, скільки копій `CircularBuffer` справді лишилося. Якщо копій забагато, зменшити їх можна стратегіями з qid:emb-tmplcx-0015.

**Типові помилки:**

- Вважати, що шаблон дає копію всіх своїх методів, а не лише використаних.
- Вважати, що однакова логіка завжди дає однаковий машинний код.
- Оцінювати розмір за вихідним кодом, а не за розміром символів у зібраному файлі.

## Sources

<!-- generated from frontmatter -->

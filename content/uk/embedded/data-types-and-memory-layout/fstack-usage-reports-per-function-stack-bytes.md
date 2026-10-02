---
id: emb-dtypes-0058
title: "Як перевірити розмір stack frame функції в GCC?"
description: "Прапорець -fstack-usage змушує GCC генерувати .su файли з розміром stack frame кожної функції."
track: embedded
section: data-types-and-memory-layout
level: middle
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
  - source_id: gcc-stack-usage
    title: "GCC: Developer Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує формат .su, значення qualifier-ів та межі звіту -fstack-usage у GCC; не визначає сумарний stack budget програми."
---

## Short answer

Прапорець `-fstack-usage`: GCC генерує `.su`-файл з оцінкою використання stack для кожної функції.[^gcc-stack-usage]

У `.su` кожен запис має поля, розділені табуляцією: місце функції у вихідному коді, mangled name, кількість байтів і qualifier на кшталт `static`, `dynamic` або `bounded`.[^gcc-stack-usage]

Звіт описує функцію окремо, а не сумарний максимум для всього шляху викликів чи стеку задачі.[^gcc-stack-usage]

GCC також має `-Wstack-usage=N` для попереджень за порогом, але цей поріг не доводить, що повний шлях викликів уміститься у стек.[^gcc-stack-usage]

## Detailed explanation

Опція GCC `-fstack-usage` просить компілятор видати окремий запис про використання стеку для кожної скомпільованої функції. Зазвичай створюється файл із суфіксом `.su`; назва залежить від імені вихідного або заданого object-файлу. Формат містить чотири поля, відокремлені табуляцією: ім’я функції з розташуванням у вихідному коді, mangled name, число байтів і qualifier.[^gcc-stack-usage]

Qualifier важливий для інтерпретації числа. `static` означає фіксований розмір frame, виділений при вході у функцію. `dynamic` вказує на зміни stack під час виконання; якщо поруч є `bounded`, GCC знає верхню межу такого використання. Без `bounded` наведене число описує лише обмежену частину, а не гарантований максимум усіх динамічних змін.[^gcc-stack-usage]

Ці дані стосуються окремої функції в конкретній компіляції й конфігурації. Вони не дорівнюють максимальному стеку всієї задачі: під час викликів кадри активних функцій можуть накопичуватися, а переривання має окремі вимоги до стеку, залежні від архітектури й ABI. Оптимізація, inline та параметри компілятора змінюють результат, тому аналізуйте саме цільову збірку. GCC також має попередження за порогом, але поріг не доводить, що повний шлях викликів уміститься у стек.[^gcc-stack-usage]

Наприклад, запис із `static` та числом 48 означає, що цей компілятор оцінює фіксований frame цієї функції у 48 байтів для даної збірки. Якщо вона викликає іншу функцію з frame 32 байти, шлях може потребувати більше ніж 48 байтів, бо обидва кадри можуть бути активними одночасно.[^gcc-stack-usage]

**Типові помилки:**
- Вважати число розміром усього стеку задачі або максимального шляху викликів.
- Ігнорувати `dynamic` і сприймати необмежений запис як точний максимум.
- Зіставляти числа з іншого target, оптимізації чи набору compiler flags із фінальною прошивкою.[^gcc-stack-usage]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

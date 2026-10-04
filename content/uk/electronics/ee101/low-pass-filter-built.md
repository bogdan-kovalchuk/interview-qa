---
id: emb-elee-0114
title: "Як побудований RL-фільтр низьких частот?"
description: "Як побудований RL-фільтр низьких частот?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 52, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Топологія та частотна дія пасивного inductive low-pass із котушкою послідовно й навантаженням на виході; реальна котушка має опір і паразитні ефекти."
---

## Short answer

У RL-ФНЧ котушка стоїть послідовно зі входом, а навантажувальний резистор – між вихідним вузлом і спільним проводом; вихід знімають з резистора. На високих частотах індуктивний імпеданс зростає, тому частка напруги на навантаженні зменшується.[^aac-low-pass-filters]

## Detailed explanation

Пасивний RL-ФНЧ утворюють послідовна котушка та резистивне навантаження, підключене від вихідного вузла до спільного проводу. Вихідна напруга вимірюється на навантажувальному резисторі. На низьких частотах ідеальна котушка має малий індуктивний опір, тому сигнал переважно з’являється на навантаженні. Зі зростанням частоти імпеданс котушки `X_L = 2π*f*L` збільшується, отже більша частина вхідної напруги припадає на неї, а вихід зменшується.[^aac-low-pass-filters]

Для ідеального джерела без вихідного опору та резистивного навантаження полюс задається `f_c = R/(2π*L)`. Тут R – саме опір, який бачить котушка; якщо є додаткове навантаження або опір джерела, еквівалентна схема може змінити розрахунок. На частоті зрізу модуль виходу дорівнює `1/sqrt(2)` від низькочастотного рівня, тобто приблизно 70.7 відсотка.[^aac-low-pass-filters]

Приклад розрахунку: за `L = 10 mH` і `R = 1 kΩ` ідеальна модель дає `f_c = 1000/(2π*0.01) ≈ 15.9 kHz`. Значно нижче цієї частоти напруга на R близька до входу; значно вище вона слабшає приблизно пропорційно оберненій частоті для однополюсного фільтра. Це розрахунок для синусоїдального усталеного режиму, а не гарантія характеристик конкретного компонента.[^aac-low-pass-filters]

Практична котушка має опір обмотки, паразитну ємність і можливі втрати в осерді. Вони можуть спричинити вставні втрати навіть на низьких частотах і змінити поведінку поблизу власного резонансу. Тому схема ідеально пояснює топологію, але для реального проєкту треба перевірити опір DC, струмовий рейтинг, насичення осердя та частотні межі котушки за документацією компонента.[^aac-low-pass-filters]

## Sources

<!-- generated from frontmatter -->

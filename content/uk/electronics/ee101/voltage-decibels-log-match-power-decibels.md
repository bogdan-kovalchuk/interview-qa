---
id: emb-elee-0098
title: "Коли децибели за напругою (20 log) збігаються з децибелами за потужністю?"
description: "Коли децибели за напругою (20 log) збігаються з децибелами за потужністю?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 49, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: rs-decibel-guide
    title: "Rohde & Schwarz: Radar and electronic warfare eGuide"
    url: https://www.allaboutcircuits.com/uploads/articles/Radar-and-electronic-warfare_eGuide-REVISED.pdf
    accessed: 2026-10-04
    kind: official
    version: "01.00, April 2022"
    applicability: "Еквівалентність voltage-ratio та power-ratio decibels за однакового імпедансу; формули для порівняння рівнів."
---

## Short answer

Формула `20*log10(|V_out/V_in|)` дає те саме значення, що й формула для відношення потужностей, коли обидві напруги прикладені до однакового активного опору. За різних опорів обчисліть потужності окремо й порівняйте їх через `10*log10(P_out/P_in)`.[^rs-decibel-guide]

## Detailed explanation

Формула для напруги `20*log10(|V_out/V_in|)` еквівалентна формулі для потужності `10*log10(P_out/P_in)` лише за однакового активного опору для обох вимірювань. Причина в залежності `P = V²/R`: коли `R` однакове, воно скорочується у відношенні потужностей, а квадрат відношення напруг виносить множник 2 перед логарифмом. Так виникає коефіцієнт 20 замість 10.[^rs-decibel-guide]

Якщо опори різні, то для тих самих напруг отримуємо різні потужності. Наприклад, подвоєння напруги на опорі, який у чотири рази більший, дає відношення потужностей `2²/4 = 1`, тобто 0 dB, хоча саме відношення напруг дорівнює 2 і формула для нього показала б приблизно 6.02 dB. Це не суперечність: числа описують різні відношення. Для складного AC-навантаження активна потужність залежить від дійсної частини імпедансу та фазових співвідношень, тому одного відношення модулів напруг може бути недостатньо.[^rs-decibel-guide]

**Як уникнути помилки:** спершу визначте, що саме потрібно порівняти – напругу чи потужність. Для напруг використовуйте RMS значення й коефіцієнт 20 лише тоді, коли опори однакові. Для різних навантажень обчисліть потужність у кожному з них та використайте коефіцієнт 10. Не переносіть формулу для однакових опорів на будь-який підсилювач або вимірювальний тракт без перевірки умов.[^rs-decibel-guide]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

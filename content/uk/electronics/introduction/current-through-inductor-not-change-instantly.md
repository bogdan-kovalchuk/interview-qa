---
id: emb-elintro-0146
title: "Чому струм через індуктор не може змінитися миттєво?"
description: "Чому струм через індуктор не може змінитися миттєво?"
track: electronics
section: introduction
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
    applicability: "Походження питання: лекція 14, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-inductor-calculus
    title: "All About Circuits: Inductor Voltage and Current Relationship"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Співвідношення напруги, індуктивності та швидкості зміни струму; ідеальний індуктор без опору обмотки."
---

## Short answer

Для ідеального індуктора `v = L*di/dt`, тому скінченна прикладена напруга змінює струм зі скінченною швидкістю. Стрибок струму за нульовий час у цій моделі вимагав би нескінченної напруги. У реальному колі різке переривання струму може створити високу напругу, обмежену паразитними параметрами та захисним колом.[^aac-inductor-calculus]

## Detailed explanation

Індуктор накопичує енергію в магнітному полі, коли через його обмотку тече струм. Якщо струм змінюється, змінюється й магнітний потік, а за законом електромагнітної індукції в обмотці виникає напруга. Для лінійного ідеального індуктора зв’язок задає `v = L*di/dt`: за більшої індуктивності та тієї самої напруги струм змінюється повільніше.[^aac-inductor-calculus]

Це не означає, що струм узагалі не може змінитися. Він змінюється поступово під дією напруги, а знак наведеної напруги визначається напрямком зміни й протидіє їй відповідно до закону Ленца. Наприклад, за сталої напруги 1 V на ідеальному індукторі 1 H струм змінюється на 1 A за секунду. Виміряна напруга залежить від вибору полярності на виводах, але модуль швидкості зміни задається співвідношенням вище.[^aac-inductor-calculus]

Фраза про «нескінченну напругу» є висновком математичної ідеальної моделі для миттєвого стрибка струму, а не реальною напругою, яку компонент може підтримувати. У справжньому колі опір обмотки, паразитні ємності, ізоляція, дуга або clamp-елемент обмежують перехідний процес; тому під час вимкнення струму напруга може стати високою, але не нескінченною. У силовому колі шлях для струму індуктора треба спроєктувати заздалегідь, інакше перенапруга може пошкодити ключ або ізоляцію.[^aac-inductor-calculus]

**Типова помилка:** сприймати індуктор як розімкнене коло для будь-якої зміни струму. Насправді він допускає зміну струму, але швидкість залежить від прикладеної напруги та індуктивності; у сталому режимі DC ідеальний індуктор має сталий струм і нульову напругу на собі.[^aac-inductor-calculus]

## Sources

<!-- generated from frontmatter -->

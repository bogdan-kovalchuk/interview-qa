---
id: emb-elintro-0179
title: "Чим `SMPS` краще за класичний лінійний wall-wart?"
description: "Чим `SMPS` краще за класичний лінійний wall-wart?"
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
    applicability: "Походження питання: лекція 17, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: adi-linear-switching
    title: "Analog Devices: Basic Concepts of Linear Regulator and Switching Mode Power Supplies"
    url: https://www.analog.com/en/resources/app-notes/2020/05/12/19/12/an-140.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Порівнює механізми втрат і типові переваги SMPS та лінійних регуляторів; наведені показники стосуються описаних прикладів, а не всіх адаптерів."
---

## Short answer

`SMPS` перемикає силові транзистори, тому зазвичай має менші втрати та може бути компактнішим за лінійний блок тієї самої потужності. Проте ефективність, розмір, шум і діапазон вхідної напруги залежать від конкретної конструкції; жодне з наведених чисел не є універсальним.[^adi-linear-switching]

## Detailed explanation

`SMPS` (switch-mode power supply) регулює напругу, швидко перемикаючи силовий транзистор і передаючи енергію через індуктивні та ємнісні елементи. Коли транзистор увімкнений, падіння напруги на ньому невелике; коли вимкнений, струм через нього малий. Через одночасно малу напругу або малий струм у цих станах втрати можуть бути нижчими, ніж у лінійному регуляторі, де надлишок напруги перетворюється на тепло.[^adi-linear-switching]

Висока частота перемикання дає змогу використовувати менші магнітні компоненти, тож багато SMPS-адаптерів легші й компактніші за старі трансформаторні лінійні адаптери аналогічної потужності. Це не означає, що кожен SMPS кращий за кожен лінійний блок: лінійний варіант часто простіший і може мати менше високочастотного шуму, а ефективність залежить від співвідношення вхідної та вихідної напруг, навантаження і реалізації.[^adi-linear-switching]

Наведені в старій картці діапазони на кшталт `85–90%` для SMPS і `50–70%` для лінійного wall-wart не можна вважати загальними характеристиками класів. Для конкретного адаптера дивляться паспортні дані та криві ефективності за навантаженням. Так само сумісність із мережею `100–240 V` має бути явно зазначена на етикетці; вона не випливає лише з того, що блок є імпульсним.[^adi-linear-switching]

**Приклад:** для лінійного регулятора, що знижує `12 V` до `3.3 V` при однаковому струмі, приблизна ефективність без урахування власного споживання обмежена відношенням `3.3/12`, тобто `27.5%`. У прикладі Analog Devices синхронний buck-перетворювач за тих самих напруг може перевищувати `90%`; це приклад топології та умов, а не специфікація будь-якого настінного адаптера.[^adi-linear-switching]

**Типова помилка:** порівнювати категорії за фіксованими відсотками або автоматично приписувати SMPS універсальний вхід. Порівнюють конкретні моделі за ефективністю при потрібному навантаженні, шумом, регулюванням, безпекою та маркуванням входу.[^adi-linear-switching]

## Sources

<!-- generated from frontmatter -->

---
id: emb-elintro-0078
title: "Що таке `RMS` і чому його використовують для `AC`?"
description: "Що таке `RMS` і чому його використовують для `AC`?"
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
    applicability: "Походження питання: лекція 9, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-ac-magnitude
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює RMS як нагрівальний еквівалент та співвідношення для чистих синусоїд; коефіцієнт не переноситься на інші форми хвилі."
---

## Short answer

`RMS` (Root Mean Square) – середньоквадратичне значення, що для резистора відповідає такій самій середній потужності, як еквівалентна напруга `DC`. Для чистої синусоїди `V_rms = V_peak/√2`; це співвідношення не є універсальним для інших форм хвилі.[^aac-ac-magnitude]

## Detailed explanation

`RMS` – середньоквадратичне значення напруги або струму. Для резистивного навантаження воно показує, яке значення `DC` дало б таку саму середню потужність, тому ним зручно описувати періодичний сигнал, який постійно змінюється.[^aac-ac-magnitude]

Звичайне середнє значення чистої синусоїди за повний період дорівнює нулю: додатна і від’ємна півхвилі взаємно компенсуються. Але нагрівання резистора залежить від квадрата миттєвої напруги, `P = V²/R`. Квадрат робить внесок обох півхвиль додатним. RMS отримують так: підносять миттєві значення до квадрата, усереднюють їх за період і беруть квадратний корінь.[^aac-ac-magnitude]

Для чистої синусоїди усереднення квадратів дає половину квадрата амплітуди, отже `V_rms = V_peak/√2`, приблизно `0.707*V_peak`. Не плутайте амплітуду з розмахом від мінімуму до максимуму: `V_pp = 2*V_peak`. Підстановка `V_pp` замість `V_peak` завищила б RMS удвічі. Для прямокутної, імпульсної або спотвореної хвилі треба обчислювати RMS за формою сигналу, а не застосовувати коефіцієнт синусоїди.[^aac-ac-magnitude]

**Приклад:** якщо синусоїда має пік `10 V`, то її `RMS` становить приблизно `7.07 V`. Така напруга на тому самому резисторі створює таку саму середню потужність, як `7.07 V DC`. Це еквівалентність для теплової дії на резистор; інші навантаження можуть мати додаткові частотно-залежні ефекти.[^aac-ac-magnitude]

**Типова помилка:** вважати, що RMS – це звичайне середнє або завжди `0.707` від піку. Спершу з’ясуйте форму сигналу та чи задано пік, `RMS` або peak-to-peak.[^aac-ac-magnitude]

## Sources

<!-- generated from frontmatter -->

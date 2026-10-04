---
id: emb-elee-0099
title: "Що означають dBm і dBV?"
description: "Що означають dBm і dBV?"
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
    applicability: "Визначає dBm відносно 1 mW, dBV відносно 1 V та відмінність абсолютного рівня від відношення dB."
---

## Short answer

`dBm` – абсолютний рівень потужності відносно 1 mW: 10 mW дорівнює +10 dBm. `dBV` – рівень напруги відносно 1 V; для RMS-вимірювань 0.1 V дорівнює −20 dBV, а 1 V – 0 dBV. На відміну від цих одиниць, звичайний dB задає лише відношення без абсолютної опори.[^rs-decibel-guide]

## Detailed explanation

`dBm` і `dBV` задають абсолютні рівні, бо їхні назви фіксують опорні значення: 1 mW для потужності та 1 V для напруги. Розрахунки мають вигляд `L_dBm = 10*log10(P/1 mW)` і `L_dBV = 20*log10(V_RMS/1 V)` для RMS-напруги. Звичайний `dB` сам по собі не визначає абсолютну величину: він лише порівнює два рівні. Тому запис «сигнал має 6 dB» неповний без контексту, відносно чого цей gain або attenuation вимірюють.[^rs-decibel-guide]

Для `dBm` 0 dBm означає 1 mW; збільшення потужності у десять разів дає +10 dBm. Отже, 10 mW – це +10 dBm, а 0.1 mW – −10 dBm. Перетворення ґрунтується на відношенні потужностей і не вимагає припускати певний опір, якщо потужність уже відома. Якщо її обчислюють із напруги, тоді потрібно знати навантаження: для суто резистивного `R` використовують `P = V_RMS²/R`.[^rs-decibel-guide]

Для `dBV` опорною є напруга 1 V, незалежно від імпедансу. Напруга 1 V RMS дорівнює 0 dBV, а 0.1 V RMS – `20*log10(0.1) = −20 dBV`. RMS-позначення тут суттєве для AC-вимірювання: пікова напруга синусоїди має інше числове значення, ніж RMS, і її не слід підставляти без перерахунку, якщо шкала приладу або специфікація визначає RMS. `dBV` також не слід плутати з `dBm`: одна шкала описує напругу, друга – потужність.[^rs-decibel-guide]

**Типові помилки:**

- Сприймати dB як абсолютну одиницю, не вказуючи опорний рівень.
- Вважати, що 0 dBm дорівнює 0 mW; це рівень 1 mW.
- Виводити потужність у dBm лише з напруги без даних про навантаження.
- Плутати RMS та пікову напругу в розрахунку dBV.[^rs-decibel-guide]

## Sources

<!-- generated from frontmatter -->

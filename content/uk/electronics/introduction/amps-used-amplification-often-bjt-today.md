---
id: emb-elintro-0207
title: "Чому для підсилення сьогодні частіше використовують OP-amps, а не `BJT`?"
description: "Чому для підсилення сьогодні частіше використовують OP-amps, а не `BJT`?"
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
    applicability: "Походження питання: лекція 19, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: opamp-feedback
    title: "TI application report: Op Amp with Resistive Feedback"
    url: https://www.ti.com/lit/an/snoa486b/snoa486b.pdf
    accessed: 2026-10-04
    kind: official
    version: "SNOA486B"
    applicability: "Пояснює негативний резистивний зворотний зв’язок і формули замкненого gain; це приклади для зазначених топологій, а не універсальна гарантія для кожного op-amp."
---

## Short answer

Операційний підсилювач часто спрощує побудову підсилювального каскаду: зовнішній негативний зворотний зв’язок задає замкнений gain переважно співвідношенням резисторів, у межах смуги й допустимого діапазону конкретного пристрою.[^opamp-feedback] `BJT` також широко застосовують; його bias і стабільність треба проєктувати з урахуванням параметрів транзистора та схеми.[^aac-semiconductors]

## Detailed explanation

Операційні підсилювачі часто зручніші для типового підсилювального каскаду, бо їхній великий внутрішній gain разом із зовнішнім негативним зворотним зв’язком задає підсилення резисторами.[^opamp-feedback]

Окремий `BJT` може підсилювати сигнал, але робоча точка залежить від його струмового gain, температури та розкиду параметрів. Щоб отримати передбачуваний аналоговий каскад, проєктувальник добирає bias і резистори, а часто додає емітерний резистор або інші елементи стабілізації. Це цілком практично для дискретних, високочастотних або потужних схем, але потребує уважного розрахунку.[^aac-semiconductors]

У типовій схемі з op-amp частина вихідного сигналу через резистивну мережу повертається на інвертувальний вхід. Підсилювач змінює вихід так, щоб зменшити різницю між входами; у межах робочого діапазону замкнений gain тоді визначається переважно відношенням резисторів. Наприклад, у неінвертувальному включенні `A_V = 1 + R_F/R_G`; це наближене співвідношення діє лише за стабільного зворотного зв’язку та в межах смуги й вихідного діапазону конкретного пристрою.[^opamp-feedback]

Інтегральний підсилювач об’єднує багато транзисторів, їхні bias-мережі та компенсацію в одному кристалі. Проте op-amp не є універсально кращим: треба перевіряти напруги живлення, common-mode range, вихідний swing, струм навантаження, смугу, noise та стабільність. Для перемикання, дискретної топології або режиму, де потрібен вихід за межі цих параметрів, окремий `BJT` може бути правильним вибором.[^opamp-feedback]

**Типова помилка:** казати, що `BJT` не використовують для підсилення або що op-amp сам гарантує потрібне підсилення. Реальну функцію задає схема зворотного зв’язку, а межі задає datasheet конкретної мікросхеми.

## Sources

<!-- generated from frontmatter -->

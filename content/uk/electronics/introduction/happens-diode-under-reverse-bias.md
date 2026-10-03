---
id: emb-elintro-0185
title: "Що відбувається з діодом при зворотному зміщенні (reverse bias)?"
description: "Що відбувається з діодом при зворотному зміщенні (reverse bias)?"
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
    applicability: "Походження питання: лекція 18, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-zener-reverse-breakdown
    title: "SLVAG25 Application Brief: Zener Noise Phenomenon"
    url: https://www.ti.com/document-viewer/lit/html/SLVAG25/GUID-C0A4AD58-A8D2-4977-8B36-7D8455E203BA
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює умови avalanche breakdown і потребу в зворотному струмі для Zener; не задає межі звичайного діода."
---

## Short answer

Струм майже не тече, тому падіння на послідовному резисторі майже нульове, а майже вся прикладена напруга опиняється на діоді у зворотному напрямку. Якщо |`V_reverse`| &gt; `V_RRM`, можливий пробій.[^ti-zener-reverse-breakdown]

## Detailed explanation

За зворотного зміщення позитивний потенціал прикладають до катода відносно анода. Електричне поле відтягує основні носії заряду від PN-переходу, збільшуючи збіднений шар і бар’єр для їх проходження. Тому в нормальному режимі діод пропускає лише малий зворотний струм витоку, а не є ідеальним розімкненим перемикачем.[^aac-semiconductors]

Витік залежить від матеріалу, температури та прикладеної напруги й задається для конкретного компонента за умовами datasheet. Якщо напруга досягає breakdown voltage, зворотний струм може різко зрости. У стабілітроні цей режим є робочим за обмеженого струму; звичайний випрямний діод може перегрітися й вийти з ладу.[^aac-semiconductors]

У простій послідовній схемі з резистором напруга на ньому визначається фактичним витоком. Для грубої оцінки ним можна знехтувати, але падіння не обов’язково дорівнює нулю. Не можна вважати, що діод витримує будь-яку зворотну напругу: перевіряють `V_RRM` у datasheet і враховують піки схеми.[^aac-semiconductors]

Приклад: якщо джерело подає зворотні 5 V на діод, який працює далеко від своєї межі пробою, протікає лише малий витік і майже вся напруга припадає на діод. Якщо перевищено допустиме повторюване пікове значення `V_RRM`, схема вже не має гарантованого безпечного режиму.[^aac-semiconductors]

**Типова помилка:** називати зворотний струм рівно нульовим або плутати граничну напругу з напругою, за якої кожен діод гарантовано руйнується. Перевіряйте тип компонента й datasheet: пробій може бути допустимим для одного діода й руйнівним для іншого.

## Sources

<!-- generated from frontmatter -->

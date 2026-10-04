---
id: emb-elee-0051
title: "Чому в індукторі напруга випереджає струм?"
description: "Чому в індукторі напруга випереджає струм?"
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
    applicability: "Походження питання: лекція 40, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-ac-inductor
    title: "All About Circuits: AC Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує співвідношення v = L*di/dt та фазу ідеального індуктора в синусоїдальному AC-колі."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Для ідеального індуктора `v = L*di/dt`: напруга пропорційна швидкості зміни струму. У синусоїдальному усталеному режимі напруга випереджає струм на 90°, а не просто «вмикається раніше»; аналогія з інерцією лише мнемонічна.[^aac-ac-inductor]

## Detailed explanation

Індуктор створює напругу, коли його струм змінюється: для ідеального елемента `v = L*di/dt`. Тут `L` вимірюють у генрі, а швидкість зміни струму – в амперах за секунду; добуток має одиницю вольт. Знак залежить від обраних напрямків струму й полярності напруги, але фізичний зміст сталий: індуктор протидіє зміні струму, підтримуючи його напрямок під час спадання та стримуючи наростання. [^aac-ac-inductor]

Якщо струм не змінюється, ідеальна індуктивність не має напруги на своїх виводах. Коли на неї подати сталу напругу, струм у простій ідеальній моделі змінюватиметься лінійно, бо `di/dt = v/L`. У реальному колі опір обмотки та джерело обмежують таку поведінку. [^aac-ac-inductor]

Для синусоїдального сигналу в усталеному режимі похідна струму зсуває напругу вперед на 90°: напруга найбільша там, де струм змінюється найшвидше, а коли струм досягає піка й миттєво перестає зростати, напруга ідеальної індуктивності проходить через нуль. Тому формулювання «напруга випереджає струм» стосується фази циклічних сигналів, а не затримки струму при ввімкненні. [^aac-ac-inductor]

**Приклад:** для синусоїдального джерела й ідеального індуктора струм досягає максимуму через чверть періоду після відповідного максимуму напруги. За частоти 60 Hz період становить приблизно 16.7 ms, а чверть періоду – приблизно 4.17 ms.

**Типові помилки:**

- Вважати, що індуктор завжди блокує струм. У сталому DC ідеальна індуктивність має нульову напругу; реальну поведінку визначає також опір обмотки.
- Застосовувати зсув 90° до повного кола з опором. У змішаному R-L колі фазовий кут залежить від відношення опору до індуктивного реактивного опору. [^aac-ac-inductor]

## Sources

<!-- generated from frontmatter -->

---
id: emb-elee-0050
title: "Що означає мнемоніка ICE?"
description: "Що означає мнемоніка ICE?"
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
    applicability: "Підтверджує фазовий зв’язок напруги й струму для ідеальної індуктивності в синусоїдальному AC-колі."
  - source_id: aac-ac-capacitor
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтверджує фазовий зв’язок струму й напруги для ідеальної ємності в синусоїдальному AC-колі."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

ICE нагадує, що в ідеальному конденсаторі струм випереджає напругу на 90° у синусоїдальному усталеному режимі; ELI нагадує, що в ідеальному індукторі напруга випереджає струм на 90°. Це мнемоніки для фазових співвідношень, а не твердження про те, що в реальному колі одна величина завжди з’являється раніше за іншу.[^aac-ac-capacitor] [^aac-ac-inductor]

## Detailed explanation

ICE розшифровують як «Current leads Voltage in a Capacitor»: струм випереджає напругу в конденсаторі. Парну мнемоніку ELI читають як «Voltage leads Current in an Inductor», тобто напруга випереджає струм в індукторі. Йдеться про фазу синусоїдальних сигналів у сталому режимі, а не про затримку запуску компонентів після подачі живлення. Наприклад, якщо в ідеальному конденсаторі синусоїдальний струм досягає максимуму раніше за напругу на чверть періоду, це і є випередження на 90°. Для ідеального індуктора взаємне розташування протилежне: напруга досягає відповідної точки раніше за струм. [^aac-ac-capacitor] [^aac-ac-inductor]

Фізична причина пов’язана з рівняннями елементів. У конденсаторі струм залежить від швидкості зміни напруги, тож його максимум збігається з найшвидшою зміною напруги; у індукторі напруга залежить від швидкості зміни струму. За синусоїдального сигналу похідна зсуває фазу на чверть періоду. Мнемоніка коротко зберігає саме цей напрямок фазового зв’язку. [^aac-ac-capacitor] [^aac-ac-inductor]

**Типові помилки:**

- Читати «lead» як послідовність увімкнення. Це фазовий зсув у періодичних сигналах.
- Застосовувати рівно 90° до реальної котушки або конденсатора в будь-якому колі. Опір, втрати та інші компоненти змінюють загальну фазу кола. [^aac-ac-inductor] [^aac-ac-capacitor]

## Sources

<!-- generated from frontmatter -->

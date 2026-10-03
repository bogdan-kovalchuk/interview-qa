---
id: emb-elintro-0272
title: "Які переваги MSO може мати над окремим осцилографом під час налагодження цифрових схем?"
description: "Які переваги MSO може мати над окремим осцилографом під час налагодження цифрових схем?"
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
    applicability: "Походження питання: лекція 24, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: tek-mso-digital-circuits
    title: "Tektronix: How to Use a Mixed Signal Oscilloscope to Test Digital Circuits"
    url: https://www.tek.com/en/documents/application-note/how-use-mixed-signal-oscilloscope-test-digital-circuits
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює синхронізоване відображення аналогових і цифрових сигналів та декодування шин."

---

## Short answer

`MSO` поєднує осцилограф і логічний аналізатор. Можна одночасно бачити аналогову форму сигналу, рівні живлення, ringing і цифрові лінії протоколу.[^tek-mso-digital-circuits]

## Detailed explanation

MSO поєднує аналогові входи осцилографа з цифровими каналами логічного аналізатора. Завдяки спільній часовій шкалі можна зіставити фізичну напругу на лінії з розпізнаним логічним станом і подіями на інших сигналах.[^tek-mso-digital-circuits]

Це корисно під час пошуку аналогової причини цифрової помилки: overshoot, ringing, ground bounce або повільний фронт можуть порушити роботу логіки. Цифровий канал трактує сигнал як high або low відносно налаштованого порога, тоді як аналоговий канал показує форму фронту та запас напруги. Якщо завада перетнула поріг, цифровий запис покаже перехід, а аналоговий допоможе зрозуміти його причину.[^tek-mso-digital-circuits]

MSO також може декодувати підтримувані послідовні чи паралельні шини та запускати захоплення за цифровими подіями. Набір протоколів, число входів, смуга пропускання, частота дискретизації та глибина пам’яті залежать від моделі. Спеціалізований логічний аналізатор може мати більше цифрових каналів, а осцилограф – характеристики аналогового вимірювання, потрібні для конкретної задачі. Отже, MSO зручний для корельованих вимірювань, але не є автоматично найкращим приладом для кожного випадку.[^tek-mso-digital-circuits]

Приклад: якщо SPI-пристрій часом читає неправильний біт, MSO дає змогу одночасно побачити тактову лінію, дані, вибір пристрою та аналогову форму фронту. Так перевіряють момент вибірки й електричну якість сигналу.

**Типові помилки:**

- Вважати, що кожен MSO має однакові канали та протокольні декодери.
- Ігнорувати налаштування цифрового порога.
- Робити висновок лише з декодованої шини, не перевіривши аналогову форму.

## Sources

<!-- generated from frontmatter -->

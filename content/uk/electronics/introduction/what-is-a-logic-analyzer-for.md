---
id: emb-elintro-0271
title: "Для чого потрібен логічний аналізатор?"
description: "Для чого потрібен логічний аналізатор?"
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
  - source_id: tek-oscilloscope-types
    title: "Tektronix: Oscilloscope Types"
    url: https://www.tek.com/en/documents/primer/oscilloscope-types
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує цифрові канали логічного аналізатора й порогове визначення high/low; можливості залежать від моделі."

---

## Short answer

Він записує багато цифрових каналів одночасно і декодує протоколи, наприклад `I²C`, `SPI`, `UART`. Це зручно, коли важлива послідовність логічних подій, а не аналогова форма сигналу.[^tek-oscilloscope-types]

## Detailed explanation

Логічний аналізатор захоплює багато цифрових входів і показує їхні логічні рівні та переходи в часі. Він порівнює кожен відлік із заданим порогом і класифікує його як high або low, тому на екрані переважно видно стани й переходи, а не точну амплітуду чи форму фронту. Поріг потрібно налаштувати відповідно до рівнів досліджуваної логічної сім’ї: хибне значення може спричинити помилкове розпізнавання бітів.[^tek-oscilloscope-types]

Захоплення кількох ліній одночасно показує часовий порядок подій. Наприклад, можна перевірити, чи з’явився сигнал вибору пристрою до тактових імпульсів SPI, чи є підтвердження після байта I²C, або скільки триває імпульс мікроконтролера. Якщо прилад підтримує декодер потрібного протоколу, він групує біти у поля та показує їхні значення. Якість декодування залежить від частоти дискретизації, глибини пам’яті, налаштованого порога та правильного підключення пробників.[^tek-oscilloscope-types]

Для аналізу аналогової поведінки цифрової лінії – дзвону, overshoot, повільного фронту чи просідання рівня – потрібен осцилографічний вхід. Логічний аналізатор може виявити помилковий перехід, але не покаже форму напруги, яка його спричинила. Якщо декодер показує неправильний байт UART, перевіряють baud rate, полярність і поріг, а потім зіставляють цифрові стани з аналоговою формою сигналу.

**Типові помилки:**

- Вважати, що логічний аналізатор вимірює точну напругу або якість фронту.
- Покладатися на декодер без перевірки параметрів захоплення.
- Ігнорувати допустимі рівні входів і правильне підключення землі.

## Sources

<!-- generated from frontmatter -->

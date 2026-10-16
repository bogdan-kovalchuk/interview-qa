---
id: emb-elee-0213
title: "Що таке AC-земля в малосигнальному аналізі?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
---

## Short answer

Під час малосигнального аналізу джерело постійної напруги не дає змінної складової, тому його замінюють ідеальним внутрішнім опором, тобто коротким замиканням. Точку, яка так з’єднана, називають AC-землею.[^fiore-common-emitter-amplifier] Це математичний прийом, а не команда фізично закоротити живлення.

## Detailed explanation

Малосигнальний аналіз виконують у два етапи. Спершу рахують постійні напруги й струми, щоб знайти робочу точку транзистора. Потім аналізують змінний сигнал окремо, за принципом суперпозиції. У такому змінному еквіваленті конденсатори замінюють короткими замиканнями, а постійні джерела – їхнім ідеальним внутрішнім опором, тобто знову коротким замиканням.[^fiore-common-emitter-amplifier]

Чому це правильно: джерело постійної напруги має сталу напругу, тож його змінна складова дорівнює нулю. Ідеальне джерело має нульовий внутрішній опір, тому на його затискачах змінна напруга не виникає, і вузол, з’єднаний із таким джерелом, має нульову змінну напругу відносно землі. У CE-каскаді з `V_CC` = 10 В це означає, що шина має постійний потенціал +10 В, але для змінного сигналу вона є землею.[^fiore-common-emitter-amplifier]

Звідси випливає наслідок для опорів. У постійному колі `R_C` підключений до `V_CC`, а в змінному колі його другий вивід іде на землю. Саме тому в змінному еквіваленті каскаду колекторний опір стоїть між колектором і землею, а не між колектором і шиною.[^fiore-common-emitter-amplifier]

AC-земля – ідеалізація. Реальне джерело має ненульовий внутрішній опір, тож коротке замикання точне лише тоді, коли цей опір малий порівняно з іншими опорами схеми на частоті сигналу. Вхідний сигнал під це правило не підпадає: його джерело не замінюють коротким замиканням, бо саме його змінну частину і аналізують.[^fiore-common-emitter-amplifier]

**Типові помилки:**

- Вважати AC-землю фізичним з’єднанням із 0 В: шина +10 В може бути AC-землею, і це не означає, що її постійна напруга дорівнює нулю.[^fiore-common-emitter-amplifier]
- Замінювати коротким замиканням джерело вхідного сигналу: в змінному еквіваленті замінюють лише постійні джерела.[^fiore-common-emitter-amplifier]

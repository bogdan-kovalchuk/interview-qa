---
id: emb-elee-0216
title: "Чому в AC-моделі каскаду навантаження стоїть паралельно `R_C`?"
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

Через розділовий конденсатор (у середній смузі – коротке з’єднання) навантаження підключене до колектора. Шина живлення, до якої йде `R_C`, для змінного сигналу є AC-землею за наявності блокувальних конденсаторів, тому `R_load` стоїть паралельно `R_C`.[^fiore-common-emitter-amplifier]

## Detailed explanation

**Постійний і змінний струм.** Розділовий конденсатор на виході для постійного струму розімкнений, тож навантаження не змінює робочу точку каскаду.[^fiore-common-emitter-amplifier] Конденсатор вибирають так, щоб його реактивний опір на робочій частоті був значно меншим за опори кола. Тоді для змінного сигналу він є коротким замиканням, і `R_load` з’єднаний від колектора до AC-землі, а не послідовно з `R_C`.[^fiore-common-emitter-amplifier]

**Чому шина живлення – AC-земля.** В AC-еквіваленті джерела постійної напруги замінюють їх внутрішніми опорами, для ідеального джерела рівними нулю. Тому вузол `V_CC` стає AC-землею.[^fiore-common-emitter-amplifier] Реальна шина має скінченний опір і пульсації. Блокувальні конденсатори, розміщені близько до активних приладів, зменшують опір шини на змінному сигналі, і тоді це наближення стає добрим.[^fiore-common-emitter-amplifier]

**Наслідок для підсилення.** Змінний опір колектора до AC-землі дорівнює `R_C || R_load = 4,7 кОм || 10 кОм ≈ 3,20 кОм`. Саме він стоїть у `A_v = -r_C/(r'_e + r_E)` з `r_C = R_C || R_load`.[^fiore-common-emitter-amplifier] Тому навантаження змінює підсилення, хоча постійна напруга колектора не змінюється: для каскаду з нешунтованим `R_E` підсилення падає з -4,54 до -3,09 (див. qid:emb-elee-0215). Якщо ж `R_E` зашунтувати, емітер стає AC-землею, `r_E` стає нулем, і підсилення визначається `r'_e` та тим самим `r_C`.[^fiore-common-emitter-amplifier]

**Типові помилки:**

- Вважати, що `R_load` з’єднаний послідовно з `R_C`: для змінного сигналу вони паралельні від колектора до AC-землі.
- Підставляти в формулу лише `R_load` і забувати про `R_C`.
- Вважати шину живлення ідеальною AC-землею без блокувальних конденсаторів.[^fiore-common-emitter-amplifier]

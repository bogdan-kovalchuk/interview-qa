---
id: emb-elintro-0260
title: "Який практичний checklist вибору MOSFET для навантаження?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ti-mosfet-selection
    title: "Texas Instruments: MOSFET Selection Guide for BQ2575x Family"
    url: https://www.ti.com/lit/an/sluaax9/sluaax9.pdf
  - source_id: infineon-mosfet-layout
    title: "Infineon: Designing with power MOSFETs"
    url: https://www.infineon.com/assets/row/public/documents/24/42/infineon-designing-with-power-mosfets-applicationnotes-en.pdf?fileId=8ac78c8c7ddc01d7017e6c619a490f47
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Перевірте максимальні drain-source напругу й струм у реальному режимі, гарантований `R_DS(on)` при доступному `V_GS`, потужність втрат, SOA та температуру кристала.[^ti-mosfet-selection] Для switching-схеми додайте `Q_g`, body diode/reverse recovery, а також придатність корпусу й PCB до відведення тепла.[^infineon-mosfet-layout]

## Detailed explanation

Вибір MOSFET починається з умов навантаження: найбільша робоча напруга разом із перехідними піками, неперервний і імпульсний струм, частота перемикання, температура довкілля та доступна напруга драйвера. Номінал `V_DS` має витримувати реальні піки з обґрунтованим запасом; самі абсолютні максимуми не замінюють аналізу перехідних процесів. Для inductive load окремо визначте шлях струму під час вимкнення й потрібний захист від перенапруги.[^ti-mosfet-selection]

Перевірте таблицю `R_DS(on)` при напрузі gate-source, яку справді забезпечує драйвер. Обчисліть приблизні conduction losses як `P_cond = I_RMS²*R_DS(on)` для відповідного профілю струму й уточніть опір за робочої температури. Для switching режиму врахуйте gate charge, частоту й переходи напруги/струму; малий опір сам по собі не гарантує малих сумарних втрат.[^ti-mosfet-selection]

Перевірте SOA, максимальну температуру junction, thermal resistance та умови, за яких заявлено струмовий рейтинг. Паспортне `I_D` може залежати від заданої температури case або ідеального охолодження, тому для реальної плати потрібен тепловий розрахунок корпусу, copper area і теплових переходів. Перевірте також `V_GS` absolute maximum і спроможність драйвера безпечно заряджати та розряджати gate.[^infineon-mosfet-layout] [^ti-mosfet-selection]

Для індуктивного чи мостового навантаження оцініть body diode forward drop, допустимий струм і reverse-recovery параметри; визначте, чи потрібна провідність diode під час dead time. Нарешті, перевірте pinout, footprint, полярність каналу та конкретну схему підключення. Жоден окремий параметр – ані низький `R_DS(on)`, ані великий струмовий рейтинг – не підтверджує придатність компонента без решти умов застосування.[^infineon-mosfet-layout]

**Типові помилки:**

- Обирати за найбільшим `I_D` на першій сторінці datasheet, ігноруючи теплові умови цього рейтингу.
- Використовувати `R_DS(on)` при іншій напрузі gate або кімнатній температурі без поправки.
- Не перевіряти піки `V_DS`, SOA, gate rating і body diode для індуктивного навантаження.

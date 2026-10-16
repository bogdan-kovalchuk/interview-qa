---
id: emb-elee-0179
title: "Джерело 9 В RMS 50 Гц, міст, C = 1000 мкФ, навантаження 0,1 А. Які пульсації і дно напруги на C?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
---

## Short answer

Після моста частота пульсацій `2*50 = 100 Гц`, тому `ΔV_pp ≈ I/(f*C) = 0.1/(100*0.001) = 1 V`.[^fiore-capacitors] Пік на конденсаторі `9*sqrt(2) - 2*0.7 ≈ 11.33 V`, отже дно `11.33 - 1 ≈ 10.33 V`; це наближена оцінка.[^fiore-rectification] Лінійному стабілізатору потрібно `V_in,trough > V_out + V_dropout`.[^ti-slva079]

## Detailed explanation

**Пульсації.** Міст випрямляє обидва півперіоди, тож піки напруги на конденсаторі повторюються з частотою `2*50 = 100 Гц`, а між піками минає не більше `1/100 = 10 ms`.[^fiore-rectification] За цей час конденсатор віддає навантаженню 0,1 А, а для сталого струму із співвідношення `i = C*dv/dt` випливає `ΔV = I*Δt/C`.[^fiore-capacitors] Звідси `ΔV_pp = 0.1*0.01/0.001 = 1 V`: розмах пульсацій 1 В, тобто приблизно ±0,5 В навколо середнього.

**Дно напруги.** Пік вторинної напруги дорівнює `9*sqrt(2) ≈ 12.73 V`. У мосту проводять два діоди, тож навантаження бачить вторинну напругу мінус два падіння.[^fiore-rectification] З умовними 0,7 В на діод пік на конденсаторі становить `12.73 - 1.4 ≈ 11.33 V`. Віднявши розмах пульсацій, отримуємо дно `11.33 - 1 ≈ 10.33 V`, а середнє значення – приблизно `11.33 - 0.5 ≈ 10.83 V`. Отже, 9 В RMS на вторинній обмотці дають не 9 В постійної напруги, а близько 10,8 В.

**Наскільки це точно.** Формула припускає сталий струм протягом усіх 10 мс, але діоди підзаряджають конденсатор ще до піка, тож реальний розряд коротший. Водночас опір обмотки й діодів знижує пік під час імпульсів зарядного струму. У чисельній моделі (синусоїдне джерело, 0,7 В на діод, сталий струм 0,1 А, 1000 мкФ) за сумарного послідовного опору 0,5 Ом розмах виходить ≈ 0,83 В і дно ≈ 10,33 В, а за 2 Ом – розмах ≈ 0,74 В і дно ≈ 9,79 В. Тому 10,33 В – це орієнтир без урахування опорів, а не гарантія. Якщо мережа на 10 % нижча (`9*0.9 = 8.1 V RMS`), за тією самою формулою дно було б `8.1*sqrt(2) - 1.4 - 1 ≈ 9.06 V`.

**Умова для стабілізатора.** Лінійний стабілізатор перестає стабілізувати, коли вхід падає нижче `V_out + V_dropout`.[^ti-slva079] Це перевіряють за найнижчою миттєвою напругою на вході, тобто за дном пульсацій, а не за середнім значенням (див. qid:emb-elee-0156). Для uA7805 рекомендована вхідна напруга становить 7–25 В, тож дно 10,33 В залишає запас `10.33 - 7 = 3.33 V`, а ≈ 9,06 В за низької мережі – приблизно `9.06 - 7 ≈ 2.1 V`.[^ti-ua78]

**Типові помилки:**

- Брати для моста частоту пульсацій 50 Гц замість 100 Гц і отримувати вдвічі завищені пульсації.
- Забувати два падіння на діодах мосту (брати одне або жодного).
- Вважати 9 В RMS амплітудою, а не діючим значенням.
- Перевіряти стабілізатор за середньою напругою замість найнижчої.

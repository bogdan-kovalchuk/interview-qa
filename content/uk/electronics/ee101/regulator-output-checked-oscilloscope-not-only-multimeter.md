---
id: emb-elee-0166
title: "Чому вихід стабілізатора треба перевіряти осцилографом, а не лише мультиметром?"
description: "Чому вихід стабілізатора треба перевіряти осцилографом, а не лише мультиметром?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 62, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: keysight-34401a-tutorial
    title: "Agilent (Keysight) 34401A: Digital Multimeter Tutorials"
    url: https://www.ee.torontomu.ca/guides/instrument-manuals/Agilent-HP_34401A_Tutorial.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Розділ про power-line noise: цифровий мультиметр з інтегрувальним АЦП вимірює середнє значення входу, інтегруючи його за фіксований час; час інтегрування, кратний періоду мережі, усереднює завади мережі майже до нуля. Документ про конкретний прилад (34401A), розміщений на сайті університету; для інших мультиметрів інтервал і режими інші."
  - source_id: tek-dmm7510-ripple-an
    title: "Tektronix (Keithley): Measuring Low Level Ripple Voltage Using the DMM7510 7-1/2-Digit Graphical Sampling Multimeter"
    url: https://www.tek.com/en/documents/application-note/measuring-low-level-ripple-voltage-using-dmm7510-7-1-2-digit-graphical-s-0
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "У вступі: традиційні DMM зазвичай не вимірюють динамічну поведінку джерел живлення, а для ripple, switching voltage і glitches при вмиканні зазвичай потрібен осцилограф; осцилограф може не мати роздільності для дуже малих пульсацій, а в DC coupling його обмежує максимальний DC offset на найчутливішій шкалі, тоді як у AC coupling він розрізняє ripple частково. Приклад у записці – імпульсний понижувальний перетворювач, а не лінійний стабілізатор."
  - source_id: teledyne-probe-ground-lead
    title: "Teledyne LeCroy: Passive Probe Ground Lead Effects"
    url: https://www.teledynelecroy.com/doc/passive-probe-ground-lead-effects
    accessed: 2026-10-06
    kind: official
    version: "June 2013"
    applicability: "Довгий ground lead із крокодилом (орієнтовно 10 дюймів, правило 20 нГн на дюйм, близько 200 нГн) разом із вхідною ємністю пробника утворює послідовний резонанс, звужує смугу й дає дзвін на швидких фронтах; ground blade чи spring мають 10–20 нГн. Числа стосуються пасивних пробників Teledyne LeCroy 500 МГц; для інших пробників вони інші."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "Вихідний конденсатор не потрібен для стабільності, але покращує перехідну характеристику; якщо стабілізатор далі приблизно ніж за шість дюймів від фільтра живлення, потрібен вхідний конденсатор від 0,1 мкФ «для стабільності». Значення стосуються родини LM340/LM7805, інші стабілізатори й виробники можуть вимагати іншого."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Розділ 10: виробники LDO зазвичай наводять діапазон стабільних значень compensation series resistance (CSR = ESR вихідного конденсатора плюс додатковий резистор), бо CSR може спричинити нестабільність залежно від вихідного струму (приклад TPS763xx: 0,2–9 Ом). Записка про LDO; для 7805 вимоги до конденсаторів інші."
---

## Short answer

У режимі DC мультиметр показує усереднене за час вимірювання значення, тож симетричні пульсації чи швидке самозбудження можуть майже не змінити показання.[^keysight-34401a-tutorial] Осцилограф показує форму напруги в часі – розмах і частоту пульсацій, коливання, провали; для таких явищ зазвичай і потрібен осцилограф.[^tek-dmm7510-ripple-an]

## Detailed explanation

Цифровий мультиметр з інтегрувальним АЦП вимірює середнє значення входу, інтегруючи його за фіксований час, а час інтегрування зазвичай підбирають кратним періоду мережі, щоб наводки мережі усереднилися майже до нуля.[^keysight-34401a-tutorial] Тому в режимі DC швидкі зміни напруги, симетричні відносно середнього, у показанні гаснуть: стабілізатор із пульсаціями 100–120 Гц чи з коливаннями на сотнях кілогерц може дати майже те саме число, що й чистий. Для вимірювань джерел живлення це відома межа: традиційні DMM зазвичай не фіксують динамічну поведінку, а для ripple, switching voltage і glitches при вмиканні зазвичай потрібен осцилограф.[^tek-dmm7510-ripple-an]

**Приклад (ілюстративні числа).** Вихід 5 В коливається по трикутнику між 4,5 і 5,5 В (розмах 1 В). Середнє дорівнює `(4,5 + 5,5)/2 = 5,0 В`, і мультиметр у режимі DC покаже приблизно 5,0 В. Навантаження ж бачить провали до 4,5 В, що виходить за допуск ±5 % (`5*0,05 = 0,25 В`, тобто 4,75–5,25 В). Осцилограф покаже обидва екстремуми й частоту, а за ними вже можна шукати причину.

Причини таких коливань реальні. Datasheet LM340/LM7805 вимагає вхідний конденсатор від 0,1 мкФ «для стабільності», якщо стабілізатор розташований далі приблизно ніж за шість дюймів від фільтра живлення; вихідний конденсатор для стабільності не потрібен, але покращує перехідну характеристику.[^ti-lm340] Для LDO виробники зазвичай наводять діапазон допустимого CSR (ESR вихідного конденсатора плюс додатковий резистор), поза яким стабілізатор нестабільний.[^ti-slva079] Невдалий конденсатор чи довгі дроти можуть тому дати самозбудження, а мультиметр цього не покаже.

Осцилограф теж має обмеження. Для дуже малих пульсацій його роздільності може бракувати, а в DC coupling на найчутливішій шкалі його обмежує максимальний DC offset; в AC coupling ripple видно краще, хоч і не ідеально.[^tek-dmm7510-ripple-an] Довгий ground lead із крокодилом (близько 200 нГн за правилом 20 нГн на дюйм) разом із ємністю пробника створює резонанс і дзвін на швидких фронтах, який легко прийняти за пульсації стабілізатора.[^teledyne-probe-ground-lead] Тому користуються коротким ground spring чи blade (10–20 нГн) і підключаються поблизу виводів стабілізатора й його конденсатора.

**Типові помилки:**

- Вважати, що стабільне показання DMM означає чисту шину: середнє може бути правильним за небезпечних екстремумів.
- Міряти пробником із довгим ground lead і приймати його дзвін за пульсації чи самозбудження.
- Шукати малі пульсації в DC coupling на грубій шкалі: для цього використовують AC coupling і чутливішу шкалу.
## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

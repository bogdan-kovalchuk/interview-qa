---
id: emb-elee-0166
title: "Чому вихід стабілізатора треба перевіряти осцилографом, а не лише мультиметром?"
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
  - source_id: keysight-34401a-tutorial
    title: "Agilent (Keysight) 34401A: Digital Multimeter Tutorials"
    url: https://www.ee.torontomu.ca/guides/instrument-manuals/Agilent-HP_34401A_Tutorial.pdf
  - source_id: tek-dmm7510-ripple-an
    title: "Tektronix (Keithley): Measuring Low Level Ripple Voltage Using the DMM7510 7-1/2-Digit Graphical Sampling Multimeter"
    url: https://www.tek.com/en/documents/application-note/measuring-low-level-ripple-voltage-using-dmm7510-7-1-2-digit-graphical-s-0
  - source_id: teledyne-probe-ground-lead
    title: "Teledyne LeCroy: Passive Probe Ground Lead Effects"
    url: https://www.teledynelecroy.com/doc/passive-probe-ground-lead-effects
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
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

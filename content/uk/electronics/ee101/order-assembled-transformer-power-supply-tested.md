---
id: emb-elee-0180
title: "У якій послідовності перевіряють зібране джерело живлення з трансформатором?"
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
  - source_id: libretexts-fiore-rectification
    title: "Fiore: Semiconductor Devices, 3.2 Rectification (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: openstax-rc-circuits
    title: "OpenStax University Physics Volume 2: 10.5 RC Circuits"
    url: https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits
---

## Short answer

Спочатку вторинну AC-напругу без регулятора, потім полярність і DC-рівень після моста і конденсатора, і лише потім підключають регулятор і розраховане навантаження. Перед перебудовою – відключити живлення і перевірити розряд конденсатора.[^openstax-rc-circuits]

## Detailed explanation

Першим вимірюють змінну напругу на вторинній обмотці, до того як щось підключено до випрямляча. Так перевіряють трансформатор і мережевий ввід без ризику пошкодити регулятор, навантаження чи конденсатор: якщо напруга далека від розрахункової або близька до нуля, причину шукають до мосту, а не після нього.

Далі перевіряють DC-рівень після мостового випрямляча і фільтрувального конденсатора. Навантаження отримує струм в обох півперіодах, і пік напруги на навантаженні дорівнює піку вторинної обмотки мінус два падіння на діодах.[^libretexts-fiore-rectification] З конденсатором без навантаження постійна напруга близька до цього піка. Для вторинної обмотки 12 В RMS пік становить близько 12 × 1,41 ≈ 17 В. При типовому падінні 0,7 В на кремнієвому діоді очікують близько 17 − 1,4 ≈ 15,6 В. Полярність перевіряють там само: полярний електролітичний конденсатор, вставлений навпаки, може вийти з ладу катастрофічно.[^fiore-capacitors]

Регулятор підключають останнім, коли DC-рівень уже відомий. Datasheet LM340 задає вхід 7,5 В як потрібний для збереження line regulation для виходу 5 В,[^ti-lm340] а 2 В dropout за струму 1 А є типовим значенням. Тому з урахуванням провалів пульсацій мінімальний рівень після конденсатора має бути не нижчим за 7,5 В. Якщо після конденсатора виміряно 6 В, стабілізатор не дасть 5 В, і це треба виправити до підключення, а не після.

Перед перебудовою живлення вимикають, але конденсатор не втрачає заряд миттєво: він розряджається через опір, тобто через навантаження або розрядний резистор.[^openstax-rc-circuits] Тому напругу на ньому перевіряють вимірювачем, а не вважають, що після вимкнення він уже порожній.

**Типові помилки:**

- Підключати регулятор і навантаження раніше, ніж перевірено полярність і DC-рівень після конденсатора.
- Вважати, що конденсатор розряджений одразу після вимкнення живлення.
- Перевіряти вихід стабілізатора, не звіривши вхід із вимогою datasheet: без запасу над нею стабілізації немає.

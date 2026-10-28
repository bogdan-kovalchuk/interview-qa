---
id: emb-elee-0252
title: "Чому генерація кварцового генератора може зникнути після підключення пробника?"
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
  - source_id: st-an2867-oscillator-design
    title: "STMicroelectronics Application Note AN2867: Oscillator design guide for STM32 microcontrollers"
    url: https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm32-microcontrollers-stmicroelectronics.pdf
  - source_id: tektronix-probe-loading
    title: "Tektronix Application Note: Low-Current and High-Impedance Probing Pitfalls"
    url: https://www.tek.com/en/documents/application-note/low-current-and-high-impedance-probing-pitfalls
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

Ємність і навантаження пробника змінюють умови петлі та резонатора. Вимірюють насамперед буферизований вихід, а не чутливий вузол резонатора, і не перевищують допустимий drive level кварцу.[^udemy-electronics-course]

## Detailed explanation

Зрив генерації кварцового генератора при підключенні стандартного осцилографічного пробника є класичною апаратною проблемою, зумовленою високою чутливістю схеми Пірса до паразитного ємнісного та активного навантаження[^udemy-electronics-course][^tektronix-probe-loading].

### Умови збудження генератора та критерій Баркгаузена

Генератор Пірса складається з інвертуючого КМОН-підсилювача та зворотного зв’язку через кварцовий резонатор і фазозсувні конденсатори `C_1`, `C_2`[^st-an2867-oscillator-design]. Для підтримання незгасних коливань на резонансній частоті повинні суворо виконуватися умови критерію Баркгаузена:
1. Модуль петльового підсилення дорівнює одиниці: `|A * beta| = 1` (для надійного самозбудження при старті потрібно `|A * beta| > 1`).
2. Сумарний фазовий зсув по петлі зворотного зв’язку кратний 360° (180° забезпечує інвертор і ще 180° – резонансна П-ланка кварцу з конденсаторами)[^st-an2867-oscillator-design][^art-of-electronics].

У сучасних низькоспоживаючих мікроконтролерах підсилювач оптимізований під мінімальний струм споживання (особливо для годинникових генераторів 32,768 кГц, де робочий струм становить сотні наноампер). Його крутизна `g_m` перебуває на межі мінімально допустимого запасу збудження: `Gain_margin = g_m / g_mcrit`[^st-an2867-oscillator-design].

### Параметри осцилографічного пробника та механізм зриву коливань

Типовий стандартний пасивний пробник 10X має такі вхідні параметри:
- вхідний активний опір `R_probe ≈ 10 МОм`;
- паразитна вхідна ємність `C_probe ≈ 10–15 пФ` (для дільника 1X ємність сягає 50–100 пФ, а опір знижується до 1 МОм)[^tektronix-probe-loading].

Коли наконечник пробника торкається високоомного входу генератора (OSC_IN):
1. **Подвоєння ємності навантаження:** Вхідна ємність пробника `C_probe` додається паралельно до власного навантажувального конденсатора `C_1` (який зазвичай має номінал 12–22 пФ). Сумарна ємність плеча миттєво зростає майже вдвічі.
2. **Стрибок критичної крутизни:** Необхідна для генерації крутизна підсилювача пропорційна квадрату навантажувальної ємності: `g_mcrit = 4 * ESR * (2 * pi * f)^2 * (C_0 + C_L)^2`[^st-an2867-oscillator-design]. При підключенні пробника величина `g_mcrit` різко підскакує в кілька разів, значно перевищуючи фактичну крутизну `g_m` вбудованого транзистора. Петльове підсилення стає меншим за одиницю (`|A * beta| < 1`), фазовий баланс руйнується, і коливання миттєво згасають[^st-an2867-oscillator-design][^tektronix-probe-loading].
3. **Шунтування виходу (OSC_OUT):** При спробі підключитися до виходу інвертора ємність і провідність пробника навантажують слабкий вихідний каскад, спричиняючи значне падіння амплітуди сигналу та спотворення фазового зсуву, що також призводить до зупинки тактування[^tektronix-probe-loading].

### Правильні методи контролю частоти кварцу

Щоб перевірити працездатність та точність кварцового генератора без зриву коливань, застосовують такі інженерні підходи[^st-an2867-oscillator-design][^tektronix-probe-loading]:
- **Вимірювання на буферизованому цифровому виході (MCO):** Більшість сучасних мікроконтролерів (зокрема лінійки STM32) мають функцію виведення тактового сигналу на спеціальний вивід GPIO (Microcontroller Clock Output – MCO). Цей сигнал проходить через внутрішній буферний логічний вентиль із низьким вихідним опором (десятки ом), і підключення стандартного пробника до нього не чинить жодного впливу на чутливий аналоговий резонатор[^st-an2867-oscillator-design].
- **Використання активного польового пробника (Active FET Probe):** Активні пробники мають вхідну ємність менше 0,5–1 пФ та гігаомний вхідний опір, що мінімізує вплив на коливальний контур[^tektronix-probe-loading].
- **Безконтактний метод (зонд ближнього поля):** До корпусу резонатора підносять невелику петлю зв’язку або вилку зонда ближнього поля (near-field probe), підключену до спектроаналізатора чи чутливого осцилографа. Вимірювання здійснюється за рахунок електромагнітного випромінювання без фізичного контакту з доріжками[^tektronix-probe-loading].

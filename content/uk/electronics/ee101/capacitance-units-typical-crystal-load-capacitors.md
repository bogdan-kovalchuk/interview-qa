---
id: emb-elee-0251
title: "Які одиниці ємності типові для навантажувальних конденсаторів кварцу?"
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
  - source_id: ti-msp430-crystal-selection
    title: "Texas Instruments Application Report SLAA322: Selection and Specification of Crystals for Texas Instruments MSP430"
    url: https://www.ti.com/lit/an/slaa322/slaa322.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

Одиниці або десятки пікофарад. Автосубтитри можуть плутати пФ з мкФ – різниця в мільйон разів, тому одиниці перевіряють за схемою і паспортом.[^udemy-electronics-course]

## Detailed explanation

Навантажувальні конденсатори для кварцових резонаторів у мікроконтролерних і цифрових схемах завжди обираються в одиницях **пікофарад (пФ / pF, 10^-12 Ф)**, типово від 5–10 пФ до 33–39 пФ[^udemy-electronics-course][^st-an2867-oscillator-design].

### Чому саме пікофаради: фізичне обґрунтування

1. **Паспортний діапазон ємності кварцу:** Кварцові кристали, що використовуються в електроніці (від низькочастотних годинникових 32,768 кГц до мегагерцових 4–48 МГц), виготовляються з розрахунку на паспортну навантажувальну ємність `C_L` у межах від 6 пФ до 20 пФ (найпоширеніші значення – 8 пФ, 12,5 пФ, 16 пФ та 18 пФ)[^st-an2867-oscillator-design][^ti-msp430-crystal-selection].
2. **Формула розрахунку:** Оскільки зовнішні конденсатори `C_1` і `C_2` утворюють послідовне коло щодо резонатора, сумарна ємність визначається співвідношенням `C_L = (C_1 * C_2) / (C_1 + C_2) + C_stray`. При однакових конденсаторах `C_1 = C_2 = C` отримуємо `C = 2 * (C_L - C_stray)`. Враховуючи типову паразитну ємність друкованої плати та виводів мікроконтролера `C_stray ≈ 2–5 пФ`, зовнішні конденсатори набувають значень від 10 пФ до 33 пФ[^st-an2867-oscillator-design].
3. **Узгодження імпедансу контуру:** Реактивний опір конденсатора на частоті коливань `f` становить `X_C = 1 / (2 * pi * f * C)`. Наприклад, для високочастотного кварцу `f = 16 МГц` і конденсатора `C = 20 пФ`:
`X_C = 1 / (2 * pi * 16 * 10^6 * 20 * 10^-12) ≈ 497 Ом`.
Цей рівень імпедансу ідеально узгоджується з вихідним динамічним опором вбудованого КМОН-інвертора (сотні ом) та еквівалентним послідовним опором кварцу (ESR від 20 до 80 Ом), забезпечуючи необхідний фазовий зсув 180° без перевантаження підсилювача[^art-of-electronics].

### Катастрофічні наслідки плутанини одиниць (пФ проти мкФ)

Між пікофарадами (`1 пФ = 10^-12 Ф`) та мікрофарадами (`1 мкФ = 10^-6 Ф`) різниця становить рівно **один мільйон разів (10^6)**[^art-of-electronics]:
- Якщо інженер чи монтажник помилково встановить конденсатори номіналом 18 мкФ (або навіть 0,1 мкФ) замість 18 пФ, реактивний опір на частоті 16 МГц складе:
`X_C = 1 / (2 * pi * 16 * 10^6 * 0,1 * 10^-6) ≈ 0,099 Ом`.
- Опір у десяті або соті частки ома фактично являє собою **пряме коротке замикання** виводів генератора OSC_IN і OSC_OUT на землю GND.
- За такого шунтування інвертуючий підсилювач не зможе розвинути амплітуду коливань, коефіцієнт підсилення петлі впаде до нуля, і генерація не запуститься за жодних умов[^st-an2867-oscillator-design].

### Причини виникнення помилок на практиці

1. **Помилки автоматичного розпізнавання мови (STT) та автосубтитрів:** У навчальних відео чи голосових лекціях системи розпізнавання мови часто плутають співзвучні англійські терміни "picofarad" та "microfarad" або графічні символи "pF" та "uF".
2. **Тип діелектрика:** Для кварцових резонаторів критично важливою є температурна стабільність, тому конденсатори ємністю одиниці-десятки пікофарад обирають виключно з керамічним діелектриком класу 1 (NP0 / C0G), що має нульовий температурний коефіцієнт ємності (TCC) та мінімальний діелектричний гістерезис[^ti-msp430-crystal-selection]. Конденсатори в мікрофарадному діапазоні належать до класів X5R/X7R чи електролітичних і для тактових контурів є принципово непридатними.

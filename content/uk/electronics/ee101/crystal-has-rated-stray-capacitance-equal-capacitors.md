---
id: emb-elee-0250
title: "Кварц має паспортну C_L = 18 пФ, паразитна ємність ≈ 3 пФ. Які однакові конденсатори C_1=C_2 потрібні?"
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
  - source_id: microchip-an826-crystal-basics
    title: "Microchip Application Note AN826: Crystal Oscillator Basics and Crystal Selection for rfPIC and PICmicro Devices"
    url: https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

C_L ≈ (C_1 * C_2) / (C_1 + C_2) + C_stray = C / 2 + 3 пФ, звідки C ≈ 30 пФ. Це початкова оцінка; реальні паразити і рекомендації виробника уточнюють номінал.[^udemy-electronics-course]

## Detailed explanation

Для стабільної генерації тактового сигналу на паспортній частоті кварцовий резонатор у схемі генератора Пірса (Pierce oscillator) вимагає суворо визначеного значення еквівалентної ємності навантаження `C_L`[^udemy-electronics-course][^st-an2867-oscillator-design].

### Топологія схеми Пірса та еквівалентне коло

Генератор Пірса, інтегрований у більшість мікроконтролерів, складається з інвертуючого підсилювача (виводи OSC_IN та OSC_OUT), резистора зворотного зв’язку та П-подібної фільтруючої ланки, утвореної кварцовим резонатором і двома зовнішніми конденсаторами `C_1` та `C_2`, що підключені до землі[^st-an2867-oscillator-design][^microchip-an826-crystal-basics].

З погляду резонатора зовнішні навантажувальні конденсатори `C_1` і `C_2` з’єднані послідовно через спільну шину заземлення:
`C_series = (C_1 * C_2) / (C_1 + C_2)`.

Паралельно до цієї послідовної комбінації приєднується сумарна паразитна ємність монтажу `C_stray` (stray capacitance). Вона враховує:
- ємність доріжок друкованої плати від виводів кварцу до виводів мікроконтролера (`C_PCB ≈ 1–3 пФ`);
- паразитні ємності контактних площадок і корпусу резонатора;
- внутрішні ємності виводів мікроконтролера `C_in` та `C_out` (зазвичай 2–5 пФ на кожен вивід)[^st-an2867-oscillator-design].

Повна ємність навантаження, яку "бачить" кварц між своїми контактами, описується фундаментальним рівнянням:
`C_L = (C_1 * C_2) / (C_1 + C_2) + C_stray`[^st-an2867-oscillator-design][^microchip-an826-crystal-basics].

### Математичний розрахунок для однакових номіналів

Для забезпечення симетрії амплітуди коливань та фазового зсуву зазвичай обирають однакові конденсатори: `C_1 = C_2 = C`.
Тоді послідовне з’єднання спрощується:
`(C * C) / (C + C) = C^2 / (2 * C) = C / 2`.

Підставивши цей вираз у загальне рівняння навантажувальної ємності, отримуємо:
`C_L = C / 2 + C_stray`.

Звідси шуканий номінал конденсаторів `C` виражається формулою:
`C / 2 = C_L - C_stray`, звідки `C = 2 * (C_L - C_stray)`[^st-an2867-oscillator-design][^art-of-electronics].

Підставляємо числові значення з умови завдання (`C_L = 18 пФ`, `C_stray ≈ 3 пФ`):
`C = 2 * (18 пФ - 3 пФ) = 2 * 15 пФ = 30 пФ`.

Таким чином, розрахункове значення кожного конденсатора становить **30 пФ**. Оскільки 30 пФ є стандартним номіналом ряду E96 (або рідше E24), інженер зазвичай обирає або точно 30 пФ, або найближчі поширені номінали з ряду E24: 27 пФ чи 33 пФ з діелектриком NP0/C0G[^st-an2867-oscillator-design].

### Вплив похибки вибору ємності

1. **Зсув частоти (Frequency Pulling):** Кварцовий резонатор працює в області паралельного резонансу (індуктивний характер реактивного опору). Якщо встановити конденсатори меншої ємності, сумарна навантажувальна ємність стане меншою за паспортну `C_L`, і резонансна частота генератора зміститься вгору від номіналу. І навпаки, за завищеної ємності частота генератора зміщується вниз[^microchip-an826-crystal-basics].
2. **Запас підсилення та зрив генерації:** Значне завищення ємності `C` збільшує навантажувальну ємність `C_L` і різко підвищує критичну крутизну збудження `g_mcrit = 4 * ESR * (2 * pi * f)^2 * (C_0 + C_L)^2` (де `C_0` – шунтуюча статична ємність кварцу). Якщо необхідне посилення перевищить можливості внутрішнього інвертора мікроконтролера, коефіцієнт запасу генератора (gain margin) впаде нижче рекомендованого значення 5, що призведе до невпевненого запуску або повної зупинки генератора при низьких температурах чи просіданні живлення[^st-an2867-oscillator-design].

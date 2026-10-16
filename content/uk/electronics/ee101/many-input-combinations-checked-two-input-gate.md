---
id: emb-elee-0240
title: "Скільки комбінацій входів треба перевірити у двовхідному вентилі і що записувати?"
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
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  - source_id: fiore-bjt-switching
    title: "Fiore: Semiconductor Devices, 4.7 BJT Switching and Driver Applications (LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04%3A_Bipolar_Junction_Transistors_(BJTs)/4.7%3A_BJT_Switching_and_Driver_Applications
---

## Short answer

Усі чотири комбінації входів: 00, 01, 10 і 11 (`2^2 = 4`), навіть якщо схема «наче працює». Для кожної записують фактичну напругу виходу, а не лише стан індикаторного LED, бо важливо, чи напруга лежить у межах логічного рівня наступного входу.[^ti-hc00]

## Detailed explanation

Двовхідний вентиль має чотири стани входів, бо кожен вхід може бути в одному з двох логічних станів: `2^2 = 4`. Таблиця істинності містить усі чотири рядки: 00, 01, 10 і 11. Перевірка лише рядків, де вихід «мав би бути 1», або лише двох рядків не доводить правильності: несправність може проявлятися саме в рядку, який не перевіряли. Для трьох входів таблиця має вісім рядків (`2^3 = 8`), тож повний перебір зростає експоненційно, але принцип той самий.

Записувати треба напругу, а не тільки висновок «горить / не горить», бо логічний рівень визначається діапазоном напруги, а не одним числом. Для SN74HC00 при VCC = 4,5 В вхід вважається високим від 3,15 В (VIH min) і низьким до 1,35 В (VIL max).[^ti-hc00] Між цими межами лежить зона, яку наступний вентиль не має права трактувати ні як 0, ні як 1; її ширина дорівнює `3,15 - 1,35 = 1,80 В`. Для рядків, де вихід NAND має бути в стані 1, datasheet при малому навантаженні дає мінімум 4,4 В.[^ti-hc00]

LED не є заміною вимірювання. Яскравість LED залежить від струму через нього, а не від порогів логіки. У прикладі з книги Fiore логічний вихід може віддати, скажімо, 5 мА, тоді як для потрібної яскравості LED може знадобитися понад 10 мА.[^fiore-bjt-switching] Тому LED може тьмяно світитися тоді, коли напруга вже лежить у забороненій зоні наступного входу.

**Приклад:** NAND має дати 1 у рядках 00, 01 і 10, та 0 у рядку 11. Припустімо, що в рядках 00, 01 і 10 вихід близько 4,4 В, а в рядку 11 – 2,9 В. Вихід у рядку 11 має бути низьким, але 2,9 В лежить між 1,35 В і 3,15 В, тож наступний вентиль цього не прочитає однозначно. LED при цьому може горіти й створювати враження, що все добре. Запис «0» або «1» без напруги цієї помилки не покаже.

**Типові помилки:**

- перевіряти лише ті рядки, де очікується 1, або кілька рядків, вважаючи решту очевидною;
- вважати, що LED, який горить, означає правильний логічний рівень;
- записувати «0» або «1» без виміряної напруги і без порога входу наступного каскаду.

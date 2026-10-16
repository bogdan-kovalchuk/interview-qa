---
id: emb-elee-0206
title: "Навіщо потрібен підсилювач з `A_v<1`?"
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
  - source_id: fiore-common-collector-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
---

## Short answer

Такий підсилювач – емітерний повторювач: його `A_v` менший за 1, але близький до 1, зате він має високий вхідний і низький вихідний опір та струмове підсилення. Тому він майже не навантажує джерело сигналу і може живити низькоомне навантаження, тобто працює як буфер між каскадами.[^fiore-common-collector-amplifier]

## Detailed explanation

Підсилювач з `A_v < 1` – це емітерний повторювач (схема зі спільним колектором). Вихідна напруга знімається з емітера й повторює напругу бази, тому `A_v = r_E/(r_e + r_E)`, де `r_E` – опір в емітерному колі разом із навантаженням. Ця величина завжди менша за 1 і наближається до 1, коли `r_E ≫ r_e`.[^fiore-common-collector-amplifier]

Потреба в такому каскаді не в підсиленні напруги, а в узгодженні опорів. Джерело з великим внутрішнім опором, навантажене низькоомним резистором, утворює подільник, і більша частина сигналу губиться. У прикладі Fiore джерело має опір 1 кОм, навантаження 500 Ом, вхідний сигнал 100 мВ: без повторювача на навантаженні 100 мВ × 500 / 1500 ≈ 33 мВ. З повторювачем вхідний опір каскаду близько 9 кОм, підсилення з навантаженням близько 0,94, коефіцієнт подільника зі джерелом близько 0,90, і на навантаженні виходить близько 85 мВ.[^fiore-common-collector-amplifier]

Повторювач не підсилює напругу, але підсилює струм і потужність. Його вихідний опір малий: у прикладі близько 37 Ом, що набагато менше, ніж у каскадів зі спільним емітером, тож він може живити низькоомне навантаження. Спотворення в повторювачах зазвичай малі, бо підсилення близьке до одиниці, а це бажана мета.[^fiore-common-collector-amplifier] Вихідний сигнал у фазі з вхідним.[^fiore-common-collector-amplifier]

**Типові помилки:**

- Очікувати від повторювача підсилення напруги більше за 1.
- Не враховувати його вхідний опір як навантаження для джерела разом з опором самого джерела.
- Вважати, що вихідний опір дорівнює нулю: він визначається паралельним `R_E` і опором бази, тож не є нульовим.

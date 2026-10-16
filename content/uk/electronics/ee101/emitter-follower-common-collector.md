---
id: emb-elee-0201
title: "Що таке емітерний повторювач (спільний колектор) і для чого він потрібен?"
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
  - source_id: fiore-common-collector
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
---

## Short answer

Вихід знімають з емітера: він повторює напругу бази зі зсувом ≈ `V_BE`. Підсилення за напругою трохи менше одиниці, зате є струмове підсилення, великий вхідний і малий вихідний опір, тож каскад мало навантажує попереднє джерело і добре віддає струм навантаженню – це буфер.[^fiore-common-collector]

## Detailed explanation

Емітерний повторювач – це схема зі спільним колектором. Вхідний сигнал подається на базу, вихід знімають з емітера через резистор `R_E` на землю, а колектор для змінного сигналу має потенціал землі, бо з’єднаний із живленням.[^fiore-common-collector] Напруга емітера йде за напругою бази з падінням на переході база–емітер `V_BE`, приблизно 0,7 В для кремнію.[^fiore-bjt-basics] Фаза не змінюється: зростання входу дає зростання виходу.[^fiore-common-collector]

Підсилення видно з малосигнальної схеми. Змінний струм емітера `i_e` проходить через динамічний опір переходу `r'_e` ≈ 26 мВ / `I_E` і через `r_E`, яке дорівнює `R_E` або `R_E` ∥ `R_load`. Вхідна напруга на базі: `v_in` = `i_e` × (`r'_e` + `r_E`), вихід на емітері: `v_out` = `i_e` × `r_E`. Звідси `A_v` = `r_E` / (`r'_e` + `r_E`), і це значення завжди менше одиниці, бо `r'_e` > 0. Коли `r_E` значно більший за `r'_e`, підсилення близьке до 1.[^fiore-common-collector][^fiore-bjt-ac-model]

Цінність повторювача – в опорах. Вхідний опір на базі дорівнює β × (`r'_e` + `r_E`), тобто великий, але паралельні резистори подільника бази знижують його. Вихідний опір дорівнює `R_E` ∥ (`r'_e` + (`r_B` ∥ `r_gen`) / β), тобто малий. У прикладі підручника джерело 1 кОм з навантаженням 500 Ом без повторювача дає на навантаженні 100 мВ × 500 / 1500 ≈ 33 мВ, а з повторювачем – близько 85 мВ при вихідному опорі ≈ 37 Ом.[^fiore-common-collector]

Щоб не переоцінити схему, треба пам’ятати два обмеження. По-перше, `V_BE` і `r'_e` залежать від струму `I_E` і температури, тож зсув між входом і виходом не сталий. По-друге, `r'_e` є малосигнальним значенням: воно справедливе, поки змінна складова струму мала, інакше сигнал спотворюється.[^fiore-bjt-ac-model]

**Типові помилки:**
- Очікувати підсилення напруги більше 1: `A_v` завжди менше 1.
- Вважати вихідний опір рівним `R_E`: точніше `R_E` ∥ (`r'_e` + (`r_B` ∥ `r_gen`) / β).[^fiore-common-collector]
- Вважати, що повторювач інвертує сигнал, як каскад зі спільним емітером: фаза зберігається.

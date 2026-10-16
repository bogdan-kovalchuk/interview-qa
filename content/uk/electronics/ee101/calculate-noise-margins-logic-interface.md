---
id: emb-elee-0235
title: "Як обчислити запаси завадостійкості логічного інтерфейсу?"
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
  - source_id: ti-szza036c
    title: "TI SZZA036C: Understanding and Interpreting Standard-Logic Data Sheets"
    url: https://www.ti.com/lit/an/szza036c/szza036c.pdf
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  - source_id: ti-sn74ls00
    title: "TI SDLS025D: SNx400, SNx4LS00, SNx4S00 quadruple 2-input NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls00.pdf
---

## Short answer

`NM_L = V_IL,max - V_OL,max` і `NM_H = V_OH,min - V_IH,min`: це запаси завадостійкості для низького та високого рівня.[^ti-szza036c] Додатний запас означає, що гарантований вихідний рівень має резерв до граничного вхідного рівня наступного каскаду.

## Detailed explanation

Вихід логічного елемента не видає ідеальних нуля й одиниці: виробник гарантує лише граничні рівні. Для виходу це `V_OL,max` і `V_OH,min`, для входу наступного каскаду – `V_IL,max` і `V_IH,min`.[^ti-szza036c] Запас завадостійкості – це зазор між ними: завада, що додає напругу до сигналу, не змінить логічного рівня, доки сигнал не перетне поріг входу. Низький і високий запаси рахують окремо, бо вони не обов’язково однакові.

Приклад з 74HC00 при `VCC = 4.5 V` (значення VOH і VOL – при 25 °C): `VIH,min = 3.15 V`, `VIL,max = 1.35 V`.[^ti-hc00] При малому навантаженні (20 мкА) `VOL,max = 0.1 V`, `VOH,min = 4.4 V`, тож `NM_L = 1.35 - 0.1 = 1.25 V` і `NM_H = 4.4 - 3.15 = 1.25 V`. При струмі 4 мА той самий datasheet дає `VOL,max = 0.26 V` і `VOH,min = 3.98 V`,[^ti-hc00] тому `NM_L = 1.35 - 0.26 = 1.09 V` і `NM_H = 3.98 - 3.15 = 0.83 V`. Менший із двох запасів, 0,83 В, визначає стійкість: навантаження найбільше зменшує саме високий рівень.

Для порівняння TTL-серії 7400 гарантує `VOH,min = 2.4 V` і `VOL,max = 0.4 V`, а входи розпізнають `VIH,min = 2 V` і `VIL,max = 0.8 V`.[^ti-sn74ls00] Тоді `NM_H = 2.4 - 2.0 = 0.4 V` і `NM_L = 0.8 - 0.4 = 0.4 V`. Умови тесту тут інші (`VOL = 0.4 V` дійсне при струмі 16 мА), тож пряме порівняння з CMOS умовне, але запас 0,4 В у TTL суттєво менший за 0,83–1,25 В у 74HC00.

Запас – статичне поняття: він описує постійні рівні й не враховує викидів, коливань після фронту чи шуму від одночасного перемикання виходів. Числа з datasheet діють лише за умов тесту (напруга живлення, температура, струм), тож їх не можна переносити на інший `VCC` чи інший струм без перевірки таблиць.

**Типові помилки:**

- Брати типові (TYP) значення замість гарантованих MIN і MAX.
- Рахувати тільки один запас і вважати елемент стійким, хоча другий може бути меншим.
- Ігнорувати навантаження: `VOH` і `VOL` задано для конкретних струмів, за інших струмів вони інші.[^ti-hc00]

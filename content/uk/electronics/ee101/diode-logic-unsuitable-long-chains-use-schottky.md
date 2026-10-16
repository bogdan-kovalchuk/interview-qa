---
id: emb-elee-0149
title: "Чому діодна логіка непридатна для довгих ланцюжків і навіщо в ній діоди Шотткі?"
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
  - source_id: nexperia-diode-handbook
    title: "Nexperia: Diode Application Handbook (Design Engineer’s Guide), 2022"
    url: https://assets.nexperia.com/documents/brochure/Nexperia_document_book_DiodeApplicationHandbook_2022.pdf
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
  - source_id: vishay-bat54
    title: "Vishay: BAT54, BAT54A, BAT54C, BAT54S small signal Schottky diodes (datasheet)"
    url: https://www.vishay.com/docs/86410/bat54_bat54a_bat54c_bat54s.pdf
  - source_id: ti-hc00
    title: "TI: SN74HC00, SN54HC00 quadruple 2-input NAND gates (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

Діодна логіка пасивна: вона не відновлює рівні й не підсилює сигнал, тому падіння `V_F` накопичуються від каскаду до каскаду.[^utah-cs6710-diode-logic] Діод Шотткі має менше `V_F`, тож логічний нуль зростає повільніше, але накопичення це не усуває, а менше `V_F` дається компромісом зі струмом витоку.[^nexperia-diode-handbook] Сумісність слід перевіряти за порогами наступного каскаду.[^ti-hc00]

## Detailed explanation

У діодному AND вихід низького рівня дорівнює низькому входу плюс `V_F`. Якщо цей вихід подати на вхід наступного такого вентиля, той додасть ще одне `V_F`, і так далі: після `n` каскадів логічний нуль піднімається приблизно до `n*V_F` (за сталого `V_F` й нульового входу). Handout наводить приклад: п’ять послідовних AND по 0,7 В дають на виході 3,5 В, що далеко від будь-якого розпізнаваного логічного нуля.[^utah-cs6710-diode-logic] У діодного OR аналогічно на кожному каскаді втрачається `V_F` високого рівня (див. qid:emb-elee-0147).

Виправити це самими діодами й резисторами не вдасться: у схемі немає активного елемента, який повернув би сигнал до напруги живлення чи землі. За handout, підвищення напруги живлення лише зсуває діапазони рівнів і збільшує потужність, не знімаючи обмеження на кількість каскадів; інвертор із самих діодів і резисторів побудувати неможливо, а ці проблеми розв’язують транзистори.[^utah-cs6710-diode-logic]

**Приклад (ідеалізований).** Візьмемо як наступний каскад SN74HC00 за `V_CC = 4.5 V`: `V_IL(max) = 1.35 V`.[^ti-hc00] Для кремнієвих діодів `V_F = 0.7 V` ланцюжок із двох AND уже дає `2*0.7 = 1.4 V > 1.35 V`, тобто нуль не гарантовано розпізнається. Для Шотткі з `V_F = 0.3 V` чотири каскади дають `4*0.3 = 1.2 V < 1.35 V`, а п’ятий – `1.5 V > 1.35 V`. Отже, Шотткі подовжує допустимий ланцюжок, але не робить його необмеженим. Це спрощена оцінка: реальне `V_F` залежить від струму (для BAT54 максимум зростає від 0,24 В за 0,1 мА до 0,8 В за 100 мА).[^vishay-bat54]

Діод Шотткі обирають через менше пряме падіння,[^nexperia-diode-handbook] яке зменшує втрату на кожному каскаді й збільшує запас до порога. Проте менше `V_F` пов’язане компромісом зі струмом витоку, тож параметри слід звіряти з datasheet.[^nexperia-diode-handbook]

**Типові помилки:**

- Вважати, що Шотткі робить діодну логіку придатною для довгих ланцюжків: вона лише збільшує допустиму довжину.
- Брати для всіх діодів `V_F = 0.7 V` і не враховувати залежність від струму та типу діода.[^vishay-bat54]
- Перевіряти лише логічний нуль у AND-ланцюжках і забувати про втрату високого рівня в OR-ланцюжках.

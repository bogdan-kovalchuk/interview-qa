---
id: emb-elee-0148
title: "Діодний AND: `V_CC` = 5 В, підтягування 10 кОм, вхід 0 В, `V_F` ≈ 0,3 В (Шотткі). Які рівень виходу і струм?"
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
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
  - source_id: nexperia-diode-handbook
    title: "Nexperia: Diode Application Handbook (Design Engineer’s Guide), 2022"
    url: https://assets.nexperia.com/documents/brochure/Nexperia_document_book_DiodeApplicationHandbook_2022.pdf
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
  - source_id: vishay-bat54
    title: "Vishay: BAT54, BAT54A, BAT54C, BAT54S small signal Schottky diodes (datasheet)"
    url: https://www.vishay.com/docs/86410/bat54_bat54a_bat54c_bat54s.pdf
  - source_id: ti-hc00
    title: "TI: SN74HC00, SN54HC00 quadruple 2-input NAND gates (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

Вихід ≈ `V_in + V_F = 0 + 0.3 = 0.3 V`, а струм `I = (5 - 0.3)/10000 ≈ 0.47 mA` (без навантаження на виході). Цей струм тече від живлення через резистор і діод у вхід, тому його має поглинути драйвер входу, що утримує логічний нуль.[^nexperia-diode-handbook][^utah-cs6710-diode-logic]

## Detailed explanation

Коли вхід діодного AND заземлено, діод між виходом і входом відкривається, і вихідний вузол сідає на рівень входу плюс пряме падіння діода: `V_out = V_in + V_F`.[^nexperia-diode-handbook][^utah-cs6710-diode-logic] Для `V_in = 0 V` і `V_F ≈ 0.3 V` це дає `0.3 V`. Усю решту напруги живлення бере на себе підтягувальний резистор, тож струм визначає закон Ома: `I = (V_CC - V_out)/R = (5 - 0.3)/10000 = 0.47 mA`. На резисторі при цьому розсіюється `P = 0.47 mA * 4.7 V ≈ 2.2 mW`.

Значення `V_F ≈ 0.3 V` для діода Шотткі правдоподібне, але воно залежить від струму й типу діода. Наприклад, для BAT54 максимальне `V_F` – 0,24 В за 0,1 мА і 0,32 В за 1 мА, тож за 0,47 мА воно не перевищує 0,32 В.[^vishay-bat54] Для кремнієвого діода в простій моделі падіння 0,7 В:[^libretexts-fiore-diode-models] тоді вихід був би `0.7 V`, а струм `(5 - 0.7)/10000 = 0.43 mA`. Різниця в струмі невелика, а рівень виходу відрізняється більш ніж удвічі, і саме це виграє Шотткі.

Є ще три застереження. По-перше, `0 V` на вході – ідеалізація: якщо драйвер входу утримує нуль із власним `V_OL`, то вихід дорівнює `V_OL + V_F`, а не просто `V_F`. По-друге, струм `0.47 mA` тече в драйвер входу, і той має його поглинути. По-третє, важливо, чи є отриманий рівень коректним логічним нулем для наступного каскаду. Для SN74HC00 за `V_CC = 4.5 V` вхідний низький рівень не вище `1.35 V`, тому `0.3 V` і навіть `0.7 V` проходять, але таблиця не охоплює 5 В і не застосовується до інших родин.[^ti-hc00]

**Типові помилки:**

- Вважати вихід нулем: він вищий за низький вхід на `V_F`.
- Забути, що струм підтягування тече у вхід, а не «в нікуди».
- Підставити для діода Шотткі 0,7 В, а для кремнієвого – 0,3 В.
- Не врахувати навантаження на виході: воно змінює струм і рівень.

---
id: emb-elee-0238
title: "Чи відтворюють прості резисторно-транзисторні вентилі промислову TTL?"
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
  - source_id: ti-sn74ls00
    title: "TI SDLS025D: SNx400, SNx4LS00, SNx4S00 quadruple 2-input NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls00.pdf
  - source_id: adi-ttl-lab
    title: "Analog Devices Wiki: TTL inverter and NAND gate activity for ADALM2000"
    url: https://wiki.analog.com/university/courses/electronics/electronics-lab-27
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
---

## Short answer

Ні. Логічна функція та сама. Серії SN74 мають багатоемітерні входи[^ti-sn74ls00], а TTL – вихід totem-pole[^adi-ttl-lab], тоді як RTL-вентиль має резистор pull-up.[^utah-cs6710-diode-logic] Тому гарантовані рівні й навантаження не збігаються, і сумісність перевіряють за datasheet.

## Detailed explanation

Пастка в тому, що логічна таблиця однакова, а електрика ні. RTL-вентиль має резистор від виходу до плюса і транзистори, що тягнуть вихід до землі. Високий рівень задає лише резистор, тому вихід слабо тягне вгору. TTL має вихід totem-pole: верхній транзистор активно тягне вихід до високого рівня, а нижній – до низького. Тому TTL-вихід здатен і джерелити, і стікати струм.[^adi-ttl-lab]

Гарантії TTL задано цифрами в datasheet: `VIH,min = 2 V`, `VIL,max = 0.8 V`, `VOH,min = 2.4 V` при струмі 0,4 мА і `VOL,max = 0.4 V` при 16 мА.[^ti-sn74ls00] Це зобов’язання виробника для конкретних умов. RTL-вентиль з довільними резисторами таких гарантій сам по собі не має: його `VOL` залежить від насичення транзистора, а `VOH` від падіння на резисторі, тож рівні треба рахувати для кожного навантаження.

Входи серій SN74 і SN74S – багатоемітерні транзистори, і datasheet окремо застерігає: напруга понад 5,5 В на таких входах пробиває перехід база–емітер.[^ti-sn74ls00] Тому однакова таблиця істинності не означає сумісності: вхідний струм, допустима напруга входу та вихідні рівні в цих схемах різні.

**Типові помилки:**

- Вважати, що однакова таблиця істинності означає сумісність: логічна функція не гарантує рівнів, навантаження чи швидкості.
- Подавати напругу понад 5,5 В на входи серій SN74 і SN74S, що пробиває їхній багатоемітерний вхід.[^ti-sn74ls00]
- Вважати RTL-вихід придатним замість TTL-виходу без розрахунку: TTL-вихід гарантує `VOL ≤ 0.4 V` при `IOL` до 16 мА, а RTL такої гарантії не має.[^ti-sn74ls00]

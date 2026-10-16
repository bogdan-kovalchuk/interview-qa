---
id: emb-elintro-0007
title: Як визначити катод діода за корпусом?
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: vishay-diode
    title: "Vishay 1N4001-1N4007 rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---

## Short answer

У поширених axial rectifier diodes смуга біля одного кінця позначає cathode; інший кінець – anode. Це convention конкретного типу корпусу, а не правило для всіх diode packages, тому marking і pinout слід звіряти з datasheet. [^vishay-diode]

## Detailed explanation

Сім’я Vishay 1N4001-1N4007 у корпусі DO-41 явно задає color band для cathode. Для такого компонента смуга визначає terminal незалежно від повороту корпусу. Не визначайте diode terminal за припущеним кольором самого виводу. [^vishay-diode]

Package marking і schematic symbol розв’язують різні задачі: позначка корпусу знаходить фізичний terminal; символ показує його електричну роль. Conventional forward current протікає від anode до cathode за forward bias. Смуга не означає, що струм входить саме в цей кінець.

Для SMD devices, multi-diode packages і LEDs використовуйте pinout точного компонента замість перенесення axial правила. Diode test мультиметра допомагає перевірити простий ізольований junction, але паралельні шляхи в зібраному колі можуть вплинути на показ. Package drawing лишається орієнтиром для assembly orientation.

---
id: emb-elintro-0225
title: "Що означає `common emitter` у схемі NPN-ключа?"
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
  - source_id: aac-common-emitter
    title: "All About Circuits: The Common-emitter Amplifier"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/common-emitter-amplifier/
---

## Short answer

У конфігурації `common emitter` вхідне коло бази й вихідне коло колектора мають емітер за спільну опорну точку; у типовому NPN-ключі її з’єднують із `GND`. За колекторного навантаження до живлення вихід інвертується: провідний транзистор дає низький рівень колектора.[^aac-common-emitter]

## Detailed explanation

Назва `common emitter` описує спосіб під’єднання: емітер є спільним вузлом для вхідного кола бази та вихідного кола колектора. «Спільний» означає спільний електричний опорний вузол цих кіл, а не обов’язково землю в кожному можливому застосуванні. У простому NPN-ключі емітер зазвичай з’єднаний із `GND`, база отримує керувальний сигнал, а вихід знімають із колектора.[^aac-common-emitter]

Коли база не відкриває транзистор, `cutoff` робить шлях колектор–емітер майже розімкненим; колекторний резистор тоді підтягує вихід до живлення. Коли базовий струм достатній для насичення, транзистор проводить, колектор наближається до потенціалу емітера, і вихідний рівень падає. Отже, інверсія виникає через резистивне навантаження колектора та поведінку транзистора, а не просто через назву конфігурації.[^aac-common-emitter]

**Приклад:** при емітері на землі та резисторі між `V_CC` і колектором низький рівень на базі залишає колектор високим, а високий рівень, що забезпечує достатній базовий струм, стягує колектор до низького рівня. Реальні напруги залежать від живлення, навантаження й характеристик транзистора.[^aac-common-emitter]

**Типова помилка:** вважати `common emitter` синонімом «емітер завжди під’єднаний до землі» або гарантією інверсії за будь-якого навантаження. Знайдіть спільний вузол на схемі й окремо простежте, як навантаження формує вихідну напругу.[^aac-common-emitter]

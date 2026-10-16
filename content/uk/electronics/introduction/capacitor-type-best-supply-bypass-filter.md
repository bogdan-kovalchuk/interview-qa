---
id: emb-elintro-0132
title: "Який тип конденсатора найкраще підходить для bypass-фільтру на живленні?"
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
  - source_id: analog-devices-an140-capacitor-selection
    title: "Analog Devices, AN-140: Basic Concepts of Linear Regulator and Switching Mode Power Supplies"
    url: https://www.analog.com/en/resources/app-notes/an-140.html
---

## Short answer

Для локального високочастотного bypass зазвичай обирають MLCC через малі ESR та ESL. Для bulk-фільтрації чи значного ripple current можуть додати електролітичний конденсатор; тип і номінал залежать від вимог схеми, робочої частоти та datasheet мікросхеми.[^analog-devices-an140-capacitor-selection] У керамічного конденсатора перевіряють ефективну ємність за робочої напруги.[^analog-devices-an140-capacitor-selection]

## Detailed explanation

Для високочастотного bypass біля мікросхеми зазвичай обирають MLCC (multilayer ceramic capacitor): він компактний і має низькі ESR та ESL, що допомагає подавати короткі імпульси струму й зменшувати високочастотний імпеданс живлення.[^analog-devices-an140-capacitor-selection]

Однак «найкращий тип» залежить від функції конденсатора. У buck-конвертері керамічний конденсатор може працювати паралельно з алюмінієвим електролітичним: вибір враховує RMS ripple current, потрібну ємність, навантаження та робочі частоти. Для кожної конкретної мікросхеми також перевіряють рекомендовані номінали й вимоги до стабільності.[^analog-devices-an140-capacitor-selection]

Номінал на корпусі керамічного конденсатора не завжди дорівнює його ефективній ємності під напругою. Діелектрики на кшталт X5R або X7R можуть втрачати частину ємності через DC bias і температуру, тому треба перевірити графік конкретного компонента в діапазоні робочих напруг.[^analog-devices-an140-capacitor-selection]

**Типова помилка:** поставити один і той самий конденсатор далеко від навантаження й очікувати, що він прибере всі пульсації. Для локального bypass важливе коротке з’єднання між виводом живлення та ground; довгі доріжки додають паразитну індуктивність. Приклад конкретного рішення для buck-живлення – паралельні MLCC та електролітичний конденсатор на вході, якщо цього вимагають струм пульсацій і схема.[^analog-devices-an140-capacitor-selection]

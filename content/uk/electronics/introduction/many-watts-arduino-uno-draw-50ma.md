---
id: emb-elintro-0049
title: "Скільки ватів споживає Arduino Uno (5В, ~50мА)?"
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
  - source_id: aac-electric-power
    title: "All About Circuits: Calculating Electric Power"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/calculating-electric-power/
---

## Short answer

Якщо плата працює від `5 V` і споживає `50 mA`, її вхідна потужність дорівнює `P = V*I = 5 V*0.050 A = 0.25 W`. Це розрахунок за заданим струмом, а не універсальне споживання кожної конфігурації Uno.[^aac-electric-power]

## Detailed explanation

Електрична потужність описує швидкість передавання або перетворення енергії. Для кола постійного струму її обчислюють як добуток напруги на струм: `P = V*I`. Спершу струм треба подати в амперах: `50 mA = 0.050 A`; отже за напруги `5 V` виходить `0.25 W`.[^aac-electric-power]

Це значення стосується повного струму, що надходить від джерела за вказаних умов. На реальне споживання Arduino Uno впливають підключені модулі, навантаження GPIO, USB-пристрої та спосіб живлення. Тому `50 mA` у формулюванні питання слід читати як задане припущення для вправи, а не як фіксовану характеристику всіх плат у будь-якому режимі. Якщо струм змінюється з часом, добуток миттєвих `V` та `I` також змінюється; наведений простий результат описує сталий режим.[^aac-electric-power]

**Приклад перерахунку одиниць:**

```text
50 mA = 50/1000 A = 0.050 A
P = 5 V * 0.050 A = 0.25 W
```

Поширена помилка – перемножити `5` на `50` і приписати результату одиницю ват. Такий розрахунок забув перетворити міліампери в ампери й завищив відповідь у тисячу разів. Вхідна потужність також не дорівнює автоматично теплу, яке виділяється на одному компоненті: вона розподіляється між платою та підключеними навантаженнями, а стабілізатор може перетворювати частину енергії на тепло.[^aac-electric-power]

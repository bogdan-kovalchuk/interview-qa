---
id: emb-elintro-0133
title: "Як читати тризначний код конденсатора, наприклад `104`?"
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
  - source_id: kemet-capacitor-picofarad-code
    title: "KEMET, Ceramic Molded/Axial & Radial – MIL-PRF-20 datasheet"
    url: https://content.kemet.com/datasheets/F3101_MIL-PRF-20.pdf
---

## Short answer

У поширеному тризначному коді перші дві цифри задають значущі цифри в пікофарадах, а третя – кількість нулів після них. Тому `104` означає `10*10^4 pF` = `100000 pF` = `100 nF` = `0.1 µF`.[^kemet-capacitor-picofarad-code]

## Detailed explanation

Тризначний код є скороченим записом номінальної ємності, зазвичай у пікофарадах. Перші дві позиції утворюють число, а третя задає степінь десяти, на який це число множать. Наприклад, у `104` значущі цифри – `10`, а суфікс `4` означає чотири нулі: виходить `100000 pF`.[^kemet-capacitor-picofarad-code]

Щоб перейти до зручнішої одиниці, пам’ятаймо, що `1000 pF = 1 nF`, а `1000 nF = 1 µF`. Отже, `100000 pF` дорівнює `100 nF`, тобто `0.1 µF`. Це номінал ємності, а не допуск, напруга чи дата виробництва; інші символи поруч на корпусі можуть кодувати окремі параметри.[^kemet-capacitor-picofarad-code]

Для такого коду цифра `9` має спеціальне значення: вона задає ділення на десять, а не дев’ять нулів. Саме тому розшифрування треба прив’язувати до конкретної системи маркування, а не сприймати будь-яку групу з трьох символів як цей формат. У таблицях виробника код і номінал слід звірити з серією деталі.[^kemet-capacitor-picofarad-code]

Приклад для `472`: значуща частина дорівнює `47`, третя цифра задає два нулі, отже отримуємо `4700 pF`, або `4.7 nF`. Зворотна перевірка проста: вирази в pF і nF мають відрізнятися у тисячу разів.

**Типова помилка:** прочитати `104` як `10 nF`, забувши, що код рахує в pF. Також не слід робити висновок про допустиму напругу з цього коду – її маркують окремо або знаходять за повним номером компонента в datasheet.[^kemet-capacitor-picofarad-code]

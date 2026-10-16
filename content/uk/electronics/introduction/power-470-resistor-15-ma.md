---
id: emb-elintro-0094
title: "Яка потужність на резисторі 470 Ω при струмі 15 mA?"
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
  - source_id: aac-resistor-power-dissipation
    title: "All About Circuits: Intro Lab - Resistor Power Dissipation"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-2/power-dissipation/
---

## Short answer

За резистивної моделі `P = I^2*R = (0.015 A)^2*470 ohm = 0.10575 W`, тобто приблизно `0.106 W`. Номінал резистора має бути вищим за це значення з урахуванням температури, монтажу та умов дерейтінгу; 0.25 W є поширеним мінімальним номіналом за придатних умов, а 0.5 W дає більший запас.[^aac-resistor-power-dissipation]

## Detailed explanation

Якщо струм через резистор відомий, його розсіювану потужність можна знайти із закону Джоуля `P = I^2*R`. Формула випливає з `P = V*I` та закону Ома `V = I*R`, тож вона передбачає резистивний елемент із відповідними значеннями напруги, струму й опору. Для незмінного опору подвоєння струму збільшує потужність учетверо, тому помилка в струмі особливо сильно впливає на результат.[^aac-resistor-power-dissipation]

У цьому прикладі 15 mA треба перевести в ампери: `0.015 A`. Отже, `P = (0.015 A)^2*470 ohm = 0.10575 W`, приблизно 106 mW. За ідеального резистора це електрична потужність, що переважно перетворюється на тепло. Такий розрахунок не враховує допуск резистора, зміну його опору з температурою чи імпульсні режими.[^aac-resistor-power-dissipation]

Номінальна потужність на корпусі – це допустиме розсіювання за умов, визначених виробником, а не потужність, яку резистор обов’язково споживає. Тому номінал 0.25 W перевищує обчислені 0.106 W за умови, що паспортні температурні та монтажні обмеження виконано. Для гарячого середовища, закритого корпусу або слабкого охолодження виробник може вимагати знизити допустиме навантаження; вибір 0.5 W дає запас, але сам по собі не замінює перевірку умов.[^aac-resistor-power-dissipation]

**Типові помилки:**
- Підставляти `15` замість `0.015` ампера: результат потужності буде завищений у мільйон разів.
- Вважати 0.25 W гарантовано безпечним у будь-якому корпусі та за будь-якої температури; перевіряйте графік дерейтінгу й теплові умови конкретного компонента.[^aac-resistor-power-dissipation]

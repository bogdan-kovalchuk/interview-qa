---
id: emb-elintro-0003
title: Яка функція резистора у колі?
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
  - source_id: aac-resistors
    title: "All About Circuits: Resistors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
---

## Short answer

Резистор пов’язує напругу та струм через опір: для ідеального ohmic resistor `V = I*R`. Він обмежує струм, утворює voltage divider та розсіює електричну енергію як тепло в межах допустимої потужності. [^aac-resistors]

## Detailed explanation

Опір не задає фіксованого падіння напруги: падіння залежить від струму. І навпаки, за сталої прикладеної напруги більший опір дає менший струм. Резистор не споживає заряд; він перетворює електричну енергію на тепло. Для ідеальної резистивної моделі використовують `P = V*I = I²*R = V²/R`. [^aac-resistors]

У розрахунковому прикладі 5 V на 1 kΩ дають `I = 5/1000 = 5 mA` та `P = 25 mW`. Йдеться про напругу саме на резисторі, а не автоматично про всю напругу живлення, якщо послідовно є інші компоненти.

Для LED з припущеним forward drop 2 V від живлення 5 V послідовний резистор 220 Ω дає приблизно `(5-2)/220 = 13.6 mA`; його розсіювання – близько 41 mW. Це розрахунок моделі, а не універсальна схема LED: перевірте фактичну forward voltage, допустимий струм LED, tolerance і rated power резистора. Реальний опір також може змінюватися з температурою.

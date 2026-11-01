---
id: emb-elintro-0097
title: "Why choose a resistor with a power rating margin?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-resistor-power
    title: "Resistors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
---

## Short answer

A resistor's power rating must not be lower than the calculated power dissipation under actual mounting conditions. There is no universal "always use `2×`" rule: you check temperature derating in the datasheet and account for ambient temperature and cooling.[^aac-resistor-power]

## Detailed explanation

A resistor's power rating is the heat dissipation limit specified by the manufacturer under specific conditions, not guaranteed power under any mounting arrangement.[^aac-resistor-power] Electrical power converts into heat within the resistive element; for direct current, it can be calculated as `P = I^2*R` or `P = V^2/R`, where `V` is the voltage across the resistor itself.[^aac-resistor-power]

Comparing only against the number on the package is insufficient. The datasheet may specify a reduction in allowable power as ambient temperature rises, the component maximum temperature, PCB mounting conditions, and separate limits for pulsed operation. For short pulses, average power does not always reflect the risk: pulse energy and the thermal mass of the resistor also matter. Therefore, the required margin is determined by the specific resistor type, temperature, ventilation, circuit tolerances, and load profile, rather than a single multiplier for all designs.[^aac-resistor-power]

Worked example: a constant current of `33 mA` flows through a `100 Ω` resistor. An ideal estimate gives `P = I^2*R = 0.109 W`, or approximately `0.11 W`. This does not yet prove that a `0.125 W` rating is sufficient: at elevated temperatures, its allowable power may be derated. You must check the derating curve in the datasheet and select the nearest rating permitted under the given conditions.[^aac-resistor-power]

**Common mistake:** treating the popular `2×` margin rule as a standard requirement. It can serve as a practical starting rule of thumb in a particular design, but it does not replace checking the datasheet, pulse withstand capability, and thermal operating conditions.

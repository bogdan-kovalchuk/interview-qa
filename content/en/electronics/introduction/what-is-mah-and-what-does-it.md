---
id: emb-elintro-0055
title: "What is mAh and what does it mean?"
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
  - source_id: analog-ampere-hour
    title: "Analog Devices: Ampere-hour"
    url: https://www.analog.com/en/resources/glossary/amp-hour-ampere-ah-mah.html
  - source_id: doe-battery-capacity-rate
    title: "U.S. Department of Energy: Primer on Lead-Acid Storage Batteries"
    url: https://www.energy.gov/documents/doe-hdbk-1084-95
---

## Short answer

Milliampere-hour (mAh) is a unit of electric charge used to designate battery capacity: `Q = I*t`.[^analog-ampere-hour] Theoretically 2400 mAh corresponds to 240 mA over 10 hours, but actual operating time depends on discharge current and battery operating conditions.[^doe-battery-capacity-rate]

## Detailed explanation

mAh stands for milliampere-hour: the product of current in milliamperes and time in hours. It is a unit of quantity of electric charge, not voltage and not energy. One ampere-hour equals 1000 mAh; in SI, one ampere-hour corresponds to 3600 coulombs of charge.[^analog-ampere-hour]

If a battery delivers a constant current, a simple approximation for charge takes the form `Q = I*t`. For example, for a rating of 2400 mAh and a current of 240 mA, an idealized calculation yields `t = Q/I = 2400 mAh/240 mA = 10 h`. This is an estimate based on the assumption of constant current and availability of the full rated capacity, rather than a guarantee of runtime until device shutdown.[^analog-ampere-hour]

Real capacity depends on battery chemistry, temperature, discharge current, cut-off voltage, and other conditions. For some batteries, higher current means less accessible capacity, and the rated value in datasheets is stated alongside test conditions. Furthermore, mAh does not allow comparing the energy stored in batteries with different voltages without accounting for voltage: energy is approximately related to the product of charge and voltage.[^doe-battery-capacity-rate]

Example: an idealized 2400 mAh can be divided by 120 mA to yield 20 hours, or by 480 mA to yield 5 hours. In an actual product, these results may differ because current can vary, and accessible capacity depends on the rate of discharge and shutdown threshold. A common mistake is considering mAh a direct measure of energy or promised runtime.[^analog-ampere-hour][^doe-battery-capacity-rate]

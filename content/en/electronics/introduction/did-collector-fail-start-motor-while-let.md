---
id: emb-elintro-0229
title: "Why did 100 Ω in the collector fail to start the motor while 10 Ω let it start?"
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
  - source_id: pololu-motor-stall
    title: "Pololu Jrk G2 Motor Controller User’s Guide: Choosing the motor, power supply, and Jrk"
    url: https://www.pololu.com/docs/0J73/4.1
---

## Short answer

With an idealized 5 V drop, a 100 Ω resistor yields an upper-bound current of 50 mA, while 10 Ω gives 0.5 A by Ohm's law. Actual current is lower and depends on winding resistance, the transistor, and the power source; a smaller resistor can increase starting torque, but whether it is sufficient depends on the specific motor.[^aac-direct-current]

## Detailed explanation

A resistor in the collector branch limits current, but calculating solely from source voltage yields an upper bound. For 5 V and 100 Ω, the idealized value is `5 V / 100 Ω = 50 mA`; for 10 Ω it is `5 V / 10 Ω = 0.5 A`. In a real circuit, part of the voltage drops across the motor winding, transistor, wiring, and power supply, so the actual current is lower and changes during acceleration.[^aac-direct-current]

At start, the motor is not yet spinning, so back-EMF is practically zero. Current is then limited primarily by winding resistance and the rest of the circuit, and can be substantially higher than motor running current after spin-up. If the series resistor is too large, available starting current and torque may not suffice to overcome static friction and load. A smaller resistor can assist startup, but increases current and power dissipation in both resistor and transistor.[^aac-direct-current]

Estimation example for an idealized 5 V source and 10 Ω resistor: even if the entire voltage drop falls across the resistor, its power dissipation would be `P = V²/R = 25/10 = 2.5 W`. This is a bounding estimate; the actual value depends on voltage drops, but a standard low-power resistor cannot automatically be assumed adequate. Similarly, 100 Ω with that same idealized voltage drop yields `0.25 W`. The resistor power rating and component limits must be verified against startup conditions.[^aac-direct-current]

Therefore, the description "100 Ω failed to start, 10 Ω allowed it to start" can be accepted only for a specific educational workbench with its specific motor, source, and transistor. It is not a universal pair of values. Selection requires knowing winding resistance or stall current at supply voltage, saturated transistor drop, maximum source current, and required torque. A common mistake is quoting `0.5 A` as a guaranteed current while ignoring the motor and transistor in that same loop.[^aac-direct-current]

---
id: emb-elintro-0057
title: "What is a battery's internal resistance and how does it affect voltage?"
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
  - source_id: libretexts-real-batteries
    title: "Physics LibreTexts: 6.5 Real Batteries"
    url: https://phys.libretexts.org/Courses/Kettering_University/Electricity_and_Magnetism_with_Applications_to_Amateur_Radio_and_Wireless_Technology/06:_Direct-Current_(DC)_Resistor_Circuits/6.05:_Real_Batteries
---

## Short answer

Internal resistance models losses inside a battery: during discharge, the terminal voltage is approximately `V_term = E - I*r`. The greater the current or internal resistance, the larger the internal voltage drop; specific values depend on the battery and operating conditions.[^libretexts-real-batteries]

## Detailed explanation

Internal resistance is a convenient model of the combined electrical losses inside a real power source. In a simple equivalent circuit, a battery is represented as an ideal source of electromotive force `E` in series with a resistance `r`. When an external circuit draws a current `I`, part of the voltage is dropped inside the battery, leaving approximately `V_term = E - I*r` at its terminals.[^libretexts-real-batteries]

With no load connected, the current is nearly zero, so the `I*r` drop is small and the measured voltage approaches the open-circuit voltage. When the load draws more current, the drop across the internal resistance increases. Part of the chemical energy is converted into heat inside the cell; with significant internal resistance, this also reduces the voltage and power available to the load.[^libretexts-real-batteries]

For example, if an equivalent source has `E = 1.5 V` and during operation a current of `I = 0.1 A` flows through it, then with `r = 2 Ω` the model predicts an internal drop of `0.1*2 = 0.2 V` and a terminal voltage of about 1.3 V. This is only a model example, not a universal value for an AA cell. Real batteries are not fixed resistors: their behavior depends on chemistry, temperature, state of charge, age, and load duration.[^libretexts-real-batteries]

**Common mistake:** assuming that a battery rated at 1.5 V always maintains exactly 1.5 V at its terminals. The nominal voltage does not eliminate voltage sag under load; evaluate it for the specific current and conditions.

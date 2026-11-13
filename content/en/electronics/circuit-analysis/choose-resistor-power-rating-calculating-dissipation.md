---
id: emb-elcirc-0009
title: "How do you choose a resistor's power rating after calculating dissipation?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-resistor-power
    title: "All About Circuits: Resistors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
  - source_id: vishay-resistor-derating
    title: "Vishay Sfernice: Power Dissipation Considerations in High Precision Thin Film Chips Resistors and Arrays"
    url: https://www.vishay.com/doc/?53047=
---

## Short answer

Calculate power dissipation as `P = V*I`, or equivalently using `I` or `V` with resistance, and select a component rated above this value under expected thermal and cooling conditions.[^aac-resistor-power] There is no universal `2×` safety margin rule; consult the manufacturer derating curve in the datasheet for high ambient temperatures.[^vishay-resistor-derating]

## Detailed explanation

A resistor power rating defines how much heat it can continuously dissipate under manufacturer-specified test conditions without exceeding its maximum operating temperature. Electrical power dissipated in a resistor equals `P = V*I`; combining this with Ohm's law yields `P = I^2*R` and `P = V^2/R`. In these equations, `V` and `I` must refer strictly to the voltage dropped across the resistor and the current flowing through it.[^aac-resistor-power]

Once operating power dissipation is calculated, select a standard component rating that safely accommodates it under actual ambient temperature, board mounting, enclosure airflow, and specified cooling conditions. Datasheets include derating curves that reduce allowable power dissipation at elevated temperatures; therefore, a component labeled as a "0.25 W resistor" does not guarantee continuous `0.25 W` dissipation in any package geometry or thermal environment.[^vishay-resistor-derating]

Example: a `100 Ω` resistor with `5 V` across it dissipates `P = V^2/R = 25/100 = 0.25 W`. A `0.25 W` rated resistor would operate with zero safety margin against elevated temperatures or supply tolerance; selecting the next higher standard rating is advisable, with the exact margin dictated by datasheet derating curves and reliability guidelines. In pulse-load applications, verify pulse-energy handling capabilities, and in high-voltage designs, verify the maximum working voltage rating, as voltage breakdown limits may be reached before power dissipation limits.[^aac-resistor-power] [^vishay-resistor-derating]

**Common mistakes:**

- Assuming a mandatory "2x power rating" rule applies universally to every resistor application.
- Comparing the power rating against a calculation that does not use the specific voltage drop and current for that component.
- Ignoring temperature derating, pulse energy ratings, or maximum working voltage limits.[^vishay-resistor-derating]

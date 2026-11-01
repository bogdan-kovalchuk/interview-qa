---
id: emb-elintro-0101
title: "What is the formula for the total resistance of series resistors?"
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
  - source_id: aac-series-circuits
    title: "All About Circuits: Series Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-series-circuits/
---

## Short answer

The equivalent resistance of series-connected resistors equals the sum of their resistances: `R_total = R_1 + R_2 + ... + R_n`. The same current flows through all elements of such a circuit because there is only one path for it.[^aac-series-circuits]

## Detailed explanation

Equivalent resistance replaces several series-connected resistors with a single resistor that has the same relationship between total voltage and circuit current. In a series connection, the output of one resistor is connected to the input of the next, so the current has no alternative branch. By Kirchhoff's law, the source voltage equals the sum of the voltage drops across the elements; since the current is identical, Ohm's law for each resistor gives `V_total = I*R_1 + I*R_2 + ...`. Factoring out the common current shows that `R_total = R_1 + R_2 + ... + R_n`.[^aac-series-circuits]

For example, if you connect 100 Ω and 330 Ω resistors in series, the equivalent resistance will be `R_total = 100 Ω + 330 Ω = 430 Ω`. With a 3 V source, this corresponds to a current of `I = 3 V/430 Ω ≈ 6.98 mA` for an ideal source and nominal resistor values. The voltage drop across each element is different: a larger resistance at the same current has a larger drop, and the sum of the drops equals the source voltage.[^aac-series-circuits]

**Common mistakes:**
- Do not apply the sum of resistances to a parallel connection: there, the resistors share two nodes and the current branches.
- Do not add nominal values if there are branches or other connections between elements that create an additional path. Identify the circuit topology first.
- The formula describes a basic model; wire resistance, component tolerances, and heating can affect the measured result.[^aac-series-circuits]

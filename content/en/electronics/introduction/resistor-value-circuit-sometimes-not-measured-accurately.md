---
id: emb-elintro-0276
title: "Why can a resistor's value in a circuit sometimes not be measured accurately with a multimeter?"
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
  - source_id: fluke-in-circuit-resistance
    title: "Fluke: How to Measure Resistance with a Digital Multimeter"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-measure-resistance
---

## Short answer

Parallel circuit paths on the PCB alter the measurement, causing the multimeter to report the equivalent network resistance across the probes rather than the value of the isolated resistor. For an accurate reading, one terminal must often be desoldered or isolated from the rest of the circuit.[^fluke-in-circuit-resistance]

## Detailed explanation

The resistance of a component inside an assembled circuit cannot always be measured directly because an ohmmeter measures the equivalent resistance of all conductive paths existing between the test probes.[^fluke-in-circuit-resistance]

In resistance measurement mode, a multimeter injects a small test current and calculates resistance from the resulting voltage drop. If another resistive path is wired in parallel with the resistor under test, the measurement current splits among the branches. For example, two `10 kΩ` resistors in parallel yield an equivalent resistance of `5 kΩ`; when probing the board, the meter measures this lower parallel combination rather than the `10 kΩ` value of the individual component.[^fluke-in-circuit-resistance]

More complex circuits often contain diodes, transistors, capacitors, and active ICs. The multimeter's test voltage can forward-bias a semiconductor PN junction, causing the reading to vary with probe polarity, measurement range, and the state of surrounding circuitry. An unexpected reading does not necessarily indicate a defective resistor. Before probing, always de-energize the circuit and discharge all capacitors, as residual voltage can damage the meter or corrupt measurements.[^fluke-in-circuit-resistance]

To verify an individual resistor accurately, consult the schematic and isolate at least one of its terminals from the board. Then measure resistance across its leads and compare the reading to its nominal rating, accounting for component tolerance. Do not confuse in-circuit resistance measurement with the continuity buzzer function: an audible tone merely indicates that loop resistance is below the meter's threshold, rather than confirming a specific component value.[^fluke-in-circuit-resistance]

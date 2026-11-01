---
id: emb-elintro-0128
title: "How should you choose a resistor power rating with a safety margin?"
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
  - source_id: ti-resistor-derating
    title: "Texas Instruments: SBAA460, Design Considerations for Isolated Current Sensing"
    url: https://www.ti.com/document-viewer/lit/html/SBAA460
---

## Short answer

First calculate the maximum power of the resistor, for example using `P = I^2*R` or `P = V^2/R`, for the worst-case normal operating condition.[^aac-direct-current] Then select the rating from the datasheet taking into account temperature derating, mounting, and cooling; there is no universal rule to "take exactly twice as much."[^ti-resistor-derating]

## Detailed explanation

A resistor's power rating is a limit for manufacturer-specified conditions, not a guaranteed power under any mounting conditions. First estimate the highest power the circuit dissipates in the resistor during normal operating conditions. For a resistor, it can be found via `P = I^2*R` or `P = V^2/R`, using the current through it or the voltage across it.[^aac-direct-current]

After calculating, check the result against the datasheet for the specific series. The power rating can decrease as ambient temperature rises, and the component temperature depends on copper trace area, package, airflow, and nearby heat sources. For shunt resistors, Texas Instruments specifically advises accounting for self-heating, checking the derating curve in the datasheet, and evaluating temperature under maximum normal load.[^ti-resistor-derating]

A practical margin is useful because calculations may not account for operating-condition variation, temperature, or short-term overload. However, a relationship like "the rating must be twice the calculated power" is an initial heuristic, not a general rule for all packages and temperatures. Make sure that after applying derating, the curve still allows the calculated load, and that permissible short-term overload is not exceeded.[^ti-resistor-derating]

Worked example:

```text
I = 0.10 A, R = 25 Ω
P = I^2*R = 0.10^2*25 = 0.25 W
```

This 0.25 W is the load in the given example, not an automatic recommendation for the rating. Next, select a specific resistor and verify its power derating curve and the board's thermal conditions. Resistors with the same power rating can have different packages and mounting conditions, so the marking alone does not prove the safety of a specific operating mode.[^ti-resistor-derating]

**Common mistakes:**

- Applying a multiplier of 2 as a mandatory rule without checking the datasheet.
- Calculating only the average operating condition and missing maximum current or short-term overload.
- Failing to account for high temperature or poor heat dissipation reducing the allowable load.[^ti-resistor-derating]

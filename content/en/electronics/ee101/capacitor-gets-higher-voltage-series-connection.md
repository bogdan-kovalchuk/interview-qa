---
id: emb-elee-0027
title: "Which capacitor gets the higher voltage in a series connection?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-capacitors-series-parallel
    title: "All About Circuits textbook: Series and Parallel Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/series-and-parallel-capacitors/
  - source_id: ti-series-capacitor-voltage-balancing
    title: "Texas Instruments: Bulk capacitors for high bus voltage – connect in series"
    url: https://www.ti.com/content/dam/videos/external-videos/en-us/2/3816841626001/5575134803001.mp4/subassets/Very_high_Voltage_bias_BK_13-Sept_complete.pdf
---

## Short answer

For equal charge in an ideal steady state, the capacitor with the smaller capacitance develops the higher voltage because `V = Q/C`. During transients, distribution is determined by capacitances, but leakage spread and component tolerances can shift the actual voltage division; high-voltage strings require deliberate balancing circuits.[^aac-capacitors-series-parallel] [^ti-series-capacitor-voltage-balancing]

## Detailed explanation

In an initial ideal calculation, the higher voltage appears across the capacitor with the smaller capacitance when the series elements carry identical charge.[^aac-capacitors-series-parallel]

For each element, `V = Q/C`. For a fixed charge, decreasing `C` increases `V`, and the sum of the voltages across the capacitors equals the source voltage. For instance, a pair of 10 µF and 20 µF capacitors in a simple model divides voltage in a 2:1 ratio: the smaller capacitance receives two-thirds of the total voltage, while the larger receives one-third. This represents a capacitance-based distribution model during charging or for ideal elements, not a guarantee of reliable division in a real DC string.[^aac-capacitors-series-parallel]

After charging, real leakage currents can differ, and capacitances have tolerances. As a result, the voltage across an individual capacitor can rise beyond the simple estimate based on nominal capacitance. TI explicitly points to the need for balancing resistors in a series string of high-voltage bulk capacitors and notes that the balancing current must significantly exceed the leakage current.[^ti-series-capacitor-voltage-balancing] In a specific circuit, active balancing is also used if passive resistors fail to meet loss or accuracy requirements.[^ti-series-capacitor-voltage-balancing]

Example for a total voltage of 30 V:

```text
V_10uF = 30 V * 20/(10+20) = 20 V
V_20uF = 30 V * 10/(10+20) = 10 V
```

**Common mistake:** assuming that voltage divides proportionally to capacitance, or relying on nominal ratings as a guarantee of safe operation. In a real bank, the maximum voltage rating of each element must be verified taking into account tolerance, leakage, temperature, and transients.

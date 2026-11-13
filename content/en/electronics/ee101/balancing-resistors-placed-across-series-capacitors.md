---
id: emb-elee-0029
title: "Why are balancing resistors placed across each of the series capacitors?"
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
  - source_id: ti-series-capacitor-voltage-balancing
    title: "Texas Instruments: Bulk capacitors for high bus voltage – connect in series"
    url: https://www.ti.com/content/dam/videos/external-videos/en-us/2/3816841626001/5575134803001.mp4/subassets/Very_high_Voltage_bias_BK_13-Sept_complete.pdf
---

## Short answer

Balancing resistors placed across each series capacitor establish a controlled current path that mitigates differences in leakage currents and equalizes voltage distribution. Their resistance is not a universal value like 100 kΩ: balancing current must comfortably exceed expected leakage, and power losses and ratings must be verified for the specific circuit.[^ti-series-capacitor-voltage-balancing]

## Detailed explanation

A balancing resistor is connected in parallel with each capacitor in a series string to provide a controlled current path through each section.[^ti-series-capacitor-voltage-balancing]

In real components, leakage currents differ. Without additional paths, these differences can lead to an uneven steady-state voltage distribution: one capacitor receives more than its intended share and may exceed its rating. The resistor establishes a current that dominates leakage variations and forms a passive DC divider. In TI application literature for series-connected high-voltage bulk capacitors, it is explicitly stated that the balancing current must significantly exceed the leakage current; the resulting additional power losses are also noted.[^ti-series-capacitor-voltage-balancing]

The resistor value cannot be chosen by a single universal rule such as "100 kΩ". It depends on the maximum voltage per section, the worst-case expected leakage, the required balancing margin, and acceptable dissipation. For example, at 200 V across a 100 kΩ resistor, the current is 2 mA and the power is 0.4 W; a component with adequate voltage and power ratings must be selected. Such an example is not a component recommendation for every string: capacitor datasheet values and operating conditions must be taken into account.[^ti-series-capacitor-voltage-balancing]

Example loss estimation:

```text
I_R = V/R = 200 V/100 kΩ = 2 mA
P_R = V*I = 200 V*2 mA = 0.4 W
```

**Common mistake:** assuming that equal resistors alone guarantee equal voltage regardless of leakage, temperature, and component tolerances. In actual design, the worst-case imbalance is evaluated, and the balancing current and resistor power rating are selected with appropriate margins; for fast transients, separate verification of capacitive division or active balancing may be required.[^ti-series-capacitor-voltage-balancing]

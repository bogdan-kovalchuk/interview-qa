---
id: emb-elintro-0091
title: "Why have processor core supply voltages often decreased across generations?"
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
  - source_id: ti-cmos-power-consumption
    title: "Texas Instruments: CMOS Power Consumption and CPD Calculation"
    url: https://www.ti.com/lit/an/scaa035b/scaa035b.pdf
---

## Short answer

In `CMOS`, dynamic switching power is approximately `P = alpha*C*V^2*f`, where `alpha` represents switching activity. All else being equal, a lower voltage reduces this power component, but the achievable voltage depends on the specific processor and operating frequency.[^ti-cmos-power-consumption]

## Detailed explanation

Lowering the processor core supply voltage reduces the dynamic power required to charge and discharge capacitances of internal nodes during switching transitions. For CMOS, this component is frequently estimated as `P = alpha*C*V^2*f`: `C` is the effective switched capacitance, `V` is the supply voltage, `f` is the clock frequency, and `alpha` is the switching activity factor. With unchanged `C`, `f`, and `alpha`, halving the voltage reduces dynamic power alone to approximately one quarter.[^ti-cmos-power-consumption]

This does not imply that total power always drops strictly with the square of voltage. There is also static consumption, particularly leakage currents, and actual circuit activity and clock frequency can vary. Reducing voltage also diminishes signal margin and transistor switching speed; to maintain the target frequency, manufacturers coordinate the voltage with the process technology and the specific operating mode. Therefore, the 12 V, 5 V, 3.3 V, and 1.2 V mentioned in the question are merely examples of different power domains and process generations, rather than a universal supply sequence for every processor.[^ti-cmos-power-consumption]

Example: if the exact same logic circuit operates with unchanged capacitance, activity, and frequency, transitioning from 1.2 V to 0.9 V yields a dynamic power ratio of `(0.9/1.2)^2`, or approximately 0.56. This comparison applies strictly to the switching component in such a simplified model; it does not account for leakage, the power converter, or frequency adjustments.[^ti-cmos-power-consumption]

**Common mistakes:**
- Attributing an automatic increase in transistor density to lower voltage: density is dictated by the manufacturing process and layout, even though voltage scaling frequently accompanies these transitions.
- Applying the quadratic relationship to total power consumption without clarifying that it applies specifically to the dynamic component under otherwise constant parameters.[^ti-cmos-power-consumption]

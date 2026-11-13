---
id: emb-elee-0253
title: "How do the comparators and the DISCH pin of the 555 timer work?"
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
  - source_id: ti-ne555-datasheet
    title: "Texas Instruments: NE555 Precision Timers Datasheet (SLAS074)"
    url: https://www.ti.com/lit/ds/symlink/ne555.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

Two internal comparators compare input voltages against internal divider thresholds of ≈ 1/3 and 2/3 `V_CC`. A TRIG voltage below 1/3 `V_CC` sets the internal flip-flop and drives OUT HIGH; a THRES voltage above 2/3 `V_CC` resets the flip-flop, pulling OUT LOW and turning on DISCH to ground the discharge path. Driving RESET LOW overrides both inputs and forces the output LOW.[^udemy-electronics-course]

## Detailed explanation

The internal circuitry of the 555 timer IC is built around three key functional blocks: a precision resistive voltage divider, two analog comparators, and an output discharge transistor (DISCH pin).[^udemy-electronics-course][^ti-ne555-datasheet]

### Internal divider and threshold levels

Connected between the supply rail `V_CC` (pin 8) and ground GND (pin 1) is a series string of three precision 5 kΩ resistors.[^ti-ne555-datasheet] This divider establishes two fixed reference potentials:
- upper threshold: `V_ref_high = 2/3 * V_CC` (brought out externally as pin 5 – CONT);
- lower threshold: `V_ref_low = 1/3 * V_CC`.[^ti-ne555-datasheet][^art-of-electronics]

### Operating principle of the comparators

1. **Upper comparator (Threshold Comparator):**
   - Inverting input (-) is connected to the internal reference node `2/3 * V_CC`.
   - Non-inverting input (+) is brought out as pin 6 (THRES).
   - **Operating logic:** As long as the voltage at the THRES input is below `2/3 * V_CC`, the comparator output remains at logic 0. When the voltage on the external capacitor exceeds `2/3 * V_CC`, the comparator output switches abruptly to logic 1, asserting a signal to the reset input (R) of the internal RS flip-flop.[^ti-ne555-datasheet]

2. **Lower comparator (Trigger Comparator):**
   - Non-inverting input (+) is connected to the internal reference node `1/3 * V_CC`.
   - Inverting input (-) is brought out as pin 2 (TRIG).
   - **Operating logic:** As long as the voltage at the TRIG input exceeds `1/3 * V_CC`, the comparator output remains at 0. When the input signal drops below `1/3 * V_CC`, the comparator output transitions to 1 and pulses the set input (S) of the RS flip-flop.[^ti-ne555-datasheet]
   - **Priority:** The TRIG input in the bipolar 555 timer takes priority over THRES: if both inputs are active simultaneously, the timer output is driven HIGH.[^art-of-electronics]

### Role of the internal RS flip-flop and the RESET input

The RS flip-flop acts as a memory element holding circuit state between comparator transitions:
- Tripping by the lower comparator drives the non-inverting output (pin 3 – OUT) HIGH, while the inverted flip-flop output `Q_bar` transitions to 0.[^ti-ne555-datasheet]
- Tripping by the upper comparator resets the flip-flop: the OUT output drops LOW, and `Q_bar` transitions to 1.
- Asynchronous RESET input (pin 4, active-low): when the voltage drops below 0.7 V, it directly turns on an internal reset transistor, forcing the OUT output to 0 regardless of the voltages at the comparator inputs.[^ti-ne555-datasheet]

### How the DISCH discharge pin (pin 7) works

The DISCH (Discharge) pin is the open collector of an internal NPN transistor whose emitter is connected to ground (pin 1):[^ti-ne555-datasheet]
- The base of this transistor is driven by the inverted RS flip-flop output `Q_bar`.
- **When OUT = HIGH (charge phase):** Signal `Q_bar = 0`. Base current is absent, and the discharge transistor is completely off in a high-impedance state (Hi-Z). The DISCH pin is disconnected from ground, allowing the external capacitor to charge freely from the supply rail through the timing resistors.[^ti-ne555-datasheet][^art-of-electronics]
- **When OUT = LOW (discharge phase):** Signal `Q_bar = 1`. Current flows into the base of the discharge transistor, driving it into deep saturation (`V_CE(sat) ≈ 0.1 V`). The DISCH pin is pulled directly to GND, creating a path for the stored capacitor charge to discharge rapidly to ground through the connected timing resistor.[^ti-ne555-datasheet]

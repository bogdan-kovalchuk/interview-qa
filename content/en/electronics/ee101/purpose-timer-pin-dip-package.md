---
id: emb-elee-0254
title: "What is the purpose of each 555 timer pin in a DIP-8 package?"
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

The DIP-8 pinout is: pin 1 is GND, pin 2 is TRIG (trigger input), pin 3 is OUT, and pin 4 is RESET. Pin 5 is CONT (control voltage), pin 6 is THRES (threshold input), pin 7 is DISCH (discharge open-collector pin), and pin 8 is `V_CC`.[^udemy-electronics-course]

## Detailed explanation

The classic 555 timer IC is produced in a standard 8-pin DIP-8 (or SOIC-8) package. Each pin serves a well-defined hardware function in the operation of the internal circuitry, which includes a voltage divider, two comparators, an RS flip-flop, and output stages.[^udemy-electronics-course][^ti-ne555-datasheet]

### Detailed pin descriptions

1. **Pin 1 – GND (Ground):**
   Connects to the negative supply rail (0 V). Serves as the reference potential for all internal voltages, comparators, and output switches.[^ti-ne555-datasheet]

2. **Pin 2 – TRIG (Trigger):**
   Connected to the inverting input of the lower comparator, whose non-inverting input is tied to `1/3 * V_CC`. When the voltage on this pin falls below `1/3 * V_CC`, the lower comparator sets the internal RS flip-flop: output OUT (pin 3) goes HIGH, and the discharge transistor DISCH (pin 7) turns off.[^ti-ne555-datasheet][^art-of-electronics]

3. **Pin 3 – OUT (Output):**
   A robust totem-pole output stage. In the classic bipolar version (NE555), it can both source and sink up to 200 mA. This allows it to directly drive LEDs, relays, optocouplers, or small buzzers without external transistor switches.[^ti-ne555-datasheet] In the HIGH state, the output voltage is approximately `V_CC - 1.5 V`, and in the LOW state it is roughly 0.1–0.25 V.

4. **Pin 4 – RESET:**
   An active-low asynchronous reset input. If the voltage on this pin drops below 0.7 V, the RS flip-flop is immediately forced into reset, pulling output OUT LOW and turning on the DISCH transistor.[^ti-ne555-datasheet] If the reset feature is not used, pin 4 must be tied directly to `V_CC`. Leaving it floating is prohibited, as coupled high-frequency noise could trigger spurious timer resets.[^art-of-electronics]

5. **Pin 5 – CONT / CV (Control Voltage):**
   A direct connection to the upper node of the internal resistive divider (which sits nominally at `2/3 * V_CC`). Applying an external voltage to this pin adjusts the trip threshold of the upper comparator and, indirectly, the lower comparator (`1/2` of the CONT voltage), which is used to implement pulse-width modulation (PWM) or frequency modulation.[^ti-ne555-datasheet][^art-of-electronics] When external adjustment is not required, pin 5 must be bypassed to ground with a 10 nF (0.01 µF) ceramic capacitor to filter divider noise.

6. **Pin 6 – THRES (Threshold):**
   Connected to the non-inverting input of the upper comparator, whose inverting input references `2/3 * V_CC` (or the potential at pin 5). When the rising voltage on the timing capacitor exceeds `2/3 * V_CC`, the upper comparator trips, resetting the flip-flop: output OUT drops LOW, and pin 7 is clamped to ground.[^ti-ne555-datasheet]

7. **Pin 7 – DISCH (Discharge):**
   The open-collector terminal of an internal NPN transistor whose emitter is connected to ground (pin 1). It operates synchronously with the output: when OUT = LOW, the transistor is saturated and shorts pin 7 to ground, discharging the external timing capacitor; when OUT = HIGH, the transistor is off (Hi-Z state), allowing the capacitor to charge.[^ti-ne555-datasheet][^art-of-electronics]

8. **Pin 8 – VCC / V+ (Supply Voltage):**
   Connects to the positive rail of the DC power source. The standard operating supply voltage range for the bipolar NE555 timer is 4.5 V to 16 V (absolute maximum 18 V).[^ti-ne555-datasheet] Modern CMOS variants (such as the LMC555, TLC555) operate from low voltages from 1.5–2 V up to 12–15 V and consume current in the microampere range.

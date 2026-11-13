---
id: emb-elee-0255
title: "How is the 555 astable mode built?"
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

Resistor `R_A` connects from the supply to DISCH, `R_B` connects from DISCH to the tied TRIG/THRES node, and timing capacitor C connects from that node to ground. Capacitor C charges through `R_A + R_B` and discharges through `R_B` alone, cycling between 1/3 and 2/3 `V_CC`. As a result, the output continuously generates a periodic pulse train without needing an external trigger.[^udemy-electronics-course]

## Detailed explanation

In astable (free-running) mode, the 555 timer operates as an unsynchronized square wave pulse generator (multivibrator) that automatically self-restarts and continuously sustains oscillations without external trigger pulses.[^udemy-electronics-course][^ti-ne555-datasheet]

### Circuit topology and connections

Building the classic astable oscillator requires only three external timing components: two resistors (`R_A`, `R_B`) and one capacitor `C`:[^ti-ne555-datasheet]
- Resistor `R_A` connects between the positive supply rail `V_CC` and pin 7 (DISCH).
- Resistor `R_B` connects between pin 7 (DISCH) and the tied node of pins 2 (TRIG) and 6 (THRES).
- Timing capacitor `C` connects between this tied node (pins 2 and 6) and ground GND (pin 1).
- Pin 4 (RESET) connects directly to `V_CC` to prevent accidental resets.
- Pin 5 (CONT) connects to ground through a 10 nF (0.01 µF) ceramic bypass capacitor.[^ti-ne555-datasheet][^art-of-electronics]

### Physical mechanism of the oscillation cycle

1. **Capacitor charging phase (output OUT = HIGH):**
   At power-up, the voltage on the capacitor is zero (`V_C = 0 V`). Because this is below the `1/3 * V_CC` threshold, the lower comparator (TRIG) trips immediately, setting the RS flip-flop: output OUT (pin 3) goes HIGH, and the internal discharge transistor on pin 7 turns off (enters the Hi-Z state).[^ti-ne555-datasheet]
   Current from the `V_CC` rail charges capacitor `C` through both series resistors: `R_charge = R_A + R_B`.
   The voltage across the capacitor rises exponentially from `1/3 * V_CC` toward `2/3 * V_CC`.
   The duration of the HIGH output phase is:
   `t_high = ln(2) * (R_A + R_B) * C ≈ 0.693 * (R_A + R_B) * C`.[^ti-ne555-datasheet][^art-of-electronics]

2. **Capacitor discharge phase (output OUT = LOW):**
   As soon as the voltage at the tied 2/6 node reaches the upper threshold `2/3 * V_CC`, the upper comparator (THRES) trips. It resets the flip-flop: output OUT drops LOW, and the discharge transistor turns on, clamping pin 7 (DISCH) to ground GND.[^ti-ne555-datasheet]
   Capacitor `C` now discharges to ground solely through resistor `R_B` and the saturated transistor at pin 7. During this phase, resistor `R_A` is simply connected between `V_CC` and ground (via the transistor), without affecting capacitor discharge.
   The voltage across the capacitor falls exponentially from `2/3 * V_CC` toward the lower threshold `1/3 * V_CC`.
   The duration of the LOW output phase is:
   `t_low = ln(2) * R_B * C ≈ 0.693 * R_B * C`.[^ti-ne555-datasheet]

3. **Closing the self-sustaining cycle:**
   When the voltage across the capacitor drops below `1/3 * V_CC`, the lower comparator (TRIG) trips again, setting the flip-flop, returning output OUT to HIGH, turning off the discharge transistor, and repeating the charging process indefinitely.[^ti-ne555-datasheet]

### Calculation formulas and duty cycle

- **Total oscillation period:**
  `T = t_high + t_low = 0.693 * (R_A + 2 * R_B) * C`.[^ti-ne555-datasheet]
- **Oscillation frequency:**
  `f = 1 / T ≈ 1.44 / ((R_A + 2 * R_B) * C)`.[^ti-ne555-datasheet][^art-of-electronics]
- **Duty Cycle:**
  `D = t_high / T = (R_A + R_B) / (R_A + 2 * R_B)`.
  Because `R_A` is strictly greater than zero, `t_high` is always greater than `t_low`. In the classic circuit, the duty cycle always exceeds 50% (`D > 0.5`).[^art-of-electronics]

### Practical engineering nuances

1. **Minimum value of `R_A`:** During discharge, current `I_discharge = V_CC / R_A` flows through the saturated pin 7 transistor. To prevent overloading and thermal destruction of the internal discharge switch, `R_A` must not be less than 1 kΩ.[^art-of-electronics]
2. **Obtaining a symmetrical square wave (Duty Cycle = 50%):** If a 50% duty cycle or lower is required, a fast small-signal diode (such as a 1N4148 or Schottky diode) is connected across resistor `R_B` with its cathode toward pins 2/6. During the charging phase, current flows through `R_A` and the forward-biased diode (bypassing `R_B`), giving `t_high ≈ 0.693 * R_A * C`. During the discharge phase, the diode is reverse-biased, and the capacitor discharges through `R_B`: `t_low ≈ 0.693 * R_B * C`. Setting `R_A = R_B` yields a symmetrical square wave.[^art-of-electronics]

---
id: emb-elee-0256
title: "What are the timing and frequency formulas of the astable 555?"
track: electronics
section: ee101
sources:
  - source_id: ti-ne555-datasheet
    title: "Texas Instruments: NE555 Precision Timers Datasheet (SLRS022)"
    url: https://www.ti.com/lit/ds/symlink/ne555.pdf
  - source_id: fiore-555-timer
    title: "Engineering LibreTexts: Operational Amplifiers and Linear Integrated Circuits (Fiore), 9.6 The 555 Timer"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/09:_Specialized_Linear_Circuits/9.6:_The_555_Timer
  - source_id: aac-555-circuits
    title: "All About Circuits: 555 Timer Circuits"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-8/555-timer-circuits/
---

## Short answer

The astable 555 intervals are `t_HIGH ≈ 0.693 * (R_A + R_B) * C` and `t_LOW ≈ 0.693 * R_B * C`. The total period is `T = t_HIGH + t_LOW ≈ 0.693 * (R_A + 2*R_B) * C`, yielding an output frequency `f ≈ 1.44 / ((R_A + 2*R_B) * C)`. The HIGH duty cycle is `D = (R_A + R_B) / (R_A + 2*R_B)`. Doubling timing capacitance C halves the oscillation frequency.[^ti-ne555-datasheet]

## Detailed explanation

### Internal structure and circuit switching

The classic astable oscillator based on the 555 timer contains an internal resistive divider of three identical 5 kΩ resistors (in the bipolar version) that establishes the reference voltages of the internal comparators at `(1/3)*V_CC` (lower threshold, TRIG input, pin 2) and `(2/3)*V_CC` (upper threshold, THRES input, pin 6).[^ti-ne555-datasheet]

The external frequency-determining circuit consists of resistors `R_A` (connected between the `V_CC` supply rail and the DISCH discharge terminal, pin 7), `R_B` (between pin 7 and the tied pins 2 and 6), and capacitor `C` (between tied pins 2 and 6 and ground GND). During operation, the capacitor voltage `v_C(t)` continuously cycles between threshold levels `(1/3)*V_CC` and `(2/3)*V_CC` without requiring external synchronization.[^fiore-555-timer]

### Charging phase (HIGH state)

At the beginning of the cycle, the internal RS flip-flop is in the set state (SET), which makes the output (pin 3) active HIGH, while the internal NPN discharge transistor, whose collector is brought out to pin 7, is off (cutoff). Current from the `V_CC` supply flows through series resistors `R_A` and `R_B`, charging capacitor `C`.[^aac-555-circuits]

The general differential equation for charging an RC circuit is:
`v_C(t) = V_final - (V_final - V_initial) * exp(-t / ((R_A + R_B) * C))`

During this phase, the capacitor charges toward `V_final = V_CC`, starting from voltage `V_initial = (1/3)*V_CC`. The process continues until voltage `v_C` reaches the upper threshold `(2/3)*V_CC`:
`(2/3)*V_CC = V_CC - (V_CC - (1/3)*V_CC) * exp(-t_HIGH / ((R_A + R_B) * C))`
`(2/3)*V_CC = V_CC - (2/3)*V_CC * exp(-t_HIGH / ((R_A + R_B) * C))`
`(1/3)*V_CC = (2/3)*V_CC * exp(-t_HIGH / ((R_A + R_B) * C))`
`1/2 = exp(-t_HIGH / ((R_A + R_B) * C))`
`exp(t_HIGH / ((R_A + R_B) * C)) = 2`

Taking the natural logarithm of both sides yields the analytical expression for the HIGH duration:[^ti-ne555-datasheet]
`t_HIGH = ln(2) * (R_A + R_B) * C ≈ 0.69315 * (R_A + R_B) * C`

### Discharge phase (LOW state)

When the capacitor voltage exceeds `(2/3)*V_CC`, the upper comparator trips and resets the RS flip-flop (RESET). This transitions the output (pin 3) to the LOW state and drives the internal NPN discharge transistor into saturation, connecting pin 7 effectively to GND.[^fiore-555-timer]

Now resistor `R_A` is connected directly between `V_CC` and the grounded collector of pin 7, drawing current `I = V_CC / R_A`, but playing no part in discharging the capacitor. Capacitor `C` discharges to ground solely through resistor `R_B` and the saturated discharge transistor:[^aac-555-circuits]
`v_C(t) = V_initial * exp(-t / (R_B * C))`

Discharge begins from `V_initial = (2/3)*V_CC` and completes when the voltage falls to the lower threshold `(1/3)*V_CC`, tripping the lower comparator:
`(1/3)*V_CC = (2/3)*V_CC * exp(-t_LOW / (R_B * C))`
`1/2 = exp(-t_LOW / (R_B * C))`
`t_LOW = ln(2) * R_B * C ≈ 0.69315 * R_B * C`

The lower comparator again sets the RS flip-flop (SET), turns off the discharge switch, and the cycle repeats indefinitely.

### Period, frequency, and duty cycle

The total oscillation period `T` equals the sum of the charge and discharge intervals:[^ti-ne555-datasheet]
`T = t_HIGH + t_LOW = ln(2) * (R_A + R_B) * C + ln(2) * R_B * C = ln(2) * (R_A + 2*R_B) * C`
`T ≈ 0.69315 * (R_A + 2*R_B) * C`

The oscillation frequency is the reciprocal of the period:
`f = 1 / T = 1 / (ln(2) * (R_A + 2*R_B) * C) ≈ 1.4427 / ((R_A + 2*R_B) * C) ≈ 1.44 / ((R_A + 2*R_B) * C)`

The HIGH duty cycle is defined as the ratio of `t_HIGH` to the full period `T`:
`D = t_HIGH / T = (ln(2) * (R_A + R_B) * C) / (ln(2) * (R_A + 2*R_B) * C) = (R_A + R_B) / (R_A + 2*R_B)`

Because resistor `R_A` is strictly greater than zero (`R_A > 0`), the numerator always exceeds half of the denominator; thus, in the standard configuration, duty cycle `D` is always strictly greater than 50% (typically in the range of 51% to 99%).[^fiore-555-timer] If a duty cycle of less than 50% or exactly 50% is required, a diode (such as a 1N4148 with cathode toward pin 6/2) is connected in parallel with `R_B` to bypass `R_B` during charging, providing separate paths for charging via `R_A` and discharging via `R_B`.

### Practical engineering factors and errors

1. Frequency dependence on capacitance: the relation `f ~ 1/C` is strictly linear with respect to reciprocal capacitance; therefore, doubling the value of `C` halves the output frequency while maintaining the same duty cycle.[^aac-555-circuits]
2. Supply voltage influence: because of the ratiometric operation of the internal divider, the `(1/3)*V_CC` and `(2/3)*V_CC` thresholds track supply voltage variations, so ideally the frequency is independent of `V_CC`. However, in bipolar NE555 timers, the saturation voltage of the discharge transistor `V_CE(sat) ≈ 0.1–0.2 V` introduces slight temperature and voltage dependencies.[^ti-ne555-datasheet]
3. Resistor value constraints: the minimum value of `R_A` is typically limited to 1 kΩ to protect the internal discharge transistor from excessive current, while the total resistance `R_A + R_B` is limited to several megohms due to the input bias currents of the comparators (up to 0.5 µA in the NE555).

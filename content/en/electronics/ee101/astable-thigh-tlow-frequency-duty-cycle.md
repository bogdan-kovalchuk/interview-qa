---
id: emb-elee-0257
title: "Astable 555: R_A = 10 kΩ, R_B = 47 kΩ, C = 1 µF. What are t_HIGH, t_LOW, the frequency and the duty cycle?"
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

For these component values, the timing intervals are `t_HIGH ≈ 39.5 ms` and `t_LOW ≈ 32.6 ms`, giving a total period `T ≈ 72.1 ms`. The resulting output frequency is `f ≈ 13.9 Hz` with a HIGH duty cycle of `D ≈ 54.8%`. Real circuit performance will deviate slightly from these nominal calculations due to component manufacturing tolerances, capacitor leakage currents, and internal comparator delays.[^ti-ne555-datasheet]

## Detailed explanation

### Pulse and pause duration calculation

In the astable mode of the 555 timer, the duration of the output HIGH level `t_HIGH` is determined by the charging time of capacitor `C` from `(1/3)*V_CC` to `(2/3)*V_CC` through the series combination of resistors `R_A` and `R_B`:[^ti-ne555-datasheet]
`t_HIGH = ln(2) * (R_A + R_B) * C ≈ 0.69315 * (R_A + R_B) * C`

Substituting the given numerical values:
- `R_A = 10 kΩ = 10 * 10^3 Ω`
- `R_B = 47 kΩ = 47 * 10^3 Ω`
- `C = 1 µF = 1 * 10^(-6) F`

We obtain:
`t_HIGH = 0.69315 * (10 * 10^3 + 47 * 10^3) * 1 * 10^(-6) = 0.69315 * 57 * 10^(-3) s ≈ 39.51 ms`

The duration of the output LOW level `t_LOW` is determined by the discharge time of the capacitor from `(2/3)*V_CC` to `(1/3)*V_CC` solely through resistor `R_B` and the internal saturated discharge transistor (DISCH, pin 7):[^fiore-555-timer]
`t_LOW = ln(2) * R_B * C ≈ 0.69315 * R_B * C`
`t_LOW = 0.69315 * (47 * 10^3) * 1 * 10^(-6) = 0.69315 * 47 * 10^(-3) s ≈ 32.58 ms`

### Period, frequency, and duty cycle

The total oscillation period `T` equals the sum of the two half-periods:[^aac-555-circuits]
`T = t_HIGH + t_LOW ≈ 39.51 ms + 32.58 ms = 72.09 ms ≈ 72.1 ms`

Or directly via the analytical formula:
`T = ln(2) * (R_A + 2*R_B) * C = 0.69315 * (10 + 2 * 47) * 10^3 * 10^(-6) = 0.69315 * 104 * 10^(-3) s ≈ 72.09 ms`

The oscillation frequency is the reciprocal of the period:
`f = 1 / T = 1 / 0.07209 s ≈ 13.87 Hz`

Using the simplified engineering coefficient from the datasheet (`1.44`):[^ti-ne555-datasheet]
`f ≈ 1.44 / ((R_A + 2*R_B) * C) = 1.44 / (104 * 10^3 * 1 * 10^(-6)) = 1.44 / 0.104 ≈ 13.85 Hz`

The duty cycle for the HIGH level is:
`D = t_HIGH / T = 39.51 ms / 72.09 ms ≈ 0.5481` (or `54.8 %`)

In analytical form, the expression is independent of capacitance `C`:
`D = (R_A + R_B) / (R_A + 2*R_B) = (10 + 47) / (10 + 94) = 57 / 104 ≈ 0.5481`

### Physical and manufacturing factors causing deviations from calculations

In a real circuit, measured results will always deviate from ideal mathematical calculations due to the following physical factors:[^ti-ne555-datasheet][^fiore-555-timer]

1. Passive component tolerances: 1 µF electrolytic or tantalum capacitors typically have manufacturing tolerances of ±20% (and ceramic X7R capacitors exhibit a pronounced drop in capacitance with applied DC-bias voltage). Resistors have tolerances of ±1% or ±5%. If the actual capacitance happens to be 1.2 µF, the time intervals will increase by 20%, and the frequency will drop to ~11.6 Hz.
2. Capacitor leakage current: for electrolytic capacitors, leakage current is equivalent to a resistor in parallel with `C`. This current reduces the effective charging current during the charge phase and accelerates discharge, which increases `t_HIGH`, slightly decreases `t_LOW`, and lowers the overall oscillation frequency.
3. Residual voltage drop across the discharge transistor: the internal NPN transistor of pin 7 in saturation has a voltage `V_CE(sat) ≈ 0.1–0.2 V`. Because of this, the capacitor discharges not to pure ground, but to `V_CE(sat)`, which slightly alters the bottom of the discharge trajectory relative to the ideal `(1/3)*V_CC` threshold.
4. Internal IC divider: the resistance of the three internal 5 kΩ resistors has an individual process spread of up to ±20% (although their matching ratio on a single die is much tighter, around 1%). This causes a slight shift of the 1/3 and 2/3 threshold voltages from their nominal values.
5. Comparator propagation delay: response time of the internal comparators in the bipolar 555 is typically 100–300 ns. At a low frequency around 14 Hz, this delay is completely negligible (accounting for less than 0.001% of the period), but it becomes a dominant source of error at frequencies above 100 kHz.

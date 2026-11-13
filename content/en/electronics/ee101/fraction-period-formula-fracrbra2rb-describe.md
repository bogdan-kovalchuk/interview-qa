---
id: emb-elee-0258
title: "Which fraction of the period does the formula R_B / (R_A + 2*R_B) describe for the 555, and can R_A be 0?"
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

This formula describes the LOW output fraction `t_LOW / T`, not the HIGH fraction. In a standard astable 555 circuit, the HIGH duty cycle is always strictly greater than 50%. Reducing `R_A` to zero is strictly forbidden, because during the discharge phase pin 7 is tied to ground by the internal switch, creating a direct short circuit across the power supply that destroys the IC.[^ti-ne555-datasheet]

## Detailed explanation

### Mathematical derivation of the period fraction

In the basic astable circuit of the 555 timer, the timing intervals are determined by the exponential charge and discharge of capacitor `C`:[^ti-ne555-datasheet]
- HIGH time (charge through `R_A + R_B`): `t_HIGH = ln(2) * (R_A + R_B) * C`
- LOW time (discharge through `R_B`): `t_LOW = ln(2) * R_B * C`
- Total oscillation period: `T = t_HIGH + t_LOW = ln(2) * (R_A + 2*R_B) * C`

Computing the fraction of the period occupied by the LOW level yields:[^fiore-555-timer]
`D_LOW = t_LOW / T = (ln(2) * R_B * C) / (ln(2) * (R_A + 2*R_B) * C) = R_B / (R_A + 2*R_B)`

The fraction of the period occupied by the HIGH level (duty cycle, `D_HIGH`) is:
`D_HIGH = t_HIGH / T = (R_A + R_B) / (R_A + 2*R_B)`

Because normal operation requires a positive resistance `R_A > 0`, it follows that `R_A + R_B > R_B`, from which it inevitably follows that:
`D_HIGH > 50 %`, and `D_LOW < 50 %`

In some popular educational resources, the formula `R_B / (R_A + 2*R_B)` is mistakenly referred to as the duty cycle of the pulse, confusing the pause interval (LOW) with the pulse interval (HIGH).[^aac-555-circuits]

### Why resistor R_A cannot be set to 0

Pin 7 (DISCH) of the 555 timer is connected directly to the collector of the internal bipolar NPN discharge transistor, whose emitter is tied to the common ground rail (GND, pin 1). Resistor `R_A` is connected between the positive supply rail `V_CC` and this pin 7.[^ti-ne555-datasheet]

During the capacitor discharge phase, the internal RS flip-flop drives the discharge transistor into full saturation, clamping pin 7 to ground in order to discharge capacitor `C` through resistor `R_B`. If `R_A = 0` were set (meaning pin 7 was connected directly to `V_CC`):[^fiore-555-timer]
1. The moment the discharge transistor turns on, a direct short circuit is formed from the `V_CC` supply rail to `GND` through the transistor structure.
2. The current through the transistor would be limited only by the negligible resistance of on-chip metallization and the internal impedance of the power supply, instantaneously reaching several amperes.
3. The absolute maximum peak current of pin 7 for a standard NE555 is `I_DISCH(max) = 200 mA` according to the Absolute Maximum Ratings section of the Texas Instruments datasheet.[^ti-ne555-datasheet]
4. Exceeding this current causes localized thermal breakdown, fusing of bond wires, or melting of the silicon junction, permanently destroying the integrated circuit.

### Safe selection of the R_A value

To guarantee reliable operation of the IC, resistance `R_A` must safely limit the collector current of the discharge transistor:[^ti-ne555-datasheet]
`I_DISCH = V_CC / R_A <= I_DISCH(max)`

At a supply voltage of `V_CC = 15 V`, the minimum allowable resistance is:
`R_A(min) >= 15 V / 0.2 A = 75 Ω`

However, to minimize power consumption and prevent excessive package heating (current through `R_A` is dumped to ground throughout the entire `t_LOW` interval), practical design rules dictate a minimum `R_A` of at least 1 kΩ.[^fiore-555-timer]

### Methods for achieving a duty cycle of 50% or less

If a circuit requires a duty cycle of 50% or less, the following circuit modifications are employed:[^aac-555-circuits]
1. Diode bypassing of resistor `R_B`: a diode (for example, a silicon 1N4148 or Schottky diode BAT85) is connected in parallel with `R_B`, anode to pin 7 and cathode to capacitor `C`. The capacitor charges through `R_A` and the forward-biased diode (bypassing `R_B`), and discharges through `R_B` into grounded pin 7. Then `t_HIGH ≈ 0.693 * R_A * C`, and `t_LOW ≈ 0.693 * R_B * C`. Choosing `R_A = R_B` yields `D ≈ 50 %`, while `R_A < R_B` yields a duty cycle below 50%.
2. Charge and discharge via the output (pin 3): the capacitor is connected through a single resistor `R` directly to the timer output (pin 3). In CMOS variants (such as the LMC555 or TLC555) with a symmetrical rail-to-rail output stage, the same resistor charges and discharges the capacitor almost symmetrically, producing a duty cycle close to 50%; in a bipolar NE555, output asymmetry (`V_OH ≈ V_CC - 1.5 V` versus `V_OL ≈ 0.1–0.25 V`) lengthens charging relative to discharging and shifts the duty cycle above 50%.
3. External flip-flop frequency divider: the 555 output is fed into the clock input of a D flip-flop or binary counter configured as a toggle flip-flop (divide-by-2). This guarantees a strict hardware 50% duty cycle regardless of tolerances in `R_A`, `R_B`, and `C`.

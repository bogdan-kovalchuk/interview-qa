---
id: emb-elee-0179
title: "9 V RMS 50 Hz source, bridge, C = 1000 µF, 0.1 A load. What are the ripple and the minimum voltage on C?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
---

## Short answer

After a full-wave bridge, ripple frequency is `2*50 = 100 Hz`, yielding `ΔV_pp ≈ I/(f*C) = 0.1/(100*0.001) = 1 V`.[^fiore-capacitors] The peak voltage on the capacitor is `9*sqrt(2) - 2*0.7 ≈ 11.33 V`, giving a trough of `11.33 - 1 ≈ 10.33 V` as an approximation.[^fiore-rectification] A linear regulator requires `V_in,trough > V_out + V_dropout` to maintain regulation.[^ti-slva079]

## Detailed explanation

**Ripple voltage.** The full-wave bridge rectifies both half-cycles, so voltage peaks across the filter capacitor repeat at twice the line frequency, `2*50 = 100 Hz`, and the time between peaks does not exceed `1/100 = 10 ms`.[^fiore-rectification] During this time, the capacitor delivers 0.1 A to the load, and for a constant discharge current the fundamental capacitor relationship `i = C*dv/dt` yields `ΔV = I*Δt/C`.[^fiore-capacitors] Hence, `ΔV_pp = 0.1*0.01/0.001 = 1 V`: the peak-to-peak ripple is 1 V, which corresponds to approximately ±0.5 V around the mean DC level.

**Minimum voltage (trough).** The peak secondary voltage is `9*sqrt(2) ≈ 12.73 V`. In a bridge rectifier two diodes conduct simultaneously, so the load experiences the secondary voltage minus two diode forward drops.[^fiore-rectification] Assuming a nominal 0.7 V per diode, the peak voltage on the capacitor is `12.73 - 1.4 ≈ 11.33 V`. Subtracting the peak-to-peak ripple yields a trough voltage of `11.33 - 1 ≈ 10.33 V`, with an average DC value of approximately `11.33 - 0.5 ≈ 10.83 V`. Consequently, a 9 V RMS secondary winding yields not 9 V DC, but approximately 10.8 V average DC.

**Approximation accuracy.** The formula assumes constant current discharge over the full 10 ms interval, whereas in reality the diodes begin recharging the capacitor before the AC peak, shortening the discharge phase. At the same time, winding resistance and diode dynamic impedance depress the peak voltage during charging current pulses. In a numerical simulation (sinusoidal source, 0.7 V per diode, constant 0.1 A load, 1000 µF), a total series resistance of 0.5 Ω produces a ripple of ≈ 0.83 V and a trough of ≈ 10.33 V, whereas 2 Ω yields a ripple of ≈ 0.74 V and a trough of ≈ 9.79 V. Therefore, 10.33 V is an initial approximation neglecting internal impedances rather than a rigid guarantee. If the mains voltage drops by 10% (`9*0.9 = 8.1 V RMS`), the same formula gives a trough of `8.1*sqrt(2) - 1.4 - 1 ≈ 9.06 V`.

**Condition for regulator operation.** A linear regulator ceases regulating when its input falls below `V_out + V_dropout`.[^ti-slva079] This condition must be checked against the lowest instantaneous input voltage (the bottom of the ripple trough) rather than the average DC level (see qid:emb-elee-0156). For the uA7805, the recommended input voltage range is 7–25 V, meaning a 10.33 V trough leaves a safety headroom of `10.33 - 7 = 3.33 V`, while ≈ 9.06 V under low mains provides approximately `9.06 - 7 ≈ 2.1 V` of headroom.[^ti-ua78]

**Common mistakes:**

- Using 50 Hz instead of 100 Hz for the ripple frequency in a full-wave bridge, doubling the estimated ripple.
- Forgetting the two diode drops in the bridge (accounting for only one or none).
- Mistaking 9 V RMS for the peak amplitude rather than the RMS value.
- Evaluating regulator dropout against the average input voltage rather than the trough of the ripple.

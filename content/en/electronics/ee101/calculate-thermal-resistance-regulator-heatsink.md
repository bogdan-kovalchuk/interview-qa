---
id: emb-elee-0160
title: "How do you calculate the thermal resistance of a regulator with a heatsink?"
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
  - source_id: ti-sboa020
    title: "Texas Instruments (Burr-Brown) SBOA020 / AB-037: Mounting Considerations for TO-3 Packages"
    url: https://www.ti.com/lit/an/sboa020/sboa020.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-spra953
    title: "Texas Instruments SPRA953: Semiconductor and IC Package Thermal Metrics"
    url: https://www.ti.com/lit/pdf/spra953
---

## Short answer

Thermal resistance from junction to ambient is the sum of series thermal resistances: `θ_JA = θ_JC + θ_CS + θ_SA` (°C/W), representing junction-to-case, case-to-sink (interface material), and sink-to-ambient.[^ti-sboa020] Thermal paste lowers `θ_CS` relative to dry contact, whereas an electrical insulator generally adds higher `θ_CS` than paste alone.[^ti-sboa020] Electrical insulation is often mandatory because the regulator mounting tab connects to ground or output.[^ti-lm340]

## Detailed explanation

Heat dissipated by a regulator travels from the die junction to ambient air through a series thermal chain, and thermal resistances of the path sum just like electrical resistors in series. For a linear regulator, power equals `P = (V_in - V_out)*I_out` (plus a small fraction `V_in*I_q`),[^ti-slva079] and junction temperature is `T_J = T_A + P*θ_JA`, where `θ_JA = θ_JC + θ_CS + θ_SA`. TI writes the identical model as `θ_JC + θ_CH + θ_HA`, where `θ_CH` represents the case-to-heatsink interface.[^ti-sboa020] The LM340 datasheet states the same principle: with a heatsink, `θ_JA` consists of package `θ_JC` plus the heatsink case-to-ambient thermal resistance.[^ti-lm340]

Each term is obtained from a different source. Package `θ_JC` is given in the IC datasheet, `θ_SA` is listed in the heatsink catalog, and `θ_CS` depends on mounting assembly: microscopic air gaps remain between package and heatsink surfaces, which are filled with thermal grease or an interface pad. For the TO-3 package, TI cites typical ranges: dry contact 0.5–1.0 °C/W, thermal grease 0.1–0.2 °C/W, Kapton with grease 0.3–0.5 °C/W, and dry mica 1.0–1.5 °C/W.[^ti-sboa020] For TO-220 packages the absolute numbers differ, but the interface hierarchy remains identical.

Electrical isolation is an independent reason for using an insulating pad. The mounting tab or case of a regulator connects internally to ground or to the output depending on the variant,[^ti-lm340] so mounting directly to a shared heatsink could short these nets, necessitating an insulating pad between package and heatsink. Because of the dielectric layer, such an insulating pad typically has higher `θ_CS` than thermal paste alone, as noted by TI.[^ti-sboa020] One must never substitute the standalone package `θ_JA` without a heatsink into this equation: that parameter depends on test board layout and boundary conditions,[^ti-spra953] and the LM340 datasheet for the TO-220 package even lists differing values (54 °C/W in a note versus 23.9 °C/W in the table).[^ti-lm340]

**Example.** A 7805 in a TO-220 package, `V_in = 12 V`, `I_out = 0.5 A`, `T_A = 40 °C`, with a target ceiling `T_J = 125 °C` (the datasheet permits `T_JMAX` of 125 or 150 °C, and thermal shutdown triggers above 150 °C).[^ti-lm340] Dissipated power is `P = (12 - 5)*0.5 = 3.5 W`; quiescent current (up to 6 mA per the LM340A datasheet) adds less than 0.1 W. Allowable `θ_JA = (125 - 40)/3.5 ≈ 24.3 °C/W`. Taking `θ_JC = 4 °C/W` (datasheet note for TO-220) and `θ_CS = 1 °C/W` (illustrative assumption for an insulating pad), required `θ_SA ≤ 24.3 - 4 - 1 ≈ 19 °C/W`. Verification: `T_J = 40 + 3.5*(4 + 1 + 19) = 124 °C`.

**Common mistakes:**

- Adding heatsink `θ_SA` to the standalone package `θ_JA` from the datasheet: `θ_JA` already includes the path to air, whereas with a heatsink one must use `θ_JC`.[^ti-lm340]
- Assuming `θ_CS` is zero or forgetting that an insulating pad has higher thermal resistance than grease alone.[^ti-sboa020]
- Applying datasheet `θ_JA` numbers directly to a custom board without verifying test conditions.[^ti-spra953]

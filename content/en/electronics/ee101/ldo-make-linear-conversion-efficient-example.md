---
id: emb-elee-0155
title: "Does an LDO make linear conversion efficient, for example 12 V -> 3.3 V?"
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
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
---

## Short answer

No. A low dropout voltage only allows operation with a small input-to-output headroom; it does not improve conversion efficiency across wide spreads. All load current passes through the regulator pass device, dissipating approximately `P = (V_in - V_out)*I_out`, with efficiency fundamentally limited by `V_out/V_in`. Stepping 12 V down to 3.3 V yields around 27.5% efficiency, with the remaining power wasted as heat.[^ti-slva079]

## Detailed explanation

An LDO is a linear regulator: its pass element operates as a controlled resistance in series with the load. The entire load current `I_out` passes through this device, so the difference `V_in - V_out` drops across it, dissipating power `P = (V_in - V_out)*I_out`.[^ti-slva079] The word "low" in the name refers to the minimum voltage difference at which the regulator still maintains output regulation: in dropout, a PMOS pass element behaves as a resistor, and `V_dropout = I_o*R_on`.[^ti-slva079] This is the lower boundary of the operating region, not an indicator of losses at actual operating differentials, which can be much larger.

LDO efficiency is defined as `η = I_o*V_o/((I_o + I_q)*V_i)`, where `I_q = I_i - I_o` is quiescent current that does not reach the load.[^ti-slva079] Even when `I_q` is negligible, efficiency cannot exceed `V_o/V_i`: according to TI, the input-to-output voltage differential is an intrinsic efficiency factor regardless of load.[^ti-slva079] Therefore, a low dropout voltage is beneficial primarily when the input is only slightly higher than the output, such as when powering 3.3 V from a discharging battery, where voltage headroom and losses are both small.

**Example:** `V_in = 12 V`, `V_out = 3.3 V`, `I_out = 0.1 A`. Power drawn is `12*0.1 = 1.2 W`, delivered load power is `3.3*0.1 = 0.33 W`, heat dissipated is `1.2 - 0.33 = 0.87 W`; efficiency is `3.3/12 = 27.5%` (neglecting `I_q`). At `I_out = 0.3 A`, heat dissipation rises to `(12 - 3.3)*0.3 = 2.61 W`; for an illustrative `θ_JA = 60 °C/W`, this represents a die junction temperature rise of approximately `2.61*60 = 156.6 °C` above ambient, making operation without a heatsink unacceptable (see also qid:emb-elee-0159). By comparison, with a 5 V input at that same 0.1 A, losses are only `(5 - 3.3)*0.1 = 0.17 W`, and efficiency is `3.3/5 = 66%`. The datasheet specifies maximum junction temperature, and actual dissipation must not exceed `P_D(max) = (T_Jmax - T_A)/R_θJA`.[^ti-slva079]

When the voltage difference is large and current is substantial, a switching converter or a pre-regulation step-down stage before the LDO is typically more efficient; LDOs are retained where simplicity and low noise are critical and thermal dissipation remains manageable. Calculations must always address worst-case conditions: dissipation peaks at maximum input voltage and maximum load current.

**Common mistakes:**

- Believing that "low dropout" implies low losses: dropout is merely the lower limit of required voltage headroom.
- Evaluating efficiency solely based on `I_q` without considering the `V_out/V_in` ratio.
- Calculating thermal dissipation using nominal input voltage rather than maximum, or average rather than peak current.

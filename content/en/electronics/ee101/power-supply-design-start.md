---
id: emb-elee-0157
title: "Where should power supply design start?"
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
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
---

## Short answer

Start with requirements: output voltage, continuous and peak load currents, input voltage range, and permissible ripple. From these, estimate dissipation `P = (V_in - V_out)*I_out` to decide whether a linear regulator is viable. Then consult the IC datasheet to verify recommended operating conditions, dropout headroom, output capacitor stability requirements, and thermal constraints.[^ti-slva079][^ti-tps752q1-datasheet]

## Detailed explanation

Power supply design begins with concrete numbers, as all subsequent architectural decisions depend on them. One must define the required output voltage and tolerance, continuous and peak load currents, input voltage range with both extremes, and permissible ripple. The minimum input voltage together with the ripple trough determines whether the dropout requirement is satisfied (see qid:emb-elee-0156), while the maximum input voltage determines how much heat is generated and whether ratings approach limiting thresholds (see qid:emb-elee-0158).

The second step is estimating power losses. For a linear regulator, losses equal `P = (V_in - V_out)*I_out`, with efficiency fundamentally limited by `V_out/V_in`.[^ti-slva079] This must be calculated for the worst-case operating combination: highest input voltage paired with highest load current. If thermal dissipation is excessive, alternative approaches must be evaluated – such as a switching converter or a pre-regulation step-down stage – before selecting a specific IC.

The third step is verifying requirements against the IC datasheet. First, check the recommended operating conditions: for example, in the TPS752-Q1, `V_I` must remain within 2.7–5.5 V and current must not exceed 2 A, whereas the absolute maximum input voltage is 6 V.[^ti-tps752q1-datasheet] These are distinct tables serving entirely different purposes: circuit design must be grounded in recommended operating conditions. Next, verify dropout voltage at maximum current: the datasheet defines minimum input voltage as `V_I(min) = V_O(max) + V_DO(max load)`.[^ti-tps752q1-datasheet] Then check output capacitor requirements: LDO manufacturers typically specify an acceptable compensation series resistance (ESR) window outside of which the regulator can oscillate, so capacitor dielectric type and ESR must match datasheet rules.[^ti-slva079] Capacitor placement and PCB layout must also follow datasheet recommendations.

The final step is thermal analysis. Actual dissipated power must not exceed `P_D(max) = (T_Jmax - T_A)/R_θJA`.[^ti-slva079] Permissible dissipation depends on board design and airflow: the TPS752-Q1 datasheet lists varying values for the PWP package across different test boards and airflow velocities.[^ti-tps752q1-datasheet]

**Example (illustrative, based on TPS752-Q1 data):** Requirements are `V_in = 4.5–5.5 V`, `V_out = 3.3 V`, `I_out(max) = 1 A`. Worst-case dissipation is `(5.5 - 3.3)*1 = 2.2 W`. According to the datasheet, for the PWP package on a 5 in x 5 in single-layer board in still air, allowable dissipation is `2.9 W` at `T_A <= 25 °C` and `1.9 W` at `T_A = 70 °C`.[^ti-tps752q1-datasheet] Thus, `2.2 W` is permissible at 25 °C, but fails at 70 °C: here, thermal constraints rather than voltage or current ratings dictate whether a heatsink, multi-layer copper plane, forced airflow, or a switching topology is required.

**Common mistakes:**

- Selecting an IC before establishing the input voltage range, peak load current, and permissible ripple.
- Checking only average or typical input voltages while ignoring minimum and maximum bounds.
- Designing to absolute maximum ratings instead of recommended operating conditions.
- Failing to calculate worst-case power dissipation and verify it against maximum ambient operating temperature.

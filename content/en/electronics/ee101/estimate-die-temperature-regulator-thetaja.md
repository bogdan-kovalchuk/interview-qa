---
id: emb-elee-0159
title: "How do you estimate the die temperature of a linear 12 V -> 5 V regulator at 0.2 A if `theta_JA` = 60 °C/W and `T_a` = 25 °C?"
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
  - source_id: ti-spra953d
    title: "Texas Instruments SPRA953D: Semiconductor and IC Package Thermal Metrics"
    url: https://www.ti.com/lit/an/spra953d/spra953d.pdf
---

## Short answer

For a linear regulator, power dissipation is `P = (12 - 5)*0.2 = 1.4 W`, yielding `T_j = T_a + P*theta_JA = 25 + 1.4*60 = 109 °C`.[^ti-slva079][^ti-spra953d] Compare this estimate against the datasheet maximum junction temperature with appropriate safety margin.[^ti-slva079] Because `theta_JA` depends heavily on PCB copper area and airflow, this is an estimate rather than a fixed universal constant.[^ti-spra953d]

## Detailed explanation

The estimation comprises two steps: converting electrical power into heat, and converting heat into temperature rise. In a linear regulator, the difference `V_in - V_out` drops across the pass element, so power dissipation is `P_D = (V_i - V_o)*I_o`; for 12 V, 5 V, and 0.2 A, this yields `7*0.2 = 1.4 W`.[^ti-slva079] More precisely, `V_i*I_q` is added to this value, where `I_q = I_i - I_o` is the quiescent current of the regulator itself, but at 0.2 A this term is typically negligible compared to 1.4 W.[^ti-slva079] The formula `P = (V_in - V_out)*I_out` holds only for linear regulators: in a switching converter, losses arise from different mechanisms and do not equal `(V_in - V_out)*I_out`.

The thermal resistance `theta_JA` indicates how many degrees hotter the die junction becomes relative to ambient air per watt of dissipated power: it is measured as the temperature rise divided by power under standardized test conditions.[^ti-spra953d] Hence `T_j = T_a + P*theta_JA`, which for our figures yields `1.4*60 = 84 °C` of temperature rise, resulting in `T_j = 25 + 84 = 109 °C`.[^ti-spra953d] This is an analog of Ohm's law: power corresponds to current, thermal resistance to electrical resistance, and temperature difference to voltage.

The primary limitation lies in the `theta_JA` parameter itself. TI emphasizes that `R_θJA` is measured on a standardized test board, whereas in a real system it depends heavily on board construction, meaning direct substitution into `T_J = T_A + R_θJA*Power` can yield substantially erroneous results; in JEDEC still-air measurements, 70–95% of die power is dissipated through the circuit board rather than the package surface.[^ti-spra953d] Consequently, 109 °C is only a first-order estimate. For accurate predictions, one must use `R_θJA(effective)` for the specific system, derived from thermal modeling or physical measurements.[^ti-spra953d]

The calculated result must be checked against ratings. LDO datasheets state maximum junction temperature, defining maximum permissible power dissipation as `P_D(max) = (T_Jmax - T_A)/R_θJA`; actual power must not exceed this value.[^ti-slva079] **Example (illustrative, `T_Jmax = 125 °C`):** `P_D(max) = (125 - 25)/60 = 1.67 W`, so 1.4 W is acceptable, but thermal headroom is only `125 - 109 = 16 °C`. If the ambient temperature inside the equipment enclosure is `T_a = 50 °C`, junction temperature reaches `T_j = 50 + 84 = 134 °C` – exceeding 125 °C; the maximum allowable `T_a` for this operating condition is `125 - 84 = 41 °C`. Thus, an operating point that is acceptable at 25 °C ambient can easily fail inside a warm enclosure.

**Common mistakes:**

- Using the datasheet `theta_JA` value as an exact constant for an arbitrary PCB design.
- Assuming `T_a = 25 °C` instead of the worst-case ambient temperature inside the equipment enclosure.
- Applying `P = (V_in - V_out)*I_out` to a switching converter.
- Failing to maintain adequate margin to maximum `T_j` and neglecting to re-evaluate at maximum input voltage and current.

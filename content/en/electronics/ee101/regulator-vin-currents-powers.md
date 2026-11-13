---
id: emb-elee-0134
title: "Regulator: `V_in` = 9 V, `V_Z` ≈ 5.1 V, R = 390 Ω. What are the currents and powers?"
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

Resistor current is `I_R = (9 - 5.1)/390 = 10 mA`. With a 5 mA load, approximately 5 mA remains for the Zener. Without load, the entire current flows through the Zener: `P_Z = 5.1*0.01 ≈ 51 mW`, while the resistor dissipates `P_R = 3.9²/390 ≈ 39 mW`. These values assume nominal `V_Z = 5.1 V`: real `V_Z` has manufacturing tolerance and varies with current.[^nexperia-an90031]

## Detailed explanation

The output stays near `V_Z = 5.1 V`, so `9 - 5.1 = 3.9 V` drops across the resistor, and the current through it is `I_R = 3.9/390 = 10 mA`. This current is largely independent of load as long as the Zener remains in breakdown, and it splits into parts: `I_Z = I_R - I_load`.[^fiore-rectification]

**Power dissipations.** Without load `I_Z = 10 mA`, so `P_Z = 5.1*0.01 = 51 mW` and `P_R = 3.9*0.01 = 39 mW`; together they total 90 mW, which matches the `9*0.01` drawn from the source. This is the worst-case condition for the Zener diode: it dissipates maximum power specifically at no load.[^nexperia-an90031] With a 5 mA load: `I_Z = 5 mA`, `P_Z = 5.1*0.005 = 25.5 mW`, the load receives the same power (25.5 mW), and the resistor continues to dissipate 39 mW because `I_R` has not changed. A 10 mA load would draw the entire resistor current: the Zener diode would turn off, regulation would be lost, and R and the load would form a divider.[^fiore-rectification]

**Tolerances and Zener operating point.** "5.1 V" is nominal. For the BZX84-C5V1, Nexperia specifies `V_Z = 4.8–5.4 V` at 5 mA, so `I_R` falls in the range from `(9 - 5.4)/390 = 9.2 mA` to `(9 - 4.8)/390 = 10.8 mA`.[^nexperia-bzx84] Consequently, with a 5 mA load, only ≈ 4.2 mA may remain for the Zener diode, which is less than the test current for `V_Z`. This is important because the maximum differential resistance for this series is 60 Ω at 5 mA, but reaches 480 Ω at 1 mA.[^nexperia-bzx84] Input voltage variations `V_in` transfer to the output roughly as a divider `r_dif/(R + r_dif)`: `60/(390 + 60) ≈ 0.13` at 5 mA (a 1 V change in `V_in` produces ≈ 0.13 V at the output) and `480/(390 + 480) ≈ 0.55` at 1 mA.

**Component power ratings and short circuit.** 51 mW in the Zener diode is well below the 250 mW allowed for the BZX84 at 25 °C,[^nexperia-bzx84] and 39 mW in the resistor is modest. However, if the output is shorted, the Zener diode is de-energized and the entire `V_in` drops across the resistor: `P_R = 9²/390 ≈ 208 mW` (≈ 83% of 0.25 W), so for reliability the resistor rating should include safety margin.

**Common mistakes:**

- Calculating `I_R = V_in/R = 9/390 ≈ 23 mA`, forgetting to subtract `V_Z`.
- Calculating `P_Z` as `V_in*I` instead of `V_Z*I_Z`.
- Assuming 5.1 V is exact and ignoring component tolerance and `r_dif`.
- Adding a 5 mA load and assuming the Zener margin is always sufficient.

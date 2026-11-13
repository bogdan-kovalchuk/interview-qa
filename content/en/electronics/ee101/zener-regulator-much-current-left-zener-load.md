---
id: emb-elee-0142
title: "Zener regulator 9 V / 5.1 V / 390 Ω: how much current is left for the Zener with a 10 kΩ and a 1 kΩ load?"
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

With the Zener in breakdown (`V_out ≈ V_Z = 5.1 V`), resistor current is `I_R = (9 - 5.1)/390 = 10 mA`, splitting between load and Zener.[^fiore-rectification] At 10 kΩ, the load draws `5.1/10000 = 0.51 mA`, leaving ≈ 9.49 mA for the Zener. At 1 kΩ, the load takes 5.1 mA, leaving ≈ 4.9 mA. These are nominal values: for a BZX84-C5V1, `V_Z` tolerance (4.8–5.4 V at 5 mA) allows residual current at 1 kΩ to range from about 3.8 to 6.0 mA.[^nexperia-bzx84]

## Detailed explanation

**Model.** As long as the Zener diode remains in reverse breakdown, it maintains approximately `V_Z` across the output, while the resistor absorbs the remaining source voltage: `I_R = (V_in - V_Z)/R`. This current splits between the load and the Zener diode, so `I_Z = I_R - I_load`.[^fiore-rectification] For `V_in = 9 V`, `V_Z = 5.1 V`, and `R = 390 Ω`, we have `I_R = 3.9/390 = 10 mA`, which is virtually independent of the load.

**Two load conditions.** With `R_L = 10 kΩ`, the load draws `5.1/10000 = 0.51 mA`, so `I_Z = 10 - 0.51 = 9.49 mA` and the Zener diode dissipates `5.1*9.49 ≈ 48 mW`. With `R_L = 1 kΩ`, the load draws `5.1/1000 = 5.1 mA`, leaving `I_Z = 10 - 5.1 = 4.9 mA` with `P_Z = 5.1*4.9 ≈ 25 mW`. That is, the heavier the load, the less current remains for the Zener diode; the sum `I_Z + I_load` remains constant and equals `I_R`.[^fiore-rectification]

**Tolerance and margins.** "5.1 V" is nominal. For a BZX84-C5V1, `V_Z` ranges from 4.8 to 5.4 V at 5 mA.[^nexperia-bzx84] For `V_Z = 5.4 V`, `I_R = 3.6/390 ≈ 9.23 mA`, whereas for `V_Z = 4.8 V`, `I_R = 4.2/390 ≈ 10.77 mA`. Therefore, with 1 kΩ: `I_Z = 9.23 - 5.4 = 3.83 mA` or `10.77 - 4.8 = 5.97 mA`; with 10 kΩ, it ranges from `9.23 - 0.54 ≈ 8.7 mA` to `10.77 - 0.48 ≈ 10.3 mA`. This spread stems from manufacturing tolerance, not arithmetic error.

**Is 4.9 mA sufficient.** Nexperia recommends sizing R1 so that at maximum load current the Zener diode receives at least the minimum operating current, which for diodes up to 17 V is approximately 5 mA, the test current for `V_Z`.[^nexperia-an90031] For this condition, the load should not draw more than `10 - 5 = 5 mA`, meaning `R_L ≳ 5.1/0.005 ≈ 1.02 kΩ`. Hence, 1 kΩ is already at the margin: the Zener diode is still conducting, but in the worst-case tolerance limit the residual current falls below 5 mA, and the maximum differential resistance of this series at 1 mA is 480 Ω versus 60 Ω at 5 mA, degrading output stability.[^nexperia-bzx84] For 10 kΩ, the operating margin is generous.

**Limits of applicability.** The calculation `I_Z = I_R - I_load` is meaningful only while `I_Z > 0`. If the load attempts to draw more than `I_R`, the Zener diode ceases conducting, regulation is lost, and the resistor and load form a voltage divider.[^fiore-rectification] The theoretical threshold here is `R_L = 5.1/0.01 = 510 Ω`; the 100 Ω case is analyzed in qid:emb-elee-0143.

**Common mistakes:**

- Calculating `I_R = V_in/R = 9/390 ≈ 23 mA`, forgetting to subtract `V_Z`.
- Calculating load current as `V_in/R_L` instead of `V_out/R_L`.
- Assuming 5.1 V is exact and ignoring the tolerance of `V_Z`.
- Applying `I_Z = I_R - I_load` even when the resulting current is negative.

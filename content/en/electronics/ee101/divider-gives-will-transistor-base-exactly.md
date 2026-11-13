---
id: emb-elee-0211
title: "A 47 kΩ / 10 kΩ divider from 10 V gives 1.75 V. Will the transistor base be at exactly 1.75 V?"
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
  - source_id: fiore-voltage-divider-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.4 Voltage Divider Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.4:_Voltage_Divider_Bias
---

## Short answer

No. The 1.75 V value is the open-circuit voltage of an unloaded divider; base current flows through the Thevenin equivalent resistance `R_TH`, producing a voltage drop so that `V_B = V_TH - I_B*R_TH` sits strictly below 1.75 V.[^fiore-voltage-divider-bias]

## Detailed explanation

An unloaded divider with `R_1` = 47 kΩ (pull-up to 10 V) and `R_2` = 10 kΩ (pull-down) yields `V_TH` = `V_CC`·`R_2`/(`R_1` + `R_2`) = 10·10/57 ≈ 1.754 V. The Thevenin equivalent resistance of the divider is `R_TH` = `R_1` || `R_2` = 47·10/57 ≈ 8.25 kΩ.[^fiore-voltage-divider-bias] The 1.75 V value is the voltage when no current is drawn from the divider. Connecting the base alters this condition.

The base draws a current `I_B` from the divider node. This current flows through `R_TH`, producing a voltage drop of `I_B`·`R_TH` across it. In Fiore, the base–emitter loop equation is written as `V_TH` = `I_B`·`R_TH` + `V_BE` + `I_E`·`R_E`, so `V_B` = `V_BE` + `I_E`·`R_E` = `V_TH` - `I_B`·`R_TH`.[^fiore-voltage-divider-bias] For example, with `I_B` = 10 µA, the drop is 8.25 kΩ · 10 µA ≈ 82 mV, giving `V_B` ≈ 1.754 - 0.082 ≈ 1.67 V.

The exact value of `V_B` depends on `I_B`, which in turn depends on `I_C` and the specific transistor's `β` (`I_B` = `I_C`/`β`).[^fiore-voltage-divider-bias] Therefore, one should never expect "exactly 1.75 V". Component tolerances compound this: a ±5% tolerance on each resistor can shift `V_TH` by more than 0.1 V. The proper verification procedure is to calculate `I_B` from the operating point, subtract `I_B`·`R_TH`, and compare the result with the measured voltage.

**Common mistakes:**

- Assuming the unloaded divider voltage appears at the base without subtracting `I_B`·`R_TH`.[^fiore-voltage-divider-bias]
- Taking `R_TH` as one of the individual resistors rather than `R_1` || `R_2`.[^fiore-voltage-divider-bias]
- Expecting an exact nominal value despite resistor tolerances: a ±5% tolerance shifts `V_TH` by more than 0.1 V.

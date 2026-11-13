---
id: emb-elee-0189
title: "What are the basic BJT current relations, and why does I_C = βI_B not always hold?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
  - source_id: fiore-bjt-datasheet
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.4 BJT Data Sheet Interpretation"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.4:_BJT_Data_Sheet_Interpretation
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

`I_E = I_C + I_B`; in the active region, `I_C = β*I_B` and `V_BE ≈ 0.7 V` for silicon, so `V_B = V_E + V_BE`. The formula fails in saturation where `I_C` is constrained by the external circuit rather than by `I_B`. For instance, with `I_B = 20 µA` and `β = 100`, the formula predicts 2 mA, but a circuit with 5 V and 5 kΩ permits only about 0.96 mA. Furthermore, β varies with current and temperature, making it only an approximation.[^fiore-bjt-basics][^mit-6071-bjt-notes][^fiore-bjt-datasheet]

## Detailed explanation

Currents are related by Kirchhoff's current law at the node: `I_E = I_C + I_B`. Because base current is small, `I_E ≈ I_C`. Current gain `β = I_C / I_B` for small-signal transistors typically ranges from 100–200, whereas for power transistors it is lower, around 25–50.[^fiore-bjt-basics]

The relation `I_C = β * I_B` is the equation for active mode: B–E is forward-biased, B–C is reverse-biased, and collector current is governed by base current rather than by the external circuit.[^mit-6071-bjt-notes] For example: with `I_B = 20 µA` and `β = 100`, active mode predicts `I_C = 2 mA`. For this current to flow through `R_C = 5 kΩ`, the voltage drop across the resistor would have to be `2 mA · 5 kΩ = 10 V`, whereas the supply delivers only 5 V. This operating point is physically unreachable.

The transistor then enters saturation. There, both junctions are forward-biased, and the maximum `I_C` is independent of `I_B` and `β`, equaling `(V_CC - V_CE(sat)) / R_C`.[^mit-6071-bjt-notes][^fiore-bjt-dc-load-line] For `V_CE(sat) ≈ 0.2 V`, we obtain `(5 - 0.2) / 5000 = 0.96 mA`. Then `I_C / I_B ≈ 0.96 mA / 20 µA ≈ 48`, which is less than `β = 100`. The formula `I_C = β * I_B` no longer applies here: the transistor cannot provide 2 mA, and its current is limited by `R_C`.

`β` is not a constant. For a given part number, it varies with `I_C` and temperature and differs between individual devices: in the 2N3904 datasheet, variation at 10 mA is roughly 3:1, and at very low or very high currents `β` drops off.[^fiore-bjt-datasheet] Therefore, calculating with a single nominal `β`, such as 100, is only an approximation. Circuits are designed with safety margins or intentionally operated in saturation, where `β` no longer governs current.[^mit-6071-bjt-notes]

**Common mistakes:**
- Assuming that `I_C = β * I_B` always holds regardless of `R_C` and `V_CC`: the external circuit limits collector current.[^fiore-bjt-dc-load-line]
- Treating `β` from a specification table as a constant: in the datasheet it is a range that depends on current and temperature.[^fiore-bjt-datasheet]
- Assuming that in saturation `I_C` increases proportionally with `I_B`: in saturation the maximum collector current is dictated by the circuit.[^mit-6071-bjt-notes]

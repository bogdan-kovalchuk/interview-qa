---
id: emb-elee-0133
title: "How does a shunt regulator with a Zener diode work?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

A series resistor R connects `V_in` to the output, the Zener diode connects cathode to output and anode to ground, and the load sits in parallel. Current through R splits between load and Zener: `I_R = (V_in - V_Z)/R = I_load + I_Z`.[^fiore-rectification] The output stays near `V_Z` only while the Zener remains in breakdown with at least its minimum operating current; if the load takes almost all resistor current, the Zener turns off, regulation is lost, and R and the load form a simple divider.[^nexperia-an90031]

## Detailed explanation

The operating principle is simple: a Zener diode in reverse breakdown maintains approximately `V_Z` across the output, while resistor R absorbs the difference `V_in - V_Z`. Therefore, the current through R is nearly constant: `I_R = (V_in - V_Z)/R`, and it splits between the load and the Zener diode: `I_R = I_load + I_Z`.[^fiore-rectification] The resistor sets the maximum current that can be delivered to the output, and the Zener absorbs whatever the load does not draw. Consequently, under light load most of the current flows through the Zener, whereas under heavy load it flows through the load, keeping total current drawn from the supply almost unchanged.[^fiore-rectification] The name "shunt regulator" comes from the fact that the Zener diode is placed in parallel with the load, shunting excess current from R to ground.

Regulation continues only as long as the Zener diode remains in breakdown. Nexperia recommends choosing R such that even at maximum load current a residual current flows through the Zener diode sufficient to keep it on the steep breakdown slope; as a minimum, they take the test current for `V_Z` from the datasheet, approximately 5 mA for `V_Z` up to 17 V and 2 mA for higher-voltage devices.[^nexperia-an90031] Hence `R = (V_in - V_Z)/(I_Z,min + I_load,max)`. If load current increases further, the Zener receives no current and turns off, regulation is lost, and R and the load behave as a resistive voltage divider.[^fiore-rectification]

**Example.** `V_in = 9 V`, `V_Z = 5.1 V`, load up to 10 mA, minimum Zener current 5 mA. Then `R ≤ 3.9/(0.005 + 0.010) = 260 Ω`; the nearest lower standard value in the E24 series is 240 Ω. With 240 Ω, `I_R = 3.9/240 ≈ 16.3 mA`, leaving ≈ 6.3 mA for the Zener diode at full load. With no load, the entire 16.3 mA flows through the Zener diode: `P_Z = 5.1*0.01625 ≈ 83 mW`, and `P_R = 3.9²/240 ≈ 63 mW`. In actual design calculations, worst-case values are used: minimum `V_in`, maximum `V_Z` within tolerance, and maximum load current.

The Zener diode dissipates maximum power specifically at no load because all of the current through R passes through it (`P_Z = V_Z*I_Z`), which makes this simple circuit suitable only for low power levels; for higher power, Nexperia shows a configuration where the output is taken from the emitter of a transistor whose base is tied to the Zener diode.[^nexperia-an90031] The output is also not perfectly rigid: due to `r_dif`, variations in `V_in` partially pass through to the output roughly as a divider `r_dif/(R + r_dif)`.

**Common mistakes:**

- Reversing the Zener diode: in the forward direction the output will be only ≈ 0.7 V.
- Calculating R from nominal values without accounting for worst-case conditions (minimum `V_in`, maximum load current) and losing regulation.
- Forgetting about Zener power dissipation in the no-load state.
- Expecting large output currents from such a regulator: it only redistributes the current delivered by R.

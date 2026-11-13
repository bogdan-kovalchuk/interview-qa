---
id: emb-elee-0135
title: "Which two extreme conditions must be checked for a Zener regulator?"
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

Two worst-case conditions must be checked. Minimum input voltage with maximum load current: the Zener may be starved of current, causing loss of regulation.[^fiore-rectification] Maximum input voltage with no load: the entire resistor current flows through the Zener, causing maximum dissipation.[^nexperia-an90031] Without a series resistor, current through the Zener is completely unlimited.[^fiore-rectification]

## Detailed explanation

In a simple regulator, a series resistor `R` connects the input to the output, and a Zener diode in reverse breakdown sits in parallel with the load. The voltage difference `V_in - V_Z` drops across `R`, so the current through it `I_R = (V_in - V_Z)/R` splits between the load and the Zener diode: `I_R = I_load + I_Z`.[^fiore-rectification] The Zener diode absorbs whatever the load does not draw, and the resistor sets the upper limit of the current that the circuit can deliver. Current `I_R` rises with `V_in`, while `I_load` determines how much of it remains for the Zener diode, so the extreme values of these two quantities yield two different ways to disrupt circuit operation.

**Case 1: minimum `V_in`, maximum `I_load`.** Here `I_R` is at its minimum, whereas the demand is at its maximum. If `I_load` nearly equals `I_R`, nothing is left for the Zener diode, it exits breakdown, regulation is lost, and `R` and the load function as a standard resistive divider.[^fiore-rectification] To prevent this, Nexperia recommends choosing `R` such that a residual current flows through the Zener diode even at maximum load: `R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max))`.[^nexperia-an90031] They advise using the datasheet test current for `V_Z` as the minimum current `I_Z(min)`, approximately 5 mA for `V_Z` up to 17 V.[^nexperia-an90031] For worst-case analysis, the lowest `V_in` is substituted into this formula. If the input is fed from a rectifier with a filter capacitor, `V_in` must be understood as the ripple trough under full load.[^fiore-rectification]

**Case 2: maximum `V_in`, zero `I_load`.** Now `I_R` is at its maximum and the entire current passes through the Zener diode: `I_Z = (V_in,max - V_Z)/R`, with dissipated power `P_Z = V_Z*I_Z`. Nexperia explicitly notes that the Zener diode dissipates maximum power with no load connected.[^nexperia-an90031] This power is compared against `P_tot` from the datasheet, specified for defined mounting conditions.[^nexperia-an90031] Without a series resistor, nothing limits the current and the Zener diode can be destroyed.[^fiore-rectification]

**Example (independent calculation).** `V_in` ranges from 9 to 12 V, `V_Z = 5.1 V`, load is 0–10 mA, and `I_Z(min) = 5 mA`. The upper limit for R is `R ≤ (9 - 5.1)/(0.005 + 0.010) = 3.9/0.015 = 260 Ω`; we choose 240 Ω (E24 series). At 9 V with 10 mA: `I_R = 3.9/240 = 16.25 mA`, leaving 6.25 mA for the Zener diode – regulation is maintained. At 12 V with no load: `I_R = 6.9/240 = 28.75 mA`, giving `P_Z = 5.1*0.02875 ≈ 0.147 W` and `P_R = 6.9²/240 ≈ 0.198 W`. In practice, tolerances on `V_Z` and `R` must also be factored in.

**Common mistakes:**

- Checking only the nominal `V_in` and failing to use a minimum that accounts for AC line variation and ripple.
- Overlooking the no-load condition (disconnected or malfunctioning load) and the resulting maximum Zener dissipation.
- Sizing `R` such that `I_Z(min)` becomes zero or drops below the breakdown knee.
- Omitting the series resistor `R` altogether under the assumption that the source is "weak."

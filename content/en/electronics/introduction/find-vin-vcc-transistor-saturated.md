---
id: emb-elintro-0212
title: "Find `I_B`, `I_C`, and `I_E` for a saturated NPN transistor: `V_in` = 5 V, `R_B` = 3.3 kΩ, `R_C` = 1 kΩ, `V_CC` = 5 V."
track: electronics
section: introduction
sources:
  - source_id: aac-bjt-saturation
    title: "All About Circuits: Transistor Ratings and Packages (BJT)"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/transistor-ratings-packages-bjt/
  - source_id: aac-bjt-active-mode
    title: "All About Circuits: Active-mode Operation (BJT)"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/active-mode-operation-bjt/
  - source_id: aac-bjt-beta-terms
    title: "All About Circuits: What Is BJT Beta? Understanding the Current Gain of a Bipolar Junction Transistor"
    url: https://www.allaboutcircuits.com/technical-articles/all-about-bjt-beta-understanding-terminology/
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

**Under the given model,** assume `V_BE` = 0.7 V and `V_CE(sat)` = 0.2 V. Then `I_B = (5 - 0.7)/3.3 kΩ ≈ 1.30 mA`, `I_C ≈ (5 - 0.2)/1 kΩ = 4.8 mA`, and `I_E = I_B + I_C ≈ 6.1 mA`. This is an estimate; actual voltages depend on the transistor and operating current.[^aac-bjt-saturation] The load limits `I_C`, so you cannot continue multiplying `I_B` by active beta after saturation.[^aac-bjt-active-mode]

## Detailed explanation

In the given circuit, the estimated currents are `I_B ≈ 1.30 mA`, `I_C ≈ 4.8 mA`, and `I_E ≈ 6.1 mA`, assuming `V_BE` = 0.7 V and `V_CE(sat)` = 0.2 V.

Assume an NPN transistor with the emitter grounded, a resistor `R_B` between `V_in` and the base, and `R_C` between `V_CC` and the collector. Also assume that the sources are ideal, the junctions are described by the assumed approximate voltages, and the transistor is indeed capable of reaching saturation. The voltage across `R_B` equals `V_in - V_BE`; Ohm's law then gives approximately 1.30 mA of base current.

The collector current in saturation is limited by the collector resistor and supply, not active beta: approximately `5 - 0.2 = 4.8 V` remains across `R_C`, so `I_C ≈ 4.8 mA`. For an NPN with outward emitter current, Kirchhoff's current law gives `I_E = I_C + I_B`, which is approximately 6.1 mA.[^aac-bjt-saturation]

**Worked example:**

```text
I_B = (5 - 0.7) / 3300 = 1.30 mA
I_C = (5 - 0.2) / 1000 = 4.80 mA
I_E = I_B + I_C = 6.10 mA
```

This is an educational approximation, not an exact prediction: real `V_BE` and `V_CE(sat)` values are determined by the datasheet under specified conditions. Verifying saturation requires comparing the available `I_B` with the forced beta required for the component; the component values alone do not prove that any transistor will saturate.[^aac-bjt-active-mode]

**Common mistake:** calculating `β*I_B` and taking the result as the actual `I_C`, even though the load may not be able to support such current.[^aac-bjt-active-mode]

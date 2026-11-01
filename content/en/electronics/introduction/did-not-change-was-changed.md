---
id: emb-elintro-0215
title: "Why did `I_B` remain unchanged when `R_C` was reduced from 1 kΩ to 330 Ω?"
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

**Base and collector currents flow through different branches.** If `V_in`, `R_B`, and the base–emitter junction have not changed, then in a simple circuit with separate loops `I_B ≈ (V_in - V_BE)/R_B` remains approximately constant. Changing `R_C` changes the allowable collector current and the operating point; a smaller resistance allows higher current at the same supply voltage.[^aac-bjt-active-mode] The independence is not absolute: the transistor may exit saturation, `V_BE` may change, and heating or source sag may affect `I_B`.[^aac-bjt-saturation]

## Detailed explanation

In a simple circuit, the base current is determined by the base loop, so changing `R_C` by itself usually does not change `I_B`.

For an NPN transistor with a grounded emitter, a separate resistor `R_B` from the control source to the base, and fixed `V_in` and `V_BE`, the base current is estimated as `I_B = (V_in - V_BE)/R_B`. `R_C` is located in the collector circuit, so replacing it does not enter this approximate equation. This separation of branches explains why, in an educational experiment, the base current remained approximately the same.

Collector current, on the other hand, is limited by the supply voltage, `R_C`, and the transistor. For the same `V_CC`, a smaller `R_C` allows a larger load current, provided the source and transistor can supply it. Replacing 1 kΩ with 330 Ω therefore alters the load line and may shift the operating point or pull the transistor out of saturation.[^aac-bjt-active-mode]

The independence of the currents is an approximation, not an absolute law for every topology. In a real circuit, `V_BE` depends on current and temperature; shared emitter resistance, supply sag, driver limits, or a change in operating region can indirectly alter `I_B`. Therefore, the statement applies to a circuit with an independent base supply and constant operating conditions.[^aac-bjt-saturation]

**Example:** for `V_in` = 5 V, `R_B` = 3.3 kΩ, and an approximate `V_BE` = 0.7 V, you obtain `I_B ≈ 1.30 mA` before and after replacing `R_C`, provided these quantities have not changed.

**Common mistake:** stating that the collector and base circuits have no effect on each other at all. Their operating points are coupled through the transistor, even though in this simple estimate `R_C` does not directly determine the base current.

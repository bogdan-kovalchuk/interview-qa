---
id: emb-elee-0197
title: "Does one large resistor from the supply to the base create a stable base voltage?"
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
  - source_id: fiore-bjt-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model
  - source_id: fiore-bias-need
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.2 The Need For Biasing"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.2:_The_Need_For_Biasing
  - source_id: fiore-voltage-divider-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.4 Voltage Divider Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.4:_Voltage_Divider_Bias
---

## Short answer

No: the resistor sets base current rather than base voltage. The base voltage is clamped by the forward-biased base-emitter junction to approximately 0.7 V, while the collector current `I_C = β*I_B` fluctuates with β, which varies widely between individual transistors and drifts with temperature.[^fiore-bjt-ebers-moll]

## Detailed explanation

A resistor `R_B` between supply `V_CC` and the base drops `V_CC - V_B`. With a forward-biased base–emitter junction and the emitter grounded, `V_B ≈ V_BE ≈ 0.7 V` for silicon.[^fiore-bjt-ebers-moll] Thus the drop across the resistor is nearly fixed, and base current is determined by the resistor itself: `I_B = (V_CC - V_BE) / R_B`. The resistor sets base current rather than base voltage, so choosing a large `R_B` is not a way to establish a stable base voltage: it merely reduces `I_B`, leaving collector current stability unimproved.

Collector current is subsequently governed by `β`, because `I_C = β * I_B`. The textbook examines such a circuit: base powered through `R_B` = 200 kΩ from 10 V, and collector powered through 1 kΩ from 15 V. At `β = 100`, this yields `I_B` = 46.5 µA, `I_C` = 4.65 mA, and `V_CE` = 10.35 V. At `β = 200`, the identical `I_B` results in double the collector current: `I_C` = 9.3 mA and `V_CE` = 5.7 V.[^fiore-bjt-ebers-moll] The operating point drifts directly with `β`, even though the base remains clamped near 0.7 V.

The textbook identifies this behavior as the chief drawback of base bias and describes the thermal effect: at constant `I_B`, higher `β` increases `I_C`, greater `I_C` generates more heat, and rising heat in turn increases `β`. The cycle can compound, necessitating an alternative topology for stability.[^fiore-bjt-ebers-moll]

A voltage divider provides a stable base voltage. Fiore refers to voltage divider bias as a high-stability configuration and approximates `V_B` by the open-circuit Thevenin voltage `V_TH` when the divider is lightly loaded. This approximation holds when `R_E` is significantly larger than `R_TH / β`; under this condition, `I_C` is virtually independent of `β`.[^fiore-voltage-divider-bias]

**Common mistakes:**

- Assuming `R_B` determines `V_B`: the voltage is clamped by `V_BE`, while the resistor establishes `I_B`.
- Believing a large `R_B` stabilizes the circuit: `I_C = β * I_B` remains directly dependent on `β`.
- Ignoring thermal positive feedback: as temperature rises, `β` increases and `I_C` climbs with it.[^fiore-bjt-ebers-moll]

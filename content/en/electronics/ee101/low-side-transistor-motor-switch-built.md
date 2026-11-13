---
id: emb-elee-0218
title: "How is a low-side transistor motor switch built?"
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
  - source_id: fiore-bjt-switching
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.7 BJT Switching and Driver Applications"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.7:_BJT_Switching_and_Driver_Applications
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
---

## Short answer

The emitter of an NPN transistor connects to ground, the collector connects to the negative motor terminal, and the positive motor terminal connects to the power supply. A base resistor sets and limits the control drive current into saturation.[^fiore-bjt-switching]

## Detailed explanation

**Topology.** A low-side switch transistor closes the circuit loop: positive supply -> motor -> collector -> emitter -> ground. Fiore's saturating LED driver uses the same arrangement: the transistor switches the path between supply, load, and collector resistor, with the emitter tied to ground. Fiore also presents direct DC motor control using a saturated BJT switch.[^fiore-bjt-switching] Because the emitter sits on the common ground rail, the control drive voltage is ground-referenced, and the motor receives full rail voltage when the transistor conducts.

**Base drive.** A logic drive voltage `V_in` establishes base current `I_B = (V_in - V_BE)/R_B`, where `V_BE` for silicon is approximately 0.7 V.[^fiore-bjt-basics] As an illustrative example: let `V_in = 5 V` and `R_B = 430 Ω`, giving `I_B = (5 - 0.7)/430 ≈ 10 mA`. Suppose the motor draws `I_C = 100 mA`, and transistor β is at least 100. Then `I_C/I_B = 10`, which is tenfold lower than β. This condition ensures saturation: collector current is limited by the external circuit rather than by β.[^fiore-bjt-switching]

**Power dissipation.** In saturation, `V_CE(sat)` drops to a few tenths of a volt.[^fiore-bjt-collector-curves] Assuming `V_CE(sat) = 0.2 V`, transistor dissipation is only `0.2 V * 0.1 A = 20 mW`. If the transistor operated in the linear region at `V_CE = 6 V` with the same 100 mA current, power dissipation would be `0.6 W`. Therefore, the switch operates strictly between two states: fully on or fully off.

**Common mistakes:**

- Choosing `R_B` too small: excessive base current needlessly loads the control logic source.
- Choosing `R_B` too large: `I_B` becomes insufficient, driving `I_C/I_B` close to β, preventing full saturation and causing transistor overheating.[^fiore-bjt-switching]
- Omitting the flyback diode across the motor winding: turn-off generates an inductive voltage spike that can destroy the switching transistor (see qid:emb-elee-0219).[^fiore-bjt-switching]

---
id: emb-elee-0193
title: "How does an emitter resistor stabilize the collector current?"
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
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
  - source_id: fiore-pn-junction
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 2.2 The PN Junction"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.2:_The_PN_Junction
  - source_id: fiore-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model
---

## Short answer

If `V_B` is held constant, then `V_E ≈ V_B - V_BE`, and `R_E` sets the emitter current according to `I_E = (V_B - V_BE)/R_E`.[^fiore-emitter-bias] Any increase in current raises `V_E`, which reduces `V_BE` and throttles the transistor, acting as local negative feedback.[^fiore-pn-junction]

## Detailed explanation

Suppose the base receives a stable voltage `V_B` from a low output impedance source. When the base–emitter junction conducts, its voltage drop is approximately 0.7 V for silicon, setting the emitter potential to `V_E = V_B - V_BE`.[^libretexts-fiore-diode-models] Emitter current is established by the resistor: `I_E = V_E / R_E = (V_B - V_BE) / R_E`. In this approximation, `β` scarcely enters the expression because current is dictated by the base voltage and emitter resistance.[^fiore-emitter-bias]

Collector current is `I_C = α * I_E`, where `α = β / (β + 1)`. For `β = 100`, `α = 0.99`, so `I_C` differs from `I_E` by only 1%.[^mit-6071-bjt-notes]

Now suppose an effect increases `I_C`, such as higher `β` or rising temperature. Then `I_E` increases as well, increasing the voltage drop `V_E = I_E * R_E`. Because `V_B` is held constant, `V_BE = V_B - V_E` decreases. Junction current depends exponentially on `V_BE`, so it drops and pulls `I_C` back down.[^fiore-pn-junction] The output current reduces the controlling voltage that produced it, providing negative feedback.

For example: `V_B` = 2.0 V, `V_BE` = 0.7 V, and `R_E` = 1 kΩ yield `I_E` = 1.30 mA. With `β = 100`, `I_C = 0.990 × 1.30 ≈ 1.287 mA`, while with `β = 200`, `I_C = 0.995 × 1.30 ≈ 1.294 mA`. Doubling `β` changes current by less than 0.5%. In contrast, with fixed base current biasing, doubling `β` doubles `I_C`.[^fiore-ebers-moll]

Stabilization has limits. If `V_B` is supplied by a voltage divider with equivalent Thevenin resistance `R_B`, base current `I_B` pulls `V_B` down by `I_B * R_B`. The approximation `I_C = (V_B - V_BE) / R_E` is valid only when `R_E` is significantly larger than `R_B / β`.[^fiore-emitter-bias] A second constraint is `V_BE` itself: with `V_E ≈ 0.2 V` and `R_E = 1 kΩ`, current `I_E ≈ 0.2 mA`, and an error of 0.1 V in `V_BE` alters current by 0.1 mA, representing a 50% shift. Therefore, a very low `V_E` fails to provide current stabilization.

**Common mistakes:**

- Assuming `R_E` stabilizes current regardless of base circuitry: a divider with high equivalent resistance `R_B` allows `I_B` to drag down base voltage.
- Treating 0.7 V as an exact constant: any error in `V_BE` directly translates into current variation as `ΔV_BE / R_E`.
- Setting `V_E` too low: slight changes in `V_BE` then cause large proportional current variations.

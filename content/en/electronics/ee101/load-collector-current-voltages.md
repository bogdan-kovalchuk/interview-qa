---
id: emb-elee-0194
title: "`V_B` = 1.7 V, `R_E` = 1 kΩ, β = 100, 1 kΩ load from +5 V to the collector. What are the current and voltages?"
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
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias
  - source_id: fiore-pn-junction
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 2.2 The PN Junction"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.2:_The_PN_Junction
---

## Short answer

With `V_BE ≈ 0.7 V`[^libretexts-fiore-diode-models], the emitter current is `I_E = (1.7 - 0.7)/1000 = 1 mA`, yielding `I_C = β/(β+1)*I_E = 0.990 mA` for β = 100.[^mit-6071-bjt-notes] The node voltages are `V_E ≈ 1 V` and `V_C = 5 - 0.99 = 4.01 V`, providing ample headroom for active mode because `V_CE ≈ 3 V`, well above typical `V_CE(sat)` values of a few tenths of a volt.[^fiore-bjt-dc-load-line]

## Detailed explanation

The circuit configuration is as follows: the base receives voltage `V_B` = 1.7 V from a low output impedance source, the emitter is connected to ground through `R_E` = 1 kΩ, and the collector connects to +5 V through a 1 kΩ load. For silicon, the base–emitter forward drop is taken as 0.7 V.[^libretexts-fiore-diode-models] This is a behavioral approximation: actual `V_BE` varies with current and temperature.[^fiore-pn-junction] Then `V_E = V_B - V_BE` = 1.0 V and `I_E = V_E / R_E` = 1.00 mA.

Collector current is found via `I_E`. Base current is `I_B = I_E / (β + 1)` ≈ 9.90 µA, giving `I_C = β * I_B` ≈ 0.990 mA. This is identical to `I_C = β / (β + 1) * I_E`, corresponding to α = 0.99 at β = 100.[^mit-6071-bjt-notes] Node voltage at the collector is: `V_C = V_CC - I_C * R_C = 5 - 0.99 * 1 = 4.01 V`.[^fiore-emitter-bias]

Operating mode verification: `V_CE = 4.01 - 1.00 = 3.01 V`, and `V_CB = 4.01 - 1.70 = 2.31 V`. The collector–base junction is reverse-biased because `V_C` exceeds `V_B`, and the emitter–base junction is forward-biased, confirming active mode operation. Saturation only occurs when `V_CE` drops to tenths of a volt.[^fiore-bjt-dc-load-line]

The emitter resistor makes current largely insensitive to `β`: at `β = 200`, `I_C` = 0.995 mA, which is only 0.5% higher.[^fiore-emitter-bias] The primary uncertainty here is not `β`, but `V_BE`. An error of 0.1 V in `V_BE` alters `V_E` by 0.1 V and therefore `I_E` by 0.1 mA, a 10% change. Calculations should account for a range of `V_BE` rather than assuming a single fixed value.

An ideal `V_B` source is an essential assumption. If `V_B` is produced by a divider with a 10 kΩ Thevenin resistance, base current of 9.9 µA drags it down by roughly 0.1 V (`I_B * R_B ≈ 0.099 V`), altering `I_E` by 10%. Thus, base voltage uncertainty has the same effect as `V_BE` uncertainty.

**Common mistakes:**

- Multiplying `I_E` by `β` instead of `β / (β + 1)`: using `I_C = β * I_E` overestimates current by 100-fold.
- Treating `V_BE` as exactly 0.7 V without considering its tolerance range.
- Failing to verify that `V_C` is higher than `V_B`: otherwise the transistor leaves active mode.

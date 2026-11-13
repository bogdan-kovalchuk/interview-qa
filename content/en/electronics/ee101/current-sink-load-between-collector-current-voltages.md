---
id: emb-elee-0224
title: "Current sink: `V_B` = 1.7 V, `R_E` = 100 Ω, 220 Ω load between +9 V and the collector. What are the current and voltages?"
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
  - source_id: rohm-bjt-basics
    title: "ROHM: Bipolar Junction Transistor (BJT) Basics: Operation and Applications (NPN & PNP)"
    url: https://techweb.rohm.com/product/transistors-diodes/transistors/27319/
---

## Short answer

With `V_BE ≈ 0.7 V`, emitter current is `I_E = (1.7 - 0.7)/100 = 10 mA`, and `I_C ≈ I_E`.[^fiore-bjt-basics] The load voltage drop is approximately 2.2 V, leaving `V_C ≈ 6.8 V` and `V_E ≈ 1 V`, which confirms active-mode operation with sufficient headroom.[^mit-6071-bjt-notes]

## Detailed explanation

The circuit is an NPN transistor current sink: the base has a fixed voltage `V_B = 1.7 V`, and the current is set by resistor `R_E` in the emitter. Emitter voltage is `V_E = V_B - V_BE`. For silicon, `V_BE ≈ 0.7 V`,[^fiore-bjt-basics] so `V_E ≈ 1.0 V` and `I_E = V_E / R_E = 1.0 / 100 = 10 mA`. Emitter current is the sum of collector and base currents: `I_E = I_C + I_B`.[^fiore-bjt-basics] When `I_C` is much greater than `I_B`, the collector current almost equals the emitter current.[^fiore-bjt-basics] With β = 100, `α = β / (β + 1) ≈ 0.99`, so `I_C ≈ 9.9 mA`, which is about 1% less.[^mit-6071-bjt-notes]

A current of 10 mA flows through the 220 Ω load: the drop is `220 Ω * 0.01 A = 2.2 V`, so `V_C = 9 - 2.2 = 6.8 V`, and `V_CE = 6.8 - 1.0 = 5.8 V`. In the active region, the base–emitter junction is forward-biased, the base–collector junction is reverse-biased, and `V_BE < V_CE < V_CC`; here `0.7 < 5.8 < 9`.[^mit-6071-bjt-notes]

There are two limitations. First, `V_BE` affects the current: with `V_BE = 0.6 V`, the current would be `(1.7 - 0.6) / 100 = 11 mA`; with 0.8 V, it would be `(1.7 - 0.8) / 100 = 9 mA`. That is, an error of 0.1 V gives about a 10% error in current. For the active mode, typical `V_BE` is 0.6–0.7 V.[^rohm-bjt-basics] Second, the active mode requires the collector to remain higher than the base, that is, `V_C > V_B`. For 10 mA, this means `R_L * 10 mA < 9 - 1.7 = 7.3 V`, hence `R_L < 730 Ω`. A higher resistance causes the base–collector junction to become forward-biased, and the transistor leaves the active mode.[^mit-6071-bjt-notes]

**Common mistakes:**

- Assuming `I_C = β * I_B` for a current sink without checking the operating region: in saturation, this relationship is nonlinear.
- Ignoring the dependence of current on `V_BE`: an error of 0.1 V causes roughly a 10% error in current.
- Using a load greater than approximately 730 Ω: the collector drops below the base, and the current sink ceases to hold 10 mA.

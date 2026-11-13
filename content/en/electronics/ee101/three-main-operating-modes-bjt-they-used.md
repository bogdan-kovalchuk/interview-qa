---
id: emb-elee-0188
title: "What are the three main operating modes of a BJT, and where are they used?"
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
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

In cutoff, the base-emitter junction is not forward-biased, collector current is virtually zero, and the transistor acts as an open switch. In active mode, base-emitter is forward-biased and base-collector is reverse-biased, enabling linear amplification. In saturation, both junctions are forward-biased, acting as a closed switch.[^mit-6071-bjt-notes] Active mode is used in analog amplifiers, while saturation is used in digital switching.[^fiore-bjt-collector-curves]

## Detailed explanation

The operating mode is determined by the bias state of two junctions: base–emitter (B–E) and base–collector (B–C). For an NPN in normal operation, three modes are fundamental, each corresponding to a distinct region on the collector characteristic curves. To the left lies saturation, and to the right lies breakdown, which must be avoided. In the middle lies an almost horizontal region where collector current depends only weakly on collector–emitter voltage; this is the active region.[^fiore-bjt-collector-curves][^mit-6071-bjt-notes]

In active mode, B–E is forward-biased, so electrons from the emitter enter the base, and most of them reach the collector. The collector current is controlled by the base current: `I_C = β * I_B`. This produces amplification, because a small change in `I_B` induces a `β`-times larger change in `I_C`. This relationship holds as long as B–C remains reverse-biased, that is, while `V_BE < V_CE < V_CC`.[^mit-6071-bjt-notes]

In cutoff, B–E does not conduct, base current is zero, and consequently collector current is also zero. The switch is open, and collector–emitter voltage equals the supply voltage because the voltage drop across the collector resistor is zero.[^fiore-bjt-dc-load-line] In saturation, both junctions are forward-biased, `I_C` is determined by the external circuit, and its maximum equals `(V_CC - V_CE(sat)) / R_C`. The voltage `V_CE(sat)` is small, around 0.2 V, so the switch is closed, and `β` no longer controls the current.[^mit-6071-bjt-notes]

Consequently, active mode is used in linear amplifiers, where the output current must reproduce the input signal. Cutoff and saturation are used in switching circuits: the transistor either does not conduct or conducts full current determined by the load.[^fiore-bjt-collector-curves]

**Common mistakes:**
- Assuming active mode is maintained for any `R_C`: a large `R_C` or low `V_CC` reduces `I_C(sat)`, preventing `I_C` from reaching `β * I_B`, so the transistor saturates.[^fiore-bjt-dc-load-line]
- Confusing cutoff with saturation: in cutoff `V_CE ≈ V_CC` and `I_C ≈ 0`, whereas in saturation `V_CE ≈ 0.2 V` and current is set by `R_C`.[^mit-6071-bjt-notes]

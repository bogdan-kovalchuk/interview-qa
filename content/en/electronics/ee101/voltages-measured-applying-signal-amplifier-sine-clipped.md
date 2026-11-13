---
id: emb-elee-0212
title: "Why should DC voltages be measured before applying a signal to an amplifier, and what should you do if the sine wave is clipped?"
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
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
---

## Short answer

Without an established Q-point, the stage may already sit in cutoff or saturation before an AC signal arrives, so `V_B`, `V_E`, and `V_C` must first be verified without input.[^mit-6071-bjt-notes] If the output sine wave clips, check the operating point: if biasing is correct, reduce the input signal amplitude; if biasing is shifted, correct the bias resistor network.[^fiore-bjt-dc-load-line]

## Detailed explanation

The AC signal rides on top of the DC operating point, so the quiescent point must be verified first.[^fiore-bjt-ac-model] For a silicon transistor, `V_BE` ≈ 0.7 V, which requires `V_E` = `V_B` - 0.7 V.[^fiore-bjt-basics] If the measured `V_B` and `V_E` do not satisfy this relationship, the bias network is malfunctioning before any signal is even applied. Applying an AC signal in this condition is counterproductive: it reveals a symptom rather than the root cause.

Two extreme states are immediately apparent from DC voltage measurements. Cutoff: `I_C` = 0, so there is no drop across `R_C`, pulling `V_C` ≈ `V_CC`.[^mit-6071-bjt-notes] Saturation: `V_CE` ≈ 0.2 V, so `V_C` ≈ `V_E` + 0.2 V.[^mit-6071-bjt-notes] If `V_C` sits near `V_CC` or near `V_E`, the stage is already at its boundary, causing the sine wave to clip even at small signal amplitudes.

The DC load line shows the range of voltages the output can assume. Its endpoints are cutoff at `V_CE` = `V_CC` and saturation at `I_C(sat)` ≈ (`V_CC` - `V_CE(sat)`)/(`R_C` + `R_E`) (or simplified as `V_CC`/`R_C` for a grounded-emitter stage).[^fiore-bjt-dc-load-line] Positioning the Q-point between these limits provides headroom for bidirectional voltage swings. If the peak swing exceeds this available headroom, the output sine wave clips even with proper biasing; the correct solution in that case is to reduce the input signal amplitude.

In a common-emitter stage, the output is taken from the collector, which inverts the signal.[^fiore-bjt-ac-model] Therefore, clipping of the positive output peak indicates that the collector is hitting `V_CC` (cutoff), while clipping of the negative output peak indicates that the collector is hitting `V_E` + 0.2 V (saturation).[^mit-6071-bjt-notes]

**Common mistakes:**

- Applying a signal without first verifying DC voltages: clipping may stem from a shifted Q-point rather than excessive input amplitude.
- Assuming clipping can always be resolved by lowering amplitude: if the Q-point is near one end of the load line, even small signals clip on one side.[^fiore-bjt-dc-load-line]

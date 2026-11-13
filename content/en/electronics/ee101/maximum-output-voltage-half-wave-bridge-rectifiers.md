---
id: emb-elee-0136
title: "What maximum output voltage do half-wave and bridge rectifiers give from a 5 V peak sine?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
  - source_id: vishay-1n4001
    title: "Vishay: 1N4001 to 1N4007 general purpose plastic rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---

## Short answer

For silicon diodes with `V_F ≈ 0.7 V`, a half-wave rectifier yields a peak of `5 - 0.7 = 4.3 V` because only one diode is in the conducting path.[^fiore-rectification] A bridge rectifier yields `5 - 2*0.7 = 3.6 V` because two diodes conduct in series during each half-cycle.[^fiore-rectification] While input voltage remains below diode drop thresholds, the diodes conduct negligibly, keeping output near zero around sine zero-crossings.[^fiore-rectification]

## Detailed explanation

The maximum output voltage (peak) is the input peak minus the diode drops in the conduction path. In a half-wave circuit, a single diode sits in series with the load: during the positive half-cycle it conducts and the output equals the input voltage minus `V_F`, while during the negative half-cycle it is off and the output is zero.[^fiore-rectification] For a sine wave with a 5 V peak and `V_F = 0.7 V`, we have `5 - 0.7 = 4.3 V`. The textbook emphasizes that at small input amplitudes (3–4 V), a 0.7 V drop is a substantial fraction of the input and cannot be neglected.[^fiore-rectification]

A bridge rectifier utilizes both half-cycles, but the load current passes sequentially through two diodes of the conducting diagonal pair, so the load sees the full input source voltage minus two forward drops.[^fiore-rectification] Therefore, the peak output voltage equals `5 - 2*0.7 = 3.6 V`. The bridge wins in efficiency (the entire input cycle is used), but loses in peak output voltage.

**Why output is small near zero.** The diode model with a 0.7 V knee voltage is a behavioral approximation rather than a literal 0.7 V source.[^libretexts-fiore-diode-models] A diode conducts significant current only when the input voltage reaches approximately 0.6–0.7 V.[^fiore-rectification] Under this model, in a half-wave circuit the output remains zero as long as `v_in < 0.7 V`, which corresponds to an interval of `asin(0.7/5) ≈ 8°` around each zero crossing. In a bridge, the threshold is twice as high: `v_in < 1.4 V`, giving `asin(1.4/5) ≈ 16°` on either side of zero, totaling about 32° out of each 180° half-cycle, or roughly 18%.

**Limitations.** This calculation applies to a constant `V_F` model. The real `V_F` varies with current: for 1N4001 diodes the maximum is 1.1 V at 1 A.[^vishay-1n4001] If both bridge diodes had 1.1 V drops, the peak from 5 V would be only `5 - 2.2 = 2.8 V`, and in the half-wave circuit `5 - 1.1 = 3.9 V`. Furthermore, 5 V peak is not 5 V RMS: the RMS value of a 5 V peak sine wave is `5/sqrt(2) ≈ 3.54 V`, and diode drops are subtracted specifically from the peak. No filter capacitor is included in this calculation; with a filter capacitor, the output waveform is completely different.

**Common mistakes:**

- Subtracting only one diode drop for a bridge or two drops for a half-wave circuit.
- Subtracting the diode drop from the RMS value rather than the peak.
- Assuming 0.7 V is an exact value for any diode and current.

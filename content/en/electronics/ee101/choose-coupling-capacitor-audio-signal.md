---
id: emb-elee-0022
title: "How do you choose a coupling capacitor for an audio signal (20 Hz–20 kHz) with R = 10 kΩ?"
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
  - source_id: aac-capacitor-highpass
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
---

## Short answer

For a targeted attenuation limit, choose an RC high-pass cutoff frequency safely below 20 Hz and calculate `C = 1/(2*π*R*f_c)`. Assuming `R = 10 kΩ` and `f_c = 2 Hz`, this yields `C ≈ 8.0 µF`; a standard 8.2 µF value provides a close match.[^aac-capacitor-highpass]

## Detailed explanation

The capacitance of an audio coupling capacitor is determined by the desired lower cutoff frequency rather than the full 20 Hz–20 kHz audio band alone. In the simplest RC model, a capacitor in series with a load forms a high-pass filter: its impedance increases at lower frequencies, so the low-frequency limit sets the capacitance requirement. The cutoff frequency represents the −3 dB point for a simple first-order filter, not a hard threshold below which signals abruptly vanish.[^aac-capacitor-highpass]

For this model, the relation `f_c = 1/(2*π*R*C)` applies, yielding `C = 1/(2*π*R*f_c)`. Choosing `f_c = 2 Hz` with `R = 10 kΩ` calculates to roughly `7.96 µF`, making a standard `8.2 µF` value a practical choice. At 20 Hz, this first-order filter operates a decade above cutoff, so its attenuation is minimal but non-zero. For a different target response, select a different `f_c` and recalculate capacitance.[^aac-capacitor-highpass]

A key constraint is the value of `R`. This must be the effective resistance seen by the capacitor rather than an arbitrary resistor in the schematic. In an amplifier, this value can be affected by the source output impedance and the input impedance of the following stage; if multiple coupling capacitors are cascaded, their combined filtering effects can push the overall low-frequency limit higher. One must also account for capacitance tolerance and, for certain ceramic capacitors, the reduction of effective capacitance caused by DC bias.[^aac-capacitor-highpass]

**Common mistake:** calling `8 µF` the only correct answer without stating the criteria. That value is valid specifically for `R = 10 kΩ` and a selected `f_c = 2 Hz`; the 20 Hz–20 kHz range mentioned in the question defines the audio band, but does not by itself establish the allowable attenuation at 20 Hz.

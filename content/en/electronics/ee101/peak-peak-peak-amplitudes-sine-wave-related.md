---
id: emb-elee-0076
title: "How are the RMS, peak and peak-to-peak amplitudes of a sine wave related?"
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
---

## Short answer

For a sine wave without DC offset, `V_RMS = V_peak/√2 = V_pp/(2√2)`, and `V_pp = 2*V_peak`. The RMS value represents the heating-equivalent DC voltage. These relationships cannot be directly applied to an arbitrary waveform.[^aac-alternating-current]

## Detailed explanation

For a pure sine wave without a DC component, peak amplitude `V_peak` is measured from the center level to the crest, and peak-to-peak amplitude `V_pp` is measured from the trough to the crest. Therefore, `V_pp = 2*V_peak`. RMS is the square root of the mean squared instantaneous voltage over a period; for a sine wave, integration yields `V_RMS = V_peak/√2`, and consequently `V_RMS = V_pp/(2√2)`.[^aac-alternating-current]

Example: a sine wave with `V_peak = 10 V` has `V_pp = 20 V` and `V_RMS ≈ 7.07 V`. Conversely, if an oscilloscope displays `V_pp = 2 V`, the RMS value is approximately `0.707 V`, but only under the stated assumptions. RMS is not simply the "average value" of the signal: the average over a full period of a symmetrical sine wave is zero, whereas RMS is positive and directly related to power dissipation in a resistor.[^aac-alternating-current]

If the signal has a DC offset, its peaks relative to zero are asymmetrical: peak-to-peak still equals the difference between the upper and lower levels, but the total RMS voltage also includes the DC contribution. For a distorted or pulsed waveform, the relationship between peak and RMS depends on the waveform shape; use a true RMS meter with sufficient bandwidth. A standard averaging multimeter is typically calibrated to read RMS only for a sine wave.[^aac-alternating-current]

**Common mistakes:**
- Confusing peak with peak-to-peak and missing a factor of two.
- Using the sinusoidal relationship for an arbitrary waveform.
- Ignoring DC offset or the meter's limited bandwidth.

When comparing a simulator, signal generator, and oscilloscope, verify whether each displays RMS, peak, or peak-to-peak, and whether the signal includes a DC offset. A label of "1 V" without an amplitude convention is insufficient for an unambiguous comparison.[^aac-alternating-current]

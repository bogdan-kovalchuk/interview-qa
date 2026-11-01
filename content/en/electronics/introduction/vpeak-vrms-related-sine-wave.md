---
id: emb-elintro-0084
title: "How are `V_peak`, `V_pp`, and `V_rms` related for a sine wave?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-ac-magnitude
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude/
---
## Short answer

For a pure sine wave, `V_pp = 2*V_peak`, and `V_rms = V_peak/sqrt(2)`. Thus, `230 V RMS` corresponds to a peak of approximately `325 V`; these relationships do not apply to an arbitrary waveform.[^aac-ac-magnitude]

## Detailed explanation

For a sine wave with zero mean, `V_peak` is the maximum instantaneous voltage relative to zero, whereas `V_pp` is the total span from minimum to maximum. A symmetrical wave has a negative peak of `-V_peak` and a positive peak of `+V_peak`, so `V_pp = 2*V_peak`. RMS is defined as the square root of the mean squared instantaneous voltage over a cycle; for a sine wave, this yields `V_rms = V_peak/sqrt(2)`.[^aac-ac-magnitude]

These quantities describe different aspects of the same signal. Peak-to-peak is useful for checking whether a signal fits within an input dynamic range, while RMS relates to the heating of a resistive load. Symmetrical pure sine waves without DC offset are assumed in the formulas; if the wave has an offset, asymmetry, or distortion, the total RMS value is no longer determined by `V_peak` alone.[^aac-ac-magnitude]

Example: for a `230 V RMS` sine wave, the amplitude is `V_peak = 230*sqrt(2) ≈ 325 V`, and `V_pp ≈ 650 V`. The nominal RMS value of the mains does not mean that the instantaneous voltage is 230 V at all times; it varies between peaks. Common mistake – calling 230 V the peak voltage or confusing `V_pp` with the distance from zero to a single peak.[^aac-ac-magnitude]

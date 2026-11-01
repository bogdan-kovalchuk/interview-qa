---
id: emb-elintro-0078
title: "What is `RMS` and why is it used for `AC`?"
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
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude
---
## Short answer

`RMS` (Root Mean Square) is the root-mean-square value that, for a resistor, produces the same average power as an equivalent `DC` voltage. For a pure sine wave, `V_rms = V_peak/√2`; this relationship is not universal for other waveforms.[^aac-ac-magnitude]

## Detailed explanation

`RMS` is the root-mean-square value of voltage or current. For a resistive load, it indicates what `DC` value would produce the same average power, making it convenient for describing a periodic signal that continuously varies.[^aac-ac-magnitude]

The simple average value of a pure sine wave over a full cycle is zero: the positive and negative half-waves cancel each other out. However, resistor heating depends on the square of the instantaneous voltage, `P = V²/R`. Squaring makes the contribution of both half-waves positive. You obtain RMS by squaring the instantaneous values, averaging them over a period, and taking the square root.[^aac-ac-magnitude]

For a pure sine wave, averaging the squares gives half the square of the amplitude, hence `V_rms = V_peak/√2`, approximately `0.707*V_peak`. Do not confuse amplitude with peak-to-peak span from minimum to maximum: `V_pp = 2*V_peak`. Substituting `V_pp` instead of `V_peak` would overestimate RMS by a factor of two. For square, pulse, or distorted waveforms, you must calculate RMS from the waveshape rather than applying the sine wave factor.[^aac-ac-magnitude]

**Example:** if a sine wave has a peak of `10 V`, its `RMS` is approximately `7.07 V`. Such a voltage across the same resistor creates the same average power as `7.07 V DC`. This equivalence applies to the heating effect on a resistor; other loads may exhibit additional frequency-dependent effects.[^aac-ac-magnitude]

**Common mistake:** assuming that RMS is a simple average or always `0.707` of the peak. First determine the waveshape and whether the given value is peak, `RMS`, or peak-to-peak.[^aac-ac-magnitude]

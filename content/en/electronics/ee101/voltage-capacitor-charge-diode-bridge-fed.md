---
id: emb-elee-0129
title: "To what voltage does the capacitor charge after a diode bridge fed from 6 V RMS?"
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
  - source_id: libretexts-fiore-rectification
    title: "Fiore: Semiconductor Devices, 3.2 Rectification (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: vishay-1n4001
    title: "Vishay: 1N4001 to 1N4007 general purpose plastic rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---

## Short answer

For a sinusoidal source, `V_peak = sqrt(2)*6 ≈ 8.49 V`. Subtracting two diode drops of 0.7 V gives `V_C,max ≈ V_peak - 2*V_F ≈ 7.09 V`.[^libretexts-fiore-rectification] This estimate assumes light load: at higher currents, `V_F` increases (up to 1.1 V at 1 A for a 1N4001), resulting in lower voltage.[^vishay-1n4001]

## Detailed explanation

6 V RMS is the root-mean-square value, while a capacitor charges to the peak value. For a sine wave `V_peak = sqrt(2)*V_RMS`, so `V_peak = 1.41421*6 ≈ 8.485 V`. It is this peak, not 6 V, that serves as the upper voltage bound to which the diode bridge could charge the capacitor if the diodes were ideal.

In a bridge rectifier, current flows through two diodes in series during each half-cycle, so the load and capacitor see the secondary voltage minus two forward drops.[^libretexts-fiore-rectification] The capacitor charges until its voltage equals `V_peak - 2*V_F`; past the peak, the diodes become reverse-biased, leaving the capacitor charged. With `V_F = 0.7 V`, we have `V_C,max ≈ 8.485 - 2*0.7 = 7.085 ≈ 7.09 V`. Under light load, the output floats to the secondary peak with virtually no ripple, but as load current increases, ripple grows and the nominal DC output voltage drops.[^libretexts-fiore-rectification]

The 7.09 V result depends on the assumption about `V_F`. The voltage 0.7 V is an approximation, and the actual drop depends on the diode and current (see qid:emb-elee-0127). Charging occurs in short current pulses near the peak: in the textbook simulation (half-wave rectifier, 10 V source, 100 Ω load) for 1000 µF, the pulse reaches approximately 800 mA with a duration of about 2.5 ms, well above the average load current.[^libretexts-fiore-rectification] For a 1N4001, the maximum `V_F` at 1 A is 1.1 V,[^vishay-1n4001] which reduces the estimate to `8.485 - 2*1.1 ≈ 6.29 V` (this is a lower-bound estimate based on maximum datasheet limits, not a typical number). Thus, a realistic range is roughly 6.3 to 7.1 V, and an exact value can only come from a calculation or measurement for the specific diodes and load current.

The capacitor must be rated for the peak voltage, not RMS: in a similar example, the textbook selects 50 V for a peak of about 34 V, providing a comfortable margin.[^libretexts-fiore-rectification] For an 8.49 V peak, a standard 6.3 V rating is insufficient; a higher voltage rating is required.

**Common mistakes:**

- Assuming that the capacitor charges to 6 V or to `V_peak` without subtracting diode drops.
- Subtracting only a single `V_F` drop instead of two, even though two diodes operate in series in a bridge.
- Using the `sqrt(2)` multiplier for non-sinusoidal waveforms or treating 7.09 V as a guaranteed voltage under load.

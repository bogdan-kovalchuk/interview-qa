---
id: emb-elee-0092
title: "What are the magnitude and phase of an RC low-pass filter at 0.1*f_c, f_c, and 10*f_c?"
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
  - source_id: aac-rc-low-pass-transfer
    title: "All About Circuits: Understanding Low-Pass Filter Transfer Functions"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-transfer-functions-for-low-pass-filters/
---

## Short answer

For an unloaded first-order RC low-pass filter, `|H| = 1/sqrt(1 + (f/f_c)^2)` and the phase is `-atan(f/f_c)`. At `0.1*f_c`, `|H| ≈ 0.995` with a phase of `-5.7°`. At `f_c`, `|H| ≈ 0.707` with a phase of `-45°`. At `10*f_c`, `|H| ≈ 0.0995` with a phase of `-84.3°`.[^aac-rc-low-pass-transfer]

## Detailed explanation

Frequency values are conveniently compared using the dimensionless ratio `x = f/f_c`. For a single-pole RC low-pass filter, the transfer magnitude is `1/sqrt(1 + x^2)`, and the phase shift of the output relative to the input is `-atan(x)`. Therefore, these values do not depend on the specific values of `R` and `C`, provided the actual circuit conforms to the first-order model and the output is not significantly loaded.[^aac-rc-low-pass-transfer]

When the frequency is one-tenth of the cutoff, `x = 0.1`: the denominator of the magnitude is only slightly greater than 1, so the amplitude is barely attenuated. At cutoff, `x = 1`, so the denominator squared equals `2`; the magnitude is `1/sqrt(2) ≈ 0.707` and the phase is `-45°`. When the frequency is ten times higher, `x = 10`: the magnitude becomes `1/sqrt(101) ≈ 0.0995`, and the phase approaches the asymptotic limit of `-90°`, but never reaches it at any finite frequency.[^aac-rc-low-pass-transfer]

**Verification example:** With `f_c = 1 kHz`, the three test points correspond to `100 Hz`, `1 kHz`, and `10 kHz`. At the highest frequency, the output amplitude is roughly one-tenth of the input, rather than zero. The phase value represents the steady-state sinusoidal phase shift; the transient response to an input step is described separately in the time domain.[^aac-rc-low-pass-transfer]

**Common mistakes:**
- Confusing the amplitude ratio `0.707` with a power ratio of `0.707`.
- Assuming that `10*f_c` yields exactly `0.1` and exactly `-90°`; these are only approximations.
- Writing a positive sign before the phase angle, even though the output of an RC low-pass filter lags the input.

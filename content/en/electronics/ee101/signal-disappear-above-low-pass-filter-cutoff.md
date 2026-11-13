---
id: emb-elee-0093
title: "Does the signal disappear above a low-pass filter's cutoff frequency?"
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

No. For a single-pole RC low-pass filter, `f_c` is simply the frequency where amplitude drops to `1/sqrt(2)` of its passband level (about `3.01 dB`), not an abrupt cutoff. Above cutoff, amplitude rolls off smoothly toward `-20 dB` per decade, reaching approximately one-tenth of the passband amplitude at `10*f_c`.[^aac-rc-low-pass-transfer]

## Detailed explanation

The cutoff frequency is not an on/off switch that passes all lower frequencies and completely cuts off all higher ones. For a single-pole RC low-pass filter, amplitude rolls off smoothly according to `|H| = 1/sqrt(1 + (f/f_c)^2)`. At the cutoff frequency itself, it equals approximately `0.707` of the low-frequency value, corresponding to `-3.01 dB` for the amplitude ratio. Even at frequencies well above cutoff, the output remains nonzero in an ideal model.[^aac-rc-low-pass-transfer]

Far above `f_c`, the term `f/f_c` dominates the denominator, so the magnitude is approximately `f_c/f`. When the frequency increases tenfold, the amplitude decreases by roughly a factor of ten. On a logarithmic plot, this represents a rolloff of about `20 dB` per decade for a single pole. For example, a signal at `10*f_c` has an amplitude of about `0.1` of its low-frequency level rather than zero; the exact value is `1/sqrt(101) ≈ 0.0995`.[^aac-rc-low-pass-transfer]

A real signal may appear to disappear if the output falls below the noise floor, the instrument's measurement resolution, or audibility limits, but this is a constraint of the measurement system or human perception rather than an absolute brick-wall cutoff by the filter. Loading and additional stages also modify the frequency response; the rolloff rate described here applies to a single pole without substantial loading.[^aac-rc-low-pass-transfer]

**Common mistakes:**
- Treating 'cutoff' as a frequency above which the output is strictly zero.
- Confusing a `20 dB` per decade rolloff with a linear decline to zero.
- Failing to specify that this asymptotic slope applies to a single pole well above cutoff.

Avoid these mistakes by evaluating `|H|` at specific operating points and distinguishing the theoretical mathematical response from the instrument's noise floor.[^aac-rc-low-pass-transfer]

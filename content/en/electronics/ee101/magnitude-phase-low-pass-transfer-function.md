---
id: emb-elee-0091
title: "What are the magnitude and phase of the RC low-pass transfer function?"
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

For a passive RC low-pass filter without significant loading, `H(f) = 1/(1 + j*f/f_c)`, where `f_c = 1/(2*pi*R*C)`. Then `|H| = 1/sqrt(1 + (f/f_c)^2)`, and the output phase relative to the input is `-atan(f/f_c)`. At the cutoff frequency, the magnitude is `1/sqrt(2)` of its low-frequency value, and the phase is `-45°`.[^aac-rc-low-pass-transfer]

## Detailed explanation

The transfer function describes how a linear circuit modifies a sinusoidal signal as a function of frequency. In a standard RC low-pass filter, the resistor is connected in series with the input, the capacitor connects from the output node to ground, and the output is taken across the capacitor. The capacitor's impedance decreases with increasing frequency, so most of the high-frequency voltage drops across the resistor. For ideal components and an unloaded output, the voltage divider yields `H(f) = 1/(1 + j*f/f_c)`, where `f_c = 1/(2*pi*R*C)`.[^aac-rc-low-pass-transfer]

The magnitude `|H|` specifies the amplitude ratio of the output to the input, and the argument of the complex number `H` specifies the phase lag. At low frequencies, the capacitor presents a high impedance, so the signal passes almost unaffected in amplitude and phase. As frequency increases, the magnitude rolls off smoothly, and the phase shifts from approximately zero toward `-90°`. At `f_c`, the magnitude equals `1/sqrt(2)` of its passband level, corresponding to approximately `-3 dB`, and the phase equals `-45°`.[^aac-rc-low-pass-transfer]

For example, if `R = 1 kΩ` and `C = 159 nF`, the cutoff frequency is close to `1 kHz`. At this frequency, the output amplitude is about 70.7% of the input amplitude. This does not mean the filter 'cuts off' all frequencies above `f_c`: the frequency response is continuous. Connected loads, source resistance, and parasitic parameters alter the actual transfer function, so the simple formulas apply when these effects are negligible or accounted for separately.[^aac-rc-low-pass-transfer]

**Common mistakes:**
- Confusing frequency in hertz `f` with angular frequency `ω = 2*pi*f`.
- Calling `f_c` a boundary beyond which the signal vanishes.
- Forgetting that the phase refers to the output relative to the input and carries a negative sign.

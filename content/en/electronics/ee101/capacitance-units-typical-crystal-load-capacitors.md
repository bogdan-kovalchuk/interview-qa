---
id: emb-elee-0251
title: "Which capacitance units are typical for crystal load capacitors?"
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
  - source_id: st-an2867-oscillator-design
    title: "STMicroelectronics Application Note AN2867: Oscillator design guide for STM32 microcontrollers"
    url: https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm32-microcontrollers-stmicroelectronics.pdf
  - source_id: ti-msp430-crystal-selection
    title: "Texas Instruments Application Report SLAA322: Selection and Specification of Crystals for Texas Instruments MSP430"
    url: https://www.ti.com/lit/an/slaa322/slaa322.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

Crystal load capacitors typically range from a few to several tens of picofarads (pF). Automated video subtitles often confuse pF with µF – a million-fold error – making it critical to verify capacitance units against the schematic and crystal datasheet.[^udemy-electronics-course]

## Detailed explanation

Load capacitors for quartz crystal resonators in microcontroller and digital circuits are always selected in units of **picofarads (pF, 10^-12 F)**, typically ranging from 5–10 pF to 33–39 pF.[^udemy-electronics-course][^st-an2867-oscillator-design]

### Why picofarads: physical rationale

1. **Rated crystal capacitance range:** Quartz crystals used in electronics (from low-frequency 32.768 kHz watch crystals to megahertz 4–48 MHz crystals) are manufactured for a rated load capacitance `C_L` ranging between 6 pF and 20 pF (the most common values are 8 pF, 12.5 pF, 16 pF, and 18 pF).[^st-an2867-oscillator-design][^ti-msp430-crystal-selection]
2. **Calculation formula:** Because external capacitors `C_1` and `C_2` form a series circuit with respect to the resonator, the total capacitance is given by `C_L = (C_1 * C_2) / (C_1 + C_2) + C_stray`. With equal capacitors `C_1 = C_2 = C`, we obtain `C = 2 * (C_L - C_stray)`. Given the typical stray capacitance of the PCB and microcontroller pins of `C_stray ≈ 2–5 pF`, the external capacitors take values from 10 pF to 33 pF.[^st-an2867-oscillator-design]
3. **Loop impedance matching:** The reactance of a capacitor at oscillation frequency `f` is `X_C = 1 / (2 * pi * f * C)`. For example, for a high-frequency crystal with `f = 16 MHz` and capacitor `C = 20 pF`:
`X_C = 1 / (2 * pi * 16 * 10^6 * 20 * 10^-12) ≈ 497 Ω`.
This impedance level matches ideally with the dynamic output resistance of an integrated CMOS inverter (hundreds of ohms) and the equivalent series resistance of the crystal (ESR from 20 to 80 Ω), providing the required 180° phase shift without overloading the amplifier.[^art-of-electronics]

### Catastrophic consequences of unit confusion (pF versus µF)

Between picofarads (`1 pF = 10^-12 F`) and microfarads (`1 µF = 10^-6 F`), the difference is exactly **one million times (10^6)**:[^art-of-electronics]
- If an engineer or assembler mistakenly installs 18 µF capacitors (or even 0.1 µF) instead of 18 pF, the reactance at 16 MHz will be:
`X_C = 1 / (2 * pi * 16 * 10^6 * 0.1 * 10^-6) ≈ 0.099 Ω`.
- A resistance in tenths or hundredths of an ohm is effectively a **direct short circuit** of the oscillator pins OSC_IN and OSC_OUT to GND.
- Under such shunting, the inverting amplifier cannot build oscillation amplitude, loop gain drops to zero, and oscillation will fail to start under any condition.[^st-an2867-oscillator-design]

### Causes of errors in practice

1. **Errors in automated speech-to-text (STT) and auto-subtitles:** In instructional videos or recorded lectures, speech recognition systems often confuse the phonetically similar English terms "picofarad" and "microfarad" or the graphical symbols "pF" and "uF".
2. **Dielectric type:** For quartz crystal resonators, temperature stability is critical; therefore, capacitors with values of a few to tens of picofarads are selected exclusively with Class 1 ceramic dielectrics (NP0 / C0G), which have a zero temperature coefficient of capacitance (TCC) and negligible dielectric hysteresis.[^ti-msp430-crystal-selection] Capacitors in the microfarad range belong to Class X5R/X7R or electrolytic types and are fundamentally unsuitable for clock resonant circuits.

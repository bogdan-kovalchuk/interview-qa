---
id: emb-elee-0250
title: "A crystal has a rated C_L = 18 pF and stray capacitance ≈ 3 pF. Which equal capacitors C_1=C_2 are needed?"
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
  - source_id: microchip-an826-crystal-basics
    title: "Microchip Application Note AN826: Crystal Oscillator Basics and Crystal Selection for rfPIC and PICmicro Devices"
    url: https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

The effective load capacitance is `C_L ≈ (C_1 * C_2) / (C_1 + C_2) + C_stray = C / 2 + 3 pF`, yielding `C ≈ 30 pF`. This provides an initial design estimate; actual PCB stray capacitance and crystal manufacturer recommendations determine the final component value.[^udemy-electronics-course]

## Detailed explanation

For stable clock generation at the specified frequency, a quartz crystal resonator in a Pierce oscillator configuration requires a strictly defined value of equivalent load capacitance `C_L`.[^udemy-electronics-course][^st-an2867-oscillator-design]

### Pierce circuit topology and equivalent circuit

The Pierce oscillator integrated into most microcontrollers consists of an inverting amplifier (OSC_IN and OSC_OUT pins), a feedback resistor, and a pi-filter network formed by the crystal resonator and two external capacitors `C_1` and `C_2` connected to ground.[^st-an2867-oscillator-design][^microchip-an826-crystal-basics]

From the perspective of the resonator, external load capacitors `C_1` and `C_2` are connected in series through the common ground plane:
`C_series = (C_1 * C_2) / (C_1 + C_2)`.

In parallel with this series combination is the total stray mounting capacitance `C_stray`. It accounts for:
- PCB trace capacitance from the crystal pins to the microcontroller pins (`C_PCB ≈ 1–3 pF`);
- parasitic capacitance of the contact pads and crystal package;
- internal capacitance of microcontroller pins `C_in` and `C_out` (typically 2–5 pF per pin).[^st-an2867-oscillator-design]

The total load capacitance seen by the crystal between its terminals is described by the fundamental equation:
`C_L = (C_1 * C_2) / (C_1 + C_2) + C_stray`.[^st-an2867-oscillator-design][^microchip-an826-crystal-basics]

### Mathematical calculation for equal values

To ensure symmetrical oscillation amplitude and phase shift, equal capacitors are typically chosen: `C_1 = C_2 = C`.
The series combination then simplifies to:
`(C * C) / (C + C) = C^2 / (2 * C) = C / 2`.

Substituting this expression into the general load capacitance equation yields:
`C_L = C / 2 + C_stray`.

From this, the required capacitance `C` is expressed by the formula:
`C / 2 = C_L - C_stray`, whence `C = 2 * (C_L - C_stray)`.[^st-an2867-oscillator-design][^art-of-electronics]

Substituting the numerical values from the problem statement (`C_L = 18 pF`, `C_stray ≈ 3 pF`):
`C = 2 * (18 pF - 3 pF) = 2 * 15 pF = 30 pF`.

Thus, the calculated value of each capacitor is **30 pF**. Because 30 pF is a standard value in the E96 series (or less commonly E24), the engineer typically selects either exactly 30 pF or the nearest common values from the E24 series: 27 pF or 33 pF with NP0/C0G dielectric.[^st-an2867-oscillator-design]

### Impact of capacitance selection error

1. **Frequency pulling:** A crystal resonator operates in the parallel resonance region (inductive reactance). If smaller capacitors are installed, the total load capacitance becomes lower than rated `C_L`, and the oscillator frequency shifts above nominal. Conversely, with excessive capacitance, the oscillator frequency shifts downward.[^microchip-an826-crystal-basics]
2. **Gain margin and oscillation stoppage:** Significantly oversizing capacitance `C` increases load capacitance `C_L` and sharply raises the critical transconductance for startup `g_mcrit = 4 * ESR * (2 * pi * f)^2 * (C_0 + C_L)^2` (where `C_0` is the shunt static capacitance of the crystal). If the required gain exceeds the capability of the microcontroller's internal inverter, the oscillator gain margin falls below the recommended value of 5, leading to unreliable startup or complete failure to oscillate at low temperatures or during supply voltage dips.[^st-an2867-oscillator-design]

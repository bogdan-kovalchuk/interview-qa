---
id: emb-elee-0252
title: "Why can a crystal oscillator stop oscillating after a probe is connected?"
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
  - source_id: tektronix-probe-loading
    title: "Tektronix Application Note: Low-Current and High-Impedance Probing Pitfalls"
    url: https://www.tek.com/en/documents/application-note/low-current-and-high-impedance-probing-pitfalls
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

The input capacitance and resistive loading of an oscilloscope probe alter the loop phase and gain conditions of the resonant tank. To prevent loading, always measure at the buffered clock output rather than the sensitive crystal nodes, while keeping drive level within specified limits.[^udemy-electronics-course]

## Detailed explanation

Oscillation stoppage in a crystal oscillator when a standard oscilloscope probe is connected is a classic hardware issue caused by the high sensitivity of the Pierce circuit to parasitic capacitive and resistive loading.[^udemy-electronics-course][^tektronix-probe-loading]

### Oscillator excitation conditions and the Barkhausen criterion

A Pierce oscillator consists of an inverting CMOS amplifier and feedback through a quartz crystal resonator and phase-shifting capacitors `C_1`, `C_2`.[^st-an2867-oscillator-design] To sustain continuous oscillations at the resonant frequency, the conditions of the Barkhausen criterion must be strictly met:
1. The magnitude of the loop gain equals unity: `|A * beta| = 1` (reliable startup requires `|A * beta| > 1`).
2. The total phase shift around the feedback loop is an integer multiple of 360° (180° is provided by the inverter and another 180° by the resonant pi-network of the crystal and capacitors).[^st-an2867-oscillator-design][^art-of-electronics]

In modern low-power microcontrollers, the amplifier is optimized for minimum current consumption (especially for 32.768 kHz watch oscillators, where operating current is hundreds of nanoamperes). Its transconductance `g_m` operates near the minimum allowable oscillation startup margin: `Gain_margin = g_m / g_mcrit`.[^st-an2867-oscillator-design]

### Oscilloscope probe parameters and oscillation stopping mechanism

A typical standard 10X passive probe has the following input characteristics:
- input resistance `R_probe ≈ 10 MΩ`;
- parasitic input capacitance `C_probe ≈ 10–15 pF` (for a 1X divider, capacitance reaches 50–100 pF, and resistance drops to 1 MΩ).[^tektronix-probe-loading]

When the probe tip touches the high-impedance oscillator input (OSC_IN):
1. **Doubling of load capacitance:** Probe input capacitance `C_probe` is added in parallel to the circuit's own load capacitor `C_1` (which typically has a value of 12–22 pF). The total capacitance of that leg instantly nearly doubles.
2. **Jump in critical transconductance:** The amplifier transconductance required for oscillation is proportional to the square of load capacitance: `g_mcrit = 4 * ESR * (2 * pi * f)^2 * (C_0 + C_L)^2`.[^st-an2867-oscillator-design] When the probe is connected, `g_mcrit` jumps sharply by several times, substantially exceeding the actual transconductance `g_m` of the internal transistor. Loop gain becomes less than unity (`|A * beta| < 1`), phase balance is disrupted, and oscillations immediately decay.[^st-an2867-oscillator-design][^tektronix-probe-loading]
3. **Output shunting (OSC_OUT):** When attempting to connect to the inverter output, probe capacitance and conductance load the weak output stage, causing a significant drop in signal amplitude and phase shift distortion, which likewise stops clock generation.[^tektronix-probe-loading]

### Correct methods for monitoring crystal frequency

To verify the operation and accuracy of a crystal oscillator without stopping oscillations, the following engineering approaches are used:[^st-an2867-oscillator-design][^tektronix-probe-loading]
- **Measurement at a buffered digital output (MCO):** Most modern microcontrollers (notably STM32 families) include a feature to output a clock signal to a dedicated GPIO pin (Microcontroller Clock Output – MCO). This signal passes through an internal buffer logic gate with low output impedance (tens of ohms), and connecting a standard probe to it exerts no loading on the sensitive analog resonator.[^st-an2867-oscillator-design]
- **Using an active FET probe:** Active probes feature an input capacitance of less than 0.5–1 pF and gigohm input resistance, minimizing loading on the resonant tank.[^tektronix-probe-loading]
- **Contactless method (near-field probe):** A small pickup loop or near-field probe fork connected to a spectrum analyzer or sensitive oscilloscope is held close to the crystal package. The measurement relies on electromagnetic radiation without physical contact with the traces.[^tektronix-probe-loading]

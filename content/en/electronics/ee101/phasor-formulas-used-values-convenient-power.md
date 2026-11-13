---
id: emb-elee-0066
title: "When can phasor formulas be used, and which values are convenient for power?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-single-frequency-phasors
    title: "All About Circuits: Introduction to Complex Numbers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/introduction-to-complex-numbers/
  - source_id: aac-ac-rms
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude
  - source_id: aac-power-phase
    title: "All About Circuits: Power in Resistive and Reactive AC Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/power-resistive-reactive-ac-circuits/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Phasor formulas apply to steady-state sinusoidal quantities of a single frequency, while different frequencies must be analyzed separately. For standard power formulas, RMS values are convenient, but using them does not replace the requirement of sinusoidal operation.[^aac-single-frequency-phasors] [^aac-ac-rms]

## Detailed explanation

A phasor is a complex representation of a sine wave's amplitude and its phase relative to a common time reference. It transforms the differential relationships of circuit components into algebraic ones: for example, inductance and capacitance are represented by frequency-dependent impedances. This simplification is valid for a linear circuit in sinusoidal steady state; a separate calculation is required for each frequency.[^aac-single-frequency-phasors]

A switching transient, a nonlinear component, or a mixture of frequencies cannot be described by a single phasor. In such cases, individual harmonics, time-domain equations, or nonlinear analysis are used. If quantities are specified as peak values, all calculated voltages and currents remain peak; if specified as RMS, the impedance calculation yields RMS values. Different amplitude conventions must not be mixed.[^aac-single-frequency-phasors] [^aac-ac-rms]

For sinusoidal voltage and current, the average real power is calculated as `P = V_RMS*I_RMS*cos(φ)`, where `φ` is the angle between voltage and current. The product of RMS values by itself gives the apparent power in volt-amperes, while the `cos(φ)` factor accounts for the phase shift. For a non-sinusoidal waveform, RMS remains meaningful for resistor heating, but the simple real power formula given above may be insufficient.[^aac-power-phase] [^aac-ac-rms]

**Common mistakes:**

- Applying a single phasor to signals of different frequencies or during a transient process.
- Confusing peak values with RMS values and introducing a scale error.
- Calling `V_RMS*I_RMS` real power without accounting for the power factor.[^aac-single-frequency-phasors] [^aac-ac-rms]

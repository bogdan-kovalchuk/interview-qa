---
id: emb-elee-0021
title: "What is AC coupling (a coupling capacitor) and where is it used?"
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
  - source_id: aac-input-output-coupling
    title: "All About Circuits: Input and Output Coupling"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/input-and-output-coupling/
  - source_id: aac-capacitor-highpass
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
---

## Short answer

A coupling capacitor placed in series with a signal blocks DC and forms a high-pass network with source and load resistances. This allows transferring an AC signal between stages without shifting their DC bias levels. For a simple RC circuit, `f_c = 1/(2*π*R*C)`, where `R` is the effective resistance seen by the capacitor.[^aac-input-output-coupling] [^aac-capacitor-highpass]

## Detailed explanation

A coupling capacitor transfers the AC component of a signal while isolating the DC operating level of one node from that of the next. For example, the output of a preceding stage may carry a DC bias required for its operating point; direct connection could shift the bias of the subsequent stage. In an ideal model, a series capacitor blocks the DC component, allowing stages to be biased independently.[^aac-input-output-coupling]

It is not an ideal "wire for AC only". Capacitor impedance depends on frequency: as frequency decreases, impedance rises, so together with the surrounding resistive network, the component forms a high-pass filter. Below the cutoff frequency, signals are attenuated, and near cutoff both amplitude and phase are altered. Therefore, DC blocking comes at a cost: sufficiently low frequencies or slow waveform variations can become distorted.[^aac-capacitor-highpass] [^aac-input-output-coupling]

In the simplest circuit, a single capacitor is connected in series between source and load, and the resistance `R` in the approximate formula represents the equivalent resistance seen across its terminals. If resistances on both sides are significant, one cannot automatically substitute only the load resistance; the effective circuit resistance must be determined. Cascaded stages, multiple coupling capacitors, and frequency-dependent input impedances require analyzing the full network, so the basic formula provides only a first-order estimate.[^aac-capacitor-highpass]

Example: in a model where the capacitor sees `10 kΩ`, a value of `C = 10 µF` yields `f_c ≈ 1.59 Hz`. This value is not universal for every amplifier: the actual resistance may include source output resistance, stage input resistance, and biasing network components.[^aac-capacitor-highpass]

**Common mistake:** claiming that a capacitor completely "blocks DC and passes all AC". In reality, it blocks DC after the transient settles, but also attenuates low-frequency AC; the magnitude of the effect is determined by signal frequency and the resistance seen by the capacitor.[^aac-input-output-coupling]

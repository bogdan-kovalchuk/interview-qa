---
id: emb-elintro-0098
title: "How does real power differ from apparent power in an `AC` circuit?"
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
  - source_id: aac-ac-power
    title: "True, Reactive, and Apparent Power"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/true-reactive-and-apparent-power/
---

## Short answer

Real power `P` is the average power over a cycle that transfers energy into other forms, such as heat or mechanical work; it is measured in `W`. Apparent power `S = V_rms*I_rms` is measured in `VA` and defines the product of the RMS voltage and current; for sinusoidal operation, `P = S*cos(φ)`, where `φ` is the phase angle.[^aac-ac-power]

## Detailed explanation

Real power `P` is the average value of instantaneous power over a period, representing the rate at which electrical energy converts into heat, mechanical work, or another non-recoverable form.[^aac-ac-power] In a sinusoidal circuit, it can be written as `P = V_rms*I_rms*cos(φ)`, where `φ` is the phase angle between voltage and current. The unit of real power is the watt (`W`).[^aac-ac-power]

Apparent power `S = V_rms*I_rms` is measured in volt-amperes (`VA`). It describes the load that the source, wiring, and transformers must deliver at the given RMS voltage and current. For a linear sinusoidal circuit, reactive power `Q` describes the periodic exchange of energy between the source and the magnetic or electric field; its unit is the `var`. For such a regime, these quantities are related by the power triangle: `S^2 = P^2 + Q^2`, and `P = S*cos(φ)`.[^aac-ac-power]

Example: if `V_rms = 120 V`, `I_rms = 2 A`, and `cos(φ) = 0.5`, then `S = 240 VA`, but `P = 120 W`. The difference does not mean that the remaining `120` units are watts that disappeared: the current creates a periodic energy exchange accounted for as `Q`; an actual load and losses can also consume real power. This calculation assumes sinusoidal voltage and current; with distorted waveforms, a simple cosine of the phase shift may not fully describe the power factor.[^aac-ac-power]

**Common mistake:** calling `VA` real power or equating `S` to `P` without the condition `cos(φ) = 1`. For a purely resistive load, voltage and current are in phase, so `P = S`; in a reactive load, these quantities differ.

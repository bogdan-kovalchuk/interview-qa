---
id: emb-elintro-0182
title: "What is the approximate ripple formula for the capacitor after a rectifier?"
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
  - source_id: power-com-rectifier-capacitor
    title: "AN-92: Input Capacitor Derivation"
    url: https://www.power.com/sites/default/files/documents/an-92_mine-cap_design_guide.pdf
---

## Short answer

For a rough estimate: `ΔV ≈ I_load/(f_ripple*C)`. In a bridge rectifier, `f_ripple` is twice the line frequency: `100 Hz` for `50 Hz` or `120 Hz` for `60 Hz`.[^power-com-rectifier-capacitor]

## Detailed explanation

The formula `ΔV ≈ I_load/(f_ripple*C)` estimates peak-to-peak ripple: between peaks of the rectified voltage, the capacitor discharges into the load, and the next peak recharges it. Under an approximately constant current, `I = C*ΔV/Δt`, and the interval between peaks equals `1/f_ripple`.[^aac-semiconductors]

In a full-wave bridge, each half-wave of the AC signal produces a pulse of the same polarity, so the ripple frequency is twice the line frequency: `100 Hz` for `50 Hz` and `120 Hz` for `60 Hz`. In a half-wave rectifier, pulses arrive only once per period, so for identical capacitance and load, the estimated ripple is approximately twice as large.[^aac-semiconductors]

Worked example: the load draws `0.1 A`, the capacitor is `1000 µF`, and the line is `50 Hz` with a bridge. Then `ΔV ≈ 0.1/(100*0.001) = 1 V`. This is a simplification: the actual waveform depends on the resistance of the transformer and diodes, the capacitor ESR, the nature of the load, and the conduction angle of the diodes.[^aac-semiconductors]

**Common mistake:** substituting `50 Hz` instead of `100 Hz` for a bridge, or treating the estimate as a guaranteed bound. For design purposes, verify the minimum voltage across the load and the allowable ripple current of the capacitor, and then measure the ripple in the actual circuit.

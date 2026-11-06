---
id: emb-elee-0259
title: "How does the 555 monostable mode differ from the astable mode?"
track: electronics
section: ee101
sources:
  - source_id: ti-ne555-datasheet
    title: "Texas Instruments: NE555 Precision Timers Datasheet (SLRS022)"
    url: https://www.ti.com/lit/ds/symlink/ne555.pdf
  - source_id: fiore-555-timer
    title: "Engineering LibreTexts: Operational Amplifiers and Linear Integrated Circuits (Fiore), 9.6 The 555 Timer"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/09:_Specialized_Linear_Circuits/9.6:_The_555_Timer
  - source_id: aac-555-circuits
    title: "All About Circuits: 555 Timer Circuits"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-8/555-timer-circuits/
---

## Short answer

Monostable mode (one-shot) has a single stable quiescent state with OUT LOW: an external negative-going trigger at TRIG produces exactly one pulse of duration `t_pulse ≈ 1.1 * R * C` before the circuit returns to rest. Astable mode (multivibrator) has no stable state, continuously free-running and generating an unending periodic pulse train through automatic self-triggering.[^ti-ne555-datasheet]

## Detailed explanation

TODO

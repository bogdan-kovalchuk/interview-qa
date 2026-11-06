---
id: emb-elee-0257
title: "Astable 555: R_A = 10 kΩ, R_B = 47 kΩ, C = 1 µF. What are t_HIGH, t_LOW, the frequency and the duty cycle?"
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

For these component values, the timing intervals are `t_HIGH ≈ 39.5 ms` and `t_LOW ≈ 32.6 ms`, giving a total period `T ≈ 72.1 ms`. The resulting output frequency is `f ≈ 13.9 Hz` with a HIGH duty cycle of `D ≈ 54.8%`. Real circuit performance will deviate slightly from these nominal calculations due to component manufacturing tolerances, capacitor leakage currents, and internal comparator delays.[^ti-ne555-datasheet]

## Detailed explanation

TODO

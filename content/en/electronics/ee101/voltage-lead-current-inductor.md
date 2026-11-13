---
id: emb-elee-0051
title: "Why does voltage lead current in an inductor?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-ac-inductor
    title: "All About Circuits: AC Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

For an ideal inductor, `v = L*di/dt`, so voltage is proportional to the rate of change of current. In sinusoidal steady state, voltage leads current by 90° rather than simply "turning on earlier", and the analogy with inertia is merely mnemonic.[^aac-ac-inductor]

## Detailed explanation

An inductor develops a voltage when its current changes: for an ideal component, `v = L*di/dt`. Here `L` is measured in henries, and the rate of change of current in amperes per second; their product has units of volts. The sign depends on the chosen reference directions for current and voltage polarity, but the physical meaning is constant: the inductor opposes changes in current, supporting its direction during decay and impeding its rise. [^aac-ac-inductor]

If current does not change, an ideal inductor has zero voltage across its terminals. When a constant voltage is applied across it, current in a simple ideal model ramps linearly because `di/dt = v/L`. In a real circuit, winding resistance and source limitations bound such behavior. [^aac-ac-inductor]

For a sinusoidal signal in steady state, the derivative of current shifts voltage forward by 90°: voltage is highest where current changes most rapidly, and when current reaches its peak and instantaneously stops growing, the voltage across an ideal inductor crosses zero. Therefore, the phrase "voltage leads current" pertains to the phase of cyclic signals, rather than a delay in current when turned on. [^aac-ac-inductor]

**Example:** for a sinusoidal source and an ideal inductor, the current reaches its peak a quarter period after the corresponding voltage peak. At a frequency of 60 Hz, the period is approximately 16.7 ms, and a quarter period is approximately 4.17 ms.

**Common mistakes:**

- Assuming that an inductor always blocks current. In steady-state DC, an ideal inductor has zero voltage across it; real behavior is also governed by winding resistance.
- Applying a 90° shift to a complete circuit containing resistance. In a mixed R-L circuit, the phase angle depends on the ratio of resistance to inductive reactance. [^aac-ac-inductor]

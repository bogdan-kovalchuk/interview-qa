---
id: emb-elintro-0144
title: "What is LC tank resonance?"
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
---

## Short answer

At the ideal resonant frequency `f_0 = 1/(2*pi*sqrt(L*C))`, the reactances of the inductor and capacitor become equal. In a series circuit, impedance is minimal, and in a parallel one it is maximal; real losses limit these extremes.[^aac-semiconductors]

## Detailed explanation

LC tank resonance occurs at the frequency where inductive and capacitive reactances are equal in magnitude. In an ideal component model, this frequency equals `f_0 = 1/(2*pi*sqrt(L*C))`; energy transfers periodically between the inductor's magnetic field and the capacitor's electric field.[^aac-semiconductors]

The cause of resonance is clear from the frequency dependence: `X_L = 2*pi*f*L` increases with frequency, whereas `X_C = 1/(2*pi*f*C)` decreases. There is a frequency where they become equal, and their reactive effects cancel each other out at the circuit's input. For `L = 100 mH` and `C = 10 µF`, the ideal formula gives approximately `159 Hz`.[^aac-semiconductors]

What the source sees depends on the connection. In a series LC circuit, the total impedance ideally approaches zero at resonance; in a parallel circuit, the input impedance ideally approaches infinity. Real losses limit these extremes, and parasitic resistances and capacitances can shift the observed peak or null.[^aac-semiconductors]

**Common mistake:** Calling impedance "minimal" for any LC circuit. This statement applies to the series case; for a parallel tank circuit, impedance is maximal at resonance. The ideal frequency formula is a useful starting calculation, but for a real circuit, losses, loading, and parasitic parameters matter.[^aac-semiconductors]

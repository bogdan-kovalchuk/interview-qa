---
id: emb-elee-0087
title: "How does resistor heating differ from the behavior of an ideal capacitor in an AC circuit?"
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
---

## Short answer

An ideal capacitor draws zero average real power, returning stored energy to the source over each cycle. A resistor dissipates average power `P_R = I_RMS^2*R` as heat, so having the same impedance magnitude does not imply identical heating.[^aac-alternating-current]

## Detailed explanation

A resistor converts electrical energy into heat, whereas an ideal capacitor temporarily stores energy in an electric field and returns it to the source over each cycle.[^aac-alternating-current]

In a resistor, voltage and current are in phase. The instantaneous power `p = v*i` never becomes negative for a passive resistor with positive resistance, and the average power over a cycle is determined by the RMS current: `P = I_RMS^2*R`. This represents average heating over time, not an instantaneous value at a specific point on the sine wave.[^aac-alternating-current]

In an ideal capacitor, current leads voltage by a quarter of a cycle. When the voltage increases, the capacitor absorbs energy; when it decreases, it returns the energy. Because of this alternating direction of energy flow, the average instantaneous power `p` over a full cycle equals zero. A real capacitor has losses, such as equivalent series resistance (ESR), so it can heat up; the statement about zero real power applies strictly to the ideal model.[^aac-alternating-current]

**Common mistakes:**
- Confusing reactive power, which describes energy exchange, with active power, which heats the resistor.
- Deducing heating solely from impedance magnitude while ignoring the phase angle between voltage and current.

For example, in a series RC circuit, the capacitor can have a reactance whose magnitude equals R, but its voltage is out of phase with the current. Heat is still dissipated only in R, while an ideal C returns its stored energy; the power balance is determined by phase relationships rather than identical impedance magnitudes.[^aac-alternating-current]

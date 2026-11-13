---
id: emb-elee-0049
title: "What does the mnemonic ELI mean?"
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
  - source_id: phase-basics
    title: "Phase Relationships in Inductive and Capacitive Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/phase-relationships/
---

## Short answer

ELI means that in an inductor (`L`), voltage (`E`, electromotive force) leads current (`I`) by 90° in sinusoidal steady state. The paired mnemonic ICE reminds us that in a capacitor, current leads voltage by 90°.[^phase-basics]

## Detailed explanation

In the mnemonic ELI, the letters help recall the phase order in an inductor: `E` (voltage, or electromotive force) leads `I` (current) in `L` by 90°. This is consistent with the equation `v = L*di/dt`: voltage is proportional to the derivative of current, and the derivative of a sine wave leads the original sine wave by a quarter period.[^phase-basics]

For a capacitor, the paired mnemonic ICE is used: `I` leads `E` in `C`. The equation `i = C*dv/dt` explains this phase relationship. "Leads" means that the corresponding peak of the sinusoid occurs earlier; an angle of 90° corresponds to a quarter of a period, and the time interval between peaks depends on the signal frequency.[^phase-basics]

For example, at a frequency of `50 Hz`, the period is `20 ms`, and a quarter period is `5 ms`. In an ideal inductor, the voltage reaches its peak `5 ms` earlier than the current. A real inductor has winding resistance and parasitic effects, so the angle between the total voltage and the current can differ from 90°.[^phase-basics]

**Common mistake:** reading ELI as though current leads voltage. Expand the letters in their mnemonic order: `E` before `I` in `L`; for a capacitor, `I` before `E` in `C`. The rule applies to sinusoidal steady state, not to transient processes or constant DC voltage, for which phase lead is not an appropriate description.

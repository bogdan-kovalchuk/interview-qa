---
id: emb-elee-0050
title: "What does the mnemonic ICE mean?"
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
  - source_id: aac-ac-capacitor
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

ICE reminds us that in an ideal capacitor, current leads voltage by 90° in sinusoidal steady state, while ELI reminds us that in an ideal inductor, voltage leads current by 90°. These are mnemonics for phase relationships rather than claims that one quantity physically appears before the other in a real circuit.[^aac-ac-capacitor] [^aac-ac-inductor]

## Detailed explanation

ICE is expanded as "Current leads Voltage in a Capacitor": current leads voltage in a capacitor. The paired mnemonic ELI is read as "Voltage leads Current in an Inductor", meaning voltage leads current in an inductor. This refers to the phase of sinusoidal signals in steady state, rather than a startup delay of components after power is applied. For instance, if in an ideal capacitor the sinusoidal current reaches its peak a quarter period earlier than the voltage, that is precisely a 90° lead. For an ideal inductor, the mutual arrangement is reversed: voltage reaches the corresponding point earlier than current. [^aac-ac-capacitor] [^aac-ac-inductor]

The physical reason is tied to the component constitutive equations. In a capacitor, current depends on the rate of change of voltage, so its maximum coincides with the fastest voltage change; in an inductor, voltage depends on the rate of change of current. For a sinusoidal signal, the derivative shifts the phase by a quarter period. The mnemonic concisely captures this specific direction of the phase relationship. [^aac-ac-capacitor] [^aac-ac-inductor]

**Common mistakes:**

- Reading "lead" as a turn-on sequence. It is a phase shift in periodic signals.
- Applying exactly 90° to a real inductor or capacitor in an arbitrary circuit. Resistance, losses, and other components alter the overall circuit phase. [^aac-ac-inductor] [^aac-ac-capacitor]

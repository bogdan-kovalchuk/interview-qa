---
id: emb-elintro-0085
title: "Why does a transformer not work on steady `DC`?"
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
  - source_id: aac-mutual-inductance
    title: "All About Circuits: Mutual Inductance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-14/mutual-inductance/
---
## Short answer

A transformer transfers energy between windings via a changing magnetic flux. Steady `DC` after the transient produces a constant flux and induces no secondary voltage; the primary winding may overheat due to excessive current.[^aac-mutual-inductance]

## Detailed explanation

A transformer transfers energy between windings through mutual induction: changing current in the primary winding changes magnetic flux in the core, and changing flux induces a voltage in the secondary winding. Under steady `DC` after the transient, the current and flux in the primary winding are constant, so no secondary voltage is sustained.[^aac-mutual-inductance]

When a direct voltage source is first connected, current in the coil cannot change instantaneously: a brief transient occurs, and the corresponding change in flux can induce a short pulse in the secondary winding. Once steady-state current is established, the flux ceases to change, and the induced voltage disappears. With alternating current, the polarity and magnitude of the current vary continuously, so the flux also varies, allowing the transformer to operate.[^aac-mutual-inductance]

In practice, you cannot simply connect a transformer winding to a `DC` source: after the transient, the primary winding behaves primarily as its wire resistance, and current may become excessive and overheat the winding. The actual current depends on the resistance of the winding and source; the core may also saturate. Battery-powered transformer circuits do exist, but they chop or switch the current to create a varying flux rather than applying steady current to the winding.[^aac-mutual-inductance]

Example: a switch momentarily connecting a battery to the primary winding can induce a voltage pulse in the secondary during turn-on and turn-off. If you leave the battery connected, there is no steady output after this pulse, while the primary winding may heat up. Common mistake – claiming that DC produces no magnetic field at all: it does produce a field, but continuous induced voltage requires a changing flux.[^aac-mutual-inductance]

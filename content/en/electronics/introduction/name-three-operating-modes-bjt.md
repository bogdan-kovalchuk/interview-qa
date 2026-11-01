---
id: emb-elintro-0201
title: "What are the three operating modes of a `BJT`?"
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
  - source_id: aac-bjt-active-mode
    title: "Active-mode Operation (BJT), All About Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/active-mode-operation-bjt/
---
## Short answer

The primary operating modes are cutoff, active, and saturation. In cutoff, collector current is virtually absent; in active, base current controls collector current; and in saturation, collector current is already limited by the external load circuit.[^aac-bjt-active-mode]

## Detailed explanation

`BJT` operating modes are distinguished by the state of the junctions and what limits the collector current. In cutoff, the transistor is nearly off: the base–emitter junction lacks sufficient forward bias, so collector and base currents are small, although a real component exhibits leakage. This approximation corresponds to an open switch rather than absolute zero current.[^aac-bjt-active-mode]

In active mode, the base–emitter junction is forward-biased, and the base–collector junction is typically reverse-biased. Within operating limits, varying the base current controls the collector current; the relationship `I_C ≈ β*I_B` is an approximate model, and β depends on the component and operating conditions. This region is used for amplification when the operating point does not reach cutoff or saturation.[^aac-bjt-active-mode]

In saturation, both junctions are forward-biased, and the load together with the power supply determines the available current. Additional base current no longer yields a proportional increase in `I_C`, making the active mode formula inapplicable. `V_CE(sat)` is not a universally fixed 0.1 V: the value depends on the transistor and currents, and the datasheet specifies it under specific conditions.[^aac-bjt-active-mode]

**Switching example:** when a `BJT` drives a load, it is approximately considered cutoff in the off state and saturation in the on state. For a linear amplifier, you aim to keep the signal in the active region so the output does not clip against either boundary.[^aac-bjt-active-mode]

**Common mistake:** calling active mode simply a "partially open switch." This obscures its purpose as a controlled amplification mode and confuses it with switching applications; verify whether current is limited by base control or already by the load.

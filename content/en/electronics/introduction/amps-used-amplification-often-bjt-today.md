---
id: emb-elintro-0207
title: "Why are op-amps used for amplification more often than a `BJT` today?"
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
  - source_id: opamp-feedback
    title: "TI application report: Op Amp with Resistive Feedback"
    url: https://www.ti.com/lit/an/snoa486b/snoa486b.pdf
---

## Short answer

An operational amplifier often simplifies building an amplifier stage: external negative feedback sets the closed-loop gain primarily by the ratio of resistors, within the bandwidth and operating range of the specific device.[^opamp-feedback] A `BJT` is also widely used; its bias and stability must be designed taking into account the transistor and circuit parameters.[^aac-semiconductors]

## Detailed explanation

Operational amplifiers are often more convenient for a typical amplifier stage because their large internal gain together with external negative feedback sets the amplification using resistors.[^opamp-feedback]

A discrete `BJT` can amplify a signal, but its operating point depends on its current gain, temperature, and parameter spread. To obtain a predictable analog stage, the designer selects the bias and resistors, and often adds an emitter resistor or other stabilization elements. This is entirely practical for discrete, high-frequency, or power circuits, but it requires careful calculation.[^aac-semiconductors]

In a typical op-amp circuit, part of the output signal is returned to the inverting input through a resistive network. The amplifier changes its output to reduce the difference between the inputs; within the operating range, the closed-loop gain is then determined primarily by the ratio of resistors. For example, in a non-inverting configuration, `A_V = 1 + R_F/R_G`; this approximate relationship holds only with stable feedback and within the bandwidth and output range of the specific device.[^opamp-feedback]

An integrated amplifier combines many transistors, their bias networks, and compensation on a single die. However, an op-amp is not universally better: you must check supply voltages, common-mode range, output swing, load current, bandwidth, noise, and stability. For switching, discrete topologies, or operation requiring limits beyond these parameters, a discrete `BJT` may be the right choice.[^opamp-feedback]

**Common mistake:** stating that a `BJT` is not used for amplification or that an op-amp alone guarantees the required gain. The feedback circuit sets the actual function, while the datasheet of the specific IC sets the limits.

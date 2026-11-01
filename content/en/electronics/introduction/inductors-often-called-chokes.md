---
id: emb-elintro-0148
title: "Why are inductors often called chokes?"
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
  - source_id: aac-inductor-choke
    title: "All About Circuits: Magnetic Fields and Inductance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/magnetic-fields-and-inductance/
---

## Short answer

The name choke originates from using an inductor to attenuate unwanted high-frequency AC signals. It is an application-based designation rather than a distinct physical component type; the response of a specific inductor depends on frequency and its real parasitic parameters.[^aac-inductor-choke]

## Detailed explanation

An inductor develops a voltage that opposes changes in the current passing through its winding. In a filter, this property helps reduce AC ripple or interference, which is why an inductor intended for such an application is called a choke. The name describes a function in a circuit rather than a special construction: a choke is still an inductor.[^aac-inductor-choke]

For an ideal inductor, the magnitude of inductive reactance to a sinusoidal signal increases with frequency: `X_L = 2π*f*L`. This explains why a series inductor can better oppose high-frequency components than low-frequency current changes. In a power supply filter, a choke can reduce AC ripple while passing useful DC current after the transient. It does not "conduct only DC": the AC component also passes, but its behavior is determined by the total circuit impedance.[^aac-inductor-choke]

**Example:** in a rectifier output filter, a series choke opposes current ripple, while a capacitor shunts part of the AC ripple to ground. The outcome depends on component values, ripple frequency, and load, so a single coil does not guarantee the required attenuation in every circuit. Real windings have resistance, and parasitic capacitance can cause resonance; at sufficiently high frequencies, the simple ideal inductance model is no longer applicable.[^aac-inductor-choke]

In modern technical language, the general word "inductor" is used more often, while "choke" remains a common component designation when referring to filtering or suppressing specific signals. When selecting a component, it is important to look at the intended purpose and specifications of the specific part rather than drawing a conclusion solely from the name.[^aac-inductor-choke]

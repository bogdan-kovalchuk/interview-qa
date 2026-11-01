---
id: emb-elintro-0155
title: "What is a transformer center tap and where is it used?"
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
  - source_id: aac-center-tap-rectifier
    title: "All About Circuits: Rectifier Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/rectifier-circuits/
---

## Short answer

A center tap is an electrical tap from the midpoint of a winding that divides it into two approximately equal sections. If chosen as the common reference point, the section ends have opposite phases and equal voltage magnitudes, for example +12 V and −12 V relative to the tap if each half yields 12 V. A center tap also enables building a two-diode full-wave rectifier; the required voltage is determined by the winding rating and circuit.[^aac-center-tap-rectifier]

## Detailed explanation

A center tap is a conductive connection from an intermediate point of a winding. In a uniformly wound secondary winding, a tap at the midpoint divides it approximately in half, so each half has a similar turn count and creates a similar voltage relative to the center tap. Instantaneous voltages at the two ends have opposite phases. Designations such as 12-0-12 V typically mean 12 V RMS from the tap to each outer terminal and 24 V RMS between the outer terminals; you always verify the datasheet of the specific transformer.[^aac-center-tap-rectifier]

The tap is often chosen as a common reference point or circuit common in a bipolar power supply. Relative to it, the voltage at the outer terminals swings with opposite polarities; after rectification and filtering, one can obtain positive and negative rails. The center tap itself is not automatically ground – this depends on how it is connected in the circuit.[^aac-center-tap-rectifier]

Another common application is a two-diode full-wave rectifier. On each half-wave, a dedicated diode and the corresponding half of the secondary winding conduct, so current through the load has the same direction in both half-cycles. Such a circuit uses only half the winding at a given moment, and also requires a center-tapped transformer; a bridge rectifier instead uses four diodes and can operate without a center tap.[^aac-center-tap-rectifier]

Example: if a winding specifies 12-0-12 V AC, there will be roughly 12 V RMS between each end and the tap, and roughly 24 V RMS between the outer terminals without load or under datasheet conditions. After rectification, peak values will differ from RMS and depend on the diodes and filter.[^aac-center-tap-rectifier]

**Common mistakes:**
- calling a center tap a separate winding;
- treating it as ground regardless of connection;
- confusing the voltage of each half with the voltage between the outer terminals.

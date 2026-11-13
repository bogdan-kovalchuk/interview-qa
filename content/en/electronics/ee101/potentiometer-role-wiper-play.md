---
id: emb-elee-0011
title: "What is a potentiometer and what role does the wiper play?"
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
  - source_id: bourns-potentiometer
    title: "Bourns: 3386 Trimpot Trimming Potentiometer Datasheet"
    url: https://bourns.com/docs/Product-Datasheets/3386.pdf
---

## Short answer

A potentiometer is a resistive component with two outer terminals and a movable contact (wiper) that connects an output to a selected point along the resistive element. The full resistance is measured across the outer terminals, while the wiper divides this into two partial resistances whose sum approximately equals the total.[^bourns-potentiometer]

## Detailed explanation

A potentiometer has a resistive track and a contact that moves along it. The outer terminals connect to both ends of the track; the third terminal connects to the wiper. When the shaft rotates or the slider moves, the contact shifts its touchpoint, causing the resistance from the wiper to each end terminal to change in opposite directions.[^bourns-potentiometer]

When measured across the outer terminals, resistance `R_total` is virtually independent of wiper position. From the wiper to one end is `R_1`, and to the other end is `R_2`; for an ideal element, `R_1 + R_2 = R_total`. Physical components have overall resistance tolerance, contact resistance, and slight residual end resistance near the travel limits, so this equality is an idealized model rather than a guarantee of zero resistance at the extremes.[^bourns-potentiometer]

In a circuit used as a voltage divider, both ends of the track connect to reference voltages, and the output signal is taken from the wiper. When used as a rheostat, the circuit uses the wiper and only one outer terminal, allowing the component to adjust current or resistance in a series branch. The wiper terminal has current and power ratings specified in the datasheet; it is not intended to drive loads without checking these ratings.[^bourns-potentiometer]

Example: in a 10 kΩ potentiometer at the center position of a linear track, the unloaded resistance from the wiper to each end will be approximately 5 kΩ. Connecting external circuitry can alter the effective division of resistance and the output voltage, because the wiper load appears in parallel with that portion of the track.

**Common mistake:** assuming that the wiper is an independent voltage source or expecting the output resistance to equal `R_total`. A potentiometer merely derives a signal from the applied voltage, and its output impedance depends on contact position and loading.

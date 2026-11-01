---
id: emb-elintro-0158
title: "Why does current in a transformer change inversely to voltage?"
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
  - source_id: electronics-tutorials-transformer-basics
    title: "Electronics Tutorials: Transformer Basics and Transformer Principles"
    url: https://www.electronics-tutorials.ws/transformer/transformer-basics.html
---

## Short answer

In an ideal transformer, the input and output powers are equal: `V1*I1 = V2*I2`. Therefore, a 10-fold increase in voltage corresponds to an approximately tenfold decrease in current for the same transferred power; in a real transformer, the output power is slightly lower due to losses.[^electronics-tutorials-transformer-basics]

## Detailed explanation

In an ideal transformer, a higher voltage on one winding corresponds to a lower current in it if the transformer transfers the same power. The reason is power conservation in the ideal model: `P1 = P2`, and for a resistive load, instantaneous or average power is described by the product of voltage and current.[^electronics-tutorials-transformer-basics]

Since voltage is proportional to the number of turns, the winding currents have an inverse relationship: for an ideal transformer, `V2/V1 = N2/N1`, and `I2/I1 = N1/N2`. This does not mean that energy appears for free: a transformer changes the ratio of voltage and current rather than creating power.[^electronics-tutorials-transformer-basics]

For example, if an ideal transformer steps up the voltage from `12 V` to `120 V`, then for an input current of `1 A`, the output current is approximately `0.1 A`, neglecting losses and load phase effects. Check: `12 V*1 A = 120 V*0.1 A = 12 W`. This is an example for the ideal model; the actual output current will be lower due to losses in the core and windings.[^electronics-tutorials-transformer-basics]

In a real AC circuit, it is important to distinguish apparent power in VA from active power in W: the load power factor affects their ratio. In addition, the transformer rating limits the allowable VA power and current; the desired turns ratio alone is not sufficient to select a component.[^electronics-tutorials-transformer-basics]

**Common mistake:** concluding that stepping up voltage increases the available power. In the best case, power is transferred with almost no loss, while in a real device, output power is somewhat lower than input power.[^electronics-tutorials-transformer-basics]

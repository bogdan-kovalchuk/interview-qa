---
id: emb-elintro-0150
title: "A transformer has 100 primary turns and 1000 secondary turns – step-up or step-down?"
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
  - source_id: aac-transformer-ratio
    title: "All About Circuits: Step-up and Step-down Transformers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-9/step-up-and-step-down-transformers/
---

## Short answer

This is a step-up transformer: the secondary winding has ten times more turns than the primary. For an ideal model, an alternating 12 V on the primary yields approximately 120 V on the secondary without load; when transferring the same power, the secondary current is ten times smaller than the primary.[^aac-transformer-ratio]

## Detailed explanation

A transformer is designated step-up or step-down depending on whether it increases the voltage on the winding connected to the load. In this problem, the primary winding has `N₁ = 100` turns and the secondary has `N₂ = 1000`. Since `N₂/N₁ = 10`, the ideal model yields a secondary voltage ten times greater than the primary; therefore, this is a step-up transformer.[^aac-transformer-ratio]

A transformer requires an alternating magnetic flux that induces voltage in both windings. The ideal ratio of RMS voltages equals the turns ratio: `V₂/V₁ = N₂/N₁`. If an alternating 12 V is applied to the primary, the ideal estimate of secondary voltage is 120 V. This is not a claim about the exact voltage of a real device: losses, magnetic leakage, and loading cause deviations.[^aac-transformer-ratio]

As voltage increases, the current available for the same transferred power decreases. For an ideal transformer `V₁*I₁ = V₂*I₂`, so the secondary winding current in this example is approximately one-tenth of the primary current, neglecting magnetizing current and losses. A real transformer also draws magnetizing current, and the primary current depends on the load and construction.[^aac-transformer-ratio]

**Worked example:**

```text
N₁ = 100, N₂ = 1000
V₁ = 12 V AC
V₂ ≈ 12 * 1000/100 = 120 V AC
```

The 12 V value in the original card is an example for an ideal transformer, not a guarantee for an arbitrary component. You cannot apply a constant 12 V DC to a conventional transformer: after the transient, there is no alternating flux to induce secondary voltage, and the primary winding can overheat due to excessive current. Operation also depends on rated frequency and allowable load.[^aac-transformer-ratio]

**Common mistake:** saying step-down because "the secondary side has higher current" or mixing up the winding indices. The name is determined specifically by the voltage ratio, and a voltage increase is accompanied by a current decrease in the ideal model.[^aac-transformer-ratio]

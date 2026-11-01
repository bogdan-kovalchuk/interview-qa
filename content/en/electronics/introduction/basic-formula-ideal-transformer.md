---
id: emb-elintro-0149
title: "What is the basic formula of an ideal transformer?"
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

For an ideal transformer, `V₁/V₂ = N₁/N₂`, where `N₁` and `N₂` are the turn counts of the primary and secondary windings. Currents have an inverse relationship: `I₁/I₂ = N₂/N₁`; therefore, in the ideal model `V₁*I₁ = V₂*I₂`.[^aac-transformer-ratio]

## Detailed explanation

An ideal transformer transfers energy between two windings via a shared alternating magnetic flux in the core. For sinusoidal operation, the voltage of each winding is proportional to its turn count, so the voltage ratio equals the turns ratio: `V₁/V₂ = N₁/N₂`. Here, indices 1 and 2 designate the primary and secondary sides; it is important to compare voltages of the same type, typically RMS for a sine wave.[^aac-transformer-ratio]

With ideal coupling and no losses, input power equals output power. Consequently, a voltage increase is accompanied by an inversely proportional decrease in current, while a voltage reduction yields an increase in available current. This does not create additional power: the load determines the actual secondary current, and the primary side draws the corresponding power.[^aac-transformer-ratio]

**Worked example:**

```text
N₁ = 100, N₂ = 500
V₁ = 12 V
V₂ = V₁ * N₂/N₁ = 12 * 5 = 60 V
```

This is an estimate for the ideal model under conditions where the transformer operates with an alternating flux and does not saturate the core. A real device has winding resistance, flux leakage, and core losses, and its voltage under load differs from the ideal calculation. A conventional transformer does not transfer a constant DC voltage: after a brief transient, a constant flux does not induce secondary voltage, whereas applied DC can cause excessive current in the primary winding.[^aac-transformer-ratio]

**Common mistake:** confusing the direction of the ratio. If the secondary winding has more turns, its voltage in the ideal mode is higher, but the available output current is lower for the same level of transferred power. When selecting a real transformer, you also verify rated frequency, voltages, power rating, and allowable load.[^aac-transformer-ratio]

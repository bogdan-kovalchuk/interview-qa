---
id: emb-elintro-0147
title: "What is inductor core saturation?"
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
  - source_id: aac-core-saturation
    title: "All About Circuits: Controlling and Preventing Core Saturation in Inductors"
    url: https://www.allaboutcircuits.com/technical-articles/controlling-and-preventing-core-saturation-in-inductors/
---

## Short answer

Core saturation is the region where further increases in magnetic field produce only a small increase in magnetic flux, and the inductance of a cored inductor decreases. At a given voltage, current can then rise much faster; heating depends on resistance, the source, and the duration of the state.[^aac-core-saturation]

## Detailed explanation

Saturation occurs in a ferromagnetic core when most of its magnetic domains are already aligned with the field. Prior to this region, the material amplifies magnetic flux: a relatively small increase in field strength yields a noticeable gain in magnetic flux density. Near the "knee" of the magnetization curve, this incremental gain becomes much smaller, so the effective permeability and coil inductance drop.[^aac-core-saturation]

The consequence depends on what the circuit imposes. If the inductor is powered from an approximately constant voltage, the relationship `v = L*di/dt` means that a lower `L` yields a higher rate of current rise. This can increase losses in the winding, switch, and source, cause overheating, and disrupt converter operation. However, saturation in itself does not guarantee damage: current and temperature also depend on circuit impedance, current limiting, and operating time.[^aac-core-saturation]

**Example:** if a driver applies the same voltage to a coil and its differential inductance drops by half after entering saturation, `di/dt` in this simplified model doubles. This does not mean the current doubles instantaneously; it ramps up faster until the voltage, switch state, or current limit changes. Manufacturers often specify saturation current at a defined inductance drop, so this value must be interpreted according to their criterion rather than as a universal destruction threshold.[^aac-core-saturation]

**Common mistake:** assuming that every inductor has a core that saturates. An air core does not exhibit such saturation, although it creates a different inductance level for the same turns and current. In a design with a core, you check the operating peak current, temperature, frequency, and datasheet inductance measurement conditions.[^aac-core-saturation]

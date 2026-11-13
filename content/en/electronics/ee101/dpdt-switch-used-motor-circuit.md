---
id: emb-elee-0009
title: "Why is a DPDT switch used in a DC motor circuit?"
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
  - source_id: mit-dc-motor-switching
    title: "MIT SeaPerch: Circuits using DPDT and SPDT switches to reverse the spin direction of DC motors"
    url: https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/5/2141/files/2025/05/SeaPerchII_SciTechNotes_5.pdf
  - source_id: aratas-switch-basics
    title: "ARATAS (formerly Omron): What is an Electrical Switch?"
    url: https://www.aratas.com/sg-en/products/basic-knowledge/switches/basics
---

## Short answer

A two-position DPDT switch can be cross-wired to swap polarity across the terminals of a reversible DC motor in each position, reversing its rotation direction. Both poles switch simultaneously, but effective operation relies on proper cross-connection of the throws and motor suitability for reversal.[^mit-dc-motor-switching]

## Detailed explanation

DPDT stands for Double Pole, Double Throw: it consists of two SPDT switches mechanically linked to a single actuator. In the appropriate circuit, the contacts are used to swap the two power supply wires relative to the two motor terminals. When the switch position changes, the polarity of the voltage across the motor reverses; for a suitable reversible DC motor, this reverses the direction of rotation.[^mit-dc-motor-switching]

For this application, both center terminals of the DPDT switch are connected to the motor leads, while the outer throws are cross-connected and routed to the power supply. In one position, the motor receives standard polarity; in the other position, it receives reversed polarity. The DPDT switch itself does not produce reverse rotation automatically: without proper cross-wiring, it may merely turn off or switch other circuits. The arrangement of COM and throw terminals must be verified against the component datasheet or with a continuity test, as terminal layouts are not standardized across all packages.[^mit-dc-motor-switching]

The direction of rotation changes only for motor types that support polarity reversal across their power terminals. For instance, a simple permanent magnet brushed DC motor typically reverses when the armature current direction is reversed; other designs may require switching a separate winding or using a dedicated driver. Therefore, claiming this works for "any DC motor" would be overly broad. Furthermore, the circuit does not control speed or guarantee braking.[^mit-dc-motor-switching]

Example: with a 12 V supply, in the first switch position terminal M1 might be connected to +12 V and M2 to 0 V; after toggling, M1 receives 0 V and M2 receives +12 V. Thus, the voltage `V_M1-M2` reverses sign. This is merely an illustrative topology: the specific circuit and ratings must match the switch and the motor.[^mit-dc-motor-switching]

**Common mistakes:** assuming that any size DPDT switch can withstand a motor's inrush/starting current or that its terminals follow a standard pinout. Choose a part with ratings appropriate for the load and verify its pinout; switching suitability is governed by the specific device documentation.[^aratas-switch-basics]

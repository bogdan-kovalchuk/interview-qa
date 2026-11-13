---
id: emb-elintro-0254
title: "How does a P-channel MOSFET work as a high-side switch?"
track: electronics
section: introduction
sources:
  - source_id: ti-pmos-high-side
    title: "Texas Instruments: P-channel controllers simplify high-side gate drive"
    url: https://www.ti.com/document-viewer/lit/html/SSZT975/GUID-2E43C966-E5BD-4918-9B79-18A6DD85D045
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

The source of the P-channel MOSFET connects to `+V`, and the drain connects to the load. To turn it on, the gate is pulled below the source, establishing a negative `V_GS`; to turn it off, the gate is pulled up to the source so that `V_GS` approaches zero. The maximum rated `V_GS` must never be exceeded.[^ti-pmos-high-side]

## Detailed explanation

A P-channel MOSFET used as a high-side switch is placed between the positive supply rail and the load: the source connects to `+V`, and the drain connects to the load. The switch state is governed by the potential difference between gate and source. If the gate sits near the source level, `V_GS ≈ 0` and the transistor is off; if the gate is pulled below the source, a negative `V_GS` turns the channel on.[^ti-pmos-high-side]

This arrangement is convenient for simple circuits: a pull-up resistor can tie the gate to the source to keep the switch off, while a small discrete transistor or open-drain driver pulls the gate to a lower potential to turn it on. Because the source sits at the positive supply rail, the gate voltage must always be evaluated relative to that rail. If the control logic runs at a lower supply voltage, direct connection to a GPIO may fail to turn the device off completely or even exceed allowable `V_GS` ratings, necessitating an intermediate level-shifting transistor or dedicated driver.[^ti-pmos-high-side]

Always verify the absolute maximum `V_GS` rating in the datasheet. At higher supply voltages, pulling the gate all the way to ground can exceed the maximum allowable gate-to-source voltage, requiring voltage limiting such as a Zener diode and a resistive divider in the drive circuit. In addition, check `R_DS(on)` at the actual negative `V_GS`, load current, and power dissipation.[^ti-pmos-high-side]

A common mistake is assuming that "gate low" always means "MOSFET on." What matters is not the absolute potential relative to ground, but the gate-to-source difference. When turning off, the gate must return fully to the source potential, and the drive circuitry must clamp the voltage between these terminals safely across all supply conditions.[^ti-pmos-high-side]

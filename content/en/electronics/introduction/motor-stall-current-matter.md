---
id: emb-elintro-0230
title: "What is a motor's `stall current` and why does it matter?"
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
  - source_id: pololu-motor-stall
    title: "Pololu Jrk G2 Motor Controller User’s Guide: Choosing the motor, power supply, and Jrk"
    url: https://www.pololu.com/docs/0J73/4.1
---

## Short answer

`Stall current` is the current of a powered DC motor when its shaft is held stationary. It is typically much higher than the free-run current, so the switch, power supply, and wiring must be sized to accommodate this starting current.[^pololu-motor-stall]

## Detailed explanation

`Stall current` describes the current drawn by a brushed DC motor when a specified voltage is applied but the shaft is held stationary. While rotating, the motor generates back-EMF that opposes applied voltage and reduces current; with a stationary rotor, this effect is absent. Current is therefore determined primarily by supply voltage and winding resistance, reaching a large value associated with maximum torque and zero speed.[^pololu-motor-stall]

In datasheets, stall current is typically specified at the rated voltage of that specific motor. It is not a single universal value across all motors, nor is it necessarily a safe continuous operating point: windings heat up rapidly, and brushes and mechanical parts experience severe stress. During normal startup from standstill, the motor briefly draws a current close to stall current, which typically drops as the rotor accelerates. If the shaft is mechanically locked, high current persists and can cause thermal destruction.[^pololu-motor-stall]

Example: if motor documentation specifies a stall current of `0.8 A` at `6 V`, the driver should be sized to handle at least that starting load at this voltage, taking into account pulse duration, heatsinking, and manufacturer ratings. At a different voltage, the value will differ; a proportional voltage-scaling approximation holds only under valid assumptions regarding winding resistance and temperature. One should also verify whether the power supply can support startup without unacceptable voltage droop.[^pololu-motor-stall]

A common mistake is sizing the transistor or driver solely based on the running current of the motor after acceleration. Starting current can exceed running current many times over, and motor reversal can create an even larger transient current spike. A return path for inductive current during turn-off is also necessary, such as a suitable flyback diode in a simple switch circuit. Thus, stall current helps define peak requirements for the power path, but does not eliminate the need for thermal checks and protection circuits.[^pololu-motor-stall]

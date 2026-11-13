---
id: emb-elintro-0247
title: "What does `enhancement mode` mean and how does it differ from `depletion mode`?"
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
  - source_id: ti-mosfet-modes-an558
    title: "Texas Instruments: AN-558 Introduction to Power MOSFETs and Their Applications"
    url: https://www.ti.com/lit/an/snva008/snva008.pdf
---

## Short answer

An enhancement-mode MOSFET is normally off at `V_GS = 0`, whereas a depletion-mode MOSFET is normally on.[^ti-mosfet-modes-an558] The required polarity and magnitude of `V_GS` needed to change state depend on channel type and device construction.[^ti-mosfet-modes-an558]

## Detailed explanation

The terminology describes the state of the channel in the absence of gate-to-source drive voltage. In an enhancement-mode MOSFET, the channel is not sufficiently conductive at zero `V_GS`, so an electric field from the gate is required to form it. In a typical N-channel device, a positive `V_GS` creates the channel; in a P-channel device, the control polarity is reversed. The required voltage magnitude cannot be inferred from the word "enhancement" alone: it must be determined from the datasheet.[^ti-mosfet-modes-an558]

In depletion mode, a conducting channel already exists without any gate drive signal. Applying a control voltage modulates carrier density in the channel and can deplete it sufficiently to pinch off current. For a classic N-channel depletion MOSFET, turning off requires a negative `V_GS`; in a P-channel device, the voltage polarities are inverted. Thus, "normally on" refers to the state at a defined voltage between gate and source, rather than an undefined floating gate state.[^ti-mosfet-modes-an558]

This distinction governs circuit behavior during power-up and loss-of-control conditions. A normally-off switch is often preferred for loads that must remain de-energized until explicitly commanded. A normally-on device can be useful where conduction is required without control power, but this operating state demands appropriate protective measures and turn-off circuitry. Do not confuse channel mode with logic level: `logic-level` describes whether a control voltage is sufficient for full required enhancement, not whether the transistor is enhancement or depletion.[^ti-mosfet-modes-an558]

**Common mistake:** calling any MOSFET "normally off" without verifying its operating mode. Check the specifications table and the schematic symbol of the specific component, especially where fail-safe behavior during reset or power loss is required.

Example: an enhancement N-channel MOSFET with its source tied to common ground is off at `V_GS = 0` within rated leakage limits; to turn it on, the gate is pulled high relative to the source. This behavior cannot be transferred to a P-channel or depletion device without reversing polarity.[^ti-mosfet-modes-an558]

---
id: emb-elintro-0188
title: "What is a regulator's load regulation?"
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
  - source_id: ti-regulator-regulation
    title: "TI: Identify the Most Accurate Linear Voltage Regulator"
    url: https://www.ti.com/document-viewer/lit/html/SSZTCA7/GUID-C15E9A5E-C4B2-4C77-98A3-C375536EE8EF
  - source_id: aac-zener-regulator
    title: "All About Circuits: What Are Zener Diodes?"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/zener-diodes/
---

## Short answer

Load regulation describes the change in `V_out` when the load current changes at a fixed input; the numerical value depends on the regulator and measurement conditions.[^ti-regulator-regulation] In a simple Zener circuit, increasing `I_load` decreases `I_Z`; when `I_Z` falls below the required minimum, the output voltage sags rather than switching off instantaneously.[^aac-zener-regulator]

## Detailed explanation

Load regulation indicates how much `V_out` changes when the load varies while holding the input voltage constant. For a linear regulator, it is typically expressed as a relative change between specified load current limits or as a voltage change; values can only be compared alongside the measurement conditions.[^ti-regulator-regulation]

In a shunt regulator with a Zener diode, the current through `R_s` is approximately determined by the difference between `V_in` and `V_Z`. This current is divided between the load and the Zener diode. When the load consumes more current, `I_Z` decreases, and regulation is maintained only as long as sufficient current margin remains for the breakdown region. Therefore, the criterion for maximum load and minimum input must account for the minimum Zener diode current from its datasheet, rather than simply subtracting an arbitrary fixed value from the capacity of `R_s`.[^aac-zener-regulator]

Example: suppose the source and resistor together supply `24 mA`, and according to the selected operating point, at least `5 mA` must be left for the Zener diode. Then at this simplified point, no more than `19 mA` is available to the load. If the load demands more, the Zener diode does not "turn off" like an ideal switch: its branch current drops, and the voltage at the common node deviates from the nominal value. The numbers here illustrate the current balance rather than the parameters of a specific diode.

**Common mistakes:**

- Assuming 5–10% is a universal characteristic of all Zener regulators; load limits and a measurement criterion are required.
- Calculating only the maximum load current and failing to verify that the Zener diode maintains the required current at minimum input.[^aac-zener-regulator]

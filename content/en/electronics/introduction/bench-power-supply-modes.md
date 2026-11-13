---
id: emb-elintro-0263
title: "What is a bench power supply with `CV` and `CC` modes for?"
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
  - source_id: keysight-bench-power-supply
    title: "Keysight: An In-Depth Guide to Bench Power Supplies"
    url: https://www.keysight.com/blogs/en/tech/educ/2023/bench-power-supply
---

## Short answer

In `CV` mode, the supply maintains a programmed voltage until the load reaches the preset current limit. In `CC` mode, it regulates current at the target level by adjusting output voltage to suit the load resistance.[^keysight-bench-power-supply] Setting a current limit restricts fault current during short circuits, though it does not guarantee protection against all transients or component damage.

## Detailed explanation

A bench power supply is designed to control two primary quantities: the voltage supplied to the load and the maximum allowable current. In `CV` (constant voltage) mode, it adjusts its output so that the voltage remains at the setpoint; the load itself then primarily determines the current draw. If the current reaches the programmed limit, the power supply transitions to current regulation, and the output voltage can drop accordingly.[^keysight-bench-power-supply]

In `CC` (constant current) mode, the supply attempts to maintain the set current, while the resulting voltage depends on load resistance and behavior. This is useful, for example, when testing LEDs or battery charging circuits where clamping current is critical. CV and CC are regulation modes rather than two independent physical outputs: the active mode is determined dynamically by the programmed limits and the connected load.[^keysight-bench-power-supply]

Example: to power a 5 V board, set `CV = 5 V` and choose a current limit appropriate for the board and wiring. If a circuit fault creates a very low impedance, the supply can transition into CC and reduce its output voltage to keep current within the limit. However, a brief inrush current transient can still occur, and the current limit itself does not replace fuses or dedicated protection devices; always verify the instrument's dynamic response specifications and the load's transient sensitivity.[^keysight-bench-power-supply]

A common mistake is to treat CC as a mode that always "delivers" the set current regardless of circuit conditions. If the load requires a voltage exceeding the programmed `CV` setpoint or the instrument's maximum output limit (or if the circuit is open), the target current cannot be reached. Before connecting the load, estimate normal operating current, configure appropriate voltage and current limits, and observe which mode indicator illuminates during operation.[^keysight-bench-power-supply]

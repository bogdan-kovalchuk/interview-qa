---
id: emb-elintro-0046
title: "Is a voltmeter connected in parallel or in series, and why?"
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
  - source_id: aac-voltmeter-loading
    title: "All About Circuits: Voltmeter Impact on Measured Circuit"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-8/voltmeter-impact-measured-circuit/
---

## Short answer

A voltmeter is connected in parallel with the circuit section across which voltage is being measured. Its input resistance must be significantly larger than the resistance of that section so that the instrument current minimally perturbs the circuit operating point; the actual impact depends on both resistances.[^aac-voltmeter-loading]

## Detailed explanation

A voltmeter measures the potential difference between two points, so its probes are placed across the terminals of the element under study – that is, in parallel with it. In a parallel connection, the voltage across the instrument equals the voltage across the element. An ideal voltmeter would have infinite input resistance and draw no current, but a real voltmeter has finite resistance, forming an additional branch and slightly loading the circuit.[^aac-voltmeter-loading]

How noticeable this loading is depends on the ratio of the resistances, rather than solely on the instrument rating. For example, a digital multimeter with an input of around `10 MΩ` will barely alter the voltage across a `10 kΩ` resistor, but can significantly distort measurements in a voltage divider with megohm-range resistors. Therefore, the input specification should be checked in the instrument documentation, especially for high impedance or specialized measurement modes.[^aac-voltmeter-loading]

Connecting in series is not the proper way to measure voltage. Due to the voltmeter's large series resistance, the circuit current will drop sharply; in some circuits, the instrument may virtually stop the current, though this does not universally "open" every circuit. An ammeter, conversely, is connected in series because it measures branch current.

**Example:** for the output section of a `10 kΩ` divider, a parallel input of `10 MΩ` yields an effective resistance of about `9.99 kΩ`, so the change is minor. If the section itself has `10 MΩ`, that same instrument significantly shunts it. Thus, the "parallel" rule matches measurement topology, while the "high resistance" rule minimizes loading error.

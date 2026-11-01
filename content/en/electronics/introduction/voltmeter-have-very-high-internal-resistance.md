---
id: emb-elintro-0050
title: "Why must a voltmeter have a very high internal resistance?"
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

A voltmeter has high input resistance to draw minimal current and reduce circuit loading. A value around `10 MΩ` is a common example for a digital multimeter, but not a universal specification; measurement error depends on the resistance of the circuit section being measured.[^aac-voltmeter-loading]

## Detailed explanation

A voltmeter is connected in parallel, and its high input resistance is required to minimize current drawn from the circuit under test. An ideal meter would possess infinite resistance and have zero effect on circuit voltages; a real instrument has finite resistance, thereby forming an additional parallel branch. This effect is known as measurement loading.[^aac-voltmeter-loading]

What matters is not an abstractly "large" number, but rather the ratio between the meter's input resistance and the resistance of the source or circuit section being measured. A `10 MΩ` input will barely affect a low-resistance circuit, but can significantly alter a voltage divider composed of megohm-range resistors. Consequently, even a properly functioning multimeter may display a voltage distinct from the unloaded node voltage: during measurement, the instrument itself becomes part of the circuit.[^aac-voltmeter-loading]

**Example:** a voltage divider formed by two `10 MΩ` resistors has an output resistance of several megohms. A `10 MΩ` voltmeter connected in parallel across the output is no longer much larger than this resistance and markedly shifts the divider ratio. Conversely, across a `10 kΩ` resistor, the same voltmeter has a much smaller effect. To evaluate this effect, one can replace the output section with its equivalent resistance and analyze the parallel combination with the meter's input resistance.[^aac-voltmeter-loading]

Input resistance values must be verified in the multimeter's specifications for the selected mode and range: it is not necessarily identical across all ranges and functions. High-impedance measurements can also depend on leakage, board contamination, and long leads. Therefore, high resistance reduces loading error, but does not guarantee zero error or imply that any given instrument is suitable for every circuit.[^aac-voltmeter-loading]

---
id: emb-elintro-0136
title: "How does resistor tolerance affect the real value?"
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
  - source_id: fda-resistor-tolerance
    title: "FDA: Electronic Components – Resistors"
    url: https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-technical-guides/electronic-components-resistors
---

## Short answer

Tolerance specifies the allowable deviation of actual resistance from the nominal value under specified conditions. For `1 kΩ ±5%`, the limits are `950 Ω` and `1050 Ω`; this is a range, not a promise that the measured value will sit exactly on one of the boundaries.[^fda-resistor-tolerance]

## Detailed explanation

Resistor tolerance is the maximum allowable deviation of its resistance from the nominal value under conditions specified by the manufacturer. The nominal value is the marked value, while tolerance specifies the interval of possible values for a new component; it does not mean that the resistor necessarily has an error of that exact magnitude.[^fda-resistor-tolerance]

For `1 kΩ ±5%`, calculate five percent of 1000 Ω: `0.05*1000 Ω = 50 Ω`. Therefore, the permissible interval extends from `1000 Ω - 50 Ω = 950 Ω` to `1000 Ω + 50 Ω = 1050 Ω`. This is the initial tolerance under the stated conditions, not a complete guarantee of stability under all operating conditions.[^fda-resistor-tolerance]

Temperature coefficient, self-heating from dissipated power, aging, and humidity can further alter resistance. For accurate circuit calculations, it is important to check the documentation not only for tolerance, but also for other component parameters and operating conditions. In a voltage divider, extreme values of both resistors can combine to shift the output, so analyze the worst-case combination rather than just nominal figures.[^fda-resistor-tolerance]

Example: if the measured resistance is `1030 Ω`, it still falls within the given interval and complies with the tolerance. A value of `1060 Ω` would exceed the limit for a new resistor under the same conditions, but before drawing a conclusion, verify the meter accuracy, component temperature, and whether the resistor is disconnected from parallel paths in the circuit.

**Common mistake:** treating ±5% as measurement accuracy or assuming that every resistor deviates by exactly 5%. Tolerance describes acceptable boundary values; the actual value can lie anywhere within the range.

---
id: emb-elintro-0130
title: "Which capacitor types are polarized and which are not?"
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
  - source_id: aac-capacitor-polarity
    title: "All About Circuits: Practical Considerations - Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/practical-considerations-capacitors/
---

## Short answer

Common aluminum electrolytic and tantalum capacitors are polarized: they must be connected with the correct polarity indicated on the case.[^aac-capacitor-polarity] Ceramic and film capacitors are typically non-polarized, but the component type should be verified from the marking and datasheet.[^aac-capacitor-polarity] You cannot generalize that polarized capacitors are always cheaper or have higher capacitance: the choice depends on requirements and the specific series.

## Detailed explanation

Polarity describes the permissible sign of the voltage between a component's terminals. In a typical polarized capacitor, the internal construction is designed for a specific voltage direction, so its marked positive or negative terminal must match the circuit. Reverse connection can damage the component; for electrolytic and tantalum capacitors, this is an especially critical constraint.[^aac-capacitor-polarity]

Common aluminum electrolytic and tantalum capacitors are polarized. Polarity is typically indicated on the package: in different designs, the marking may designate the negative or the positive lead, so do not rely solely on the familiar look of a stripe or lead length. Before installation, check the specific part and its datasheet.[^aac-capacitor-polarity]

Ceramic and film capacitors are typically non-polarized, meaning their leads can be swapped without violating polarity. This does not mean they are interchangeable with any other type: voltage rating, capacitance, temperature characteristics, and application remain important. A generic family name does not replace checking the specific component, especially when the designation on the schematic or package is ambiguous.[^aac-capacitor-polarity]

Example of a pre-assembly check: find the polarity marking on the case, verify it against the documentation, and then match the positive circuit node with the positive terminal of the polarized component. For a non-polarized ceramic capacitor, such terminal matching for polarity is not required, although orientation may matter for mechanical placement or other design requirements.[^aac-capacitor-polarity]

**Common mistakes:**

- Assuming any electrolytic capacitor is suitable for connection in either direction.
- Determining polarity solely from the package shape without reading its markings.
- Assuming that all ceramic and film parts can be chosen without checking the voltage rating and datasheet.[^aac-capacitor-polarity]

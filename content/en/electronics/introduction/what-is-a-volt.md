---
id: emb-elintro-0023
title: "What is a volt?"
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
  - source_id: nist-sp330-section2
    title: "NIST Special Publication 330: The International System of Units, Section 2"
    url: https://www.nist.gov/pml/special-publication-330/sp-330-section-2
---

## Short answer

The volt (V) is the unit of electric potential difference; `1 V = 1 J/C`. It indicates how much energy is associated with a unit of charge transferred between two points.[^nist-sp330-section2]

## Detailed explanation

Voltage between two points describes the change in electric potential energy per unit charge. One volt equals one joule per coulomb: `V = E/Q`.[^nist-sp330-section2]

Voltage is always defined between two points, not "at a single point". Its polarity depends on the order in which the measurement points are selected. A source creates a potential difference, while a closed path and component properties determine the current; voltage alone does not guarantee a specific current.[^aac-direct-current]

The pressure analogy sometimes helps visualize the role of voltage in a circuit, but it is not a definition and does not replace circuit laws. In particular, current also depends on the load and its operating conditions, such as the resistance in a simple resistive circuit.[^aac-direct-current]

The sign of the voltage depends on the chosen order of points: swapping the voltmeter probes reverses the sign of the reading, even though the physical potential difference between the same points does not disappear. Therefore, it is useful to indicate a reference node and measurement polarity in a schematic. This is especially important when comparing multiple voltages or verifying the voltage drop across a component.[^aac-direct-current]

**Example:** if a charge of `2 C` receives `6 J` of energy while moving between points, the potential difference equals `V = E/Q = 6 J/2 C = 3 V`.

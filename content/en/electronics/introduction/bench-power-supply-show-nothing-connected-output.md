---
id: emb-elintro-0107
title: "What does a bench power supply show when nothing is connected to its output?"
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
  - source_id: aac-open-circuit
    title: "All About Circuits: Resistance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-1/resistance/
---

## Short answer

With no load connected, the output circuit is open, so the load current is 0 A. The voltage display can show the set output voltage, while the current indicator will show zero or a value near zero. Once a load is connected, the current is determined by the voltage, resistance, and the power supply's current limit mode.[^aac-open-circuit]

## Detailed explanation

When nothing is connected to the output terminals of a bench power supply, a voltage may be present across the terminals, but there is no closed path through an external load. This condition is called an open circuit: charge does not have a complete conductive path, so the current in the external circuit is zero. This does not mean the output voltage is also zero: a voltage source can maintain the set potential difference across unloaded terminals.[^aac-open-circuit]

Therefore, the displayed value depends on which indicator is being considered. The voltmeter displays the set voltage if the output is enabled; the ammeter reads 0 A or a very small value caused by measurement offset or the instrument's own internal currents. If the output is turned off with the `OUTPUT` button, the voltage reading may be zero even when the voltage control is set above zero. Display behavior, resolution, and whether current is measured at the output depend on the specific power supply model.[^aac-open-circuit]

Once a resistor is connected, the circuit is closed, and the current is approximately determined by Ohm's law. For example, for an ideal 5 V source and a 1 kΩ resistor, the current would be 5 mA; the real-world result also depends on component tolerances, wire resistance, and the configured current limit. If the load demands more current than the limit allows, the supply enters constant-current mode and the output voltage drops. Thus, the correct short answer for the current indicator is zero under no load, but this does not predict the voltage reading or the state when the output is turned off.[^aac-open-circuit]

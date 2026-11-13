---
id: emb-elintro-0245
title: "What is the body diode in a MOSFET?"
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
  - source_id: toshiba-body-diode
    title: "Toshiba: What are the characteristics of MOSFET body diodes?"
    url: https://toshiba.semicon-storage.com/ap-en/semiconductor/knowledge/faq/mosfet/electrical-characteristics-of-mosfetsbody-diode-idr-idrp-vdsf-tr.html
---

## Short answer

The body diode is an inherent parasitic PN junction between source and drain formed by the MOSFET semiconductor structure. In a standard enhancement-mode N-channel MOSFET, its anode connects to the source and its cathode connects to the drain, so it conducts in reverse when the transistor is off; the polarity is inverted for P-channel devices.[^toshiba-body-diode]

## Detailed explanation

The body diode is a parasitic PN junction between source and drain inherent to the structure of a power MOSFET. In a conventional discrete N-channel component, the diode has its anode at the source and its cathode at the drain; in a P-channel device, this polarity is reversed. Always verify the schematic symbol of the specific component in its datasheet.[^toshiba-body-diode]

The gate controls the channel, but does not eliminate this PN junction. Therefore, an off-state MOSFET does not block current bidirectionally: if the source voltage is sufficiently higher than the drain voltage in an N-channel device, the body diode can forward-bias and conduct current. In a simple unidirectional switch, this means a reverse-polarity load or power source can create an unintended conduction path.[^toshiba-body-diode]

Forward voltage drop, rated forward current, and reverse-recovery characteristics vary by part number and manufacturer test conditions. The diode can provide a useful freewheeling path for inductive currents, such as during the dead time of a half-bridge, but its losses and recovery speed must be evaluated for the specific circuit. In a synchronous rectifier, once the channel turns on, current can commutate from the body diode into the low-resistance MOSFET channel, reducing losses under proper control timing.[^toshiba-body-diode]

Example: in a low-side N-channel switch, the drain typically connects to the load and the source connects to ground. The body diode points from source to drain, so under normal positive load voltage it is reverse-biased when the switch is turned off. Reversing the power supply polarity, however, can forward-bias the diode even with no gate drive signal applied.[^toshiba-body-diode]

**Common mistake:** assuming that turning off the gate isolates drain from source bidirectionally. Before finalizing a design, verify the body diode orientation on the component schematic, check the reverse voltage rating, and analyze the current in all operating states.[^toshiba-body-diode]

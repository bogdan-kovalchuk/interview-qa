---
id: emb-elintro-0176
title: "What is a wired-OR circuit and why does it use Schottky diodes?"
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
  - source_id: ti-diode-oring
    title: "TI: PowerPath Management Solution for ASH"
    url: https://www.ti.com/lit/pdf/SLVAF21
  - source_id: aac-schottky-diodes
    title: "All About Circuits textbook: Special-purpose Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
  - source_id: ti-schottky-selection
    title: "TI: Schottky Diode Selection in Asynchronous Boost Converters"
    url: https://www.ti.com/tw/lit/pdf/snva762
---


## Short answer

In a diode ORing circuit, each power source is connected to a common output through a diode that allows current to flow to the load while isolating branches from reverse current. Schottky diodes are often chosen for their relatively low forward voltage drop, but the exact value depends on the specific diode, current, and temperature.[^ti-diode-oring][^aac-schottky-diodes]

## Detailed explanation

Diode ORing combines multiple power sources so that the load can receive power from an available branch while preventing current from flowing back from the output into another source. To achieve this, each branch is connected through a diode: anode toward the source, cathode toward the common node. When a source voltage is sufficient, its diode conducts; if another branch's voltage is lower, its diode turns off and blocks reverse current. This does not guarantee ideal redundancy: source voltages, regulation characteristics, and switching conditions determine which branch actually carries the load.[^ti-diode-oring]

In an example with USB and an adapter, this connection reduces the risk of back-feeding voltage from one input into the other. Two sources should not simply be wired in parallel unless their manufacturers permit current sharing: even a slight difference in output voltage can force one source to sink current from the other. The diode provides isolation, but its voltage drop reduces the voltage delivered to the load.[^ti-diode-oring]

Schottky diodes are often used because their forward voltage drop is typically lower than that of a standard silicon rectifier diode, which can reduce losses `P = V_f*I`. A value like `0.3 V` is not a fixed property of all Schottky diodes: check the graph or specification for the specific part at the operating current and temperature. Also important are maximum reverse voltage, allowable current, and reverse leakage, which can increase significantly with temperature in Schottky diodes.[^aac-schottky-diodes][^ti-schottky-selection]

**Common mistakes:**
- assuming that both sources automatically share current equally;
- taking `0.3 V` as a guaranteed drop for every diode;
- neglecting heating from forward current and reverse leakage.[^ti-diode-oring][^ti-schottky-selection]

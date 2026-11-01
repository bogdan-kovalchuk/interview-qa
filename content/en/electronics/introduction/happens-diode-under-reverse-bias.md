---
id: emb-elintro-0185
title: "What happens to a diode under reverse bias?"
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
  - source_id: ti-zener-reverse-breakdown
    title: "SLVAG25 Application Brief: Zener Noise Phenomenon"
    url: https://www.ti.com/document-viewer/lit/html/SLVAG25/GUID-C0A4AD58-A8D2-4977-8B36-7D8455E203BA
---

## Short answer

Almost no current flows, so the voltage drop across a series resistor is near zero, and almost the entire applied voltage appears across the diode in the reverse direction. If |`V_reverse`| &gt; `V_RRM`, breakdown can occur.[^ti-zener-reverse-breakdown]

## Detailed explanation

Under reverse bias, a positive potential is applied to the cathode relative to the anode. The electric field pulls majority charge carriers away from the PN junction, widening the depletion region and the barrier to their flow. Therefore, in normal operation the diode passes only a small reverse leakage current rather than acting as an ideal open switch.[^aac-semiconductors]

Leakage depends on material, temperature, and applied voltage, and is specified for a particular component under datasheet conditions. If the voltage reaches the breakdown voltage, the reverse current can rise sharply. In a Zener diode, this is the normal operating mode provided current is limited; an ordinary rectifier diode can overheat and fail.[^aac-semiconductors]

In a simple series circuit with a resistor, the voltage across it is determined by the actual leakage. For a rough estimate it can be neglected, but the drop is not necessarily zero. You cannot assume that a diode withstands arbitrary reverse voltage: verify `V_RRM` in the datasheet and account for circuit voltage spikes.[^aac-semiconductors]

Example: if the source applies a reverse 5 V to a diode operating far from its breakdown limit, only a small leakage current flows and almost the entire voltage drops across the diode. If the permissible repetitive peak value `V_RRM` is exceeded, the circuit no longer has a guaranteed safe operating condition.[^aac-semiconductors]

**Common mistake:** calling the reverse current strictly zero or confusing the rated limit with the voltage at which every diode is guaranteed to be destroyed. Check the component type and datasheet: breakdown can be a normal operating mode for one diode and catastrophic for another.

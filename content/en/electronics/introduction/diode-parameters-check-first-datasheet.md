---
id: emb-elintro-0172
title: "Which diode parameters should you check first in a datasheet?"
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
  - source_id: onsemi-nsr0630p2-datasheet
    title: "onsemi NSR0630P2 Schottky Barrier Diode datasheet"
    url: https://www.onsemi.com/download/data-sheet/pdf/nsr0630p2-d.pdf
---


## Short answer

Start with repetitive peak reverse voltage `V_RRM`, required forward current `I_F`, and forward voltage drop `V_F` at that specific current. Also check reverse leakage, thermal limits, surge current, and test conditions: ratings depend on temperature and mounting.[^onsemi-nsr0630p2-datasheet]

## Detailed explanation

Diode parameters should be read as a set of constraints for a specific circuit rather than a single universal number. First verify that `V_RRM` withstands the highest repetitive reverse voltage including transients and safety margin. `I_F` must match the average and peak current of the circuit; allowable current is often limited not by the die itself, but by heating for a given copper area or ambient temperature.[^onsemi-nsr0630p2-datasheet]

Next, find `V_F` at your operating current: a value at 10 mA does not predict the drop at 1 A. For forward conduction loss, the estimate `P = V_F*I_F` is useful; then check thermal resistance, power dissipation rating, and maximum junction temperature. In a rectifier, surge current `I_FSM` is also important, but a brief surge rating does not permit continuous operation at that current.[^onsemi-nsr0630p2-datasheet]

Reverse leakage `I_R` can be significant in battery-powered devices or at elevated temperatures. Check the test conditions – reverse voltage and temperature – and graphs if your operating point lies between table values. For example, the NSR0630P2 datasheet lists `V_F` for several specified currents and `I_R` at specific values of `V_R`; these numbers apply specifically to this device, not to all diodes.[^onsemi-nsr0630p2-datasheet]

**Common mistake:** comparing two diodes based solely on maximum current or typical `V_F` while ignoring test conditions, cooling, and reverse leakage. Check table columns and notes, not just the parameter header.

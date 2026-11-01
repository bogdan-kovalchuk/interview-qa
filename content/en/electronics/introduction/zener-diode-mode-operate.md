---
id: emb-elintro-0164
title: "What is a Zener diode and in which mode does it operate?"
track: electronics
section: introduction
sources:
  - source_id: onsemi-zener-handbook
    title: "onsemi: Zener Theory and Design Considerations Handbook"
    url: https://www.onsemi.com/PowerSolutions/document/HBD854-D.PDF
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

A Zener diode is specifically designed to operate under reverse bias in the breakdown region. There, the voltage across it is nearly constant and changes only weakly with current (dynamic resistance), so it regulates the voltage across a load. This requires current limiting, typically with a series resistor.[^onsemi-zener-handbook]

## Detailed explanation

A Zener diode is a diode designed to operate in the reverse direction near a controlled breakdown voltage. In standard operation below breakdown, only a small leakage current flows. When the reverse voltage reaches the breakdown region, current increases sharply, while the voltage across the diode changes relatively little. The name "Zener" in catalogs covers components where the breakdown mechanism can be Zener or avalanche.[^onsemi-zener-handbook]

A practical regulator typically connects the Zener diode in parallel with the load, and a series resistor limits the total current. Excess current beyond the load requirements flows through the diode. If the input voltage increases or the load draws less, the Zener current increases; if the load draws more, this current decreases. Regulation is possible only while the current remains within the limits specified in the datasheet, particularly above the knee current and below the maximum allowable current.[^onsemi-zener-handbook]

Therefore, a Zener diode does not "hold V_Z" unconditionally. Its voltage depends slightly on current through dynamic resistance, as well as on tolerance, temperature, and self-heating. The diode power is estimated as `P = V_Z*I_Z`; the resistor must also withstand its own power dissipation. Without current limiting, connecting to a voltage source higher than V_Z can damage the diode.[^onsemi-zener-handbook]

**Example:** for an educational model, a 12 V source powers a 5.1 V Zener diode through a 680 Ω resistor, no load is connected, and the source and diode are assumed ideal. The current is approximately `(12 V - 5.1 V)/680 Ω`, that is, 10.1 mA; the diode power is about `5.1 V*10.1 mA`, or 52 mW. This is only an estimate: real-world selection requires verifying the minimum regulation current, source tolerances, maximum current, and thermal conditions against the datasheet.[^onsemi-zener-handbook]

**Common mistakes:**
- Considering a Zener diode an ordinary diode that regulates voltage in the forward direction.
- Connecting it to a source without series current limiting.
- Considering V_Z absolutely constant regardless of current and temperature.[^onsemi-zener-handbook]

---
id: emb-elintro-0178
title: "Why is a large electrolytic capacitor needed after the rectifier in a power supply?"
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
  - source_id: adi-rectifier-filter
    title: "Analog Devices Wiki: Chapter 6: Diode applications"
    url: https://wiki.analog.com/university/courses/electronics/text/chapter-6
  - source_id: aac-bridge-filter-lab
    title: "All About Circuits: Full-wave Bridge Rectifier With Output Filtering"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-5/rectifier-filter-circuit/
---

## Short answer

A large electrolytic capacitor after the rectifier stores charge near the peaks and delivers it to the load between peaks, reducing ripple. The required capacitance depends on load current, ripple frequency, and permissible voltage variation; the "1000 µF per amp" guideline is only a rough rule of thumb for specific assumptions.[^adi-rectifier-filter]

## Detailed explanation

After rectification, the voltage has repeating peaks, and between them the source delivers almost no energy to the load. A large electrolytic capacitor is connected in parallel with the output so that it charges near the peak of the rectified voltage, and then maintains the load current while the instantaneous source voltage is lower than the capacitor voltage. Because of this, the output becomes closer to DC, although the residual periodic variation – ripple – never disappears completely.[^aac-bridge-filter-lab][^adi-rectifier-filter]

Between peaks, the capacitor discharges. At higher load currents or longer intervals between peaks, it loses more charge; a larger capacitance reduces this voltage variation. For a single-phase bridge, there are two peaks per period of the input sinusoid, so the ripple frequency is twice the source frequency. For half-wave rectification, there is only one peak per period, so under otherwise identical conditions the capacitor must wait longer for the next recharge.[^adi-rectifier-filter]

For an approximate estimate with relatively small ripple, `ΔV ≈ I_load/(f_ripple*C)` is used. This approximation does not account for ESR, the pulsed nature of current through the diodes, transformer winding resistance, or load variations, so the final choice is verified for the actual circuit and allowable ripple. Too small a capacitance yields noticeable dips; an excessively large one can increase pulsed charging current and stress on the diodes and transformer.[^adi-rectifier-filter][^aac-bridge-filter-lab]

**Worked example:** for a bridge from `50 Hz`, we have `f_ripple = 100 Hz`. If the load draws `0.5 A` and the target ripple is `2 V`, the idealized estimate gives `C ≈ 0.5/(100*2) = 0.0025 F`, which is about `2500 µF`. This is an initial estimate, not a finished component rating: add a margin and check the voltage rating, ripple-current rating, and inrush current.[^adi-rectifier-filter]

**Common mistake:** considering the `1000 µF per amp` guideline to be universal. Such a rule of thumb specifies neither rectifier topology, nor frequency, nor acceptable ripple, so for a different load it may produce an unusable result.[^adi-rectifier-filter]

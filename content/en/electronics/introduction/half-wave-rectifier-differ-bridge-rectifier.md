---
id: emb-elintro-0177
title: "How does a half-wave rectifier differ from a bridge rectifier?"
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
  - source_id: aac-half-wave-lab
    title: "All About Circuits: Si Lab - Half-wave Rectifier"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-5/half-wave-rectifier/
  - source_id: aac-bridge-filter-lab
    title: "All About Circuits: Full-wave Bridge Rectifier With Output Filtering"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-5/rectifier-filter-circuit/
---

## Short answer

A half-wave rectifier passes only one half-cycle of `AC`, whereas a bridge rectifier rectifies both, so its post-filtering ripple is typically lower. In a bridge circuit, current flows through two diodes during each half-cycle, so the total forward voltage drop must be accounted for; average output voltage depends on the load, filter, and diodes.[^aac-half-wave-lab][^aac-bridge-filter-lab]

## Detailed explanation

A half-wave rectifier converts AC voltage into unidirectional pulses by passing only one half-cycle of the input signal. The simplest circuit uses a single diode: during the forward half-cycle it conducts, and during the reverse half-cycle it blocks current. Without a smoothing capacitor, the output is not a steady voltage – it is a pulsating voltage with a gap between pulses.[^aac-half-wave-lab]

A bridge rectifier, or full-wave bridge rectifier, uses four diodes. During each half-period a dedicated pair of diodes conducts, but current through the load flows in the same direction. Therefore, two pulses appear at the output per source period instead of one; for a 60 Hz line, the fundamental ripple frequency after the bridge is 120 Hz, and for 50 Hz it is 100 Hz. A bridge does not produce ideal DC: without a filter, the voltage still pulsates.[^aac-bridge-filter-lab]

If both circuits have a capacitor in parallel with the load, it charges near the peaks and delivers charge to the load between them. In a full-wave circuit, the interval between peaks is shorter, so for identical capacitance and current the capacitor discharges less and the ripple is typically smaller. However, the bridge has two series diode junctions in the current path, which lowers the peak output voltage; the actual voltage is also determined by the transformer, diodes, load, and capacitor.[^aac-bridge-filter-lab]

**Example:** if the input has a frequency of 50 Hz, a half-wave rectifier gives one charging peak per period, or 50 peaks per second, while a bridge gives two, or 100. This explains the difference in ripple frequencies, but does not by itself determine its amplitude: it depends on the load and capacitance.[^aac-half-wave-lab][^aac-bridge-filter-lab]

**Common mistake:** stating that a bridge rectifier always provides a higher average voltage without qualifications. Smoothing and load change the average value, and the two forward junctions of the bridge add voltage drops; comparisons must be made under identical conditions.[^aac-bridge-filter-lab]

---
id: emb-elee-0107
title: "What distorts filter measurements at high frequencies?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: tek-probe-capacitive-loading
    title: "Tektronix: How Oscilloscope Probes Affect Your Measurement"
    url: https://www.tek.com/en/documents/application-note/how-oscilloscope-probes-affect-your-measurement
---

## Short answer

Probe input capacitance and parasitic wiring parameters load the circuit node and alter the measured amplitude, phase, or waveform, as the probe's capacitive reactance drops at high frequencies.[^tek-probe-capacitive-loading] Consequently, deviations from the theoretical model may stem from the measurement setup itself.

## Detailed explanation

At high frequencies, the measurement signal path itself becomes part of the circuit: the probe, cable, breadboard, and interconnects add capacitance, inductance, and resistance. In particular, the probe's input capacitance exhibits lower reactance as frequency increases, so it loads the node more heavily and can alter the signal's amplitude, phase, and edge transitions.[^tek-probe-capacitive-loading]

For an ideal RC filter, a single pole is sufficient, but such a model does not capture all the details of a real test bench. Parasitic capacitance together with the node's output resistance forms an additional time constant; lead inductance and capacitance can interact to cause resonance. This does not mean the basic formula is wrong: it simply does not include these components. Their effect becomes noticeable when the parasitic impedance becomes comparable to the impedance of the node under test.

For example, if a probe is connected to a high-impedance node, its capacitance can substantially reduce the measured bandwidth. Tektronix demonstrates that higher probe capacitance distorts the edge and increases rise time; thus, the mere fact of having high input resistance, such as 10 MΩ, does not guarantee the absence of loading at high frequencies.[^tek-probe-capacitive-loading]

**Common mistakes:**
- Attributing the entire change in frequency response to a defect in the filter itself.
- Ignoring probe capacitance simply because the probe specifies a high input resistance.

To verify the result, use a probe with low input capacitance, a short ground lead, and compact layout. Compare measurements with the probe connected and disconnected, or change probe types; if the response changes noticeably, the measurement loading must be included in the model.

---
id: emb-elee-0247
title: "Where can overshoot and ringing that are not in the circuit come from on a clock waveform?"
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
  - source_id: keysight-probing-5988-5021
    title: "Keysight: Optimizing Oscilloscope Measurement Accuracy on High-Performance Systems with Keysight Active Probes (application note 5988-5021EN)"
    url: https://prc.keysight.com/Content/PDF_Files/5988-5021EN.pdf
---

## Short answer

Overshoot and ringing can be introduced by a long oscilloscope probe ground lead: its parasitic inductance forms a resonant LC circuit with the probe's input capacitance.[^keysight-probing-5988-5021] Using a short ground attachment minimizes inductance and shifts the ringing frequency beyond the bandwidth of the probe and oscilloscope.[^keysight-probing-5988-5021]

## Detailed explanation

Overshoot is the excursion of voltage past the final level following an edge, and ringing consists of decaying oscillations following that same edge. When such spikes appear on a waveform and are not present in the circuit, the question is whether they are part of the design or were caused by the measurement system. Keysight puts this question directly to the engineer.[^keysight-probing-5988-5021]

The mechanism in the ground lead is as follows: the wire adds an inductance L, and the probe has an input capacitance C. Keysight describes ringing as an LC circuit formed by the probe capacitance and the inductance of the ground lead and probe tip.[^keysight-probing-5988-5021] The resonant frequency of such a tank is `f = 1/(2*pi*sqrt(L*C))`. For illustration, let `L = 200 nH` and `C = 16 pF`: `f = 1/(2*pi*sqrt(200e-9*16e-12)) ≈ 89 MHz`. Keysight quotes up to 25 nH per inch for wires extending the probe signal path.[^keysight-probing-5988-5021] The value of 200 nH for the ground lead here is an order-of-magnitude assumption, not a value taken from the source.

The same calculation for a wire with an inductance on the order of 25 nH (one inch according to Keysight) yields `f ≈ 252 MHz`. A higher ringing frequency moves outside the bandwidth of the oscilloscope and probe more easily, which aligns with Keysight's guidance.[^keysight-probing-5988-5021] The numbers are illustrative: 200 nH and 16 pF are assumptions, not the specifications of a particular probe.

Probe bandwidth also operates in the reverse direction. Beyond the probe bandwidth, signal amplitudes become excessively attenuated, and measurements become unpredictable.[^keysight-probing-5988-5021] Therefore, edges measured outside the bandwidth may appear softer than they actually are. Within the bandwidth, the probe's internal resonance can cause the output to differ from the input and manifest as overshoot and ringing.[^keysight-probing-5988-5021]

For accurate edge-time measurements, Keysight advises using the shortest possible ground wire.[^keysight-probing-5988-5021] Practical verification: repeat the measurement with a shorter ground connection and compare the waveform. If the ringing disappears or shifts, it originates in the measurement setup rather than the circuit.

**Common mistakes:**

- Searching for the cause of overshoot and ringing in the circuit without checking the probe ground;[^keysight-probing-5988-5021]
- Assuming that ringing within the probe bandwidth is always a circuit property: the probe's internal resonance can introduce overshoot and ringing;[^keysight-probing-5988-5021]
- Evaluating edge shape outside the oscilloscope or probe bandwidth, where amplitude is attenuated.[^keysight-probing-5988-5021]

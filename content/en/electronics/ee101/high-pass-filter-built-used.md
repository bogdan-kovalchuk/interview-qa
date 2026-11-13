---
id: emb-elee-0108
title: "How is an RC high-pass filter built and where is it used?"
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
  - source_id: aac-capacitive-high-pass
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
---

## Short answer

In a simple RC high-pass filter, a capacitor is placed in series with the input, and the output is taken across a resistor connected to common ground.[^aac-capacitive-high-pass] The capacitor attenuates lower frequencies, while higher frequencies pass through above the cutoff frequency, allowing the circuit to serve as an AC coupling network.

## Detailed explanation

A first-order RC high-pass filter consists of a capacitor connected in series with the signal path and a resistor connected from the output node to common ground; the output voltage is measured across the resistor.[^aac-capacitive-high-pass]

The capacitor's impedance decreases as frequency increases. At low frequencies it is large, so most of the signal drops across the capacitor and less voltage reaches the load. At high frequencies its impedance becomes small, so the signal appears across the resistor. For a DC voltage after the transient has settled, an ideal capacitor is equivalent to an open circuit, so the DC component is blocked.[^aac-capacitive-high-pass]

The transition frequency depends on the capacitance and the effective resistance seen by the capacitor. The actual input of a subsequent stage may act as a parallel load to the resistor, and the generator's output resistance also affects the transfer characteristic; therefore, the nominal value of a single resistor is not always equal to the effective R.[^aac-capacitive-high-pass]

**Example:** in an audio signal path, a series capacitor can block the DC bias between stages while passing the AC audio signal above a chosen cutoff frequency. In a loudspeaker crossover, a capacitor in front of a tweeter attenuates low frequencies, although a simple RC example does not fully model a complete crossover with the frequency-dependent impedance of a loudspeaker driver.[^aac-capacitive-high-pass]

**Common mistakes:**
- Taking the output across the capacitor and expecting high-pass behavior: that point corresponds to a different response.
- Calling a high-pass filter a "DC blocker" without the caveat regarding transients and leakage in real capacitors.

The circuit is used for AC coupling and for attenuating low-frequency components. Before calculating, verify the load and where the output is taken: they determine the actual cutoff frequency and the passband level.

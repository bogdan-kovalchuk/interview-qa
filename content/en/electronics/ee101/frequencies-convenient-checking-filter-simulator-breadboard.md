---
id: emb-elee-0086
title: "Which frequencies are convenient for checking an RL filter in a simulator and on a breadboard?"
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
---

## Short answer

Test the RL filter at frequencies of `0.1*f_c`, `f_c`, and `10*f_c`, measuring `V_in`, `V_out`, the amplitude ratio, and the phase at each point.[^aac-alternating-current] A real inductor has winding resistance, so practical results will deviate from the ideal model.[^aac-alternating-current]

## Detailed explanation

The cutoff frequency `f_c` is determined by the nominal values of R and L; for a series RL circuit, it corresponds to the point where the magnitudes of the resistance and inductive reactance are equal. The output voltage depends on which component it is taken from, so clarify the circuit schematic and the output node before measuring.[^aac-alternating-current]

The points `0.1*f_c`, `f_c`, and `10*f_c` lie below the cutoff, near it, and above it. They quickly show whether the signal transmission changes in the expected direction. For a first-order filter, the amplitude at cutoff relative to the passband level is approximately `1/sqrt(2)`, or 0.707 or −3 dB; the phase also changes near this region.[^aac-alternating-current]

In a simulator, configure an AC sweep or test individual sinusoidal signals. On a breadboard, verify the actual component values, winding resistance, and instrument loading: they alter the response compared to an ideal calculation. The trio of frequencies is not a fixed set of hertz, but scales relative to the circuit's own `f_c`.[^aac-alternating-current]

**Common mistakes:**
- Using arbitrary frequencies without calculating `f_c`.
- Ignoring the inductor's winding resistance and the output load.

For example, with `R = 1 kΩ` and `L = 100 mH`, `f_c = R/(2*pi*L)`, which is approximately 1.59 kHz. In that case, test near 159 Hz, 1.59 kHz, and 15.9 kHz, provided the generator and components operate in that range.[^aac-alternating-current]

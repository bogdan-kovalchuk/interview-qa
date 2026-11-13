---
id: emb-elee-0071
title: "Which conventions must be kept consistent within one phasor problem?"
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
  - source_id: aac-phasor-conventions
    title: "All About Circuits: Simple AC Circuit Calculations"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/simple-ac-circuit-calculations/
---

## Short answer

Within a single phasor calculation, maintain a consistent amplitude representation (for instance, all RMS or all peak values) and a single phase reference. Phasors directly describe sinusoidal quantities of a single frequency. Components of different frequencies must be analyzed separately, and their instantaneous signals can then be summed in the time domain.[^aac-phasor-conventions]

## Detailed explanation

A phasor is a complex representation of the amplitude and phase of a sinusoidal signal at a specified frequency. It simplifies the differential equations of a circuit into algebra with complex impedances, but all voltages and currents within one such calculation must correspond to that same frequency. Therefore, a sum of phasors cannot represent the sum of sine waves of different frequencies as a single phasor.[^aac-phasor-conventions]

Choose one waveform as the phase reference, such as a source with an angle of 0°, and consistently measure all other phases relative to it. Likewise, use a consistent amplitude convention: RMS, peak, or peak-to-peak. It is possible to convert from one convention to another, but all quantities must be converted rather than just a subset. For a sine wave, `V_RMS = V_peak/sqrt(2)`, so mixing an RMS source with a peak component voltage introduces errors in ratios and verification checks.[^aac-phasor-conventions]

For example, if a resistor and a capacitor are connected in series to a 1 V RMS source, assign an angle of 0° to the source and find both voltages as RMS phasors. Their vector sum must reproduce the source phasor according to Kirchhoff's voltage law; adding only magnitudes generally will not work because the voltages have different phases.[^aac-phasor-conventions]

**Common mistakes:**
- Adding phasors of different frequencies without separate frequency-domain analysis.
- Mixing RMS and peak values in a single equation.
- Changing the phase reference mid-solution or adding magnitudes instead of complex quantities.

After completing calculations, verify the amplitude units, the frequency of each phasor, and the complex sum of voltages around the loop.[^aac-phasor-conventions]

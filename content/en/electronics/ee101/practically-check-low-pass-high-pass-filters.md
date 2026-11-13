---
id: emb-elee-0123
title: "How do you practically check RL low-pass and high-pass filters on a breadboard?"
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
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: kuphaldt-low-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.2 Low-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.02:_Low-pass_Filters
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
---

## Short answer

For each circuit, apply a small sine wave at `0.1*f_c`, `f_c`, and `10*f_c`, record frequency, `V_in`, `V_out`, and phase shift, and compare them with calculations. In a low-pass filter the output rolls off with frequency, while in a high-pass filter it rises; cutoff is the frequency where output equals approximately 70.7% of the passband level (around `-3.01 dB`).[^kuphaldt-low-pass-filters][^fiore-ac-circuit-analysis]

## Detailed explanation

**What we check.** A first-order filter has three characteristic operating points. For an RL filter with `R = 470 Ω` and `L = 10 mH`, the calculated cutoff is `f_c = R/(2*pi*L) = 470/(2*pi*0.01) ≈ 7.48 kHz`, so we test at `≈ 748 Hz`, `≈ 7.48 kHz`, and `≈ 74.8 kHz`. For an RL low-pass filter (output across the resistor), we expect `|V_out/V_in|` ≈ 0.995, 0.707, and 0.0995 (`-0.04 dB`, `-3.01 dB`, `-20.04 dB`) and phase shifts of `-5.7°`, `-45°`, and `-84.3°`. For an RL high-pass filter (output across the inductor), the amplitudes appear in reverse order: 0.0995, 0.707, and 0.995, while the phase shift is `+84.3°`, `+45°`, and `+5.7°`. Cutoff is defined as the frequency where the output is 3 dB below the passband level (a factor of 0.707).[^fiore-ac-circuit-analysis][^kuphaldt-low-pass-filters]

**Measurement procedure.** The generator supplies a sine wave to the filter input. Channel 1 of the oscilloscope is connected to the filter input, Channel 2 to the output, and the ground clips are tied together. Both circuits naturally share a common ground with the output: in the high-pass filter the inductor goes to ground, and in the low-pass filter the resistor goes to ground. The amplitude of `V_in` must be checked at every test frequency because the filter loads the generator and the input voltage may sag. The frequency is then fine-tuned until `V_out` reaches 0.707 of the passband level (the low-frequency reading for an LPF, or the high-frequency reading for an HPF); at this frequency, the phase shift should be around 45°, which provides a second, independent indication of the cutoff.

**Why the result differs from calculation.** The calculation yields a nominal value, whereas the measurement reflects reality. Inductor tolerance shifts `f_c`, winding resistance adds to `R`, and the generator output resistance and load resistance also alter the response.[^kuphaldt-low-pass-filters] The measurement signal path also has its own bandwidth: at its bandwidth limit, the oscilloscope and probe already attenuate the signal by 3 dB, and the probe further loads the circuit with its tip capacitance.[^tektronix-abcs-probes] Therefore, at the highest test frequency, make sure it remains far from instrument limits. Back-calculation helps find the real inductance: if the measured cutoff is `7.0 kHz`, then `L = R/(2*pi*f_c) = 470/(2*pi*7000) ≈ 10.7 mH`.

**Common mistakes:**

- Assuming the cutoff is where the output drops by half (`-6 dB`): cutoff is at `-3 dB`, meaning 0.707, not 0.5.
- Measuring `V_in` on the generator once and assuming it stays constant: filter loading varies with frequency.
- Comparing amplitudes against unity when the actual passband gain is less than 1: cutoff must be measured relative to the measured passband level.
- Using only a single frequency for testing: at least three points are required to distinguish LPF from HPF and to verify the slope.

---
id: emb-elee-0246
title: "How does jitter differ from an oscillator's frequency error?"
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
  - source_id: abracon-quartz-glossary
    title: "Abracon: Quartz Crystal Oscillators Glossary of Terms"
    url: https://abracon.com/Support/qtzcryoscil_glossary.pdf
  - source_id: ti-snaa285
    title: "TI SNAA285: Time-Domain Jitter Measurement Considerations for Low-Noise Oscillators"
    url: https://www.ti.com/lit/an/snaa285/snaa285.pdf
---

## Short answer

Frequency error is the static deviation from nominal frequency at room temperature, specified in ppm (such as ±50 ppm).[^abracon-quartz-glossary] Jitter represents short-term variations in the timing of individual clock periods relative to their ideal positions, changing cycle to cycle.[^ti-snaa285]

## Detailed explanation

Frequency error and jitter describe different properties. Frequency error is the offset of the average frequency from nominal. Manufacturers specify it in ppm, meaning parts per million of the nominal value, and Abracon's definition applies to the deviation at room temperature (25 ± 5 °C).[^abracon-quartz-glossary] Example: for an 8 MHz oscillator with a tolerance of ±50 ppm, `8*10^6 * 50*10^-6 = 400 Hz`, so the average frequency lies between 7,999,600 Hz and 8,000,400 Hz.

The same offset can be expressed in terms of period. The period of a nominal 8 MHz oscillator is 125 ns. At +50 ppm, the period becomes approximately 124.99375 ns, which is about 6.25 ps shorter in every cycle. This is a systematic quantity: it is identical for every period, so the difference between adjacent periods equals zero.

Jitter describes something else. According to TI, period jitter is the deviation of cycle duration from the ideal period, while cycle-to-cycle jitter is the variation in duration between adjacent cycles.[^ti-snaa285] A constant shift of 6.25 ps does not change the difference between adjacent periods, so the resulting cycle-to-cycle jitter is zero. Example from the source: the largest positive change of +62 ps and the largest negative change of –65 ps yield a cycle-to-cycle jitter of 65 ps, because the larger of the absolute values is taken.[^ti-snaa285]

Jitter is measured over a sufficient sample size: TI recommends 1,000 to 10,000 cycles for the result to be reliable.[^ti-snaa285] Frequency error, on the other hand, is checked against the average frequency, rather than the dispersion of individual edges.

**Common mistakes:**

- Confusing a constant frequency offset with jitter: the offset is identical on every period, whereas jitter varies from cycle to cycle;
- Evaluating jitter over only a few cycles; TI recommends 1,000 to 10,000;[^ti-snaa285]
- Assuming that ±50 ppm at 25 °C guarantees the same error over the entire temperature range; stability over temperature is specified by Abracon separately.[^abracon-quartz-glossary]

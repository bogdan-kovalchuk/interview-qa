---
id: emb-elintro-0270
title: "Why does an oscilloscope's sampling rate matter?"
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
  - source_id: tek-oscilloscope-specs
    title: "Tektronix: Evaluating Oscilloscope Bandwidth, Sample Rate, and Key Specifications"
    url: https://www.tek.com/en/documents/primer/evaluating-oscilloscopes
---

## Short answer

Sampling rate is the number of waveform samples an oscilloscope captures per second; it determines the time resolution of the digitized signal.[^tek-oscilloscope-specs] An insufficient sampling rate leads to aliasing or missed narrow glitches, and the Nyquist criterion of "at least twice the highest frequency" is insufficient in practice for faithfully reconstructing non-sinusoidal edges and arbitrary transients.[^tek-oscilloscope-specs]

## Detailed explanation

An oscilloscope's sampling rate is the number of digitized signal samples captured per second, typically specified in S/s, MS/s, or GS/s. Between samples, the instrument acquires no direct signal information; therefore, all else being equal, a higher sampling rate provides greater time resolution and reduces the risk of missing brief transient events.[^tek-oscilloscope-specs]

For an ideal, band-limited continuous signal, the Nyquist theorem requires a sampling rate greater than twice the highest frequency component to prevent aliasing. However, a practical digital oscilloscope operates with finite record length, and a narrow glitch is not an ongoing periodic waveform: sample points can simply fall outside its brief duration. Consequently, faithfully reconstructing waveform geometry in practice demands a substantial sampling margin that depends on the signal type, interpolation algorithm, and measurement objective.[^tek-oscilloscope-specs]

Example: a signal period of 1 µs corresponds to a frequency of 1 MHz. At 2 MS/s, an average of only two sample points are captured per cycle – far too few to reliably discern waveshape, transition edges, or a brief glitch. At 100 MS/s, the sampling interval is 10 ns, providing approximately 100 sample points per period. Even then, an edge transition faster than this sample interval cannot be fully resolved, and the achievable timing accuracy also depends on analog bandwidth and memory record length.[^tek-oscilloscope-specs]

**Common mistakes:**

- Applying the "two samples per period" rule as a guarantee of accurate arbitrary waveform reconstruction.
- Confusing sampling rate with bandwidth: a high sample rate cannot compensate for an inadequate analog front-end.
- Ignoring record length: with a fixed memory depth, increasing the sample rate shortens the total time window captured in a single acquisition.[^tek-oscilloscope-specs]

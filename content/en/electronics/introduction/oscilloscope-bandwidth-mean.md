---
id: emb-elintro-0269
title: "What does oscilloscope bandwidth mean?"
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

Bandwidth specifies the frequency at which the measured amplitude of an input sine wave is attenuated to 70.7% of its true amplitude, which corresponds to the -3 dB cutoff point.[^tek-oscilloscope-specs] Insufficient bandwidth attenuates high-frequency harmonics and slows displayed edge transitions; the required bandwidth margin depends on signal edge speeds and target measurement accuracy.[^tek-oscilloscope-specs]

## Detailed explanation

Oscilloscope bandwidth is a characteristic of its analog front-end that describes how effectively it passes signals of varying frequencies. It is conventionally defined as the input sine wave frequency at which the measured amplitude drops to 70.7% of its low-frequency value. This corresponds to the -3 dB cutoff point rather than a brick-wall limit where the oscilloscope ceases to display signals altogether.[^tek-oscilloscope-specs]

As the frequency of a signal component approaches the instrument's bandwidth, its displayed amplitude is attenuated. In a complex waveform such as a square wave, edges are composed of numerous high-frequency harmonics, so limited bandwidth attenuates these components: edges appear slower and rounded, and the overall shape and peak amplitude can be distorted. For fast digital transitions, it is also essential to evaluate the rise time of the instrument and probe; comparing bandwidth solely against the square wave's fundamental repetition frequency is insufficient.[^tek-oscilloscope-specs]

Example: if a measured sine wave matches the oscilloscope's nominal bandwidth frequency, the measured amplitude will already be roughly 29.3% lower than the true input amplitude, per the -3 dB definition. If amplitude must be measured within a few percent accuracy, an instrument with significantly higher bandwidth must be selected, or its frequency-response accuracy specification verified; the common rule of thumb of "five times bandwidth" is a practical guideline, not a universal guarantee.[^tek-oscilloscope-specs]

**Common mistakes:**

- Treating bandwidth and sampling rate as interchangeable: the former characterizes the analog front-end, whereas the latter dictates sample timing resolution.
- Assuming amplitude measurements remain fully accurate right up to the rated cutoff frequency without attenuation error.
- Evaluating a square wave solely by its fundamental frequency while ignoring the speed of its edge transitions.

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

TODO

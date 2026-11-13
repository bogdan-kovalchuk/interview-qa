---
id: emb-elee-0075
title: "How do you measure the phase shift between two sine waves on an oscilloscope?"
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

Measure the time difference `Δt` between corresponding phase points and the period `T`; the magnitude of the phase shift is `φ = 360°*Δt/T`. The signal that reaches the corresponding point earlier leads, and the sign depends on which signal is chosen as the reference.[^aac-alternating-current]

## Detailed explanation

The phase shift between two sine waves of the same frequency is measured on an oscilloscope as the time difference between corresponding points on the waveforms. Connect the signals to two channels, adjust the display, and measure the interval `Δt` between zero crossings in the same direction or between peaks. Do not compare the peak of one signal to the trough of the other: this produces a half-period error.[^aac-alternating-current]

Find the period `T` of one wave and calculate the fraction of the period: `|φ| = 360°*Δt/T`. The sign must be interpreted relative to the reference channel: if the corresponding point of the second signal occurs later, it lags; if earlier, it leads. Specify the order of the signals, because swapping channels changes the sign, though not the magnitude of the shift.[^aac-alternating-current]

Example: for a frequency of 1 kHz, the period is `1 ms`. If the second signal passes the corresponding zero `0.25 ms` after the first, the magnitude of the shift is `360°*0.25/1 = 90°`. The frequencies must be identical or sufficiently close; otherwise, the phase shift will vary over time. Noise, a low sample count per period, and an unstable trigger increase error, so use averaging or automated phase measurements if available.[^aac-alternating-current]

**Common mistakes:**
- Taking different phases of the waveforms as corresponding points.
- Forgetting that the formula applies to periodic signals of the same frequency.
- Calling a signal leading without specifying the reference channel.

The time shift defines the phase modulo full cycles: for example, a difference of `1.25T` has the same phase angle as `0.25T` when considering phase modulo 360°. For signals containing harmonics, an automated measurement algorithm might track an individual harmonic rather than the fundamental frequency; check the waveform shape and the selected measurement mode.[^aac-alternating-current]

---
id: emb-elintro-0083
title: "Which formula relates `V_rms` and `V_pp` for a sine wave?"
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
  - source_id: aac-ac-magnitude
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude/
---
## Short answer

For a pure sine wave, `V_rms = V_pp/(2*sqrt(2))`, or approximately `0.3536*V_pp`; conversely, `V_pp = 2*sqrt(2)*V_rms` (approximately `2.828*V_rms`). This relationship is not general for an arbitrary waveform.[^aac-ac-magnitude]

## Detailed explanation

RMS (root mean square) is the effective value of alternating voltage: the same direct current voltage would dissipate the same average power in a resistor. For a pure sine wave with zero mean, the peak value `V_peak` is a factor of `sqrt(2)` greater than RMS, and the span from negative to positive peak equals `V_pp = 2*V_peak`. Combining these two definitions yields `V_rms = V_pp/(2*sqrt(2))`.[^aac-ac-magnitude]

The factor depends on the waveshape, not merely on the "AC" label. For a square, clipped, or distorted signal, you must calculate RMS from the waveshape or use a True-RMS instrument within its frequency range and crest factor limits. A conventional meter calibrated for a sine wave can display an erroneous RMS reading for a different waveform.[^aac-ac-magnitude]

Example: for a sine wave with `V_pp = 10 V`, the peak amplitude equals `5 V`, and RMS is approximately `5/sqrt(2) = 3.54 V`. Common mistake – applying this factor to a peak-to-peak signal without dividing by two, or using it for a square wave. Before converting, determine whether the given value is peak, peak-to-peak, or RMS.[^aac-ac-magnitude]

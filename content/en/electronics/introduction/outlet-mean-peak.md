---
id: emb-elintro-0079
title: "What does \"120 V at a US outlet\" mean – is it `RMS` or peak?"
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
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude
---
## Short answer

120 V in the US mains is a nominal `RMS` value, not peak. For a pure sine wave, the peak is approximately `120*√2 = 170 V`, and peak-to-peak is approximately `340 V`. An AC multimeter reading depends on its design and the waveform; not every meter measures true RMS.[^aac-ac-magnitude]

## Detailed explanation

The designation `120 V` for the US household mains indicates the nominal effective (RMS) voltage. It does not describe the instantaneous voltage at every moment and is not a peak value; for a sine wave, peaks are greater than RMS by a factor of approximately `√2`.[^aac-ac-magnitude]

RMS relates an alternating signal to its average power on a resistive load. Therefore, nominal mains voltages are usually given as RMS. The instantaneous voltage of a sine wave varies between positive and negative peaks rather than staying at the `120 V` level.[^aac-ac-magnitude]

For an ideal sine wave, the amplitude equals `V_peak = V_rms*√2`. Thus, at `120 V RMS`, the peak is approximately `169.7 V`, which is about `±170 V`; the full span `V_pp = 2*V_peak` is approximately `339.4 V`. This is a calculation for a pure sine wave, not an assertion about the actual instantaneous value of every outlet under all conditions.[^aac-ac-magnitude]

A multimeter's `AC` mode does not guarantee true RMS: simple meters may be calibrated for a sine wave, and their accuracy degrades on distorted waveforms. Measuring a non-sinusoidal signal requires a meter with a true-RMS function and adequate bandwidth/crest factor. You should also check the voltage limits and safety category of the instrument before working with mains.[^aac-ac-magnitude]

**Common mistake:** interpreting `120 V` as peak or automatically expecting any AC meter to display true RMS. Distinguish nominal RMS from peak, and verify measurement capabilities against the documentation of the specific instrument.[^aac-ac-magnitude]

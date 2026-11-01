---
id: emb-elintro-0088
title: "Why does a mains value of `230 V RMS` not mean the maximum is only 230 V?"
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
  - source_id: aac-rms
    title: "All About Circuits: Introduction to RMS Measurements"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/analog-measurements/introduction-to-rms-measurements/
---

## Short answer

`RMS` is the effective value, not the peak voltage. For a pure sine wave, `230 V RMS` corresponds to approximately `325 V` zero-to-peak and `650 V` peak-to-peak, which is why insulation and components are selected taking peak values and transient overvoltages into account.[^aac-rms]

## Detailed explanation

The root-mean-square (RMS) value of an alternating voltage is defined by its heating effect: it is the direct-current voltage that dissipates the same average power in a resistive load. Therefore, RMS is neither the average value of the instantaneous sine wave over a full cycle nor its maximum. For a pure sine wave, the peak value is `√2` times greater than RMS.[^aac-rms]

This relationship depends on waveform shape. For instance, for pulsed or clipped voltages, the `√2` factor is generally inapplicable; a true-RMS measurement or waveform analysis is required. The common household mains designation of `230 V` typically indicates the nominal RMS value of a sinusoidal voltage, not a guarantee that the instantaneous voltage will never exceed 230 V.[^aac-rms]

**Worked example:** for an ideal sine wave with `230 V RMS`, the peak voltage is `230*√2 ≈ 325 V`. The swing from negative peak to positive peak equals twice the peak, or approximately `650 V` peak-to-peak. Real mains systems have tolerances and transient surges, so these figures do not replace standard requirements or datasheet insulation margins.[^aac-rms]

**Common mistake:** selecting a capacitor or transistor rated only slightly above the RMS value. In an unloaded rectifier, the capacitor can charge close to the peak, and brief overvoltages require an additional safety margin that must be factored into the design.[^aac-rms]

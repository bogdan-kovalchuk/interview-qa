---
id: emb-elee-0111
title: "What happens to a square wave after an RC high-pass filter with a small time constant?"
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
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor Transient Response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
---

## Short answer

If `τ = R*C` is small compared to the half-period, the RC high-pass filter output forms short pulses near the edges: positive after a rising edge and negative after a falling edge. Between edges, the exponential transient decays almost to zero; the circuit does not rectify the signal.[^aac-high-pass-filters] [^aac-capacitor-transient]

## Detailed explanation

An RC high-pass filter responds to input changes rather than maintaining the input's DC level at the output. At an edge of a square wave, the capacitor voltage cannot change instantaneously, so initially a significant fraction of the step appears across the resistor. Subsequently, the capacitor charges through the circuit resistance, and the output exponentially approaches zero. On a falling edge, the pulse sign reverses. For the basic circuit, the time constant is `τ = R*C`, and the cutoff frequency is `f_c = 1/(2π*R*C)`.[^aac-high-pass-filters] [^aac-capacitor-transient]

The expression "small time constant" is meaningful only relative to the duration of the signal levels. If the period is `T` and the square wave has a 50 percent duty cycle, each level lasts `T/2`. When `τ` is much smaller than `T/2`, the preceding transient almost completely decays before the next edge. If, however, `τ` is comparable to the level duration, the transients overlap and the output does not return close to zero before the next transition.[^aac-capacitor-transient]

Example: let `τ = 1 ms`, and the signal level lasts `5 ms`. After one `τ`, the exponential component decays to approximately 37 percent of its initial value, and after five `τ`, less than one percent remains. Therefore, such a choice produces a short spike and an output near zero before the next edge. The amplitude of the initial spike depends on the step magnitude, the initial charge on the capacitor, and the voltage divider formed by the source and load.[^aac-capacitor-transient]

**Common mistake:** calling these spikes a rectified square wave or assuming that a high-pass filter always produces identical narrow pulses. The polarity corresponds to the edge direction, and the waveform between edges depends on `τ`, period, duty cycle, and loading. For an accurate prediction, one must account for the entire resistance seen by the capacitor, not merely the marking of a single resistor.[^aac-high-pass-filters] [^aac-capacitor-transient]

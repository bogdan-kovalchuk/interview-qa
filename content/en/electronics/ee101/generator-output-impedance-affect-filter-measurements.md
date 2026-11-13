---
id: emb-elee-0105
title: "Why does the generator's output impedance affect RC filter measurements?"
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
  - source_id: keysight-generator-load-termination
    title: "Keysight: Output Load Termination"
    url: https://helpfiles.keysight.com/Standalone_BenchVueSoftware_PW_HelpFiles/PWFGApp/Content/Configure%20Waveforms/Waveform%20Configuration/Output%20Load%20Termination.htm
---

## Short answer

The generator's output impedance forms a voltage divider with the filter's input impedance; on many generators it is 50 Ω, though this must be verified for the specific instrument.[^keysight-generator-load-termination] Therefore, measure the reference input signal directly at the filter input node rather than relying on the amplitude displayed on the generator panel.

## Detailed explanation

The generator's output impedance is a series resistance in the source's equivalent circuit, so together with the connected circuit's impedance, it determines the actual voltage at the filter input. In many generators this impedance is 50 Ω, but the value and amplitude display mode depend on the model and the specified load.[^keysight-generator-load-termination]

For a simple RC low-pass filter, if the source has a resistance `R_s` and the filter resistor is `R`, the capacitor sees a total series resistance of `R_s + R`. Therefore, the actual pole frequency is determined by this sum when the output is taken across the capacitor and the source can be described by a Thévenin model. The input level may also sag, especially if the filter resistance is comparable to the generator's output impedance.

For example, setting the generator amplitude for a 50 Ω load does not guarantee that same amplitude at a high-impedance input: for many instruments, the voltage without a 50 Ω load will be approximately twice the displayed value. This rule pertains to the instrument's calibration specifically for such a load; the High-Z setting may change the display readout rather than the physical output circuit.[^keysight-generator-load-termination]

**Common mistakes:**
- Substituting only the filter resistor into the formula without accounting for the source output impedance.
- Assuming the amplitude on the display is the guaranteed voltage at the measured node.

When measuring the frequency response, monitor `V_in` directly at the filter input and determine the generator's output impedance from its documentation. This allows you to separate the filter's intrinsic response from the source loading and prevent a shift in the estimated cutoff frequency.

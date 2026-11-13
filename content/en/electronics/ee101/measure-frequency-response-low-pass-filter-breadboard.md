---
id: emb-elee-0104
title: "How do you measure the frequency response of an RC low-pass filter on a breadboard?"
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
  - source_id: aac-low-pass
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
  - source_id: tek-scope-frequency-response
    title: "Tektronix: Measuring Impedance and Capacitance with an Oscilloscope and Function Generator"
    url: https://download.tek.com/document/48W-29165-0%20Using%20an%20oscillocope%20and%20function%20generator%20to%20measure%20capacitor%204-24-2013%20DP.pdf
  - source_id: tek-generator-load
    title: "Tektronix: Function generator amplitude and load impedance FAQ"
    url: https://www.tek.com/en/support/faqs/if-i-set-my-amplitude-my-afg3000-series-generator-actual-amplitude-measured-my-scope-or
---

## Short answer

Apply a sine wave with zero DC offset, probing CH1 at the filter input and CH2 at the output. At each frequency, measure the actual `V_in` and `V_out`, calculate `A = V_out/V_in` and `G_dB = 20*log10(A)`, and verify the generator's load termination setting.[^tek-scope-frequency-response] [^tek-generator-load]

## Detailed explanation

Measuring the frequency response shows how signal transmission changes with frequency. For an RC low-pass filter, assemble the circuit with short connections on a breadboard and a common ground. Apply a sinusoidal signal with zero DC offset, unless the circuit requires separate biasing, and connect oscilloscope channel 1 to the input and channel 2 to the output. This pair of measurements provides the actual voltages at both nodes, rather than just the nominal generator setting.[^tek-scope-frequency-response]

Begin at a frequency well below the expected cutoff, then measure near it and above it. At each step, wait for a stable sine wave and record the frequency and amplitudes of both channels in the same format, such as RMS or peak-to-peak. The amplitude ratio is calculated as `A = V_out/V_in`, and the relative level as `G_dB = 20*log10(A)`. If the input amplitude varies with frequency, this normalized ratio helps evaluate the filter itself.[^tek-scope-frequency-response]

Procedure example: for each frequency, record `f`, `V_in`, `V_out`, `A`, and `G_dB`, and then plot a table or graph of `G_dB` against the logarithm of frequency. For an ideal first-order RC low-pass filter, the point where the level is approximately 3 dB below the low-frequency level is close to the cutoff frequency. In practice, component values, output loading, and the input impedance of the measuring instrument can alter the curve.[^aac-low-pass]

Before interpretation, check how the generator defines amplitude. For example, some Tektronix AFG generators display a value calculated for a 50 Ω load; with a high-impedance oscilloscope input, the measured value can be almost twice as large. The exact behavior depends on the model, so verify the load mode in the menu or manual of the instrument, and rely on the CH1 measurement as the actual filter input.[^tek-generator-load]

**Common mistake:** Plotting the response using the generator's nominal amplitude setting and the output measurement without verifying the actual input. The discrepancy between 50 Ω and High Z modes then mistakenly appears as filter gain or attenuation. Measure both nodes simultaneously, use the same amplitude metric, and ensure that the probe ground clips are connected to the circuit ground.[^tek-scope-frequency-response] [^tek-generator-load]

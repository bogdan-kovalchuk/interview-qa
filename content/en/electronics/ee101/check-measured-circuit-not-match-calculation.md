---
id: emb-elee-0077
title: "What should you check if a measured RC circuit does not match the calculation?"
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

First verify the actual wiring, component values and tolerances, source settings, and measurement technique before altering the theoretical model. In an RC circuit, the result depends on actual values of `R` and `C`, frequency, loading, and parasitic parameters.[^aac-alternating-current]

## Detailed explanation

When measurements of an RC circuit do not match calculations, check the system from simple to complex. First, de-energize the circuit, compare the physical wiring against the schematic, and check the orientation of polarized components, ground points, and breadboard contacts. An open circuit, a misconnected node, or a shared ground connected in the wrong place often accounts for a discrepancy much better than complex theory.[^aac-alternating-current]

Next, check exactly what was substituted into the formulas: measured rather than merely nominal values of `R` and `C`, actual frequency, source amplitude, and DC offset. Resistor and capacitor tolerances alter the time constant `τ = R*C` and the filter cutoff frequency. Electrolytic capacitors can have wide tolerances, and their capacitance can vary with operating conditions and frequency.[^aac-alternating-current]

Inspect the test instruments. Ensure the oscilloscope probe has the correct attenuation setting in the menu, and that its ground lead does not create a short circuit between nodes. The probe's input resistance and capacitance load the node under test, especially at high impedance levels or high frequencies. Check the function generator under load: its output impedance can alter the voltage if the circuit load does not match the generator's expected termination.[^aac-alternating-current]

Example: if a calculation is made for `R = 10 kΩ` and `C = 100 nF`, then `τ = 1 ms`; an actual capacitance of `80 nF` yields `0.8 ms` even before accounting for resistor tolerance. Such a difference does not necessarily imply an error in the formula. Measure the components individually, verify the unloaded signal, and check node voltages one by one.[^aac-alternating-current]

**Common mistake:** immediately tweaking nominal values to fit the result without checking units, probe configuration, frequency, and actual component parameters. Record the measurement conditions; this makes it possible to distinguish wiring errors from normal effects of tolerances and loading.[^aac-alternating-current]

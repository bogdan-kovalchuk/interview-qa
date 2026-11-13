---
id: emb-elee-0081
title: "Why may a coil model with only jωL not match measurements, and what does a multimeter show on a coil?"
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
  - source_id: aac-inductor-quirks
    title: "All About Circuits: Inductor Quirks"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/inductor-quirks/
  - source_id: keysight-4263b-lcr
    title: "Keysight 4263B LCR Meter User's Guide"
    url: https://www.keysight.com/cd/en/assets/9018-40465/user-manuals/9018-40465.pdf
---

## Short answer

A real inductor has winding resistance and frequency-dependent core losses, and at sufficiently high frequencies parasitic capacitance also matters, making a pure `j*ω*L` model limited. A multimeter in Ω mode measures winding DC resistance, not inductance. Measuring L requires an LCR meter or another instrument that measures impedance at a specified frequency.[^aac-inductor-quirks] [^keysight-4263b-lcr]

## Detailed explanation

The model `Z_L = j*ω*L` describes an ideal inductor: its impedance consists solely of a reactive component proportional to frequency. A real component is wound from wire that has resistance, and a magnetic core can introduce additional losses. Therefore, at the operating frequency, the model is often expanded to `Z_L ≈ r_L + j*ω*L`, where `r_L` lumps the series winding resistance and other losses acceptable for a simplified model.[^aac-inductor-quirks]

An inductor also has inter-turn parasitic capacitance. Together with the inductance, this creates resonant behavior; near the self-resonant frequency, the simple series model no longer predicts the measured impedance. Parameter values may depend on frequency, core material, signal level, and connection method. Consequently, before comparing calculations with measurements, one must know the test frequency, instrument model, and the conditions under which the manufacturer specifies the inductance.[^aac-inductor-quirks]

A standard digital multimeter in resistance mode supplies a small DC test current and evaluates the DC resistance between the probes. On an inductor, this is primarily the resistance of its wire, along with the contact resistance of the probes and leads; the meter cannot determine L because it does not measure the response to an alternating signal at a specified frequency. An LCR meter, by contrast, measures AC voltage and current and displays the selected parameter, such as L along with Q or DCR. The Keysight user guide for model 4263B lists separate Lp-Q and Lp-Rdc modes for an inductor, demonstrating the distinction between these measurements.[^keysight-4263b-lcr]

Example: if a multimeter reads 18 Ω, this does not mean the inductance is 18 H or that the inductor will exhibit that exact impedance at the operating frequency. The reading is its DC resistance within the instrument's accuracy specifications. To verify L, one must record the test frequency and LCR meter configuration, because measured inductance without these conditions may not be comparable to the datasheet value.[^keysight-4263b-lcr]

**Common mistake:** interpreting an Ω reading as an inductance measurement or assuming `j*ω*L` is an accurate model across the entire frequency range. First, select the appropriate instrument mode: Ω for DC resistance, and an LCR meter or impedance analyzer for AC parameters. Next, verify the test frequency and test conditions against the component documentation; if the measurement differs, check winding resistance, parasitic elements, contact quality, and frequency rather than arbitrarily changing the model.[^aac-inductor-quirks] [^keysight-4263b-lcr]

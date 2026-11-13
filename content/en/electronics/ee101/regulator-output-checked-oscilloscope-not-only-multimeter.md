---
id: emb-elee-0166
title: "Why should a regulator's output be checked with an oscilloscope and not only with a multimeter?"
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
  - source_id: keysight-34401a-tutorial
    title: "Agilent (Keysight) 34401A: Digital Multimeter Tutorials"
    url: https://www.ee.torontomu.ca/guides/instrument-manuals/Agilent-HP_34401A_Tutorial.pdf
  - source_id: tek-dmm7510-ripple-an
    title: "Tektronix (Keithley): Measuring Low Level Ripple Voltage Using the DMM7510 7-1/2-Digit Graphical Sampling Multimeter"
    url: https://www.tek.com/en/documents/application-note/measuring-low-level-ripple-voltage-using-dmm7510-7-1-2-digit-graphical-s-0
  - source_id: teledyne-probe-ground-lead
    title: "Teledyne LeCroy: Passive Probe Ground Lead Effects"
    url: https://www.teledynelecroy.com/doc/passive-probe-ground-lead-effects
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
---

## Short answer

In DC mode, a multimeter displays a time-averaged reading, meaning symmetrical ripple or high-frequency oscillations may go entirely unnoticed.[^keysight-34401a-tutorial] An oscilloscope captures the actual time-domain waveform, revealing ripple amplitude and frequency, ringing, and dropouts; detecting such anomalies requires an oscilloscope.[^tek-dmm7510-ripple-an]

## Detailed explanation

A digital multimeter with an integrating ADC measures the average value of an input by integrating it over a fixed time period, typically chosen as a multiple of the power-line period so that mains noise averages out to nearly zero.[^keysight-34401a-tutorial] Therefore, in DC mode, rapid voltage variations that are symmetrical about the mean disappear from the display: a regulator exhibiting 100–120 Hz ripple or high-frequency oscillations in the hundreds of kilohertz may display virtually the same reading as a clean one. For power supply measurements, this is a well-known limitation: traditional DMMs generally do not capture dynamic behavior, and an oscilloscope is typically required to detect ripple, switching voltage, and turn-on glitches.[^tek-dmm7510-ripple-an]

**Example (illustrative numbers).** A 5 V output oscillates in a triangular waveform between 4.5 and 5.5 V (1 V peak-to-peak). The mean is `(4.5 + 5.5)/2 = 5.0 V`, and the multimeter in DC mode will read approximately 5.0 V. The load, however, experiences dips down to 4.5 V, which falls outside a ±5% tolerance (`5*0.05 = 0.25 V`, i.e., 4.75–5.25 V). An oscilloscope reveals both extremes and the frequency, allowing the root cause to be investigated.

The causes of such oscillations are real. The LM340/LM7805 datasheet requires an input capacitor of at least 0.1 µF "for stability" if the regulator is located more than approximately six inches from the power-supply filter; an output capacitor is not required for stability, but improves transient response.[^ti-lm340] For LDOs, manufacturers typically specify an allowable range of CSR (the output capacitor's ESR plus any series resistor), outside of which the regulator becomes unstable.[^ti-slva079] A poorly chosen capacitor or long leads can therefore trigger oscillations that a multimeter will fail to reveal.

An oscilloscope also has limitations. For very small ripple voltages, its resolution may be insufficient, and in DC coupling on the most sensitive scale it is restricted by the maximum DC offset; in AC coupling, ripple is seen more clearly, though still not ideally.[^tek-dmm7510-ripple-an] A long ground lead with an alligator clip (around 200 nH, following the rule of 20 nH per inch) combined with the probe capacitance forms a resonant circuit that rings on fast edges, which is easily mistaken for regulator ripple.[^teledyne-probe-ground-lead] Therefore, one should use a short ground spring or blade (10–20 nH) and connect directly across the regulator pins and its bypass capacitor.

**Common mistakes:**

- Assuming a steady DMM reading indicates a clean power rail: the average voltage may appear correct despite dangerous extremes.
- Measuring with a long alligator ground lead on the probe and mistaking its inductive ringing for ripple or oscillation.
- Searching for small ripple in DC coupling on a coarse vertical scale: AC coupling and a more sensitive scale should be used instead.

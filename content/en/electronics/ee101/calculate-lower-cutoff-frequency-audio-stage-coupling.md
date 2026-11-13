---
id: emb-elee-0230
title: "How do you calculate the lower cutoff frequency of an audio stage's coupling capacitor?"
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
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
---

## Short answer

For a single RC network with a coupling capacitor, the cutoff frequency where the signal drops by 3 dB is `f_c = 1/(2*pi*R*C)`, where R is the equivalent resistance seen by the capacitor.[^fiore-ac-circuit-analysis] With R = 10 kΩ, a 1 µF capacitor gives ≈ 15.9 Hz and 100 nF gives ≈ 159 Hz; reducing C tenfold raises the cutoff frequency tenfold.

## Detailed explanation

A coupling capacitor between two stages passes the AC signal component and blocks DC, so the bias of one stage does not alter the operating point of the other. When its reactance `X_C` is small compared to surrounding resistors (at frequencies several times higher than `f_c`), it acts as an AC short circuit for the signal.[^fiore-common-emitter-amplifier] Together with the resistance in the loop, it forms a high-pass filter: the lower the frequency, the larger the reactance `X_C = 1 / (2 * pi * f * C)` and the more the signal is attenuated.[^fiore-ac-circuit-analysis]

The value R in the formula is the resistance seen by the capacitor looking out from its terminals with voltage sources shorted. In a typical circuit, the source resistance (the output impedance of the preceding stage) is in series with the capacitor, while the input impedance of the following stage together with the base bias resistors appears between the node after the capacitor and ground. Their sum gives R, so the nominal value of a single resistor on the schematic does not necessarily equal R.

**Example:** with R = 10 kΩ, the cutoff `1 / (2 * pi * 10000 * 1e-6)` gives ≈ 15.9 Hz for C = 1 µF, and for C = 100 nF, ≈ 159 Hz. For a 159 Hz cutoff, attenuation at 100 Hz is `10 * log10(1 + (159 / 100)^2) ≈ 5.5 dB`, whereas at 1 kHz it is only ≈ 0.11 dB. A 100 nF capacitor already noticeably cuts low audio frequencies, whereas 1 µF barely affects them.

The formula describes a single first-order RC network. If the circuit contains multiple RC networks (for example, an emitter bypass capacitor also forms its own cutoff), each contributes its own frequency, and the overall frequency response is determined for the entire circuit. The point `f_c` is not a brick-wall boundary below which the signal disappears, but the point where attenuation is 3 dB; below it, attenuation increases at approximately 20 dB per decade.[^fiore-ac-circuit-analysis]

**Common mistakes:**

- Taking R as the marked resistor value on the schematic while ignoring source resistance and the input impedance of the subsequent stage.
- Considering `f_c` a boundary below which the signal disappears: at `f_c`, attenuation is only 3 dB.
- Calculating only one RC network when another is operating in the circuit, such as an emitter bypass capacitor.

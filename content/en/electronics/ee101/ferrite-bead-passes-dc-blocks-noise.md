---
id: emb-elee-0262
title: "Why does a ferrite bead in a supply line pass DC but suppress noise?"
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
  - source_id: wuerth-ferrite-bead-behavior
    title: "Würth Elektronik Application Note ANP008: The Real Behavior of Ferrite Beads"
    url: https://www.we-online.com/catalog/media/o109033v410%20AppNotes_ANP008_TheRealBehaviorOfFerriteBeads_EN.pdf
  - source_id: analog-devices-ferrite-beads
    title: "Analog Devices Tutorial MT-101: Decoupling Techniques"
    url: https://www.analog.com/media/en/training-seminars/tutorials/MT-101.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

A ferrite bead acts as an inductor whose inductive reactance `X_L = 2*pi*f*L` increases with frequency. For direct current (DC), the reactance is near zero, but for high-frequency noise in the kilohertz and megahertz range, the impedance is substantial and dissipative. It is therefore placed in series with the power rail, often at the input and output of a voltage regulator.[^udemy-electronics-course]

## Detailed explanation

A ferrite bead is not merely an inductive component, but a frequency-dependent dissipative filter whose complex impedance substantially changes its nature depending on signal frequency[^udemy-electronics-course][^wuerth-ferrite-bead-behavior].

### Complex impedance of ferrite

The electrical impedance of a ferrite bead in the frequency domain is described by the complex expression:
`Z = R(f) + j * X(f)`, with magnitude `|Z| = sqrt(R(f)^2 + X(f)^2)`.

Here, the component `X(f) = 2 * pi * f * L` is the inductive reactance determined by the real part of the ferrite material's magnetic permeability `mu'`. The component `R(f)` is the active loss resistance caused by the imaginary part of the magnetic permeability `mu''` (magnetic hysteresis and eddy-current losses in the core material)[^wuerth-ferrite-bead-behavior][^analog-devices-ferrite-beads].

### Behavior across frequency ranges

1. **Direct current (DC) and low frequencies:**
   The reactive component `X(f)` approaches zero. The impedance of the bead is determined entirely by the ohmic resistance of its internal copper conductor (DCR – Direct Current Resistance). Typically, DCR ranges from 0.01 to 0.2 Ω[^wuerth-ferrite-bead-behavior]. With such low resistance, DC load current flows through the bead with negligible voltage drop (`Delta V = I_DC * DCR`), without heating the component or disturbing circuit power.

2. **Low and medium frequencies (from hundreds of kilohertz to several megahertz):**
   The reactive component dominates over resistance (`X(f) >> R(f)`). The bead operates as a typical inductor (usually from hundreds of nanohenries to several microhenries). Interference in this band is reflected back toward the source due to high inductive reactance[^analog-devices-ferrite-beads].

3. **High frequencies (from 10–30 MHz to 1 GHz and above):**
   Magnetic relaxation occurs in the ferrite ceramic: real permeability `mu'` rolls off sharply while imaginary permeability `mu''` rises to a peak. Consequently, reactance decreases and active loss resistance becomes dominant (`R(f) >> X(f)`)[^wuerth-ferrite-bead-behavior]. At these frequencies, the ferrite bead behaves as a frequency-dependent resistor (specified impedance is typically rated at 100 MHz, such as 600 Ω or 1000 Ω). The critical advantage is that high-frequency noise energy is not merely reflected (which could induce unwanted resonance on the power rail), but is **absorbed and converted into heat** within the ferrite material[^wuerth-ferrite-bead-behavior][^art-of-electronics].

### DC bias saturation effect

A critical engineering limitation of ferrite beads is core saturation caused by DC bias current[^wuerth-ferrite-bead-behavior]. As operating load current flows, magnetic domains align with the field, causing differential magnetic permeability to drop steeply. As a result, rated impedance at 100 MHz can degrade by 50–80% from its catalog specification. Therefore, the rated current of a ferrite bead is always selected with a safety margin of at least 2–3 times above maximum load current[^wuerth-ferrite-bead-behavior][^analog-devices-ferrite-beads].

### Applications in power rails

Ferrite beads are placed in series with supply rails preceding sensitive nodes (PLLs, ADCs, clock oscillators) or at the outputs of switching regulators (buck converters). In combination with shunt ceramic capacitors, the bead forms a second-order low-pass LC or Pi filter that effectively suppresses high-frequency switching noise and harmonics without the risk of high-Q parasitic resonance[^analog-devices-ferrite-beads][^art-of-electronics].

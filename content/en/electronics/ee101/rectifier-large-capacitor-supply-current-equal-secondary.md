---
id: emb-elee-0175
title: "Can a rectifier with a large capacitor supply a DC current equal to the secondary's rated RMS current?"
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
  - source_id: hammond-rectifier-guide
    title: "Hammond Manufacturing: Design Guide for Rectifier Use"
    url: https://www.hammfg.com/pdf/5c007.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

No. A capacitor filter forces the diodes to conduct only in short charging current pulses near the peaks, so the secondary RMS current is higher than the average DC load current.[^fiore-rectification] For a bridge rectifier with a capacitor input filter, transformer manufacturer guidelines suggest approximately `I_DC ≈ 0.62*I_RMS` of the secondary.[^hammond-rectifier-guide]

## Detailed explanation

**What the rating means.** The rated current of a transformer secondary is an RMS value: it determines resistive heating in the winding, and the VA rating equals the rated secondary voltage multiplied by the maximum secondary RMS current; in Fiore's example, this is 24 V RMS × 0.3 A = 7.2 VA.[^fiore-rectification] The DC load current, by contrast, is an average value. For a bridge rectifier feeding a purely resistive load, the two values are close: according to the Hammond design guide, `I_DC = 0.90*I_RMS`.[^hammond-rectifier-guide]

**Why adding a capacitor changes the relationship.** A rectifier diode conducts only when the transformer AC voltage exceeds the capacitor voltage by approximately 0.7 V (or two diode drops in a bridge), and larger filter capacitance narrows this conduction interval while forcing peak currents higher.[^fiore-rectification] In Fiore's half-wave rectifier simulation with 100 Ω and 1000 µF, the charging current reaches approximately 800 mA even though the load draws less than 0.1 A.[^fiore-rectification] The charge that the capacitor supplies to the load throughout an entire cycle must be replenished by the transformer winding during this brief fraction of a cycle. In a simplified model of rectangular pulses occupying a duty fraction `d` of the ripple period, `I_RMS = I_DC/sqrt(d)`: for `d = 0.4` this gives 1.6*I_DC, while for `d = 0.1` it reaches 3.2*I_DC.

**Example.** Consider a 12 V / 1 A RMS (12 VA) transformer with a bridge rectifier and a large filter capacitor. Applying the Hammond guideline, allowable DC load current is approximately `0.62*1 A = 0.62 A`, not 1 A. Conversely, to obtain 1 A of continuous DC current, one needs a secondary winding rated for approximately `1/0.62 ≈ 1.6 A` RMS, corresponding to ≈ 19 VA at 12 V.[^hammond-rectifier-guide] This is a rule of thumb rather than an absolute law. In a numerical simulation of the circuit from qid:emb-elee-0179 (9 V RMS sinusoidal source, 1000 µF, constant 0.1 A load, 0.7 V per diode), secondary winding current depends heavily on total loop series resistance: with 0.5 Ω, the RMS current is ≈ 0.26 A (≈ 2.6*I_DC) with a peak of ≈ 0.86 A; with 2 Ω, the RMS current is ≈ 0.21 A (≈ 2.1*I_DC).

**Limits and side effects.** The de-rating factor depends on rectifier topology: according to Hammond, for a half-wave rectifier with a capacitor input filter, `I_DC = 0.28*I_RMS`, making thermal utilization significantly worse.[^hammond-rectifier-guide] Pulsed charging currents stress more than just the transformer windings: Hammond recommends diodes rated for at least twice the DC output current (providing margin for turn-on surge), while the capacitor's RMS ripple current can reach 2–3 times I_DC.[^hammond-rectifier-guide] Peak diode currents are analyzed in greater detail in qid:emb-elee-0139.

**Common mistakes:**

- Directly equating DC load current to the secondary's rated RMS current on a 1:1 basis.
- Calculating required transformer VA simply as `V*I_DC`, neglecting current waveform peaking.
- Increasing filter capacitance to reduce ripple without verifying peak currents in the diodes and transformer winding.
- Sizing rectifier diodes solely based on average current rather than peak repetitive and surge ratings.

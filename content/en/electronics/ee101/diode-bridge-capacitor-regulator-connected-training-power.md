---
id: emb-elee-0178
title: "How are the diode bridge, capacitor, and regulator connected in a training power supply?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: vishay-gbu4
    title: "Vishay: GBU4A-GBU4M glass passivated single-phase bridge rectifier (datasheet)"
    url: https://www.vishay.com/docs/88614/gbu4a.pdf
  - source_id: vishay-alu-intro
    title: "Vishay BCcomponents: Aluminum Electrolytic Capacitors – Introduction, Basic Concepts, and Definitions"
    url: https://www.vishay.com/docs/28356/alucapsintrobcc.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
---

## Short answer

The two bridge `~` AC terminals connect to the secondary winding, while `+` and `-` output rectified DC; verify terminal pinouts from the package markings.[^vishay-gbu4] The electrolytic capacitor's positive terminal connects to bridge `+` and its negative terminal connects to `-` (common return). The voltage regulator input connects to the capacitor's positive node, and regulator GND connects to `-`.[^vishay-alu-intro][^ti-lm340]

## Detailed explanation

**Circuit sequence.** The secondary winding feeds the `~` AC terminals of the bridge rectifier, while the `+` and `-` terminals output pulsating DC voltage. In each half-cycle, two diodes conduct, so the load sees the secondary voltage minus two diode voltage drops.[^fiore-rectification] The bulk filter capacitor is placed in parallel between `+` and `-`: it supplies the load between AC peaks, and its discharge creates the ripple voltage (for ripple estimation, see qid:emb-elee-0130).[^fiore-rectification] The regulator input connects to this same positive capacitor node, so the regulator sees the filtered capacitor voltage rather than the raw bridge pulses. The regulator GND pin, the `-` terminal of the bridge, the negative capacitor terminal, and the load return are tied together into a single common ground rail.

**Numerical example.** A 9 V RMS secondary winding produces a peak voltage of `9*sqrt(2) ≈ 12.7 V`; with two diodes dropping ≈ 0.7 V each, the peak on the capacitor is `12.7 - 1.4 ≈ 11.3 V`. For the uA7805, the recommended input operating range is 7–25 V, so 11.3 V leaves a margin of `11.3 - 7 = 4.3 V` above the lower operating limit: this margin accommodates ripple valleys and mains dips before the input violates the recommended range.[^ti-ua78] The capacitor voltage rating is chosen with margin above the peak voltage: in Fiore's example, the peak is 34 V, and a 50 V capacitor is chosen.[^fiore-rectification] For a 12.7 V peak, a 25 V rating provides good margin.

**Polarity and pinout markings.** An electrolytic capacitor is polarized: Vishay indicates the negative terminal with a stripe, band, or `-` marking, and specifies U_REV as the maximum allowable reverse voltage across the terminals.[^vishay-alu-intro] Therefore, the capacitor's negative lead connects to the bridge `-` terminal, and the positive lead connects to `+`. In datasheets for GBU4 series bridge rectifiers, the `~`, `+`, and `-` terminals are identified on the outline drawing, with polarity indicated by markings on the case.[^vishay-gbu4] Terminal pinouts must always be verified against the physical case or datasheet rather than memory (for why bridge connections must not be swapped at random, see qid:emb-elee-0181).

**Regulator connections.** In the TO-220 package of the LM7805 regulator, pin 1 is input, pin 2 is ground, and pin 3 is output.[^ti-lm340] An input bypass capacitor directly at the IC pins is necessary only when the regulator is located far from the main power-supply filter capacitor, so long conductors between the two should be avoided.[^ti-lm340] For further details on wiring the 7805, see qid:emb-elee-0163.

**Common mistakes:**

- Connecting the bridge `~` AC terminals to the capacitor or load rather than to the transformer secondary winding.
- Installing an electrolytic capacitor with reversed polarity.
- Failing to connect the bridge `-` terminal, regulator GND, and load return into a single common ground bus.
- Determining bridge or regulator pinouts from memory instead of verifying the datasheet.

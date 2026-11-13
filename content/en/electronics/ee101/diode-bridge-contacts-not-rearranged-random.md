---
id: emb-elee-0181
title: "Why must the diode bridge terminals not be rearranged at random?"
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
  - source_id: libretexts-fiore-rectification
    title: "Fiore: Semiconductor Devices, 3.2 Rectification (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
---

## Short answer

The two AC terminals of a bridge rectifier are interchangeable because output DC polarity does not depend on which AC pin is positive.[^libretexts-fiore-rectification] Only the `+` and `-` DC terminals have fixed polarity, so connecting the secondary winding directly across them causes two bridge diodes to short-circuit the winding on alternate half-cycles. If both secondary leads are wired to the same terminal node, the winding is shorted directly.

## Detailed explanation

A four-diode bridge rectifier has two AC input terminals and two DC output terminals, `+` and `-`. In each half-cycle two diodes conduct, and current through the load flows in a single direction, so the output polarity is positive regardless of which AC input pin is positive.[^libretexts-fiore-rectification] Consequently, the two AC terminals can be interchanged without consequence, whereas the `+` and `-` terminals cannot, because the correct operational polarity of the filter capacitor and voltage regulator depends on them.

Consider a secondary winding connected directly across the `+` and `-` terminals (with the bridge AC pins left unconnected). During the half-cycle when the `+` terminal is more positive, the capacitor charges directly from the winding without any diode voltage drops. During the opposite half-cycle, the two series bridge diodes connected from `-` to `+` become forward-biased, placing an effective short circuit across the winding and clamping the capacitor voltage to approximately -1.4 V. Current is limited primarily by winding resistance. The danger is severe overheating of the bridge diodes, transformer, and fuse.

A polarized capacitor is not designed to withstand reverse voltage: an electrolytic capacitor installed backward can fail catastrophically.[^fiore-capacitors] In this scenario, a reverse voltage of approximately -1.4 V appears across it, subjecting the capacitor to conditions outside its design ratings.

**Example:** a 12 V RMS secondary winding produces a peak voltage of approximately 17 V. During the opposite half-cycle, the winding attempts to produce those same 17 V while the forward-biased diodes clamp the capacitor node to -1.4 V, resulting in approximately `17 - 1.4 ≈ 15.6 V` dropped across the winding's internal resistance. Assuming a winding resistance of 0.5 Ω (an illustrative assumption rather than data for a specific transformer), the current is approximately `15.6 / 0.5 ≈ 31 A`, and at 1 Ω it is approximately 16 A. This estimate considers resistance alone without winding leakage inductance; in either case, these current levels represent a dead short circuit rather than an operating condition.

**Common mistakes:**

- Assuming that AC and `+`/`-` terminals can be swapped interchangeably: the AC terminals are interchangeable, but the DC terminals are not.
- Wiring the secondary winding directly across `+` and `-` in an attempt to simplify assembly.
- Installing a polarized electrolytic capacitor across the bridge output without verifying terminal polarity.

---
id: emb-elee-0128
title: "How does a half-wave rectifier differ from a bridge rectifier?"
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
---

## Short answer

In a half-wave rectifier, a single diode conducts only during one half-cycle, and ripple frequency equals the input frequency f. In a bridge rectifier, two diodes conduct in series during each half-cycle (alternating pairs), load current maintains a single direction, and ripple frequency is 2f.[^libretexts-fiore-rectification] The penalty for the bridge is two `V_F` drops instead of one.

## Detailed explanation

In a half-wave rectifier, a single diode is forward-biased during the positive half-cycle and passes current to the load, while during the negative half-cycle it is reverse-biased: current is zero, and the entire input voltage drops across the diode itself.[^libretexts-fiore-rectification] The output is a pulsating voltage of a single polarity that repeats once per input period, so the ripple frequency equals `f`. The pause between pulses lasts half a period: about 8.3 ms for 60 Hz.[^libretexts-fiore-rectification]

A bridge rectifier uses four diodes. During the positive half-cycle D2 and D3 conduct, and during the negative half-cycle D1 and D4 conduct, so in each half-cycle current passes through two diodes in series, while flowing through the load always in the same direction.[^libretexts-fiore-rectification] Both halves of the input are used, and during one input period two pulses appear at the output, meaning the ripple frequency equals `2*f`. By comparison, in a center-tapped secondary circuit only one diode conducts at a time, but the load sees only half of the secondary voltage.[^libretexts-fiore-rectification]

**Why this matters for filtering.** The capacitor supplies current to the load during the pauses between pulses, and the voltage sag over each pause is estimated as `ΔV ≈ I/(f_ripple*C)` (an upper bound because charge time is neglected). For `I = 100 mA` and `C = 1000 µF` on a 50 Hz line, in a half-wave rectifier `f_ripple = 50 Hz`, giving `ΔV ≈ 0.1/(50*0.001) = 2 V`; in a bridge rectifier `f_ripple = 100 Hz` and `ΔV ≈ 1 V`. Thus, for the same ripple, the bridge requires roughly half the capacitance; the textbook also notes that full-wave rectification noticeably reduces the required capacitor size.[^libretexts-fiore-rectification]

**The penalty and caveats of the bridge.** In a bridge there are always two diodes in the conduction path, so the load sees the secondary voltage minus two forward drops, whereas in a half-wave rectifier it sees secondary voltage minus one drop.[^libretexts-fiore-rectification] At a current of 1 A and `V_F ≈ 0.7 V`, power dissipated in the diodes is `0.7 W` versus `1.4 W` in the bridge. The statement "the diode conducts for half a period" holds for a resistive load; with a filter capacitor, the diodes turn on only near the peak in a short pulse, and the larger the capacitance, the shorter and higher the charging current pulse.[^libretexts-fiore-rectification]

**Common mistakes:**

- Believing that all four diodes in a bridge conduct simultaneously, rather than alternating opposite pairs.
- Forgetting about the two `V_F` drops in a bridge, especially at low secondary voltages (see qid:emb-elee-0129).
- Confusing ripple frequency (`f` or `2*f`) with line frequency at the bridge input.

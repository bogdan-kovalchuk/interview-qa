---
id: emb-elintro-0065
title: "What happens when two 9V batteries are connected in parallel with reversed polarity?"
track: electronics
section: introduction
sources:
  - source_id: openstax-emf
    title: "OpenStax University Physics Volume 2, 10.1 Electromotive Force"
    url: https://openstax.org/books/university-physics-volume-2/pages/10-1-electromotive-force
  - source_id: openstax-kirchhoff
    title: "OpenStax University Physics Volume 2, 10.3 Kirchhoff's Rules"
    url: https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules
  - source_id: ti-slva139
    title: "Texas Instruments SLVA139: Reverse Current/Battery Protection Circuits"
    url: https://www.ti.com/lit/an/slva139/slva139.pdf
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

If two identical 9 V batteries are connected in parallel with opposing polarity, their EMFs add around the closed loop (about `18 V` in total), so the current is very high and limited only by internal resistances and contacts.[^openstax-kirchhoff] [^openstax-emf] Without data for the specific batteries, one cannot cite a current of `9 A` or claim the outcome is always the same: heating, leakage, or damage depends on chemistry, internal resistance, and connection duration.

## Detailed explanation

A parallel connection means connecting terminals of like polarity: positive to positive and negative to negative. If one battery is reversed, the positive terminal of one connects to the negative terminal of the other; this is not a normal, proper parallel connection of sources, but a closed loop in which their voltages aid each other and add up, as in a series connection.

The current in such a loop is determined by the sum of the internal resistances of both batteries, contact resistance, and lead resistance. Therefore, a calculation based on invented, identical internal resistances does not yield a universal number: the short-term current can be substantial, causing rapid heating, damaging cells, or causing leakage. The actual outcome depends on battery chemistry and construction.[^openstax-emf]

**Common mistake:** calculating current using only the nominal `9 V` and an arbitrarily chosen resistance. Label voltage does not determine battery internal resistance, which varies with type, state of charge, temperature, and degradation. An answer should describe the hazardous short-circuit current and how its magnitude depends on specific cells, rather than providing an unverified exact number.

Reverse polarity protection can be mechanical – specialized connectors, such as the distinct terminals of a 9 V battery – or electronic: a series diode or MOSFET blocks reverse current, though a diode introduces its own voltage drop.[^ti-slva139] Therefore, batteries should never be intentionally connected with reverse polarity for testing.

**How to avoid the problem:**

- Before connecting, verify the `+` and `−` markings on both batteries and the circuit.
- Use a polarized connector or other mechanical keying against improper installation.[^ti-slva139]
- For a parallel battery pack, follow manufacturer requirements regarding cell type, voltage, and compatibility.

If an incorrect connection has already been made, do not touch an overheated or damaged battery with bare hands and do not continue the experiment; safe handling is defined by the specific battery manufacturer's instructions.

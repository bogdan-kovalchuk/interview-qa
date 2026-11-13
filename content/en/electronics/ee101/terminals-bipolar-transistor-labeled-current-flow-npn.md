---
id: emb-elee-0187
title: "How are the terminals of a bipolar transistor labeled, and how does current flow in an NPN?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
---

## Short answer

The terminals are base `B`, collector `C`, and emitter `E`. In an `NPN` transistor operating in active mode, conventional current flows into the collector and base and exits through the emitter; in a `PNP` transistor, polarities and current directions are reversed. The emitter schematic arrow points outward for `NPN` and toward the base for `PNP`.[^fiore-bjt-basics]

## Detailed explanation

The three terminals of a bipolar junction transistor are named after the semiconductor layers they contact. The emitter (E) injects charge carriers into the base; the base (B) is a thin, lightly doped middle layer; and the collector (C) is the largest layer, which collects most of the carriers. In an NPN, the layers follow an N–P–N sequence: the emitter and collector are N-type regions, and the base is a P-type region. In a PNP, the sequence is P–N–P, so supply polarities and current directions are reversed. The emitter and collector are not interchangeable: the emitter is heavily doped, whereas the collector is the largest and more lightly doped region (with a thin, lightly doped base).[^fiore-bjt-basics] A transistor connected in reverse typically still functions, but with a drastically reduced `β`, so datasheet specifications are no longer met.

In an NPN with a forward-biased B–E junction, electrons from the emitter enter the base. Because the base is thin and lightly doped, only a tiny percentage of electrons recombine with base holes; over 95% reach the collector and flow toward the positive collector supply. Conventional current flows in the opposite direction: it enters the collector and base and exits through the emitter. Kirchhoff's current law for the node yields `I_E = I_C + I_B`, and because `I_B` is small, `I_E ≈ I_C`. For example: with `I_B = 0.02 mA` and `I_C = 2 mA`, we get `I_E = 2.02 mA`.[^fiore-bjt-basics]

The schematic arrow on the symbol indicates the direction of conventional current through the emitter: in an NPN it points outward, and in a PNP it points toward the base. From the symbol, both transistor type and emitter current direction are immediately apparent: in an NPN current exits, while in a PNP it enters.[^fiore-bjt-basics]

**Common mistakes:**
- Confusing conventional current with electron flow: electrons travel in the opposite direction, meaning that in an NPN electrons enter the emitter from its supply circuit.[^fiore-bjt-basics]
- Assuming the emitter and collector are interchangeable simply because both are N-type regions: they are physically asymmetric.[^fiore-bjt-basics]

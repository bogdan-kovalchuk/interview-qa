---
id: emb-elee-0192
title: "What is the \"two-diode\" transistor model useful for, and where is its limit?"
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
  - source_id: fiore-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model
---

## Short answer

The two-diode model is useful for checking the B–E and B–C junctions with a multimeter in diode test mode.[^fiore-bjt-basics] However, two discrete diodes cannot replace a transistor because they cannot reproduce transistor action or controlled collector current.[^fiore-ebers-moll] Pinout configurations for B, C, and E must always be verified against the device datasheet.

## Detailed explanation

Each transistor junction can be modeled as a diode, yielding expected readings on an ohmmeter or multimeter in diode-test mode. For an NPN: placing the positive probe on the base and the negative probe on either the emitter or collector shows low resistance; reversing polarity shows high resistance. Between emitter and collector, resistance is high in both polarities because one of the two junctions is always reverse-biased.[^fiore-bjt-basics] For an NPN this provides a fast check: conduction must occur from the base to both other terminals, with neither a short circuit nor an open circuit present.

The limitation of the model becomes obvious in active mode. With a forward-biased B–E junction and a reverse-biased B–C junction, two discrete diodes would show only tiny leakage current in the second loop. In reality, both loops carry virtually the same substantial current because the base is thin and lightly doped. The two-diode model splits the base into two separate, isolated blocks, and that is precisely where it fails.[^fiore-bjt-basics]

For bias calculations, the simplified Ebers–Moll model is used: an ideal B–E diode and a current-controlled current source between collector and base. It predicts `I_C = β * I_B` in forward-active mode, though `β` depends on the device, current, `V_CE`, and temperature, requiring exact figures to be taken from datasheets or measured.[^fiore-ebers-moll]

The diode test proves that the base forms a p-n junction with each of the other two terminals,[^fiore-bjt-basics] but does not identify which is E and which is C. Terminal pinout must therefore be taken from the specific device datasheet. The diode test is suitable for locating the base and verifying junction health, but not for evaluating current gain.

**Common mistakes:**

- Assuming two discrete diodes explain amplification or active mode operation.
- Distinguishing between emitter and collector using a diode test: it only confirms junctions relative to the base.
- Treating "normal" diode-test readings as confirmation of adequate `β`.

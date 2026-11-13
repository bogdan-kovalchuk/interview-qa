---
id: emb-elee-0147
title: "How is a diode OR gate built and what is its peculiarity?"
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
  - source_id: nexperia-diode-handbook
    title: "Nexperia: Diode Application Handbook (Design Engineer’s Guide), 2022"
    url: https://assets.nexperia.com/documents/brochure/Nexperia_document_book_DiodeApplicationHandbook_2022.pdf
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
---

## Short answer

Diode anodes connect to the inputs, cathodes connect to the output, and the output is pulled down to ground through a resistor. Any high input pulls the output high, but the high logic output is degraded by approximately `V_F` below the input voltage.[^nexperia-diode-handbook][^utah-cs6710-diode-logic]

## Detailed explanation

In a diode OR gate, each input connects to the anode of its respective diode, and all cathodes converge at the output node, which is held near ground by a resistor. When a voltage noticeably higher than `V_F` appears at any input, its diode turns on, current flows through the resistor, and a positive voltage develops at the output; for multiple inputs, one simply adds more diodes.[^nexperia-diode-handbook] This yields the OR function: the output is high if at least one input is high.[^utah-cs6710-diode-logic]

The key peculiarity stems from the fact that a conducting diode is not an ideal conductor: a forward drop `V_F` remains across it (0.7 V in a simple model for silicon).[^libretexts-fiore-diode-models] Therefore, the high output level equals approximately `V_in,HIGH - V_F`, which is lower than the input level by `V_F`, and an input that does not exceed `V_F` will not turn the diode on at all. The diodes also isolate the inputs: if one signal is high, current does not back-feed into low inputs.[^nexperia-diode-handbook]

**Example.** Input A = 5 V, input B = 0 V, `10 kΩ` resistor to ground. For `V_F = 0.7 V`, output ≈ `5 - 0.7 = 4.3 V`, drawing a current of `4.3/10000 = 0.43 mA` from the input A source. Diode B is reverse-biased: its anode is 0 V and cathode is 4.3 V. If both inputs are 0 V, the diodes do not conduct, and the resistor holds the output near 0 V (without load). For a Schottky diode with `V_F ≈ 0.3 V`, the output would be `4.7 V` and current `0.47 mA`.

Thus, a diode OR gate loses part of the logic level, and the subsequent stage must tolerate this degradation. Nexperia describes such circuits as a very low-cost solution for simple, slow logic functions.[^nexperia-diode-handbook]

**Common mistakes:**

- Expecting the full input level at the output: in reality, it is lower by `V_F`.
- Applying an input voltage that does not exceed `V_F` and expecting a high output.
- Connecting diodes in reverse (anodes to output), yielding an AND gate instead of an OR gate.

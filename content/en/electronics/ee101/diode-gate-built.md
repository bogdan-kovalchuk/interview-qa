---
id: emb-elee-0146
title: "How is a diode AND gate built?"
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

The output is pulled up to the supply with a resistor, diode anodes connect to the output node, and cathodes connect to the inputs. Any low input turns its diode on, holding the output at approximately `V_in,LOW + V_F`; a high output appears only when all inputs are high.[^nexperia-diode-handbook][^utah-cs6710-diode-logic]

## Detailed explanation

The circuit consists of a resistor between the power supply and the output node, and diodes whose anodes connect to this node while their cathodes connect to the inputs. As long as at least one input is low, its diode is forward-biased: current flows from the supply through the resistor and diode into the low-signal source, leaving the output at only `V_F` above the level of that input.[^nexperia-diode-handbook][^utah-cs6710-diode-logic] If all inputs are high (at the supply level or higher), the diodes are off, and the resistor pulls the output up to the supply; when `V_in,HIGH < V_CC`, the diodes remain forward-biased, see below. This implements the AND function.[^nexperia-diode-handbook]

In that case, any other diodes remain reverse-biased: their cathodes are at a higher voltage than the output, so a high input does not source current into a low input. This is how the diodes isolate the inputs from each other. Under a simple diode model, the same mechanism operates when the high input level is below the supply voltage: the diodes remain forward-biased, and the high output equals approximately `V_in,HIGH + V_F`, capped by the supply voltage.

**Example.** `V_CC = 5 V`, `10 kΩ` pull-up, `V_F ≈ 0.7 V` (approximation for silicon).[^libretexts-fiore-diode-models] Input A = 0 V, input B = 5 V: diode A is on, output ≈ `0 + 0.7 = 0.7 V`, current `(5 - 0.7)/10000 = 0.43 mA`, which the input A driver must sink. Diode B is off because its cathode (5 V) is higher than its anode (0.7 V). Both inputs 5 V: no current flows, and the output pulls up to 5 V (without load).

This circuit is used as a very low-cost solution for simple, slow logic functions.[^nexperia-diode-handbook] However, the low output level does not equal zero, and when cascaded, the `V_F` drops accumulate, making it difficult to connect such gates in long chains (see qid:emb-elee-0149).[^utah-cs6710-diode-logic]

**Common mistakes:**

- Assuming that logic low at the output equals 0 V: it is higher than the low input by `V_F`.
- Confusing polarity: in an AND gate, diode anodes meet at the output (pull-up to supply); in an OR gate, cathodes meet at the output (pull-down to ground).
- Forgetting that pull-up current flows into the low-signal source, and the input driver must be capable of sinking it.

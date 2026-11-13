---
id: emb-elee-0148
title: "Diode AND: `V_CC` = 5 V, 10 kΩ pull-up, input 0 V, `V_F` ≈ 0.3 V (Schottky). What are the output level and current?"
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
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
  - source_id: nexperia-diode-handbook
    title: "Nexperia: Diode Application Handbook (Design Engineer’s Guide), 2022"
    url: https://assets.nexperia.com/documents/brochure/Nexperia_document_book_DiodeApplicationHandbook_2022.pdf
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
  - source_id: vishay-bat54
    title: "Vishay: BAT54, BAT54A, BAT54C, BAT54S small signal Schottky diodes (datasheet)"
    url: https://www.vishay.com/docs/86410/bat54_bat54a_bat54c_bat54s.pdf
  - source_id: ti-hc00
    title: "TI: SN74HC00, SN54HC00 quadruple 2-input NAND gates (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

Output is approximately `V_in + V_F = 0 + 0.3 = 0.3 V`, and current is `I = (5 - 0.3)/10000 ≈ 0.47 mA` without an external load. This current flows from the supply through the pull-up resistor and diode into the input, so the driving device asserting logic low must sink it.[^nexperia-diode-handbook][^utah-cs6710-diode-logic]

## Detailed explanation

When the input of a diode AND gate is grounded, the diode between the output and input conducts, and the output node settles at the input level plus the diode forward drop: `V_out = V_in + V_F`.[^nexperia-diode-handbook][^utah-cs6710-diode-logic] For `V_in = 0 V` and `V_F ≈ 0.3 V`, this yields `0.3 V`. The pull-up resistor drops the remainder of the supply voltage, so the current is determined by Ohm's law: `I = (V_CC - V_out)/R = (5 - 0.3)/10000 = 0.47 mA`. The power dissipated in the resistor is `P = 0.47 mA * 4.7 V ≈ 2.2 mW`.

The value `V_F ≈ 0.3 V` for a Schottky diode is plausible, but it depends on current and diode type. For example, for the BAT54, maximum `V_F` is 0.24 V at 0.1 mA and 0.32 V at 1 mA, so at 0.47 mA it does not exceed 0.32 V.[^vishay-bat54] For a silicon diode in a simple model, the drop is 0.7 V:[^libretexts-fiore-diode-models] the output would then be `0.7 V` and the current `(5 - 0.7)/10000 = 0.43 mA`. The difference in current is small, but the output voltage differs by more than a factor of two, which is where Schottky diodes excel.

There are three additional caveats. First, `0 V` at the input is an idealization: if the input driver holds zero with its own `V_OL`, the output equals `V_OL + V_F` rather than simply `V_F`. Second, the `0.47 mA` current flows into the input driver, which must sink it. Third, it is critical whether the resulting voltage is a valid logic low for the subsequent stage. For the SN74HC00 at `V_CC = 4.5 V`, the maximum low-level input voltage `V_IL(max)` is `1.35 V`, so `0.3 V` and even `0.7 V` pass, but this table does not cover 5 V and does not apply to other logic families.[^ti-hc00]

**Common mistakes:**

- Assuming the output is zero: it is higher than the low input by `V_F`.
- Forgetting that the pull-up current flows into the input rather than "nowhere".
- Substituting 0.7 V for a Schottky diode and 0.3 V for a silicon diode.
- Overlooking the load at the output: it alters both current and voltage level.

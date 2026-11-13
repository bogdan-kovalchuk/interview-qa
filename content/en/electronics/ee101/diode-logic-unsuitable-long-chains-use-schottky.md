---
id: emb-elee-0149
title: "Why is diode logic unsuitable for long chains, and why does it use Schottky diodes?"
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
  - source_id: vishay-bat54
    title: "Vishay: BAT54, BAT54A, BAT54C, BAT54S small signal Schottky diodes (datasheet)"
    url: https://www.vishay.com/docs/86410/bat54_bat54a_bat54c_bat54s.pdf
  - source_id: ti-hc00
    title: "TI: SN74HC00, SN54HC00 quadruple 2-input NAND gates (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

Diode logic is passive: it provides neither signal amplification nor level restoration, causing `V_F` voltage drops to accumulate with each cascaded stage.[^utah-cs6710-diode-logic] Schottky diodes feature lower `V_F`, which slows logic-level degradation, but cascading degradation still occurs and lower `V_F` trades off against higher reverse leakage.[^nexperia-diode-handbook] Compatibility must always be verified against input logic thresholds of following stages.[^ti-hc00]

## Detailed explanation

In a diode AND gate, the low-level output equals the low input plus `V_F`. If this output is fed into the input of a subsequent identical gate, that gate adds another `V_F`, and so forth: after `n` stages, logic low rises to approximately `n*V_F` (assuming constant `V_F` and zero initial input). The handout provides an example: five cascaded AND gates at 0.7 V each yield 3.5 V at the output, which is far from any recognizable logic low.[^utah-cs6710-diode-logic] In a diode OR gate, a `V_F` drop of the high logic level is lost at each stage in a similar manner (see qid:emb-elee-0147).

This cannot be corrected using diodes and resistors alone: the circuit lacks an active element to restore the signal to the supply rail or ground. According to the handout, raising the supply voltage merely shifts logic level ranges and increases power dissipation without removing the limit on the number of stages; an inverter cannot be built from diodes and resistors alone, and these limitations are resolved by transistors.[^utah-cs6710-diode-logic]

**Example (idealized).** Consider an SN74HC00 at `V_CC = 4.5 V` as the subsequent stage: `V_IL(max) = 1.35 V`.[^ti-hc00] For silicon diodes with `V_F = 0.7 V`, a chain of two AND gates already yields `2*0.7 = 1.4 V > 1.35 V`, meaning logic low is no longer guaranteed to be recognized. For Schottky diodes with `V_F = 0.3 V`, four stages yield `4*0.3 = 1.2 V < 1.35 V`, while the fifth gives `1.5 V > 1.35 V`. Thus, Schottky diodes extend the permissible chain length, but do not make it unlimited. This is a simplified estimate: actual `V_F` depends on current (for the BAT54, the maximum rises from 0.24 V at 0.1 mA to 0.8 V at 100 mA).[^vishay-bat54]

Schottky diodes are chosen for their lower forward voltage drop,[^nexperia-diode-handbook] which reduces the loss per stage and increases headroom to the logic threshold. However, lower `V_F` involves a trade-off with reverse leakage current, so parameters must be verified against the datasheet.[^nexperia-diode-handbook]

**Common mistakes:**

- Believing that Schottky diodes make diode logic suitable for arbitrarily long chains: they only increase permissible length.
- Assuming `V_F = 0.7 V` for all diodes without considering dependence on current and diode type.[^vishay-bat54]
- Checking only logic low in AND chains while ignoring high-level degradation in OR chains.

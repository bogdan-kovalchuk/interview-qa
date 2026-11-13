---
id: emb-elee-0239
title: "What are the truth tables of two-input AND, NAND, OR and NOR?"
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
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  - source_id: ti-hc08
    title: "TI SN74HC08 quadruple 2-input AND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc08.pdf
  - source_id: ti-hc32
    title: "TI SN74HC32 quadruple 2-input OR gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc32.pdf
  - source_id: ti-hc02
    title: "TI SN74HC02 quadruple 2-input NOR gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc02.pdf
  - source_id: ti-hc04
    title: "TI SN74HC04 hex inverters datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc04.pdf
---

## Short answer

AND outputs 1 only for input 11[^ti-hc08], while NAND outputs 0 only for 11.[^ti-hc00] OR outputs 0 only for 00[^ti-hc32], while NOR outputs 1 only for 00.[^ti-hc02] The governing Boolean equations are `Y = A*B` (AND)[^ti-hc08], `Y = NOT(A*B)` (NAND)[^ti-hc00], `Y = A+B` (OR)[^ti-hc32], `Y = NOT(A+B)` (NOR)[^ti-hc02], and `Y = NOT A` (NOT).[^ti-hc04]

## Detailed explanation

A truth table lists the output for every combination of inputs. For two inputs, there are `2^2 = 4` combinations (00, 01, 10, 11); for three inputs, `2^3 = 8`. A truth table unambiguously defines the logic function, but not the physical gate itself: TTL and CMOS NAND gates share the same truth table, so devices with identical truth tables are interchangeable logically, but not necessarily in terms of voltage levels, drive capability, and propagation speed.

For inputs 00, AND and OR output 0, while NAND and NOR output 1. For 01 and 10, AND and NOR output 0, while NAND and OR output 1. For 11, AND and OR output 1, while NAND and NOR output 0.[^ti-hc00][^ti-hc02][^ti-hc08][^ti-hc32]

NAND and NOR are the inversions of AND and OR in every row: `NAND = NOT(AND)`, `NOR = NOT(OR)`. From this follows De Morgan's law `NOT(A * B) = NOT A + NOT B`, meaning NAND is an OR gate with inverted inputs. Row-by-row verification: for 01, both expressions yield 1; for 11, both yield 0.

The truth table describes ideal logic levels. A physical input is recognized as 0 or 1 only within the limits of `V_IL` and `V_IH`, and the output must comply with `V_OL` and `V_OH`. For a floating input, the table does not apply, because standard CMOS inputs must never be left floating.[^ti-hc00]

**Common mistakes:**

- Confusing NAND with AND: NAND outputs 0 only for 11, which is the inverted result.
- Assuming that NOR outputs 1 for any input 1: it outputs 1 only for 00.
- Using 4 rows instead of 8 for three inputs.

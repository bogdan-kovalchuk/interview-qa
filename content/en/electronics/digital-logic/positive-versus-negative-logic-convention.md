---
id: emb-eldig-0001
title: "What is the difference between positive and negative logic conventions in digital circuits?"
track: electronics
section: digital-logic
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications (12th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003291
  - source_id: aac-logic-signal-voltage-levels
    title: "All About Circuits textbook, Volume IV: Digital, Chapter 3: Logic Signal Voltage Levels"
    url: https://www.allaboutcircuits.com/textbook/digital/chpt-3/logic-signal-voltage-levels/
---

## Short answer

In the positive logic convention, the higher voltage level (HIGH) represents logic 1 (TRUE) and the lower level (LOW) represents logic 0 (FALSE). In negative logic, this mapping is inverted: HIGH represents logic 0 and LOW represents logic 1. Digital processors generally use positive logic for internal data paths, while using negative logic for active-low control and handshake signals.[^floyd-digital-fundamentals]

## Detailed explanation

### Basic definitions of level representation conventions

In physical digital electronics, electrical signals are measured in voltages (such as 0 V and 5 V, or 0 V and 3.3 V), whereas Boolean algebra operates on abstract truth values (TRUE / 1) and false values (FALSE / 0). The connection between physical voltage and a Boolean variable is established by a logic level convention:[^floyd-digital-fundamentals]

1. Positive Logic:
   - The more positive voltage potential (HIGH level, `H`) corresponds to logic one (`1` or TRUE).
   - The less positive voltage potential (LOW level, `L`, typically ground potential) corresponds to logic zero (`0` or FALSE).
2. Negative Logic:
   - The more positive voltage potential (HIGH level, `H`) corresponds to logic zero (`0` or FALSE).
   - The less positive voltage potential (LOW level, `L`) corresponds to logic one (`1` or TRUE).

### Principle of duality and gate logic function transformation

A physical logic gate based on semiconductor transistors responds purely to input voltage potentials `H` and `L`, with no intrinsic notion of Boolean conventions.[^tocci-digital-systems] If the electrical state table of an IC is:
- Inputs (L, L) -> Output L
- Inputs (L, H) -> Output L
- Inputs (H, L) -> Output L
- Inputs (H, H) -> Output H

Then the interpretation of this IC depends on the selected convention:[^floyd-digital-fundamentals]
- Under positive logic (`H = 1`, `L = 0`): we obtain the truth table (0,0)->0, (0,1)->0, (1,0)->0, (1,1)->1. This is the conjunction function (AND gate).
- Under negative logic (`H = 0`, `L = 1`): we obtain the truth table (1,1)->1, (1,0)->1, (0,1)->1, (0,0)->0. This is the disjunction function (OR gate).

Thus, any physical AND gate under positive logic simultaneously acts as an OR gate under negative logic. Similarly:[^aac-logic-signal-voltage-levels]
- A positive NAND is a negative NOR;
- A positive NOR is a negative NAND;
- A positive OR is a negative AND;
- A logic inverter (NOT) remains an inverter under either convention.

This property is a direct physical manifestation of the duality principle in Boolean algebra and De Morgan's laws.

### Practical applications of negative logic in digital electronics

Although processor datapaths and data buses predominantly use positive logic, negative logic (active-low signals) dominates in system control lines:[^floyd-digital-fundamentals][^tocci-digital-systems]

1. Reset and interrupt lines (`/RESET`, `/IRQ`, `/NMI`): an active-low level ensures that during power loss, voltage brownouts, or severed cables, the line defaults to a safe low-potential state or can be reliably pulled down with a grounded pushbutton.
2. Chip select and memory strobes (`/CS`, `/OE`, `/WE`): RAM and ROM chips enable output buffers only when driven with a logic zero.
3. Open-collector / open-drain buses: in protocols such as I2C, 1-Wire, or wired-OR interrupt lines, a passive pull-up resistor holds the line at the HIGH level (idle state / no event). Any node can activate the bus by turning on a transistor and pulling the line to GND (LOW state). Here asserting zero represents an active event (logic 1 under negative logic or "wired-OR").
4. Noise immunity and TTL circuit characteristics: historically in TTL logic, the output sink current in the LOW state (`I_OL`) was 10–20 times greater than the source current in the HIGH state (`I_OH`), and low-level noise immunity was significantly better. Therefore, asserting devices with a low level provided maximum speed for discharging parasitic line capacitances.

To unambiguously designate inverted signals on schematics, an overbar (`/RESET`), a prefix `n` (`nRESET`), a suffix `#`, or an inversion bubble on the gate pin is used.[^floyd-digital-fundamentals]

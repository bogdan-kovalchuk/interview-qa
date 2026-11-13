---
id: emb-elee-0249
title: "What does a Pierce crystal oscillator consist of?"
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
  - source_id: ti-sn74lvc1gx04-oscillator
    title: "Texas Instruments: SN74LVC1GX04 datasheet (SCES581D), section 9 Application and Implementation"
    url: https://www.ti.com/lit/ds/symlink/sn74lvc1gx04.pdf
---

## Short answer

A Pierce crystal oscillator consists of an inverting amplifier (unbuffered in the TI reference design), a quartz crystal resonator, two load capacitors `C_1` and `C_2`, and a feedback resistor `R_F` that biases the inverter into its linear region.[^ti-sn74lvc1gx04-oscillator] In the TI design, a secondary buffered inverter shapes the output to provide full rail-to-rail logic swing.[^ti-sn74lvc1gx04-oscillator]

## Detailed explanation

A Pierce oscillator is a loop in which an inverter operates as an amplifier and a crystal determines the frequency. In TI's SN74LVC1GX04 example, there are two inverters: an unbuffered inverter serves as the oscillator amplifier. In TI's design, the output is shaped by a buffered inverter, providing a full rail-to-rail swing signal.[^ti-sn74lvc1gx04-oscillator] Resistor R_F, typically 1 MΩ to 10 MΩ, biases the unbuffered inverter into its linear operating region, where it amplifies rather than switches as a digital gate.[^ti-sn74lvc1gx04-oscillator]

The crystal resonator connects between the input and output of the inverter, while capacitors C1 and C2 each connect their respective node to ground. TI states that values for C1 and C2 are selected to compute load capacitance C_L, with a recommended C_L of 16 pF for the crystal in the example.[^ti-sn74lvc1gx04-oscillator] For equal C1 = C2 = C, this yields `C_L = C/2 + C_stray`, where `C_stray` is the stray capacitance of the PCB and pins. Example: with C1 = C2 = 26 pF and `C_stray = 3 pF` (an assumption for illustration), we have `C_L = 26*26/(26+26) + 3 = 13 + 3 = 16 pF`, matching TI's example.

A series resistor R_s limits the drive current through the crystal. TI notes that its value depends on the maximum drive level of the crystal, and that decreasing R_s increases closed-loop gain, provided the power remains within limits.[^ti-sn74lvc1gx04-oscillator] Verification begins by ensuring that the circuit cannot oscillate without the crystal; for this test, the crystal is replaced by an equivalent parallel resistance.[^ti-sn74lvc1gx04-oscillator]

The gain of the unbuffered inverter decreases as supply voltage drops, which reduces closed-loop gain. Therefore, TI advises verifying that the circuit oscillates at the desired frequency at both minimum and maximum supply voltage.[^ti-sn74lvc1gx04-oscillator]

**Common mistakes:**

- Choosing R_F and R_s arbitrarily: R_F biases the inverter into the linear region, and R_s limits crystal current;[^ti-sn74lvc1gx04-oscillator]
- Assuming that C_L equals C1 or C2: with equal C1 and C2, the load equals C/2 plus stray capacitance;
- Testing the oscillator only at nominal supply voltage, even though gain drops with VCC.[^ti-sn74lvc1gx04-oscillator]

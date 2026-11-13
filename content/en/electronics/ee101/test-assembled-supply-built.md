---
id: emb-elee-0167
title: "How do you test an assembled 5 V supply built on a 7805?"
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
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
---

## Short answer

First measure output voltage without load, then connect a sized load resistor to draw test current. Measure `V_in` directly across the IC INPUT and GND pins to confirm adequate headroom above dropout. Check output variation against load shifts and moderate input adjustments within datasheet limits for line and load regulation.[^ti-lm340] Any power indicator LED requires a current-limiting resistor, and its draw adds to total load.

## Detailed explanation

Testing is conducted in stages so that each step isolates a single potential fault. Unloaded, the output merely indicates that the regulator is functional and connected correctly. The LM340/LM7805 datasheet specifies an output voltage of 4.8–5.2 V for load currents from 5 mA to 1 A (`T_J = 25 °C`),[^ti-lm340] so the no-load reading is an initial sanity check rather than an accuracy verification. Next, a load resistor sized to draw the target test current is connected: for 100 mA, this is `R = 5 V / 0.1 A = 50 Ω` with a power dissipation of `5*0.1 = 0.5 W`, so a resistor with margin, say rated for 1 W, should be selected.

`V_in` is measured directly across the IC pins rather than at the transformer secondary or filter capacitor: voltage drops across wiring, connectors, and rectifier diodes can reduce the actual input voltage. This is critical because the datasheet requires an input of at least 7.5 V to guarantee line regulation (see qid:emb-elee-0165).[^ti-lm340] Thermal dissipation is evaluated at this stage as well: the regulator dissipates `P_D = (V_in - V_out)*I_out`,[^ti-slva079] for example, with a 9 V input and 100 mA load, this is `(9 - 5)*0.1 = 0.4 W`, while the quiescent current (up to 8 mA at `T_J = 25 °C`)[^ti-lm340] adds up to another `9*0.008 = 0.072 W`.

The change in output voltage is compared against datasheet specifications. Load regulation for a current change from 5 mA to 1.5 A is typically 10 mV, with a maximum of 50 mV; line regulation for an input of 7.5–20 V at up to 1 A is at most 50 mV.[^ti-lm340] For example, if the output shifts from 5.03 to 5.01 V (20 mV) when transitioning from 5 mA to 100 mA, this is well within specification. Shifts of hundreds of millivolts indicate problems: input voltage falling below 7.5 V, poor contacts, or excessive wiring resistance. The datasheet tests regulation using short pulses (`t_w ≤ 10 ms`), so under continuous DC load, thermal drift adds to this variation.[^ti-lm340]

An LED is never connected across 5 V without a resistor: the current is determined by `R = (5 - V_F)/I`. For illustration, `V_F = 2 V` and 10 mA yield 300 Ω; with a standard 330 Ω resistor, the current is `3 V / 330 Ω ≈ 9.1 mA`, and these milliamperes form part of the total load. Finally, the output waveform under load is inspected with an oscilloscope rather than just a multimeter (see qid:emb-elee-0166).

**Common mistakes:**

- Measuring `V_in` at the power source rather than directly at the IC pins, thereby missing supply rail sag.
- Connecting an indicator LED without its own series resistor or failing to account for its current in the total load.
- Sizing the load resistor for a power rating exactly equal to the calculated dissipation: dissipating `0.5 W` in a 0.5 W resistor causes it to operate at its thermal limit.
- Comparing no-load measurements against the datasheet tolerance, which is specified for currents of at least 5 mA.

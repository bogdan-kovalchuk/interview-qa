---
id: emb-elee-0232
title: "Can a voltage amplifier with kilohm resistors drive an 8 Ω speaker directly?"
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
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
  - source_id: fiore-common-collector-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
  - source_id: ti-slaa067
    title: "Texas Instruments: Understanding Basic Analog – Circuit Equations"
    url: https://www.ti.com/lit/pdf/slaa067
---

## Short answer

No: the output impedance of a stage with a collector resistor approximately equals `R_C` (when `R_C` is much smaller than the transistor's internal output resistance), so an 8 Ω speaker forms a voltage divider with it and receives only a tiny fraction of the voltage.[^fiore-common-emitter-amplifier] Driving a speaker requires a stage with low output impedance, such as an emitter follower.[^fiore-common-collector-amplifier]

## Detailed explanation

In a common-emitter stage, the collector resistor `R_C` sets the AC output impedance. From the perspective of the load, the transistor looks like a current source with a very high internal output resistance, so the output can be modeled as a voltage source with a series resistance roughly equal to `R_C`.[^fiore-common-emitter-amplifier] The load `R_L` and `R_C` form a voltage divider, and the load receives a fraction `R_L / (R_L + R_C)` of the open-circuit voltage.[^fiore-common-emitter-amplifier]

**Example:** `R_C = 4.7 kΩ`, speaker `R_L = 8 Ω`, open-circuit output voltage 1 V RMS. The fraction is `8 / (4700 + 8) ≈ 0.0017`, meaning only about 1.7 mV appears across the speaker, corresponding to an attenuation of roughly 55 dB. The power delivered to 8 Ω at this voltage is `(0.0017)^2 / 8 ≈ 0.36 µW`. To deliver 1 V RMS across 8 Ω would require a current `I = V / R = 0.125 A` (Ohm's law[^ti-slaa067]) and a power of `V^2 / R = 0.125 W`.

The other factor is current. Collector current cannot be less than zero: at `I_C = 0`, the transistor is in cutoff.[^fiore-bjt-dc-load-line] Therefore, an unclipped sine wave cannot have a current amplitude greater than the quiescent current. With `V_CC = 9 V` and `V_CE ≈ V_CC / 2 = 4.5 V` (without an emitter resistor), the quiescent current through `R_C = 4.7 kΩ` is about 0.96 mA, so even through a coupling capacitor no more than ≈ 0.96 mA peak can reach the speaker. The resulting power is `(0.96 mA)^2 * 8 Ω / 2 ≈ 3.7 µW`, which is several orders of magnitude below 0.125 W.

The solution is a buffer stage with low output impedance. An emitter follower has a voltage gain near unity, low output impedance, and current gain, making it well-suited as a driver for low-impedance loads such as speakers.[^fiore-common-collector-amplifier] For loudness, transistors must be rated for current and power dissipation, not voltage alone.

**Common mistakes:**

- Assuming that the speaker receives the full calculated open-circuit voltage: the divider formed with the output impedance attenuates it.
- Connecting a speaker to the collector without a coupling capacitor: the DC collector voltage drops almost to zero, driving the stage into saturation.
- Assessing volume by voltage alone without calculating current and power into 8 Ω.

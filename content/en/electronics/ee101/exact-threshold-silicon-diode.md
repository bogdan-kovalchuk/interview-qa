---
id: emb-elee-0127
title: "Is 0.7 V the exact threshold of a silicon diode?"
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
  - source_id: vishay-1n4148
    title: "Vishay: 1N4148 small signal fast switching diode datasheet"
    url: https://www.vishay.com/docs/81857/1n4148.pdf
  - source_id: vishay-1n4001
    title: "Vishay: 1N4001 to 1N4007 general purpose plastic rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
---

## Short answer

No. Forward drop `V_F` depends on current, temperature, and device type; 0.7 V is merely a convenient approximation.[^libretexts-fiore-diode-models] For instance, according to datasheets, `V_F` reaches 1 V at 10 mA for a 1N4148 and 1.1 V at 1 A for a 1N4001 rectifier.[^vishay-1n4148][^vishay-1n4001] In the reverse direction, leakage current and reverse voltage ratings also apply.

## Detailed explanation

The 0.7 V value belongs not to the physical diode, but to the model. In the "second approximation," a diode is a switch with a "knee" voltage `V_knee`, which for silicon is taken as 0.7 V; the textbook explicitly emphasizes that these are behavioral models, not literal 0.7 V sources inside the diode.[^libretexts-fiore-diode-models] The real current-voltage characteristic is described by the Shockley diode equation, so `V_F` naturally, albeit relatively slowly, increases with current and is by no means constant.[^libretexts-fiore-diode-models]

**Current dependence.** The 1N4148 datasheet guarantees only an upper bound: `V_F ≤ 1 V` at `I_F = 10 mA` at 25 °C.[^vishay-1n4148] On the Fig. 1 curve of that same document at 25 °C, `V_F` ranges approximately from 0.5 V at 0.1 mA to 0.85 V at 100 mA (values read from the graph, so they are approximate). The 1N4001 rectifier diode can have up to 1.1 V at 1 A.[^vishay-1n4001] Even a simple model with bulk resistance `R_bulk` yields a voltage that increases with current: in the textbook example with `R_bulk = 10 Ω` at ≈ 5.6 mA, the diode has ≈ 0.756 V, not 0.7 V.[^libretexts-fiore-diode-models]

**Temperature dependence.** According to the same Fig. 1, at a fixed current `V_F` decreases as junction temperature rises: for `I_F = 10 mA`, approximately from 0.83 V at -40 °C to 0.54 V at 150 °C, which is about -1.5 mV/°C (approximately, from the graph).[^vishay-1n4148] Therefore, a diode in a hot package has a different voltage drop than one on the bench at room temperature.

**Reverse direction.** The "open switch" model is also an approximation. For the 1N4148, reverse leakage current is no more than 25 nA at `V_R = 20 V` at 25 °C, but up to 50 µA at that same voltage at 150 °C – 2000 times higher; the 1N4001 has up to 5 µA at 25 °C and up to 50 µA at 125 °C at rated reverse voltage.[^vishay-1n4148][^vishay-1n4001] Furthermore, the maximum reverse voltage rating depends on the device type: `V_RRM` in the 1N4001–1N4007 series ranges from 50 to 1000 V, while `V(BR)` for the 1N4148 is at least 100 V.

**Impact example.** For a 3.3 V source and a 1 kΩ resistor, `I = (3.3 - 0.7)/1000 = 2.6 mA`. If the actual `V_F = 0.55 V`, then `I = 2.75 mA`; if `0.85 V`, then `I = 2.45 mA`. That is a spread of approximately ±6% from `V_F` alone, and the lower the source voltage, the more pronounced the effect.

**Common mistakes:**

- Treating 0.7 V as a guaranteed property of a silicon diode and using it in calculations without margin.
- Failing to account for `V_F` varying with current and temperature, especially in low-voltage circuits and power rectifiers.
- Ignoring reverse leakage current and `V_RRM` / `V(BR)`, especially at elevated temperatures.

---
id: emb-elee-0131
title: "How many `V_F` drops are subtracted for an ordinary four-diode bridge?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: vishay-1n400x
    title: "Vishay: 1N4001–1N4007 datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---

## Short answer

Two: in each half-cycle, current flows through two bridge diodes in series (a diagonal pair), so `2*V_F` is subtracted from the peak secondary voltage.[^fiore-rectification] Only one `V_F` is subtracted in a center-tapped transformer rectifier, but applying that to a bridge is an error.[^fiore-rectification] The `V_F` value must be taken from the datasheet for the actual operating current: for a 1N4001 at 1 A, it reaches 1.1 V per diode.[^vishay-1n400x]

## Detailed explanation

A bridge consists of four diodes arranged such that during each half-cycle one diagonal pair conducts while the other is reverse-biased. In the positive half-cycle, current flows from the top terminal of the secondary winding through one diode to the load, returns through ground, and passes through the second diode back to the bottom terminal; in the negative half-cycle, the other diagonal pair performs this role.[^fiore-rectification] Consequently, at any instant two forward-biased diodes sit in series in the load current loop, and their drops add up: `V_out,peak = V_sec,peak - 2*V_F`.[^fiore-rectification]

In a center-tapped secondary circuit (two diodes), only one diode is in the load circuit, and only one `V_F` is subtracted from the voltage of half the winding.[^fiore-rectification] Confusion arises when a formula with a single drop is carried over to a bridge: the bridge utilizes the entire secondary winding, but pays for this with a second diode drop.

**Example.** A 12 V RMS secondary winding gives a peak of `12*sqrt(2) ≈ 16.97 V`. With silicon diodes where `V_F ≈ 0.7 V`, the peak at the bridge output is `16.97 - 1.4 = 15.57 V`; if one mistakenly subtracts only a single drop, the result is `16.97 - 0.7 = 16.27 V`: an overestimate of 0.7 V, or about 4.5%. For a 5 V RMS secondary (peak `5*sqrt(2) ≈ 7.07 V`), the correct result is `7.07 - 1.4 = 5.67 V`, while the erroneous result is `7.07 - 0.7 = 6.37 V`: an error of ≈ 12%.

The value of 0.7 V is only a rule of thumb. `V_F` increases with current: the 1N4001–1N4007 diode datasheet specifies a maximum of 1.1 V at 1 A per diode (at 25 °C).[^vishay-1n400x] When 1 A flows through a pair of diodes, up to `2*1.1 = 2.2 V` drops across them, dissipating up to `2.2*1 = 2.2 W`. When a filter capacitor follows the bridge, diodes conduct in short pulses whose peak current is much larger than the average load current,[^fiore-rectification] so at the peak instant the drop is higher than at the average current level.

**Common mistakes:**

- Subtracting only a single `V_F` drop for a four-diode bridge.
- Subtracting the drop from the RMS value rather than the peak value: `V_pk = V_rms*sqrt(2)`.
- Using 0.7 V for any diode and current instead of consulting the datasheet.
- Neglecting `2*V_F` at low secondary voltages, where it accounts for a large fraction of the total voltage.

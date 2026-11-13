---
id: emb-elee-0206
title: "Why is an amplifier with `A_v<1` needed?"
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
  - source_id: fiore-common-collector-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
---

## Short answer

Such an amplifier is an emitter follower: its voltage gain `A_v` is slightly less than unity, but it provides substantial current gain, high input impedance, and low output impedance. Consequently, it presents minimal loading to high-impedance signal sources while driving low-impedance loads, functioning as an impedance buffer between stages.[^fiore-common-collector-amplifier]

## Detailed explanation

An amplifier with `A_v < 1` is an emitter follower (common-collector circuit). The output voltage is taken from the emitter and follows the base voltage, so `A_v = r_E/(r_e + r_E)`, where `r_E` is the total AC resistance in the emitter circuit including the load. This value is always less than 1 and approaches 1 when `r_E ≫ r_e`.[^fiore-common-collector-amplifier]

The need for such a stage is not voltage amplification, but impedance matching. A signal source with high internal resistance driving a low-resistance load forms a voltage divider where most of the signal voltage is lost. In Fiore's example, a source has an internal resistance of 1 kΩ, the load is 500 Ω, and the open-circuit input signal is 100 mV: without a follower, the voltage across the load is 100 mV × 500 / 1500 ≈ 33 mV. With a follower, the stage input resistance is about 9 kΩ, the loaded gain is about 0.94, the divider attenuation with the source is about 0.90, and the load receives about 85 mV.[^fiore-common-collector-amplifier]

The follower does not amplify voltage, but it provides significant current and power gain. Its output resistance is low: about 37 Ω in the example, which is far lower than that of common-emitter stages, allowing it to drive low-impedance loads effectively. Distortion in followers is typically low because the voltage gain is close to unity, which is a desirable design goal.[^fiore-common-collector-amplifier] The output signal is in phase with the input.[^fiore-common-collector-amplifier]

**Common mistakes:**

- Expecting a voltage gain greater than 1 from a follower.
- Failing to account for its input resistance as a load on the signal source alongside the source's internal resistance.
- Assuming the output resistance is zero: it is determined by `R_E` in parallel with the reflected base circuit impedance, so it is non-zero.

---
id: emb-elee-0144
title: "What is a Zener diode's dynamic resistance `r_Z`?"
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
---

## Short answer

Dynamic (differential) resistance `r_Z = ΔV_Z/ΔI_Z` is the inverse slope of the Zener breakdown curve at an operating point, giving small-signal changes `ΔV_Z ≈ r_Z*ΔI_Z`.[^nexperia-an90031] It is non-zero and current-dependent: for a BZX84-C5V1, maximum `r_Z` is 480 Ω at 1 mA and 60 Ω at 5 mA.[^nexperia-bzx84] Because of `r_Z`, regulator output drifts slightly with load and input voltage; smaller `r_Z` produces tighter regulation.

## Detailed explanation

**Where `r_Z` comes from.** An ideal Zener diode would hold `V_Z` strictly constant regardless of the current flowing through it. The real I-V curve in breakdown is not vertical, so voltage increases slightly with current, meaning dynamic resistance `R_dyn = ΔV_Z/ΔI_Z` is greater than zero.[^nexperia-an90031] In datasheets it is designated `r_dif` and described as the steepness of the `V_Z–I_Z` curve: the steeper the curve, the smaller the dynamic resistance and the more stable the voltage.[^nexperia-an90031] For small deviations from an operating point, `ΔV_Z ≈ r_Z*ΔI_Z`. For large current swings, this linear model is no longer applicable.

**It is not `V_Z/I_Z`.** Dynamic resistance is the slope of the characteristic curve, not the static ratio of voltage to current at that point. For a BZX84-C5V1 at 5 mA, the static ratio is `5.1/0.005 ≈ 1.02 kΩ`, whereas maximum `r_dif` at this current is only 60 Ω.[^nexperia-bzx84] That is a difference of at least a factor of 17. The small-signal approximation `ΔV_Z ≈ r_Z*ΔI_Z` requires specifically `r_dif`.

**Dependence on current and device type.** `r_Z` is not a fixed diode constant. For the BZX84-C5V1, the maximum is 480 Ω at 1 mA and 60 Ω at 5 mA, meaning that at lower current the curve is flatter.[^nexperia-bzx84] For a 6.2 V part in that same series, the maximum at 5 mA is only 10 Ω.[^nexperia-bzx84] Consequently, Nexperia recommends maintaining a minimum Zener current of approximately 5 mA (for devices up to 17 V) to ensure operation on the steep slope.[^nexperia-an90031] All these numbers are maximum limits for this specific series at `T_j = 25 °C`; specific values for your diode and operating current must be taken from its datasheet.

**Impact in a regulator.** In a circuit with a series resistor `R` and a load in parallel with the Zener diode, any variation in `V_in` or load current redistributes current and shifts `V_out` by `r_Z*ΔI_Z`. For small variations in a simple linear model, `ΔV_out/ΔV_in = r_Z/(R + r_Z)`. With `R = 390 Ω` and `r_Z = 60 Ω`, this evaluates to `60/450 ≈ 0.13`: a 1 V change at the input causes up to ≈ 133 mV of drift at the output. For `r_Z = 480 Ω`, it would reach `480/870 ≈ 0.55`. For more details on line and load regulation, see qid:emb-elee-0141.

**Common mistakes:**

- Confusing `r_Z` with the static ratio `V_Z/I_Z`: ≈ 1.02 kΩ versus ≤ 60 Ω in this example.
- Assuming `r_Z` is a fixed constant of the diode and taking a value specified for a different current.
- Applying `ΔV_Z ≈ r_Z*ΔI_Z` to large current swings or outside the breakdown region.

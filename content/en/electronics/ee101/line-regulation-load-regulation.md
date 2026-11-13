---
id: emb-elee-0141
title: "What are line regulation and load regulation?"
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
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

Line regulation specifies the change in output voltage resulting from input voltage variation at constant load: `ΔV_out/ΔV_in`. Load regulation specifies output voltage variation resulting from load current changes at constant input voltage: `ΔV_out/ΔI_out`.[^ti-slva079] Both parameters describe steady-state behavior rather than transient response, and a smaller absolute value indicates superior voltage stabilization.[^ti-slva079]

## Detailed explanation

Any voltage regulator is intended to maintain a steady output despite external variations. The two primary disturbances are input voltage variations and load current changes, and each has its corresponding performance metric. Line regulation is the response of the output voltage to a change in input voltage at constant load: `ΔV_out/ΔV_in`. Load regulation is the response to a change in load current at constant input voltage: `ΔV_out/ΔI_out`.[^ti-slva079] By definition, the former parameter is dimensionless (for example, mV/V), while the latter has units of resistance (mV/mA = Ω): it represents the static output resistance of the regulator.

These parameters describe steady-state behavior: they characterize the new steady-state output value rather than the settling trajectory. The response speed and overshoot following a step in input voltage or load current constitute a distinct metric (transient response).[^ti-slva079] In a linear regulator, both figures depend on open-loop gain: higher loop gain delivers superior line and load regulation.[^ti-slva079] Finite loop gain is one reason these parameters are non-zero.

**Example: simple Zener diode regulator.** A Zener diode has a finite dynamic resistance `r_Z = ΔV_Z/ΔI_Z`.[^nexperia-an90031] Adopting the model `V_out = V_Z + r_Z*I_Z` and `I_Z = (V_in - V_out)/R - I_load`, for small variations we find `ΔV_out/ΔV_in = r_Z/(R + r_Z)` and `ΔV_out/ΔI_load = -(R*r_Z)/(R + r_Z)`. For a BZX84-C5V1, maximum `r_Z` at 5 mA is 60 Ω,[^nexperia-bzx84] with `R = 390 Ω`. This gives line regulation `≤ 60/450 ≈ 0.13`, meaning a 1 V input variation produces up to 133 mV of output change. Load regulation magnitude is `≤ 60*390/450 = 52 Ω`: a 1 mA increase in load current causes up to a 52 mV drop. This is an upper-bound estimate for an operating point near 5 mA. If the Zener diode operated near 1 mA where maximum `r_Z` reaches 480 Ω,[^nexperia-bzx84] then `ΔV_out/ΔV_in` would degrade to `480/870 ≈ 0.55` and load regulation to `480*390/870 ≈ 215 Ω`.

**Operating conditions.** Both metrics are meaningful only while the regulator remains in active regulation. If the load draws almost the entire resistor current, the Zener diode cuts off, regulation is lost, and the resistor and load behave as a simple voltage divider (see qid:emb-elee-0143).[^fiore-rectification] Datasheet values are tied to specific input voltage and current test ranges and cannot be extrapolated arbitrarily to other conditions.

**Common mistakes:**

- Confusing line and load regulation: the former concerns input voltage change, the latter concerns load current change.
- Comparing load regulation without checking the `ΔI_out` test range for which it is specified.
- Treating these metrics as descriptions of transient dynamics rather than steady-state values.
- Expecting regulation outside active operating conditions: when the Zener diode is starved of current or the input drops below minimum required headroom.

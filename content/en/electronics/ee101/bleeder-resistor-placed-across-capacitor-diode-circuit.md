---
id: emb-elee-0150
title: "Why is a bleeder resistor placed across the capacitor in a diode circuit?"
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
  - source_id: kuphaldt-bleeder-supply
    title: "Workforce LibreTexts: Electric Circuits VI – Experiments (Kuphaldt), 5.19 Vacuum Tube Audio Amplifier"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_VI_-_Experiments_(Kuphaldt)/05:_Discrete_Semiconductor_Circuits/5.19:_Vacuum_Tube_Audio_Amplifier
  - source_id: vishay-pre-charge-bleed
    title: "Vishay: Pre-charge resistor and bleed resistor selection (Did You Know?, MS8772259-1810)"
    url: https://www.vishay.com/docs/48468/_ms8772259-1810-didyouknow-rs_rh-nh.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-peak-detector
    title: "Engineering LibreTexts: Operational Amplifiers and Linear Integrated Circuits (Fiore), 7.2 Precision Rectifiers"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/07:_Nonlinear_Circuits/7.02:_Precision_Rectifiers
  - source_id: gatech-rc-charging-discharging
    title: "Georgia Tech Physics Book: Charging and Discharging a Capacitor"
    url: https://physicsbook.gatech.edu/Charging_and_Discharging_a_Capacitor
---

## Short answer

A bleeder resistor provides a discharge path for the capacitor because the diode blocks reverse current: without it, a charged capacitor retains high voltage long after power-off, which is dangerous, and tracks falling input peaks sluggishly.[^kuphaldt-bleeder-supply][^fiore-peak-detector] For example, 100 kΩ and 1 µF give `τ = R*C = 0.1 s`; after `5τ`, approximately 0.67% of initial voltage remains.[^gatech-rc-charging-discharging] The penalty is continuous quiescent power dissipated in the resistor.

## Detailed explanation

A diode conducts current in only one direction. In a "diode plus capacitor" circuit (a filtered rectifier or peak detector), the capacitor charges to the peak of the input voltage, and when the input drops below the capacitor voltage, the diode turns off. From then on, only the load and internal leakages can discharge the capacitor.[^fiore-rectification] Consequently, under light load the output remains near the peak with small ripple, while with no load the voltage decays very slowly, limited only by leakage currents.[^fiore-rectification][^fiore-peak-detector]

A bleeder resistor in parallel with the capacitor provides a guaranteed discharge path. The primary reason is safety: in a power supply, such a resistor discharges the filter capacitor after AC mains is turned off, preventing the capacitor from retaining a hazardous charge for long periods.[^kuphaldt-bleeder-supply] In high-voltage systems (such as electric vehicle inverters), the role is identical – safely discharging capacitors when the equipment is inactive.[^vishay-pre-charge-bleed] The secondary reason is functional: in a peak detector or a rectifier with minimal load, the discharge time constant determines how quickly the output tracks decreases in input amplitude; with a long time constant the output remains virtually flat, while with a shorter one it tracks the envelope.[^fiore-peak-detector]

The discharge rate is described by `V(t) = V0*e^(-t/(R*C))`, `τ = R*C`.[^gatech-rc-charging-discharging] For 100 kΩ and 1 µF, `τ = 10^5 * 10^-6 = 0.1 s`, and after `5τ = 0.5 s` what remains is `e^-5 ≈ 0.0067`, or ≈ 0.67% of initial voltage. Kuphaldt's experiment shows that 47 µF and 100 kΩ give `τ = 4.7 s`; a larger capacitor requires a smaller resistor or longer waiting time.[^kuphaldt-bleeder-supply]

**Trade-off example.** Rectified 230 V RMS mains produces a peak of `230*√2 ≈ 325 V`. For a 1000 µF capacitor and 100 kΩ resistor, `τ = 100 s`, and the voltage drops to 50 V (an illustrative threshold, not an official safety standard) in `t = τ*ln(325/50) ≈ 100*1.87 ≈ 187 s`, or roughly 3 minutes. Meanwhile, the resistor continuously dissipates `P = V²/R = 325²/10^5 ≈ 1.06 W`. A smaller resistance discharges faster, but heats up and wastes power continuously while the device operates; the resistor must be rated for both power dissipation and operating voltage.

**Common mistakes:**

- Treating a bleeder resistor as an absolute safety guarantee: the resistor can fail open, so capacitor voltage must always be measured before servicing.
- Choosing a resistance that is too low (excessive power loss and heat) or too high (discharge takes minutes).
- Believing that discharge finishes completely at `5τ`: an exponential decay only approaches zero asymptotically, leaving ≈ 0.67%.

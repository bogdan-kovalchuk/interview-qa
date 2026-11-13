---
id: emb-elee-0173
title: "What are the basic relations of an ideal transformer, and what does its VA rating mean?"
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
  - source_id: kuphaldt-transformer-operation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.1 Mutual Inductance and Basic Operation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.01:_Mutual_Inductance_and_Basic_Operation
  - source_id: kuphaldt-transformer-ratios
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.2 Step-up and Step-down Transformers (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.02:_Step-up_and_Step-down_Transformers
  - source_id: kuphaldt-transformer-practical
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.8 Practical Considerations – Transformers (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.08:_Practical_Considerations_-_Transformers
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-ac-apparent-power
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (section 7.2, Power Waveforms)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
---

## Short answer

For an ideal transformer, `V_s/V_p = N_s/N_p` and `I_s/I_p = N_p/N_s`: voltage and current scale inversely, and power is conserved.[^kuphaldt-transformer-ratios] The VA rating is the apparent power `S = V_s,RMS*I_s,RMS` at the rated secondary voltage; it defines the maximum secondary RMS current `I_s,max = S/V_s` rather than real power in watts.[^kuphaldt-transformer-practical][^fiore-ac-apparent-power]

## Detailed explanation

An ideal transformer is a lossless model with unity magnetic coupling between both windings. The voltage across a winding is proportional to its turn count and the rate of change of the mutual magnetic flux,[^kuphaldt-transformer-operation] so the voltages scale directly with the turns ratio: `V_s/V_p = N_s/N_p`. Because a transformer transforms power rather than generating it, currents scale inversely: `I_s/I_p = N_p/N_s`, and input power equals output power.[^kuphaldt-transformer-ratios] Therefore, a step-down transformer that reduces voltage increases secondary current, requiring the secondary to be wound with heavier-gauge wire.[^kuphaldt-transformer-ratios] Example: for a `230 V / 12 V` mains transformer, the turns ratio is `N_p/N_s = 230/12 ≈ 19.2`; if the secondary delivers `2 A`, then in the ideal case the primary draws `2*12/230 ≈ 0.104 A`.

The volt-ampere rating defines the load limit. The windings must handle their respective currents without overheating, so a transformer is rated by its winding voltages and its VA rating, from which allowable current is calculated: `I = S/V`.[^kuphaldt-transformer-practical] For a 120 V / 48 V, 1 kVA transformer, the maximum primary current is `1000/120 ≈ 8.33 A` and the maximum secondary current is `1000/48 ≈ 20.8 A`.[^kuphaldt-transformer-practical] In other words, the VA rating is the product of the rated secondary voltage and the maximum allowable secondary current.[^fiore-rectification]

The rating is given in VA rather than watts because the windings are constrained by current (resistive wire heating), not by the real power absorbed by the load.[^kuphaldt-transformer-practical] The product of RMS voltage and RMS current is apparent power, which equals real power only for a purely resistive load; when a phase displacement exists between voltage and current, real power is lower.[^fiore-ac-apparent-power] The transformer does not dictate the load type, so it limits the current at a given rated voltage. A prime example is a rectifier with a filter capacitor: the diode conducts only in short pulses, and in the rectification textbook example, the peak capacitor charging current (around 800 mA) greatly exceeds the DC current drawn by a 100 Ω load at 8–9 V.[^fiore-rectification] The secondary RMS current is therefore substantially higher than the average DC load current, which is why the VA rating must be sized with margin for such loads, treating a naive `V*I_load` calculation as an absolute minimum.

Real transformers deviate from ideal relationships. Winding resistance and core losses produce dissipation, while leakage inductance acts like a series impedance, causing secondary terminal voltage to sag under increasing load; the efficiency of modern power transformers typically exceeds 95%.[^kuphaldt-transformer-practical] Thus, `V_s/V_p ≈ N_s/N_p` is an effective approximation for estimation, but not an exact equality under load.

**Common mistakes:**

- Confusing the scaling ratios: voltage is proportional to `N_s/N_p`, whereas current is proportional to `N_p/N_s`.[^kuphaldt-transformer-ratios]
- Dividing VA by the wrong winding voltage: secondary current is `S/V_s`, while primary current is `S/V_p`.[^kuphaldt-transformer-practical]
- Reading VA as watts and ignoring power factor or non-sinusoidal current waveforms.[^fiore-ac-apparent-power]
- Expecting exactly the rated secondary voltage to appear under full load.[^kuphaldt-transformer-practical]

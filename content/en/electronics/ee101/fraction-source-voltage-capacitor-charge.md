---
id: emb-elee-0033
title: "To what fraction of the source voltage does a capacitor charge after 1τ, 2τ, 3τ, and 5τ?"
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
  - source_id: gatech-rc-charging-discharging
    title: "Georgia Tech Physics Book: Charging and Discharging a Capacitor"
    url: https://physicsbook.gatech.edu/Charging_and_Discharging_a_Capacitor
---

## Short answer

After `1τ`, `2τ`, `3τ`, and `5τ`, an ideally charging capacitor reaches approximately 63.2%, 86.5%, 95.0%, and 99.3% of the final voltage, respectively. After `5τ`, roughly 0.7% of the step remains, so being "practically charged" depends on the required application tolerance.[^gatech-rc-charging-discharging]

## Detailed explanation

For an ideal series RC circuit where an uncharged capacitor is connected through a resistor to a constant voltage `V_s`, the voltage is described by `V_C(t) = V_s*(1 - e^(-t/τ))`, where `τ = R*C`. When time is substituted as multiples of τ, the fraction of the final voltage depends solely on the exponential term, rather than on the specific values of the resistor and capacitor.[^gatech-rc-charging-discharging]

For instance, at `t = τ`, we obtain `1 - e^(-1)`, or approximately 63.2%. At `2τ`, this becomes `1 - e^(-2)`, approximately 86.5%; at `3τ`, approximately 95.0%; and at `5τ`, approximately 99.3%. Consequently, the difference between the capacitor voltage and the final source voltage decays as `e^(-t/τ)`. This is why each successive equal interval of time divides the remaining error by the same factor, rather than adding a fixed number of percentage points.[^gatech-rc-charging-discharging]

These fractions apply to voltage charging from an initial zero to the final value. If the capacitor already carried an initial voltage, after `τ` it covers 63.2% of the difference between that initial level and the new steady-state level. In a physical circuit, the actual values also depend on real component values of `R` and `C`, leakage, load impedances, and how accurately a single-pole RC model reflects the circuit.[^gatech-rc-charging-discharging]

Example for a 5 V source: after `3τ`, the voltage will be approximately `5 V*0.950 = 4.75 V`; after `5τ`, approximately `5 V*0.993 = 4.965 V`. Thus, the statement that a capacitor is "fully charged after `5τ`" is an engineering approximation with a remaining difference of about 35 mV in this example, rather than a mathematically exact completion.[^gatech-rc-charging-discharging]

**Common mistakes:**

- Confusing the fraction of voltage already attained with the fraction remaining to reach the final value.
- Treating `5τ` as the exact moment of full charging rather than an agreed-upon threshold of practical accuracy.
- Applying these percentages to a circuit with a non-zero initial voltage without scaling relative to the full voltage step.

---
id: emb-elee-0154
title: "What are the losses and efficiency of a 9 V -> 5 V linear regulator at 100 mA and at 500 mA?"
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
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
---

## Short answer

`P_loss ≈ (V_in - V_out)*I_out`: at 100 mA this equals `4 V * 0.1 A = 0.4 W`, giving `η ≈ V_out/V_in ≈ 55.6%` assuming negligible quiescent current.[^ti-slva118a] At 500 mA losses increase to 2 W with the same efficiency, demanding verification of package and board thermal limits.[^ti-slva118a]

## Detailed explanation

A linear regulator acts as a variable resistor between input and output: the pass element conducts continuously, and the input current approximately equals the output current.[^ti-slva118a] Therefore, power drawn from the source is `P_I = V_in*I_in`, while power delivered to the load is `P_O = V_out*I_out`. The difference `P_D = P_I - P_O ≈ (V_in - V_out)*I_out` is converted almost entirely into heat within the regulator.[^ti-slva118a] For 9 V input, 5 V output, and 100 mA load: `P_I = 9*0.1 = 0.9 W`, `P_O = 5*0.1 = 0.5 W`, `P_D = 0.4 W`, and `η = 0.5/0.9 ≈ 55.6%`.

At 500 mA (input remains 9 V, output 5 V): `P_I = 4.5 W`, `P_O = 2.5 W`, `P_D = 2.0 W`, and `η` is again `2.5/4.5 ≈ 55.6%`. Thus, efficiency is determined solely by the voltage ratio `V_out/V_in`, which is independent of current, while power dissipation scales proportionally with current: a fivefold increase.[^ti-slva118a] Efficiency alone does not indicate whether a package will survive: 56% represents 0.4 W of heat at 100 mA, but 2 W at 500 mA, and the 9 V source must supply `4.5 W` rather than merely 2.5 W.

The simplification `η ≈ V_out/V_in` assumes that the regulator quiescent current `I_q` is negligible compared to `I_out`. Including it yields `η = V_out*I_out/(V_in*(I_out + I_q))`.[^ti-slva118a] For illustration, assume `I_q = 5 mA`: at 100 mA, `η = 0.5/(9*0.105) ≈ 52.9%`; at 500 mA, `η = 2.5/(9*0.505) ≈ 55.0%`. As load current decreases, the contribution of `I_q` becomes more prominent; in bipolar regulators `I_q` also varies with load, whereas in PMOS regulators it remains nearly constant.[^ti-slva118a]

Thermal calculation: power dissipation must not exceed the package dissipation capability, `P_D ≤ (T_J - T_A)/θ_JA`, requiring `θ_JA ≤ (T_J - T_A)/P_D`.[^ti-slva118a] Assume (for illustration) `T_J = 125 °C` and `T_A = 40 °C`. At 0.4 W, the allowable thermal resistance is `θ_JA ≤ 85/0.4 = 212.5 °C/W`, whereas at 2 W it is only `85/2 = 42.5 °C/W`. In SLVA118A (Figure 5), θ_JA for packages in still air ranges from 22–58 °C/W for large packages up to 314–478 °C/W for the smallest; thus, at 500 mA a large package with substantial PCB copper heat sinking is required, and under these assumptions the smallest package fails even at 100 mA.[^ti-slva118a] If a package is inadequate, one must select a larger package, reduce the `V_in - V_out` drop, or choose a switching converter topology.

**Common mistakes:**

- Evaluating thermal performance based on efficiency percentage rather than absolute dissipation `(V_in - V_out)*I_out`.
- Using `η = V_out/V_in` for very light loads where `I_q` is comparable to `I_out`.
- Comparing load power (2.5 W) against package dissipation limits instead of regulator internal dissipation (2 W).
- Forgetting that allowable `P_D` depends on `T_A`, `T_J`, and PCB copper area, so a θ_JA number is meaningless without these operating conditions.

---
id: emb-elintro-0240
title: "What is the simplified MOSFET current formula in the saturation region?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

For an ideal long-channel NMOS in the saturation region, `I_D = K*(V_GS - V_th)^2`, where `K` combines process and geometry parameters and depends on whether the `1/2` factor is absorbed. The model requires `V_GS > V_th` and `V_DS >= V_GS - V_th`; real current also deviates due to device non-idealities.[^aac-semiconductors]

## Detailed explanation

For a long-channel enhancement-mode NMOS in the simplified square-law model of the saturation region, the drain current is given by `I_D = K*(V_GS - V_th)^2`. Here, `V_GS - V_th` is the overdrive voltage, and `K` combines mobility, gate oxide capacitance, and the channel width-to-length ratio. In common derivations, the coefficient `K = μ*C_ox*(W/L)/2` already includes the `1/2` factor; in other references, `K` is defined without `1/2` as `μ*C_ox*(W/L)` and written `I_D = (1/2)*K*(V_GS - V_th)^2`, so the formula must always be read alongside the definition of `K`.[^aac-semiconductors]

For NMOS, the saturation condition is approximately `V_DS >= V_GS - V_th` with `V_GS > V_th`. In this region, the channel pinches off near the drain, and the ideal model treats `I_D` as independent of further increases in `V_DS`. A real transistor exhibits channel-length modulation and other non-idealities, so the current is not perfectly constant.[^aac-semiconductors]

Example: doubling the overdrive voltage `V_GS - V_th` quadruples `I_D` according to the ideal formula, assuming constant `K` and that the device remains in saturation. This is not a universal formula for a power MOSFET operated as a switch: in its on-state, one typically uses the `R_DS(on)` specification rather than extrapolating the square-law model.[^aac-semiconductors]

**Common mistakes:**
- Failing to clarify whether the factor `1/2` is already absorbed into `K`.
- Applying the formula in the triode region or below threshold.
- Assuming the current of a real MOSFET is completely independent of `V_DS`.

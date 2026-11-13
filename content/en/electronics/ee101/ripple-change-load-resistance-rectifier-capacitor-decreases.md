---
id: emb-elee-0138
title: "How does the ripple change when the load resistance of a rectifier with a capacitor decreases?"
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
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
---

## Short answer

Ripple increases: lower load resistance draws higher current, discharging the capacitor faster between peaks.[^fiore-rectification] For small ripple, `ΔV_pp ≈ I_load/(f_ripple*C)`, meaning ripple amplitude scales approximately with load current,[^fiore-capacitors] while average output voltage drops.[^fiore-rectification] Laboratory verification is done in steps: without a filter capacitor, with a capacitor in proper polarity, and finally under increased load.

## Detailed explanation

Between peaks, the diodes are reverse-biased and the load is powered solely by the capacitor. Its voltage drops according to `i = C*dv/dt`: at approximately constant current, the decrease is linear, `ΔV = I*Δt/C`, where `Δt` is the interval between peaks.[^fiore-capacitors] Load current is `I = V/R_load`, so reducing `R_load` increases current and consequently increases voltage sag over that same interval. The textbook summarizes this: ripple increases with load current, whereas under light load the output remains near the secondary peak with very low ripple; at large currents, ripple increases and average output voltage drops.[^fiore-rectification]

This can also be understood through the time constant `τ = R_load*C`: discharge is exponential, and the lower `R_load`, the smaller `τ` is relative to the interval between peaks, meaning the filter is less effective at holding voltage.[^fiore-rectification] The linear formula `ΔV ≈ I/(f*C)` is an approximation valid only when `τ` is much larger than the ripple period; for large ripple it is not sufficiently accurate.

**Example (independent calculation).** A bridge rectifier fed from a 50 Hz line, `f_ripple = 100 Hz`, `C = 1000 µF`, voltage about 12 V:

- `R_load = 600 Ω`: `I = 12/600 = 20 mA`, `ΔV ≈ 0.02/(100*0.001) = 0.2 V`;
- `R_load = 120 Ω`: `I = 100 mA`, `ΔV ≈ 0.1/(100*0.001) = 1.0 V`; exponential calculation `12*(1 - e^(-0.01/0.12)) ≈ 0.96 V` closely agrees;
- `R_load = 12 Ω`: `I = 1 A`, the linear formula gives 10 V, which is absurd; the exponential `12*(1 - e^(-0.01/0.012)) ≈ 6.8 V` shows that over 10 ms the capacitor loses more than half its voltage, and filtering has practically collapsed.

Reducing resistance by a factor of 5 increases ripple approximately 5 times, as long as `τ` remains much larger than 10 ms. For 600 Ω `τ = 0.6 s`, for 120 Ω `τ = 0.12 s`, and for 12 Ω `τ = 12 ms`, which is already comparable to the period, and the linear estimate ceases to apply.

There is also a side effect: higher load current produces larger short diode current pulses (in the textbook simulation, peaks reach hundreds of mA).[^fiore-rectification] Therefore, reducing `R_load` must also be verified against the peak current ratings of the diodes and transformer.

**Common mistakes:**

- Believing that higher current "smooths" the output: on the contrary, the filter performs worse with smaller `R_load`.
- Using the linear formula for large ripple when `R_load*C` is comparable to the ripple period.
- Forgetting that in a bridge `f_ripple = 2*f_mains`, whereas in a half-wave circuit `f_ripple = f_mains`.

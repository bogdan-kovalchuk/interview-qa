---
id: emb-elee-0130
title: "How do you estimate the ripple after a bridge rectifier with a capacitor?"
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

For small ripple, `ΔV_pp ≈ I_load/(f_ripple*C)`: between peaks the capacitor supplies the load current for approximately one ripple period.[^fiore-capacitors] After a bridge rectifier, `f_ripple = 2*f_mains`, or 100 Hz for a 50 Hz line, so at 20 mA and 1000 µF, `ΔV_pp ≈ 0.02/(100*0.001) = 0.2 V`. This approximation assumes constant current and neglects capacitor ESR. To reduce ripple at the same load current, C is increased, though diodes then conduct in shorter, higher-current pulses.[^fiore-rectification]

## Detailed explanation

Between peaks of the rectified voltage, the diodes are reverse-biased because the input voltage falls below the capacitor voltage, and the load is supplied exclusively by the capacitor. Capacitor current is related to voltage by `i = C*dv/dt`, so with approximately constant load current, the voltage drops linearly: `ΔV = I*Δt/C`.[^fiore-capacitors] The maximum discharge time is the interval between adjacent peaks, `Δt = 1/f_ripple`, which gives the formula `ΔV_pp ≈ I_load/(f_ripple*C)`. The higher the load current, the larger the ripple, whereas under light load the output remains near the secondary peak with very low ripple.[^fiore-rectification]

**Why `f_ripple = 2*f_mains`.** In a bridge rectifier, current flows through the load in the same direction during both line half-cycles, producing two peaks per AC line period: 100 Hz for 50 Hz and 120 Hz for 60 Hz.[^fiore-rectification] In a half-wave rectifier `f_ripple = f_mains`, so twice the capacitance is needed for the same ripple; this is why full-wave circuits allow using a smaller filter capacitor.[^fiore-rectification]

**Limits of the approximation.** The formula holds when ripple is small compared to the DC level, meaning the time constant `R_load*C` is much larger than the ripple period. For 12 V and 20 mA, we have `R_load = 12/0.02 = 600 Ω` and `τ = 600*0.001 = 0.6 s` versus 10 ms between peaks; an exponential calculation `12*(1 - e^(-0.01/0.6))` yields ≈ 0.20 V, which is the same result. In practice, the capacitor discharges for slightly less than 10 ms because diodes turn on just before the peak, and capacitor ESR adds a step component `I*ESR`, so the actual value departs from the estimate. When ripple is large or `R_load*C` is comparable to the period, discharge is no longer linear and an exponential calculation is required.

**Example.** For a 60 Hz line with the same 20 mA and 1000 µF: `f_ripple = 120 Hz` and `ΔV_pp ≈ 0.02/(120*0.001) ≈ 0.17 V`. To keep ripple below 0.1 V at 50 Hz, `C ≥ 0.02/(100*0.1) = 0.002 F = 2000 µF` is required. Increasing capacitance is not without penalty: a diode turns on only when the input voltage exceeds the capacitor voltage, so increasing C narrows the conduction interval and drives up the peak charging current.[^fiore-rectification] Diodes and transformers must be verified against peak, rather than average, current ratings.

**Common mistakes:**

- Using `f_ripple = 50 Hz` for a bridge instead of 100 Hz, leading to double the estimated ripple.
- Substituting microfarads as farads: 1000 µF is 0.001 F, not 1000.
- Assuming the formula remains accurate for large ripple (`R_load*C` comparable to the period) and neglecting ESR.
- Increasing C without verifying the peak current ratings of diodes and transformers.

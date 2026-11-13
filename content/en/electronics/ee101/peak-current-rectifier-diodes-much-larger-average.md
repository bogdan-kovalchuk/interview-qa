---
id: emb-elee-0139
title: "Why is the peak current of rectifier diodes much larger than the average load current?"
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
  - source_id: vishay-1n4001
    title: "Vishay: 1N4001 to 1N4007 general purpose plastic rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---

## Short answer

Diodes conduct only when the input AC voltage exceeds the capacitor voltage by approximately `V_F`, creating short conduction pulses near waveform peaks.[^fiore-rectification] Over each ripple period, the diodes must replenish all charge drained by the load during the non-conducting interval, forcing peak diode current to be substantially higher than average load current.[^fiore-rectification]

## Detailed explanation

Past the peak, the input voltage drops faster than the capacitor discharges through the load, so the diodes turn off and the load is subsequently supplied solely by the capacitor. A diode turns on again only when the input voltage exceeds the capacitor voltage by approximately 0.7 V; it is during this short interval that the capacitor is replenished, which results in very large current pulses.[^fiore-rectification] The larger the capacitor, the higher its voltage is sustained, the shorter the diode conduction interval, and the higher the current pulse: in the textbook simulation, increasing capacitance from 50 µF to 1000 µF with the same 100 Ω load raised the peak charging current from approximately 180 mA to approximately 800 mA while shortening the pulse from ≈ 4 ms to ≈ 2.5 ms.[^fiore-rectification]

The root cause is charge conservation. In steady state, capacitor voltage repeats cyclically every period, so the charge drained by the load during the ripple period, `Q = I_load*T`, must be restored by the diodes during the conduction time `t_c`, which is much shorter than `T`. The average diode current during the conduction interval is ≈ `I_load*T/t_c`, which is `T/t_c` times higher than `I_load`, and the peak of the pulse is higher still.

**Example (independent calculation).** A bridge rectifier, 50 Hz line, `f_ripple = 100 Hz`, `T = 10 ms`, `I_load = 100 mA`, `C = 2000 µF`, capacitor peak `V_p ≈ 12 V`. Ripple is `ΔV ≈ I/(f*C) = 0.1/(100*0.002) = 0.5 V`; the charge per period `Q = 0.1*0.01 = 1 mC` matches `C*ΔV = 0.002*0.5 = 1 mC`. Diodes conduct while the input voltage exceeds `V_p - ΔV`, which spans an angle of `acos(1 - 0.5/12) ≈ 16.6°` before the peak out of 180° between peaks, giving `t_c ≈ 10*16.6/180 ≈ 0.92 ms`. Thus, the average pulse current is ≈ `1 mC/0.92 ms ≈ 1.1 A`, which is ≈ 11 times higher than 0.1 A, and the peak of the pulse is even higher. In a bridge, each diode conducts only every other half-cycle, so the average current through an individual diode equals half of `I_load`.

**Implications for diode selection.** Diodes cannot be chosen based on average load current alone. For the 1N4001, the datasheet specifies an average rectified forward current `I_F(AV) = 1.0 A`, but also a non-repetitive surge peak current `I_FSM = 30 A` (8.3 ms half sine),[^vishay-1n4001] so repetitive peak currents and transformer loading must be checked. Peak current is also limited by transformer winding resistance and capacitor ESR, which are outside this simple model.

**Common mistakes:**

- Selecting diodes based solely on the average load current.
- Increasing filter capacitance without verifying peak current ratings of the diodes and transformer.
- Assuming that diodes conduct over the entire half-cycle, as in an unfiltered rectifier.

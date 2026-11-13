---
id: emb-elee-0145
title: "When is an integrated regulator better than a Zener with a resistor?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
---

## Short answer

An integrated regulator is preferable when load current varies widely or the load draws heavy current. In a Zener circuit, the series resistor must be sized for maximum load current, meaning that at no load the entire current passes through the Zener as waste heat.[^nexperia-an90031] An IC linear regulator provides specified load regulation (up to 25 mV across 5 mA to 1.5 A for LM340A) along with internal current limiting and thermal shutdown.[^ti-lm340]

## Detailed explanation

A Zener diode with a resistor forms a shunt regulator: resistor `R1` sets the total current from the source, and the Zener diverts whatever portion the load does not draw. To keep the Zener diode in its steep breakdown region at maximum load, the resistor is selected using the formula `R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max))`.[^nexperia-an90031] If the load demands more current than `R1` delivers, no current remains for the Zener, it stops conducting, regulation is lost, and the resistor forms a voltage divider with the load.[^fiore-rectification]

Hence the limitation: `R1` is fixed while the load current varies, so the Zener current must compensate for the entire difference. At no load, the entire current through `R1` passes through the Zener, which is precisely when it dissipates the most power: `P_Z = V_Z*(V_IN - V_Z)/R1`.[^nexperia-an90031] Furthermore, the dynamic resistance of the Zener is non-zero, so the voltage varies slightly with current: `ΔV_Z = r_dif*ΔI_Z`.[^nexperia-an90031] Therefore, Nexperia describes such a basic circuit as suitable for relatively low power levels.[^nexperia-an90031]

**Example.** `V_IN = 12 V`, `V_Z = 5.1 V`, `I_Z(min) = 5 mA`, `I_LOAD(max) = 100 mA`. Then `R1 = 6.9/0.105 ≈ 65.7 Ω`. At no load, `6.9/65.7 ≈ 105 mA` flows through the Zener, dissipating `5.1*0.105 ≈ 0.54 W`, the resistor dissipates `6.9*0.105 ≈ 0.72 W`, and `12*0.105 = 1.26 W` is drawn from the source to no useful effect. A linear regulator such as the LM340A in the same mode consumes only its own quiescent current, up to 6 mA per the datasheet table, or on the order of `12*0.006 ≈ 0.07 W` (estimate).[^ti-lm340]

An integrated regulator inverts this operating mode: it draws approximately the load current plus its own quiescent current from the input, rather than a fixed worst-case current. For the LM340A, load regulation is at most 25 mV over the 5 mA to 1.5 A range, which is no worse than 0.5% of 5 V; it also includes internal current limiting and thermal shutdown.[^ti-lm340] However, this comes at a cost: voltage headroom is required (dropout is typically 2 V at 1 A), and die dissipation roughly equals `(V_IN - V_OUT)*I_LOAD`, bounded by package thermal resistance.[^ti-lm340]

**Common mistakes:**

- Sizing `R1` only for the typical current rather than the maximum: at peak load, the Zener drops out of breakdown and regulation is lost.[^fiore-rectification]
- Forgetting about Zener power dissipation when the load is disconnected: that is precisely when dissipation peaks.[^nexperia-an90031]
- Assuming an integrated linear regulator is "lossless": it dissipates the difference between input and output and requires dropout headroom.[^ti-lm340]

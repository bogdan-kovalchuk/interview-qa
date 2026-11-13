---
id: emb-elintro-0293
title: "Why is the current in a circuit with a 9 V battery, 220 Ω resistor, and LED not exactly `9/220`?"
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
  - source_id: ti-led-resistor
    title: "Texas Instruments: AN-1293 Driving RGB LED Using LP3936"
    url: https://www.ti.com/jp/lit/pdf/snva071
---

## Short answer

The LED drops a forward voltage `V_f`, leaving approximately `9 V - V_f` across the series resistor, so the circuit current equals this remaining voltage divided by 220 Ω.[^ti-led-resistor] Assuming `V_f = 2 V`, the estimated current is about 31.8 mA rather than `9/220`.

## Detailed explanation

In a series circuit, the battery, resistor, and LED share the same current, but the battery voltage divides across the components. When the LED is forward-biased, it drops a forward voltage `V_f`; the series resistor sees only the remaining difference between the supply voltage and the LED forward voltage. Therefore, the estimated circuit current is `I = (V_supply - V_f)/R`.[^ti-led-resistor]

Suppose the battery provides 9 V, the resistor is exactly 220 Ω, and `V_f` at the operating point is 2 V. The resistor drops 7 V, resulting in an estimated current of approximately 31.8 mA. This is an engineering estimate, not a guaranteed exact value: battery terminal voltage sags under load, resistor tolerance is non-zero, and `V_f` varies with LED chemistry, current, and junction temperature.[^ti-led-resistor]

A diode's current-voltage characteristic is non-linear. An LED cannot be treated as a resistor with a fixed resistance; as current changes, its forward voltage changes as well. The series resistor establishes the operating point and limits the current, while a robust design accounts for supply voltage extremes, `V_f` spread, resistor tolerance, and the maximum rated continuous current of the LED.[^ti-led-resistor]

**Common mistake:** dividing the entire 9 V by 220 Ω as if all source voltage dropped across the resistor alone. This ignores the LED forward voltage. Likewise, 2 V should not be assumed as a universal constant: the manufacturer specifies `V_f` for specific test conditions.

In the above estimate, the resistor dissipates approximately `P = 7 V * 31.8 mA ≈ 0.223 W`, leaving little safety margin for a 0.25 W resistor. Real-world power rating selection must factor in component tolerances and ambient thermal conditions.[^ti-led-resistor]

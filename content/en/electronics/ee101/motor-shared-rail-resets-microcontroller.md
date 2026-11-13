---
id: emb-elee-0260
title: "Why can a motor on a shared supply rail cause a microcontroller to hang?"
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
  - source_id: ti-motor-drive-protection
    title: "Texas Instruments Application Report SLVA636: Designing Motor Drive Circuits for High Reliability"
    url: https://www.ti.com/lit/an/slva636/slva636.pdf
  - source_id: st-mcu-noise-immunity
    title: "STMicroelectronics Application Note AN4683: Robust design for microcontroller applications"
    url: https://www.st.com/resource/en/application_note/an4683-robust-design-for-microcontroller-applications-stmicroelectronics.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

A motor is an inductive load: during rotation and commutation, it generates voltage spikes and back-EMF that kick back onto the power rail. In the course lecture, spikes on a 3.3 V rail reached 2–3 V peak-to-peak and even pulled the voltage below ground. Such transients trigger brownout resets or corrupt digital logic, which is easily mistaken for a firmware bug.[^udemy-electronics-course]

## Detailed explanation

Connecting a DC electric motor to the same power rail that supplies a microcontroller creates complex hardware problems due to the physics of inductive loads and the brush-commutator assembly[^udemy-electronics-course][^ti-motor-drive-protection].

### Physical mechanisms of interference

1. **Starting currents and voltage sags (brownout):** At startup or when the rotor is stalled, rotational back-EMF is zero. Motor current is limited only by the low ohmic resistance of the armature winding (`R_a`): inrush starting current `I_start = V / R_a` can exceed nominal operating current by 5–10 times[^ti-motor-drive-protection]. This pulsed current flows through the parasitic resistance and inductance of shared power traces (`Delta V = I * R_trace + L_trace * (di/dt)`), causing a deep, transient sag in supply voltage. If the rail voltage falls below the threshold of the microcontroller's BOR (brown-out reset) or POR (power-on reset) circuit, the internal supervisor forces a core reset or triggers an undefined register state[^st-mcu-noise-immunity].

2. **Inductive kickback and commutation spikes:** Motor windings possess self-inductance `L`. During operation, brushes alternately make and break contact with commutator segments (and in PWM control, power switches switch the current). According to Faraday's law of electromagnetic induction, abruptly interrupting current through an inductor generates a self-induced EMF:
`V_kick = -L * (di/dt)`.
Because the rate of change of current `di/dt` over nanosecond opening intervals is extraordinarily high, spike amplitudes without proper damping reach tens of volts, swinging both far above `V_CC` and well below ground potential `GND`[^ti-motor-drive-protection][^art-of-electronics].

3. **Brush arcing and high-frequency emissions (EMI):** Commutation arcing is accompanied by micro-arc discharges that radiate broadband electromagnetic noise (from hundreds of kilohertz to hundreds of megahertz). This noise couples into high-impedance microcontroller lines: crystal oscillator pins, the NRST hardware reset pin, and I2C/SPI bus signal traces[^st-mcu-noise-immunity].

### Impact on microcontroller CMOS structure

- **Carrier injection and latch-up (CMOS latch-up):** Negative voltage spikes on I/O pins or the power rail pull potential below -0.3 to -0.7 V, forward-biasing parasitically integrated p-n junctions of internal ESD protection diodes and the substrate. This injects excess minority carriers into the silicon substrate, triggering parasitic four-layer p-n-p-n thyristor structures within the CMOS chip (latch-up)[^st-mcu-noise-immunity]. The microcontroller enters a low-impedance short-circuit state between its power rails, hangs, heats up critically, and can suffer irreversible destruction.
- **Program counter corruption:** Even a microsecond voltage sag corrupts reads from Flash or SRAM cells, causing execution of invalid instructions, entry into infinite loops, or triggering a HardFault exception[^st-mcu-noise-immunity].

### Circuit mitigation techniques

To eliminate lockups, the following solutions are employed:
- **Inductive clamping:** A fast flyback diode or Schottky diode is placed directly across the motor terminals to recirculate self-induction currents during turn-off[^ti-motor-drive-protection].
- **Interference filtering:** A high-value electrolytic reservoir capacitor (100–2200 µF) is mounted across the motor supply to buffer inrush currents, along with a 0.1 µF ceramic capacitor to shunt high-frequency brush arcing[^art-of-electronics].
- **Layout and galvanic isolation:** Power rails for the power stage and logic are routed in a star topology, using separate regulators (LDO/DC-DC), decoupling ferrite beads in supply lines, or complete optical isolation of control signals[^st-mcu-noise-immunity][^art-of-electronics].

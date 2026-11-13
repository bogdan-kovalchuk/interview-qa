---
id: emb-elee-0259
title: "How does the 555 monostable mode differ from the astable mode?"
track: electronics
section: ee101
sources:
  - source_id: ti-ne555-datasheet
    title: "Texas Instruments: NE555 Precision Timers Datasheet (SLRS022)"
    url: https://www.ti.com/lit/ds/symlink/ne555.pdf
  - source_id: fiore-555-timer
    title: "Engineering LibreTexts: Operational Amplifiers and Linear Integrated Circuits (Fiore), 9.6 The 555 Timer"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/09:_Specialized_Linear_Circuits/9.6:_The_555_Timer
  - source_id: aac-555-circuits
    title: "All About Circuits: 555 Timer Circuits"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-8/555-timer-circuits/
---

## Short answer

Monostable mode (one-shot) has a single stable quiescent state with OUT LOW: an external negative-going trigger at TRIG produces exactly one pulse of duration `t_pulse ≈ 1.1 * R * C` before the circuit returns to rest. Astable mode (multivibrator) has no stable state, continuously free-running and generating an unending periodic pulse train through automatic self-triggering.[^ti-ne555-datasheet]

## Detailed explanation

### Number of stable states and mode of operation

The fundamental distinction between the modes lies in feedback topology and the number of stable equilibrium states of the circuit:[^ti-ne555-datasheet]
- Monostable mode (one-shot or waiting multivibrator) has one stable quiescent state (output LOW, capacitor discharged to zero) and one quasi-stable state (output HIGH during pulse generation). The circuit continuously awaits an external trigger pulse.[^fiore-555-timer]
- Astable mode (free-running multivibrator) has no stable equilibrium state. The circuit has two mutually quasi-stable states and undergoes continuous free-running oscillations between levels `(1/3)*V_CC` and `(2/3)*V_CC` without any external synchronization signal.[^aac-555-circuits]

### Circuit differences in pin connections

The circuit configuration of the 555 timer differs significantly between these two modes:[^ti-ne555-datasheet]

1. In monostable mode:
   - The trigger input TRIG (pin 2) is pulled up via an external resistor to `V_CC` and connected to an external trigger source.
   - The threshold input THRES (pin 6) and discharge terminal DISCH (pin 7) are tied together into a single node.
   - Only a single timing resistor `R` (between `V_CC` and tied pins 6 and 7) and one capacitor `C` (between pins 6, 7 and ground GND) are used.
2. In astable mode:
   - The trigger input TRIG (pin 2) is tied to the threshold input THRES (pin 6) directly at the terminal of capacitor `C`. This connection enables automatic re-triggering of the circuit when the voltage drops to 1/3 `V_CC`.
   - The discharge terminal DISCH (pin 7) connects to the midpoint between the two resistors `R_A` and `R_B`.

### Physical mechanism of monostable pulse generation

Operation of the monostable one-shot proceeds through the following stages:[^fiore-555-timer]
1. Quiescent state: voltage on the TRIG input is HIGH (above `(1/3)*V_CC`). The internal RS flip-flop is in the RESET state, the output (pin 3) is held LOW, and the internal NPN discharge transistor is saturated, holding capacitor `C` grounded (`v_C ≈ 0 V`).
2. Triggering: a brief negative-going pulse with a voltage below `(1/3)*V_CC` is applied to the TRIG input. The lower comparator trips, placing the RS flip-flop into the SET state. The output (pin 3) goes HIGH, and the discharge transistor turns off.
3. Pulse duration timing: capacitor `C` begins charging exponentially from zero toward the `V_CC` supply rail through resistor `R`:[^aac-555-circuits]
   `v_C(t) = V_CC * (1 - exp(-t / (R * C)))`
4. Pulse completion: when the capacitor voltage reaches threshold `(2/3)*V_CC`, the upper comparator (THRES input) trips, returning the RS flip-flop to the RESET state. The output immediately returns to the LOW state, and the discharge transistor turns on, rapidly discharging capacitor `C` back to zero.

The output pulse duration `t_pulse` is derived from the condition of reaching threshold `(2/3)*V_CC`:[^ti-ne555-datasheet]
`(2/3)*V_CC = V_CC * (1 - exp(-t_pulse / (R * C)))`
`1/3 = exp(-t_pulse / (R * C))`
`exp(t_pulse / (R * C)) = 3`
`t_pulse = ln(3) * R * C ≈ 1.0986 * R * C ≈ 1.1 * R * C`

Unlike astable mode (where the factor is `ln(2) ≈ 0.693`), in monostable mode the factor is `ln(3) ≈ 1.1` because charging starts from `0 V` rather than `(1/3)*V_CC`.

### Important engineering constraints and typical applications

- Trigger pulse duration: the input trigger pulse on pin TRIG must return to the HIGH level before output interval `t_pulse` expires.[^ti-ne555-datasheet] If the TRIG input remains below `(1/3)*V_CC`, the lower comparator will continue to hold the RS flip-flop in the SET state, and the output will remain HIGH even after the capacitor charges above 2/3 `V_CC`. To prevent this issue, a differentiating RC network (series capacitor and pull-up resistor to `V_CC`) is installed at the TRIG input, producing narrow spikes only on the transitions of the input edge.
- Pulse interruption (RESET): in monostable mode, pulse generation can be aborted at any moment by asserting a LOW level on the reset input RESET (pin 4), which immediately drives the output LOW and discharges the capacitor.
- Typical applications:
  - Monostable mode: hardware pushbutton debouncing, power-on delay generation, pulse stretching, missing pulse detectors.
  - Astable mode: clock pulse generators for digital counters, PWM modulators, strobe flashers, audio tone generators (buzzers).

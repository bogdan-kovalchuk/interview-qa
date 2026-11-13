---
id: emb-elcirc-0003
title: "How do you find a resistor value given the desired current and the source voltage?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-ohms-law
    title: "All About Circuits: Ohm's Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
  - source_id: aac-resistor-power
    title: "All About Circuits: Resistors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
---

## Short answer

For an ideal resistor connected directly across a source, the resistance is given by `R = V/I`.[^aac-ohms-law] Given `V = 10.5 V` and `I = 25 mA`, `R = 420 Ω`, and the dissipated power is `P = V*I = 0.2625 W`; choose a resistor power rating with adequate margin for operating temperature and cooling.[^aac-resistor-power]

## Detailed explanation

To find resistance, apply Ohm's law: for a resistor, `R = V/I`, where `V` is the voltage dropped across the resistor itself and `I` is the current flowing through it. If the resistor is connected directly across an ideal source, the voltage across it equals the source voltage. In a circuit containing an LED, lamp, or other series load, subtract that component's forward drop: the resistor does not receive the entire supply voltage.[^aac-ohms-law]

Before calculating, convert all quantities to consistent SI units. Milliamperes must be converted to amperes, and resistance is typically expressed in ohms or kilohms. For example, for a single resistor connected across a 10.5 V source requiring 25 mA, the calculation proceeds as follows:

```text
I = 25 mA = 0.025 A
R = 10.5 V / 0.025 A = 420 Ω
P = 10.5 V * 0.025 A = 0.2625 W
```

Thus, the ideal resistance value is 420 Ω. In a physical circuit, check standard preferred values, resistor tolerance, and variations in supply voltage: selecting the nearest standard value yields a current slightly above or below the target value. For an LED circuit, the numerator becomes `V_supply - V_f` rather than the raw supply voltage.[^aac-ohms-law]

Power dissipation does not determine the required resistance value, but it dictates whether the component can withstand the resulting heat. After determining the current, calculate `P = V*I` or `P = I²*R` using the voltage drop across the resistor. A resistor power rating represents the maximum allowable dissipation under the specific conditions defined by the manufacturer; elevated ambient temperatures, poor airflow, and sustained operation near limits necessitate derating margins verified against component documentation.[^aac-resistor-power]

**Common mistakes:**

- Plugging 25 into the formula instead of 0.025, yielding a resistance value one thousand times too small.
- Using the full source voltage when part of it drops across a series load.
- Selecting a resistor solely by its resistance value without checking power dissipation and thermal operating conditions.

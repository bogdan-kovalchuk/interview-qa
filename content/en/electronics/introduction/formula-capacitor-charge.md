---
id: emb-elintro-0129
title: "What is the formula for a capacitor's charge?"
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
  - source_id: aac-capacitance-charge
    title: "All About Circuits: Electric Fields and Capacitance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/electric-fields-capacitance/
---

## Short answer

For a linear capacitor, charge is related to capacitance and voltage by the formula `Q = C*V`, where Q is measured in coulombs, C in farads, and V in volts.[^aac-capacitance-charge] For example, 1000 µF at 12 V corresponds to `0.001*12 = 0.012 C`.[^aac-capacitance-charge] A real disconnected capacitor can hold charge for some time, but eventually discharges through internal leakage or a connected load.[^aac-capacitance-charge]

## Detailed explanation

A capacitor's charge is the separation of electric charges on its plates, associated with the voltage between them. For a linear capacitance, their magnitude is proportional to voltage: `Q = C*V`. In this expression, `Q` is charge in coulombs, `C` is capacitance in farads, and `V` is voltage in volts; one farad means one coulomb of charge per one volt.[^aac-capacitance-charge]

You apply the formula when both the component's capacitance and the voltage directly across its terminals are known. Convert units before substitution: a microfarad equals `10^-6 F`. For example, for 1000 µF, that is 0.001 F, at a voltage of 12 V you get 0.012 C. This is a calculation of stored charge at a given voltage, not an estimate of energy: energy in a capacitor is determined separately and depends quadratically on voltage.[^aac-capacitance-charge]

Worked example:

```text
C = 1000 µF = 0.001 F
Q = C*V = 0.001 F*12 V = 0.012 C
```

After disconnecting the source, the charge does not have to disappear instantly. An ideal model without a current path would maintain voltage, but a practical capacitor has leakage, and an external resistor or other load drains the charge. The discharge rate depends on the components and circuit, so before touching or measuring, you must check the voltage rather than assuming that a disconnected component is already safe.[^aac-capacitance-charge]

**Common mistakes:**

- Substituting 1000 µF as the number 1000 without converting it to 0.001 F.
- Confusing charge in coulombs with energy in joules.
- Assuming that charge after disconnection is retained forever or disappears immediately.[^aac-capacitance-charge]

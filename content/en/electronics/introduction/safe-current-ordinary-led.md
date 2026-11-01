---
id: emb-elintro-0118
title: "What is a safe current for an ordinary `LED`?"
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
  - source_id: aac-led-current
    title: "All About Circuits: Special-purpose Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
---

## Short answer

For a standard through-hole `LED`, a current of around `20 mA` is a common guideline, but the safe value is determined by the specific part's datasheet.[^aac-led-current] When powering from a voltage source higher than the forward voltage of the `LED`, a series resistor or other current limiter is required; without it, the current can exceed the allowable limit.[^aac-led-current]

## Detailed explanation

A safe `LED` current is a current that does not exceed the limit specified by the manufacturer for the specific part and cooling conditions; for many standard through-hole indicator models, a guideline is around `20 mA`.[^aac-led-current]

An `LED` is a semiconductor diode with a non-linear current-voltage characteristic. After reaching the forward voltage, a small change in applied voltage can cause a significant change in current. Therefore, you cannot assume that the diode will limit the current to a safe level on its own: in a simple DC voltage circuit, a resistor is added in series to take up the difference between the source voltage and the diode's forward voltage.[^aac-led-current]

The figure `20 mA` is not a universal guarantee and not a required target. The datasheet specifies the maximum continuous current, measurement conditions, temperature derating, and often a lower recommended operating condition. Heating is affected by the package, PCB copper area, ambient temperature, and pulse duration. For pulsed mode, you cannot automatically use the peak current as continuous: in the datasheet, the peak value is tied to pulse duration and duty cycle.[^aac-led-current]

**Estimation example:** if the source is `5 V` and the forward drop across the chosen red `LED` is close to `2 V`, the resistor must absorb approximately `3 V`. For a desired `10 mA`, the initial calculation gives `R = (5 - 2)/0.010 = 300 Ω`; then a standard value is selected and the current is verified at the minimum forward drop and maximum supply voltage. The `V_f` value depends on current and temperature, so calculating with a single typical number is only an approximation.[^aac-led-current]

**Common mistakes:**

- Treating `30 mA` as the same dangerous limit for all LEDs. Permissible current depends on the component, temperature, and operating mode.
- Assuming that a resistor is always needed specifically for `20 mA`. A lower current may be sufficient and leaves a larger margin for temperature and lifespan.
- Confusing the maximum rating with the recommended operating mode. For a reliable circuit, check the absolute maximum ratings table, operating conditions, and the manufacturer's derating curves.[^aac-led-current]

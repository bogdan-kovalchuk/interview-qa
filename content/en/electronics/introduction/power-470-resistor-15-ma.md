---
id: emb-elintro-0094
title: "What is the power in a 470 Ω resistor at 15 mA?"
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
  - source_id: aac-resistor-power-dissipation
    title: "All About Circuits: Intro Lab - Resistor Power Dissipation"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-2/power-dissipation/
---

## Short answer

Under the resistive model, `P = I^2*R = (0.015 A)^2*470 ohm = 0.10575 W`, or approximately `0.106 W`. The resistor power rating must exceed this value, taking into account temperature, mounting, and derating conditions; 0.25 W is a common minimum rating under suitable conditions, while 0.5 W provides a larger margin.[^aac-resistor-power-dissipation]

## Detailed explanation

When the current through a resistor is known, its dissipated power can be calculated from Joule's law `P = I^2*R`. The formula derives from `P = V*I` and Ohm's law `V = I*R`, so it assumes a resistive element with corresponding values of voltage, current, and resistance. For a constant resistance, doubling the current quadruples the power, so an error in current has an especially strong impact on the result.[^aac-resistor-power-dissipation]

In this example, 15 mA must be converted to amperes: `0.015 A`. Thus, `P = (0.015 A)^2*470 ohm = 0.10575 W`, or approximately 106 mW. For an ideal resistor, this is electrical power converted predominantly into heat. Such a calculation does not account for resistor tolerance, temperature-dependent resistance variation, or pulsed operating conditions.[^aac-resistor-power-dissipation]

The rated power specified on the package is the permissible dissipation under conditions defined by the manufacturer, not the power that the resistor necessarily draws. Therefore, a 0.25 W rating exceeds the calculated 0.106 W, provided that datasheet temperature and mounting constraints are satisfied. In hot environments, enclosed cases, or with limited airflow, the manufacturer may require derating the permissible load; choosing 0.5 W adds margin, but on its own does not replace verifying operating conditions.[^aac-resistor-power-dissipation]

**Common mistakes:**
- Substituting `15` instead of `0.015` amperes: the resulting power will be overstated by a factor of one million.
- Assuming that 0.25 W is guaranteed to be safe in any enclosure and at any temperature; check the derating curve and thermal operating conditions of the specific component.[^aac-resistor-power-dissipation]

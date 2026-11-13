---
id: emb-elee-0227
title: "How should current be measured with an ammeter, and why is any other connection dangerous?"
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
  - source_id: kuphaldt-ammeter-usage
    title: "Workforce LibreTexts: Electric Circuits VI – Experiments (Kuphaldt), 2.4 How to Use an Ammeter to Measure Current"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_VI_-_Experiments_(Kuphaldt)/02%3A_Basic_Concepts_and_Test_Equipment/2.04%3A_How_to_Use_an_Ammeter_to_Measure_Current
  - source_id: fiore-source-conversions
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 6.2 Source Conversions"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/06:_Analysis_Theorems_and_Techniques/6.2:_Source_Conversions
  - source_id: fiore-ohms-law
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 3.5 Ohm's Law"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/03:_Series_Resistive_Circuits/3.05:_Ohm's_Law
---

## Short answer

An ammeter is connected in series with the component whose current is being measured: it has near-zero internal resistance and barely alters the circuit current.[^kuphaldt-ammeter-usage] Connecting it in parallel across a voltage source causes a near short circuit where current is limited only by the shorted path resistance `E/R` (where `R` is the internal source resistance plus meter resistance), blowing the meter's internal fuse.[^kuphaldt-ammeter-usage][^fiore-source-conversions] Current can also be determined from the voltage drop across a known resistor, `I = V/R`.[^fiore-ohms-law]

## Detailed explanation

An ammeter measures current by passing it through itself, so it is connected into a break in the conductor: in series with the load or resistor through which the current flows.[^kuphaldt-ammeter-usage] An ideal ammeter produces no voltage drop, so it barely alters the circuit current. The measurement is performed by breaking the circuit at the desired point and inserting the instrument into this break.

For illustration, assume an ideal 9 V source (having zero internal resistance), a 1 kΩ load, and an ammeter resistance of 0.1 Ω on that current range (a nominal example value, not a datasheet spec). In a series circuit, `I = 9 / (1000 + 0.1) ≈ 9.0 mA`, meaning the instrument barely alters the current. If, however, the ammeter is placed in parallel across the source, the path from the source goes solely through the meter, and `I = E / R = 9 / 0.1 = 90 A`, which is approximately 10,000 times higher. Here, the current is determined by the meter resistance because the source internal resistance is zero; in the general case, the current is limited only by the resistance of the shorted path.[^fiore-source-conversions]

Why this is dangerous: 90 A vastly exceeds the current rating the meter is designed to measure, so the surge can damage it. The internal fuse blows, and the instrument cannot measure current until the fuse is replaced.[^kuphaldt-ammeter-usage] For handheld meters, it is recommended to start at the highest current range and step down to lower ranges until the reading is strongest without overload.[^kuphaldt-ammeter-usage]

**Common mistakes:**

- Connecting an ammeter in parallel across a source or component, like a voltmeter.
- Touching probes across conductors instead of breaking the circuit and inserting the meter into the break.
- Selecting too low a current range instead of starting from the highest.

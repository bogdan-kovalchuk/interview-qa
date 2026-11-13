---
id: emb-elee-0202
title: "What output voltage does a series regulator with a 5.6 V Zener on an emitter follower's base give?"
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
  - source_id: fiore-zener-follower
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.7 BJT Switching and Driver Applications"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.7:_BJT_Switching_and_Driver_Applications
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
---

## Short answer

The output is taken from the emitter: `V_out ≈ V_Z - V_BE ≈ 5.6 - 0.7 = 4.9 V`, where `V_BE` varies with load current and operating temperature.[^fiore-zener-follower][^fiore-bjt-ac-model] Resistor bias current must exceed the minimum Zener knee current plus peak base current `I_B` to keep the diode in steep breakdown regulation.[^nexperia-an90031]

## Detailed explanation

The Zener diode is connected in reverse bias between base and ground, while the input voltage is fed to the base through resistor `R`. The Zener clamps the base voltage at `V_Z` = 5.6 V, so the emitter, and with it the output, sits at `V_Z` − `V_BE` ≈ 4.9 V. This is how the textbook describes a Zener follower: the Zener diode establishes the output voltage, while the load current is supplied through the transistor.[^fiore-zener-follower]

For silicon, `V_BE` is typically 0.7 V, making 4.9 V the nominal value.[^fiore-bjt-basics] However, `V_BE` is not constant: according to the exponential model, it increases by approximately 26 mV when the emitter current increases by a factor of e. If the load current increases from 1 mA to 10 mA (a tenfold increase), `V_BE` rises by approximately 25.9 mV × ln 10 ≈ 60 mV, and the output drops by approximately 60 mV.[^fiore-bjt-ac-model]

The current through `R` equals `I_Z` + `I_B`, where `I_B` = `I_E` / (β + 1), since `I_E` = (β + 1) × `I_B`.[^fiore-bjt-basics] Suppose `V_in` = 9 V, load current is up to 10 mA, β = 100, and the Zener diode requires 5 mA; datasheets typically specify `V_Z` near this current level.[^nexperia-an90031] Then `I_B` ≈ 10 mA / 101 ≈ 0.1 mA, and `R` ≤ (9 − 5.6) V / (5 + 0.1) mA ≈ 3.4 V / 5.1 mA ≈ 667 Ω. If a larger `R` is selected, at maximum load current the Zener diode will receive less than the minimum required for the steep breakdown region, degrading regulation.[^nexperia-an90031]

Circuit limitations. The temperature coefficient of the Zener diode depends on the operating current, and for lower voltages this effect is significant, so 4.9 V is a nominal value for the given current and temperature, not a universal guarantee.[^nexperia-an90031] The load is powered through the collector, whereas only `I_B` flows through `R`: if `I_E` exceeds ≈ (β + 1) × (`I_R` − `I_Z,min`), where `I_R` is the current through resistor `R`, the Zener diode will lose its minimum knee current and `V_out` will drop.[^fiore-zener-follower][^fiore-bjt-basics] There is no current limiting, so an output short circuit can overheat the transistor.

**Common mistakes:**
- Assuming the output equals `V_Z` = 5.6 V without subtracting `V_BE`.
- Assuming the output is independent of load: `V_BE` increases with current.
- Checking `R` only at no-load: at maximum load, the Zener diode receives the least current.

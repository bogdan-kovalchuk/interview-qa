---
id: emb-elee-0130
title: "How do you estimate the ripple after a bridge rectifier with a capacitor?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
---

## Short answer

For small ripple, `ΔV_pp ≈ I_load/(f_ripple*C)`: between peaks the capacitor supplies the load current for approximately one ripple period.[^fiore-capacitors] After a bridge rectifier, `f_ripple = 2*f_mains`, or 100 Hz for a 50 Hz line, so at 20 mA and 1000 µF, `ΔV_pp ≈ 0.02/(100*0.001) = 0.2 V`. This approximation assumes constant current and neglects capacitor ESR. To reduce ripple at the same load current, C is increased, though diodes then conduct in shorter, higher-current pulses.[^fiore-rectification]

## Detailed explanation

TODO

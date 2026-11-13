---
id: emb-elee-0015
title: "How do you turn a potentiometer into a rheostat?"
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
  - source_id: aac-potentiometer-rheostat
    title: "All About Circuits: DC Lab - Potentiometer as a Rheostat"
    url: https://www.allaboutcircuits.com/TEXTBOOK/experiments/chpt-3/potentiometer-rheostat/
---

## Short answer

Connect the wiper to one outer terminal, and place the external circuit between this joined connection and the remaining outer terminal: the potentiometer then operates as a two-terminal variable resistor. Its resistance varies roughly from zero to `R_total`, allowing current adjustment in a series circuit; actual limits depend on contact resistance and component construction.[^aac-potentiometer-rheostat]

## Detailed explanation

A potentiometer has a resistive track between two outer terminals and a movable contact – the wiper. When an external circuit is connected between the wiper and one outer terminal, current flows through only a portion of the track. Moving the wiper changes the length of this portion and thus its resistance; the terminal on the opposite end can be left unconnected. Using the opposite outer terminal provides the reverse direction of resistance change for the same knob rotation.[^aac-potentiometer-rheostat]

In an idealized model, resistance is nearly zero near the chosen end and approaches the full track resistance at the opposite end. This does not mean the component can safely handle any current: its power rating, maximum current limit, cooling, and voltage rating are critical. For higher-current loads, even a low track resistance can dissipate significant power; calculate `P = I²*R` and verify the result against the specific component datasheet.[^aac-potentiometer-rheostat]

Example: if the track is 10 kΩ and the wiper position leaves approximately 25% of its length to the selected end, the resistance between these terminals is roughly 2.5 kΩ for a uniform track. This is an estimate of position rather than a calibrated exact law: tolerances and track taper can be linear or logarithmic. A rheostat is typically connected in series to adjust current or voltage drop across a load; by itself, it does not regulate or stabilize current.[^aac-potentiometer-rheostat]

**Common mistake:** using the two outer terminals without the wiper and expecting variable resistance. Between the outer terminals, the track resistance remains constant regardless of knob position. In circuits where an intermittent open circuit at the wiper contact would be hazardous, the unused outer terminal can be tied to the wiper: if the wiper contact momentarily loses connection, a conduction path through the full track remains. This protects against a single failure mode rather than substituting for component reliability verification.[^aac-potentiometer-rheostat]

---
id: emb-elintro-0226
title: "How does an LED in the emitter branch differ from an LED in the collector branch?"
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
---

## Short answer

In a collector circuit, the NPN controls the LED current as a low-side switch; an LED in the emitter branch operates as an emitter follower, where the emitter voltage depends on the base and the load current. In both cases, a series resistor is required to limit the LED current.[^aac-semiconductors]

## Detailed explanation

An LED in the collector branch is connected in series with a current-limiting resistor between the supply and the collector of the NPN; the emitter is grounded, and the base is driven through a resistor. When the transistor enters saturation, it pulls the collector to a low voltage, and almost the full supply voltage appears across the LED and resistor, turning the LED on. When the transistor is off, collector current is negligible and the LED goes out. This is a low-side switch, not a guarantee of an ideal zero: a saturated transistor has a non-zero voltage `V_CE(sat)`.[^aac-semiconductors]

If the LED and resistor are placed in the emitter branch, emitter current flows through the load, and the emitter voltage follows the base voltage, remaining approximately `V_BE` below it. This is an emitter follower: the output is not pulled to ground, and controlling the load depends on the base signal, current, and transistor characteristics. Light output in this circuit also depends on LED polarity, forward voltage, and the presence of current limiting; the branch name alone does not define an "on" state.[^aac-semiconductors]

Example: if an unloaded emitter node sits at about `0.7 V`, an LED with a forward voltage above this value might conduct almost no current even when the base is actively driven. In a collector circuit, current is determined by the supply voltage, LED forward voltage, resistor, and `V_CE(sat)`. A common mistake is connecting the LED without a series resistor or explaining the difference merely as logic inversion without specifying circuit topology and polarity.[^aac-semiconductors]

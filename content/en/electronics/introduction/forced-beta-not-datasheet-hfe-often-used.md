---
id: emb-elintro-0208
title: "Why is forced beta, not the datasheet hFE, often used for a BJT switch?"
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
  - source_id: bjt-switch
    title: "TI application report: Maximum Output Power and Thermal Considerations for UCC28720 and UCC28722"
    url: https://www.ti.com/lit/an/slua858/slua858.pdf
---

## Short answer

For a switch, datasheet `hFE` should not be interpreted directly as guaranteed gain in saturation: manufacturers specify saturation conditions separately.[^bjt-switch] `Forced beta = I_C/I_B` is chosen to calculate sufficient base current; a value like 10 is only a design example, not a universal standard.[^bjt-switch]

## Detailed explanation

`Forced beta` is a designer-selected ratio of collector current to base current, deliberately lower than the minimum active `hFE`, to keep the BJT operating in saturation as a switch.[^bjt-switch]

Datasheet `hFE` is measured under specified conditions, typically in the forward-active region. It varies with part-to-part variation, current, voltage, and temperature, and the specification itself does not promise that the linear relationship `I_C = hFE*I_B` is maintained after entering saturation. In saturation, both transistor junctions are forward-biased, and additional base current primarily reduces `V_CE` rather than increasing collector current proportionally.[^bjt-switch]

For a switch, you first estimate the maximum required load current, then choose a conservative forced beta according to the transistor requirements or specific circuit practice. There is no universal value of `10`: the manufacturer specifies saturation conditions for a specific part number. After that, you find the required base current and resistor, taking into account the control voltage and the base-emitter drop; you also verify that the control output can supply this current.[^bjt-switch]

An example for illustration, not a component specification: for a load `I_C = 50 mA` and a chosen `beta_forced = 10`, you need at least `I_B = I_C/beta_forced = 5 mA`. This does not prove that any transistor will saturate at 5 mA: you must verify the guaranteed `V_CE(sat)` and test conditions in its datasheet.[^bjt-switch]

**Common mistake:** substituting typical `hFE` from a chart and expecting the switch to be guaranteed to saturate. Calculate the base current for the given load and verify saturation using the manufacturer table.

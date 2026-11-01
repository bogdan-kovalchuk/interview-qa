---
id: emb-elintro-0202
title: "What is the condition for the active mode of an `NPN` transistor?"
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
  - source_id: aac-bjt-junctions
    title: "Bipolar Junction Transistors, All About Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bipolar-junction-transistors/
---
## Short answer

For an NPN in the forward-active mode, the base–emitter junction is forward-biased and the base–collector junction is reverse-biased; in a conventional circuit, this corresponds to `V_C > V_B > V_E`. For a silicon transistor, `V_BE` is often around 0.6–0.7 V, but this is not a constant, universal voltage.[^aac-bjt-junctions]

## Detailed explanation

The forward-active mode of an NPN transistor means that the base–emitter junction is forward-biased and the base–collector junction is reverse-biased. If node voltages are defined relative to a common reference, the typical order is `V_C > V_B > V_E`; what matters is the bias of each junction, not the absolute voltage with respect to ground.[^aac-bjt-junctions]

Forward-biasing the emitter junction injects electrons from the N-type emitter into the thin P-type base. A small fraction of carriers recombines in the base, forming the base current; the majority reaches the depletion region of the collector junction and is swept into the collector by the electric field. Therefore, a small base signal can control a significantly larger collector current. In a simplified circuit model, this is written as `I_C ≈ β*I_B`, but β is not an exact constant and varies depending on the individual device and operating conditions.[^aac-bjt-junctions]

For a silicon transistor, `V_BE` often has a value on the order of 0.6–0.7 V in typical operating regimes, but its actual value depends on current, temperature, and the specific device model. Therefore, the active mode is not determined by checking for "exactly 0.7 V": you must also ensure that the collector junction has not become forward-biased. If it becomes forward-biased, the transistor enters saturation, and the linear amplification model ceases to describe the current.[^aac-bjt-junctions]

**Verification example:** if the emitter is connected to 0 V, the base to approximately 0.65 V, and the collector is held at 3 V, both inequalities hold and the polarities correspond to forward-active mode. This is merely a consistency check; actual voltages depend on the bias circuit and the load.[^aac-bjt-junctions]

**Common mistake:** assuming 0.7 V is a sufficient condition regardless of the collector voltage. Verify both junctions relative to their terminals and keep in mind that the boundary condition depends on the circuit and transistor characteristics.

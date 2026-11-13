---
id: emb-elintro-0233
title: "How do you parallel BJTs for more current, and what is the risk?"
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
  - source_id: aac-bjt-basics
    title: "All About Circuits: Introduction to Bipolar Junction Transistors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bipolar-junction-transistors-bjt/
---

## Short answer

BJTs can be connected in parallel to increase total current, but current does not necessarily split equally: parameter spread can cause one transistor to carry excessive load. Dedicated emitter ballast resistors provide local negative feedback to help balance currents; matched thermal mounting and adequate heat sinking are also required.[^aac-bjt-basics]

## Detailed explanation

A BJT is a transistor in which base current controls a larger collector current. When several discrete BJTs are paralleled, the same voltage is applied across them, but their `V_BE`, current gains, and junction temperatures will not be perfectly identical. Therefore, a shared base voltage does not guarantee equal current sharing: a transistor that turns on at a slightly lower base–emitter voltage can hog a disproportionate share of the load current.[^aac-bjt-basics]

This creates a risk of localized overheating and overloading a single device well before reaching the aggregate current that appears acceptable from individual component ratings. For a power BJT, temperature also shifts its operating point; an unmanaged current-sharing design can experience thermal runaway. Paralleling collectors and emitters alone provides no balancing mechanism.[^aac-bjt-basics]

A practical way to introduce negative feedback is to place a dedicated small ballast resistor in series with the emitter of each transistor. If one branch begins conducting more current, the increased voltage drop across its emitter resistor reduces the effective base–emitter drive of that branch. This helps counteract the initial imbalance. These resistors dissipate power and reduce voltage available to the load, so their resistance and wattage must be calculated for the operating current; separate base resistors can decouple driver branches, but do not replace emitter ballasting.[^aac-bjt-basics]

**Common mistake:** assuming that identical part markings guarantee identical current sharing. In a real design, verify current and power margins, operating temperature, thermal coupling, safe operating area (SOA), and behavior if one branch fails. When high currents are required, a dedicated power switch or power module is often simpler to design than paralleling multiple discrete BJTs.

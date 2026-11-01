---
id: emb-elintro-0059
title: "How do voltage and capacity change when batteries are connected in parallel?"
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
  - source_id: iata-lithium-guidance-2023
    title: "IATA Lithium Battery Guidance Document 2023"
    url: https://data.energizer.com/wp-content/uploads/2023/04/IATA-Lithium-Guidance-2023.pdf
---

## Short answer

In a parallel connection of identical cells, the voltage remains the same, while the capacities in Ah add up. The connection must be designed for compatible cells: a simple parallel connection does not guarantee equal current sharing or safe charging.[^iata-lithium-guidance-2023]

## Detailed explanation

In a parallel connection, terminals of like polarity are connected together. All branches share a common terminal voltage, so the nominal voltage of the combination matches the voltage of a single cell. Charge capacities in Ah add up: two identical 2 Ah cells form nominally 4 Ah at the same voltage.[^iata-lithium-guidance-2023]

Total capacity does not mean that each cell is guaranteed to deliver an equal share of current. The distribution depends on internal resistances, temperature, connections, condition, and cell characteristics. A finished battery manufacturer may use matched cells, protection, and monitoring; a parallel connection by itself is neither a charging circuit nor a battery management system.[^iata-lithium-guidance-2023]

The calculation adds Ah only for cells that can be safely operated together and share a common nominal voltage and compatible operating limits. For example, one cannot conclude that a combination is suitable solely from an identical physical form factor. Rated capacity is measured under specified load and cutoff voltage conditions, so the actual available capacity depends on the operating mode.[^iata-lithium-guidance-2023]

**Common mistake:** assuming that parallel cells will automatically share current equally. Check manufacturer requirements for configuration, compatibility, and protection.

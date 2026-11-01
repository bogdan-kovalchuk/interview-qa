---
id: emb-elintro-0058
title: "How do voltage and capacity change when batteries are connected in series?"
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

In a series string, cell voltages add up, while capacity in Ah does not increase for identical cells. For example, four 1.5 V cells provide nominally 6 V; actual performance parameters depend on the cells and the load.[^iata-lithium-guidance-2023]

## Detailed explanation

In a series connection, the positive terminal of one cell is connected to the negative terminal of the next. The cell voltages add up because the voltage between the outer terminals is the sum of the potential differences across each cell. For four identical cells with a rating of 1.5 V, the nominal voltage of the battery string equals 6 V.[^iata-lithium-guidance-2023]

The same current flows through all cells connected in series. Therefore, the string is limited by the cell that reaches the end-of-discharge state first; adding cells does not increase Ah the way parallel connection does. For identical cells, the nominal capacity in Ah remains the capacity of a single cell, while the total nominal voltage increases.[^iata-lithium-guidance-2023]

Because energy is roughly equal to the product of charge and voltage, adding series cells increases the battery's Wh, even though Ah does not change. This explains why higher voltage does not mean greater capacity in Ah. Real batteries also have internal losses, and datasheet ratings are specified for particular test conditions; nominal numbers should not be viewed as fixed under any load.[^iata-lithium-guidance-2023]

**Common mistake:** stating that a series connection increases capacity in mAh. It increases voltage and total energy; capacity in Ah for identical cells remains constant.

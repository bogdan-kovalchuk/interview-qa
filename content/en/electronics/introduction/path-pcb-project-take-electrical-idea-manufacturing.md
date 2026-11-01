---
id: emb-elintro-0309
title: "What path does a PCB project take from an electrical idea to a manufacturing order?"
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
  - source_id: sparkfun-eagle-board-layout
    title: "SparkFun Learn: Using EAGLE – Board Layout"
    url: https://learn.sparkfun.com/tutorials/using-eagle-board-layout/all
  - source_id: altium-drc
    title: "Altium Designer Documentation: Design Rule Check"
    url: https://www.altium.com/documentation/altium-designer/pcb/drc
---

## Short answer

The typical path is: define requirements and draw the schematic, transfer components to the PCB, place and route them with traces, run checks, generate manufacturing files, and send them to the fab. The specific set of output files depends on the manufacturer.[^sparkfun-eagle-board-layout] A DRC check looks for violations of configured design rules, but in itself does not prove functional correctness of the device.[^altium-drc]

## Detailed explanation

Moving from an electrical idea to ordering a PCB begins with requirements: what the device must do, what power sources and signals it uses, and what mechanical environment it will operate in. Next, one draws the schematic with components and their electrical connections. The schematic is a logical description of the circuit; it does not yet define the exact placement of components on the board.

In PCB CAD, components receive footprints, that is, physical land patterns, and are transferred to the board workspace. After defining the board shape and layers, they are placed while considering connectors, assembly access, thermal, and electrical requirements. Traces connect the necessary pins according to the netlist. In an EAGLE example, after layout and routing, Gerber files for individual layers and drill data are prepared and sent to the fab; the exact format and file set must be verified against the requirements of the chosen manufacturer.[^sparkfun-eagle-board-layout]

Before releasing files, one checks whether the schematic and board are synchronized, whether there are unrouted pins or short circuits, and whether clearances, trace widths, and manufacturing constraints are satisfied. DRC automates the verification of configured rules and flags violations, but does not replace schematic review, engineering judgment, or prototype testing.[^altium-drc]

**Example:**

For an LED board, one first defines the power supply, LED, and current-limiting resistor on the schematic. In PCB CAD, one selects footprints, places the LED so it is visible from the enclosure, and makes the connector accessible from the outside; then routes connections and verifies design rules. After inspecting the manufacturing layers, files are exported in the format required by the fab and uploaded to its order system.

**Common mistakes:**

- Assuming that a schematic automatically produces a finished board: it defines electrical connectivity, while layout and routing require separate effort.
- Treating a passing DRC as proof of correct circuit operation: it only verifies the configured design rules.
- Sending only the CAD project file to the fab without checking which Gerber, drill, stackup, or other data that specific fab requires.[^sparkfun-eagle-board-layout]

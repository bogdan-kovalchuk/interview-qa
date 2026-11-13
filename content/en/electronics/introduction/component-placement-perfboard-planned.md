---
id: emb-elintro-0299
title: "How should component placement on a perfboard be planned?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: adafruit-perfboard
    title: "Adafruit: Collin's Lab, Breadboards & Perfboards"
    url: https://learn.adafruit.com/collins-lab-breadboards-and-perfboards?view=all
  - source_id: mit-perfboard
    title: "MIT OpenCourseWare: 8.01x Physics I, Low Voltage Power Supply Lab"
    url: https://mitocw.ups.edu.ec/courses/physics/8-01x-physics-i-classical-mechanics-with-an-experimental-focus-fall-2002/labs/801x.pdf
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Plan component placement and routing paths in advance, noting LED polarity and dedicated locations for connectors, switches, and resistors. Leave adequate space for jumpers and inspection; the physical perfboard layout must accurately reflect the schematic topology.[^mit-perfboard]

## Detailed explanation

Component placement on a perfboard should be planned before soldering because the grid holes do not automatically determine the electrical connections: many nodes must be linked using separate jumper wires or component leads. First, transfer the schematic into a top-side and copper-pad-side sketch, noting polarities, power rails, ground, and jumper locations. Such a plan helps identify trace crossings and clearance constraints before components are soldered into place.[^adafruit-perfboard]

Position connectors and controls where they remain physically accessible, and orient polarized components so their markings can be inspected. Leave adequate clearance for component widths, package heights, hookup wires, and the soldering iron tip. On a standard perfboard with isolated pads, adjacent holes are not electrically connected to each other; however, some prototyping boards feature continuous copper bus strips, so verify your specific board type with a multimeter or its datasheet before assembly.[^adafruit-perfboard]

After placing components, trace each electrical connection on the solder side and verify routing from node to node. Shorter jumper wires generally simplify visual inspection and minimize the chance of accidental contact, but they must not be routed across adjacent pads or obstruct other components. It is often helpful to assemble the circuit on a breadboard first to verify operation before transferring the validated connections to perfboard; for a prototype, this reduces rework, but it does not eliminate the need for a final continuity check with a multimeter.[^adafruit-perfboard]

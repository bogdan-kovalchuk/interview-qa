---
id: emb-elintro-0234
title: "Why learn BJTs if a MOSFET is often better for power switches?"
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
  - source_id: ti-bjt-mosfet-switching
    title: "TI: When to Choose a BJT Instead of a MOSFET for a Flyback Converter"
    url: https://www.ti.com/document-viewer/lit/html/SSZTBM9/GUID-E6584C27-2056-49A5-8305-1C98C74F6175
  - source_id: aac-bjt-basics
    title: "All About Circuits: Introduction to Bipolar Junction Transistors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bipolar-junction-transistors-bjt/
---

## Short answer

BJTs are worth learning because they represent a fundamental technology for amplification and switching that is still widely encountered and offers distinct practical advantages. MOSFETs are often preferred as power switches due to simpler drive requirements and faster switching, but the choice depends on voltage, losses, speed, and cost for the specific application.[^ti-bjt-mosfet-switching]

## Detailed explanation

BJTs remain essential for understanding analog and digital circuits: they serve as amplifiers, current switches, and building blocks of integrated circuits. Their operation demonstrates how a small base current controls collector current, providing the foundation for analyzing biasing, amplification, and saturation. This knowledge helps when reading legacy schematics, servicing equipment, and designing circuits where a BJT remains an appropriate choice.[^aac-bjt-basics]

For many power switching applications, MOSFETs are simpler to drive: once gate capacitance is charged, no continuous DC gate current is needed, whereas a BJT requires continuous base current to maintain low `V_CE(sat)` in saturation. MOSFETs also frequently switch faster. This does not mean a MOSFET is superior in every situation: in certain high-voltage or specialized circuits, a BJT can offer advantages in cost, availability, or specific device characteristics. The decision is driven by individual component specifications and operating conditions, not by a generic "newer is always better" rule.[^ti-bjt-mosfet-switching]

Understanding both device types helps balance drive requirements against power losses. For a BJT, one checks required base current, `V_CE(sat)`, saturation storage time, and thermal constraints. For a MOSFET, one evaluates `R_DS(on)` at the actual gate voltage, gate charge, voltage limits, and switching losses; having an insulated gate does not imply zero instantaneous driver energy, because gate capacitance must be charged and discharged.[^ti-bjt-mosfet-switching]

**Common mistake:** memorizing only that "MOSFETs are better for power" while ignoring application constraints. For slow switching of small currents, an inexpensive BJT can be a straightforward solution, whereas for high switching frequencies or large currents, a MOSFET often wins on efficiency and drive simplicity. Compare specific operating points rather than just absolute maximum ratings from the first page of a datasheet.

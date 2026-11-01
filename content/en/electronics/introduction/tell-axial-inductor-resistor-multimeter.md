---
id: emb-elintro-0143
title: "How do you tell an axial inductor from a resistor with a multimeter?"
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

Measure resistance on a de-energized circuit: an inductor typically shows the winding wire resistance, while a resistor shows its rated value. Isolate one terminal of the component, because parallel paths distort the result; resistance alone does not confirm the component type.[^aac-direct-current]

## Detailed explanation

To distinguish an axial inductor from a resistor, measure their DC resistance with a multimeter and compare the reading with the markings and expected construction of the component. An inductor typically shows a low copper winding resistance, whereas a resistor has its rated resistance; a low reading alone does not prove that the component is an inductor.[^aac-direct-current]

Before measuring, turn off power and discharge any capacitors. For a reliable result, disconnect at least one terminal of the component: otherwise, the multimeter's current can flow through other elements, and the display will show the equivalent resistance of part of the circuit rather than the component itself.[^aac-direct-current]

Axial packages of resistors and inductors can look similar, so it is helpful to check color markings or documentation. An ohmmeter does not measure inductance: it injects a small DC test current and evaluates the voltage, so the steady-state inductive component does not manifest as a separate resistance. Determining inductance requires an LCR meter or testing in a known frequency circuit.[^aac-direct-current]

For example, if an unknown element reads `1.8 Ω`, this could be the wire resistance of a coil, a low-value resistor, or the result of an in-circuit measurement. Check the bands and markings, and measure the component in isolation; the expected winding resistance depends on the size and purpose of the inductor, so there is no fixed threshold.[^aac-direct-current]

**Common mistake:** Taking the continuity beeper as proof that a component is an inductor. The beeper only signals a resistance below the threshold of the specific multimeter; compare the numerical resistance with the markings and, if necessary, measure inductance with a separate instrument.[^aac-direct-current]

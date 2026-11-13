---
id: emb-elee-0003
title: "Which knowledge from section 2 is needed before section 4?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: udemy-course-sections-2-and-4
    title: "Udemy: Crash Course Electronics and PCB Design, course outline"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-series-parallel-method
    title: "All About Circuits: Solving Series and Parallel Circuits With the Table Method and Ohm's Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/solving-series-and-parallel-circuits-with-the-table-method-and-ohms-law/
---

## Short answer

Before proceeding, it is useful to have a confident grasp of voltage, current, Ohm's law `V = I*R`, and basic series-parallel circuit analysis. Fundamentals of capacitors, inductors, and DC/AC distinctions help with subsequent topics, but comprehensive analysis of reactive circuits begins directly in section 4 of the course.[^aac-series-parallel-method] [^udemy-course-sections-2-and-4]

## Detailed explanation

Before starting section 4, it is essential to understand core circuit quantities – voltage, current, resistance, and power – and be able to relate them using Ohm's law. The syllabus of introductory section 2 covers Ohm's law and basic circuit analysis; section 4 subsequently builds upon these principles when examining reactive components and AC.[^udemy-course-sections-2-and-4] [^aac-series-parallel-method]

For resistive DC circuits, one must distinguish series from parallel connections and associate circuit quantities with the specific component or branch where they apply. For instance, in a series circuit, current is identical through all resistors while source voltage divides among them; in a parallel circuit, voltage across branches is identical while branch currents sum together. A common mistake is plugging the total source voltage and an individual branch current into the same `V = I*R` equation, even though the quantities pertain to different parts of the circuit.[^aac-series-parallel-method]

Basic familiarity with capacitors, inductors, and the distinction between DC and AC is helpful, but one does not need to master the entire syllabus in advance: the section 4 outline includes dedicated lectures on capacitors, inductors, RC/RL circuits, phasors, and impedance. Advanced mathematics enters gradually when AC analysis is introduced, rather than being required for the first baseline check of a resistive network.[^udemy-course-sections-2-and-4] [^aac-alternating-current]

**Self-check example:**

For an ideal 9 V source connected to 3 kΩ and 6 kΩ resistors in series, the total resistance is 9 kΩ, yielding a current of `I = 9 V / 9 kΩ = 1 mA`. Such a simple calculation helps catch unit errors or connection mistakes before moving on to more complex models.[^aac-series-parallel-method]

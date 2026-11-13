---
id: emb-elee-0024
title: "How do you calculate the total capacitance of parallel capacitors, and why does it increase?"
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
  - source_id: aac-parallel-capacitors
    title: "All About Circuits: Series and Parallel Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/series-and-parallel-capacitors/
  - source_id: aac-capacitor-factors
    title: "All About Circuits: Factors Affecting Capacitance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/factors-affecting-capacitance/
---

## Short answer

For capacitors connected in parallel, `C_total = C_1 + C_2 + ... + C_n`, provided their terminals connect to the same pair of nodes. For instance, `10 µF + 22 µF = 32 µF` in an ideal model. This equivalence arises because all components share the same voltage while their stored charges sum together.[^aac-parallel-capacitors]

## Detailed explanation

A parallel connection means that each capacitor is connected to the same pair of nodes, so the voltage across each is identical. For each component, `Q_i = C_i*V`; the total charge at the node is the sum of the branch charges. Writing `Q_total = C_total*V` and dividing by the common voltage yields `C_total = C_1 + C_2 + ... + C_n`. This rule applies regardless of whether the individual capacitance values are equal.[^aac-parallel-capacitors]

Intuitively, for ideal parallel-plate capacitors, a parallel connection acts like a larger total plate area with identical separation distance and dielectric. Capacitance increases with plate overlap area and permittivity and decreases with increasing distance; plate areas add directly in this model. In physical components, package geometry, tolerances, and parasitics constrain this simple analogy, but summing the nominal capacitance values remains the foundation for calculating the parallel equivalent.[^aac-parallel-capacitors] [^aac-capacitor-factors]

Example: for `10 µF` and `22 µF` connected in parallel, `C_total = 10 µF + 22 µF = 32 µF`. Both components share the terminal voltage, and the source supplies the combined charge during charging. This does not mean the operating voltage rating of the combination increases: parallel connection increases capacitance rather than voltage rating; voltage is limited by the rating of each individual component and the operating conditions.[^aac-parallel-capacitors]

The formula assumes a true parallel connection across the exact same two nodes. If components are placed in series, the voltage divides between them, and the equivalent capacitance is calculated differently. Furthermore, physical circuits have trace resistance and ESR, so at high frequencies a simple scalar capacitance value no longer describes the total network impedance.[^aac-parallel-capacitors]

**Common mistake:** applying the parallel resistor formula or summing capacitances of components that are actually wired in series. First trace the circuit nodes: only components connected across the same pair of nodes sum their capacitances directly.[^aac-parallel-capacitors]

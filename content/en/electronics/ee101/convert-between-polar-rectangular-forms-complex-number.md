---
id: emb-elee-0056
title: "How do you convert between the polar and rectangular forms of a complex number?"
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
  - source_id: aac-complex-polar-rectangular
    title: "All About Circuits: Polar Form and Rectangular Form Notation for Complex Numbers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/polar-rectangular-notation
---

## Short answer

For `z = a + j*b`, the magnitude is `M = sqrt(a² + b²)`, and the angle should be found as `φ = atan2(b, a)` to correctly account for the quadrant. In the reverse direction, `a = M*cos(φ)` and `b = M*sin(φ)`, giving `z = M∠φ`. In electronics, the imaginary unit is denoted by `j` to avoid confusion with current `i`.[^aac-complex-polar-rectangular]

## Detailed explanation

TODO

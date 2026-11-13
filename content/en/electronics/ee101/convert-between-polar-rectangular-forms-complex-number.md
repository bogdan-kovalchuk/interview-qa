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

A complex number can be expressed in rectangular form as `z = a + j*b` or in polar form as `z = M∠φ`. In rectangular form, `a` is the real part and `b` is the coefficient of the imaginary unit; in polar form, `M` defines the vector magnitude and `φ` is its angle relative to the positive real axis. Both representations describe the same number, but each is better suited for certain operations.[^aac-complex-polar-rectangular]

To convert from polar to rectangular form, one projects the vector onto the axes: `a = M*cos(φ)`, `b = M*sin(φ)`. In the reverse direction, the magnitude is obtained via the Pythagorean theorem, and the angle via the two-argument function `atan2(b, a)`. The ordinary `atan(b/a)` does not distinguish points lying in opposite quadrants and is undefined when `a = 0`; `atan2` returns the correct quadrant and works on the vertical axis, except for the zero vector whose angle is undefined.[^aac-complex-polar-rectangular]

Example: for `z = -3 + j*4`, the magnitude is `5`, and the argument lies in the second quadrant, approximately `126.9°`. Mechanically computing `atan(4/-3)` would yield about `-53.1°`, mistakenly placing the direction in the fourth quadrant. Using `atan2(4, -3)` preserves the correct direction. Angles can be expressed in degrees or radians, but the calculator mode must match the chosen units.[^aac-complex-polar-rectangular]

Rectangular notation is especially convenient for addition and subtraction, where real and imaginary parts are handled separately. Polar notation simplifies multiplication and division: magnitudes are multiplied or divided, while angles are added or subtracted. In AC circuits, after arithmetic operations, one must maintain consistent phase units and refer to a common reference.[^aac-complex-polar-rectangular]

**Common mistakes:**

- Using `atan(b/a)` without checking the quadrant.
- Confusing the coefficient `b` with the imaginary part itself `j*b`.
- Adding polar magnitudes and angles directly instead of converting to rectangular form.[^aac-complex-polar-rectangular]

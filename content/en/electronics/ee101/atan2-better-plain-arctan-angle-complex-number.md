---
id: emb-elee-0070
title: "Why is atan2 better than a plain arctan(b/a) for the angle of a complex number?"
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
  - source_id: aac-atan2-quadrants
    title: "All About Circuits: Quadrature Frequency and Phase Demodulation"
    url: https://www.allaboutcircuits.com/textbook/radio-frequency-analysis-design/radio-frequency-demodulation/quadrature-frequency-and-phase-demodulation/
---

## Short answer

A plain `arctan(b/a)` cannot determine the quadrant of a complex number because the ratio loses the signs of the individual components; for `-3 + j4`, it gives −53.13°, whereas the true angle is 126.87°. The `atan2(b, a)` function accepts both coordinates and returns the angle in the correct quadrant. Always verify whether the returned angle is in radians or degrees.[^aac-atan2-quadrants]

## Detailed explanation

The argument of a complex number `z = a + jb` is the direction of the vector from the origin to the point `(a, b)`. The `arctan(b/a)` function computes the slope from the ratio of coordinates, but points in opposite quadrants yield the same ratio. Therefore, the signs of the real and imaginary parts cannot be determined from the result alone, and division by a zero `a` is completely impossible.[^aac-atan2-quadrants]

`atan2(b, a)` receives both coordinates separately and uses their signs to select the correct quadrant. The order of arguments depends on the programming language or calculator: typically it is `atan2(y, x)`, where `y` corresponds to the imaginary part and `x` to the real part. Furthermore, the result can be in radians or degrees, which must be reconciled with subsequent calculations. At the point `(0, 0)`, the direction is undefined, so the function's output there should not be interpreted as a physically meaningful angle.[^aac-atan2-quadrants]

For `z = -3 + j4`, the point lies in the second quadrant. Standard division gives `b/a = -4/3`, and `arctan(-4/3)` returns approximately −53.13°, which describes a vector in the fourth quadrant. `atan2(4, -3)` returns approximately 126.87° (or 2.214 rad), which is the correct direction. The magnitude of the number is separately `sqrt(a² + b²) = 5`; the angle and magnitude together define the polar form.[^aac-atan2-quadrants]

**Common mistakes:**
- Passing arguments to `atan2` in reverse order.
- Confusing degrees with radians or assuming that the result must always fall in the range 0–360°.
- Using `atan2` on a zero complex number whose argument does not exist.

When verifying a calculation, inspect the signs of both components, identify the expected quadrant, and only then evaluate the value returned by the calculator.[^aac-atan2-quadrants]

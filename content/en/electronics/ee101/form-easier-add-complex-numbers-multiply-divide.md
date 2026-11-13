---
id: emb-elee-0068
title: "In which form is it easier to add complex numbers, and in which to multiply and divide them?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-complex-arithmetic
    title: "All About Circuits: Complex Number Arithmetic"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/complex-number-arithmetic/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Addition and subtraction are convenient in rectangular form, done component by component. Multiplication and division are convenient in polar form: magnitudes are multiplied or divided, while angles are added or subtracted. Multiplying by `j` rotates a complex number by `+90°`, while multiplying by `-j` rotates it by `-90°`.[^aac-complex-arithmetic]

## Detailed explanation

In rectangular form `a + jb`, a complex number is specified by two coordinates. During addition, corresponding coordinates are added together: `(a + jb) + (c + jd) = (a + c) + j(b + d)`. The same component-wise principle applies to subtraction. Therefore, this form is convenient when quantities must be added, such as when finding the total impedance of series components.[^aac-complex-arithmetic]

In polar form, a number is specified by a magnitude and an angle, `r∠θ`. When multiplying, the resulting magnitude is the product of the magnitudes and the resulting angle is the sum of the angles; when dividing, the magnitudes are divided and the denominator angle is subtracted. This is convenient for phasor relationships such as `I = V/Z`. If an operation combines addition and multiplication, converting from one form to the other between steps is often necessary.[^aac-complex-arithmetic]

Multiplying by `j` is equivalent to a rotation by `+90°`, since `j = 1∠90°`; multiplying by `-j` rotates by `-90°`. This applies to the complex plane and phasor algebra, not to a mechanical rotation of a physical component. In calculations, it is important not to mix degrees and radians in a calculator and to preserve the correct quadrant when converting from rectangular to polar form.[^aac-complex-arithmetic]

Example: `3 + j4` and `1 - j2` are easily added in rectangular form to give `4 + j2`. To multiply them, one can convert both numbers to polar form or expand the brackets. Checking the result in the other form helps identify sign errors in the imaginary coordinate or angle.[^aac-complex-arithmetic]

**Common mistakes:**

- Adding polar magnitudes and angles directly as ordinary coordinates.
- During division, subtracting the numerator angle from the denominator angle instead of the other way around.
- Assuming that `j` adds phase independently of multiplication.[^aac-complex-arithmetic]

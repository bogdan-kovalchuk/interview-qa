---
id: emb-elee-0069
title: "Find the current if `Z` = 3 + j4 Ω and the source is 10∠0° V RMS."
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-ac-complex-ohms
    title: "All About Circuits: R, L and C Summary"
    url: https://www.allaboutcircuits.com/TEXTBOOK/alternating-current/chpt-5/r-l-and-c-summary/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

The impedance `Z = 3 + j4 Ω` has a magnitude of `5 Ω` and an angle of `53.13°`. By Ohm's law for phasors, the current equals `2∠-53.13° A`, or `1.2 - j1.6 A RMS`. The sign of the angle indicates that current lags voltage.[^aac-ac-complex-ohms]

## Detailed explanation

The phasor form of Ohm's law has the same structure as the standard form, but voltage, current, and impedance are complex quantities: `I = V/Z`. The denominator must be understood as a magnitude and an angle, rather than merely a scalar resistance. Since the source is specified as `10∠0° V RMS`, the resulting current is also in RMS.[^aac-ac-complex-ohms]

First, convert the impedance `3 + j4 Ω` to polar form. Its magnitude is the hypotenuse of a right triangle with legs 3 and 4; the angle is determined by the ratio of the imaginary component to the real component, taking the quadrant into account. Since both components are positive, the angle lies in the first quadrant.[^aac-ac-complex-ohms]

When dividing complex numbers in polar form, the magnitudes are divided and the denominator angle is subtracted from the numerator angle. Therefore, the current phase is `0° - 53.13°`: for this passive impedance, current lags voltage. After calculation, the result can be converted back to rectangular form to see its two coordinates.[^aac-ac-complex-ohms]

Calculation example:

```text
|Z| = sqrt(3^2 + 4^2) = 5 Ω
angle(Z) = atan2(4, 3) ≈ 53.13°
I = (10∠0° V)/(5∠53.13° Ω) = 2∠-53.13° A RMS
I ≈ 1.2 - j1.6 A RMS
```

Checking by multiplication recovers the original voltage: `(1.2 - j1.6)*(3 + j4) = 10 + j0 V`. If the minus sign in the current phase is omitted or the angle subtraction is inverted, this verification will not match. The number here is provided for an ideal linear impedance with the specified value at the source frequency; a real circuit may have different parameters.[^aac-ac-complex-ohms]

**Common mistakes:**

- Dividing only by the real part `3 Ω` while ignoring the reactive component.
- Dividing magnitudes but adding instead of subtracting the denominator angle.
- Reporting the result as peak even though the source is given in RMS.[^aac-ac-complex-ohms]

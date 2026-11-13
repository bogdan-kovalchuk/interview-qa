---
id: emb-elee-0067
title: "What is the imaginary unit j, and what does a complex number a + jb really mean in electronics?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-complex-intro
    title: "All About Circuits: Introduction to Complex Numbers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/introduction-to-complex-numbers/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

`j² = -1`. In a complex phasor, the real and imaginary parts are coordinates that encode the amplitude and phase of a sinusoidal quantity. Therefore, an "imaginary voltage" is not a separate physical voltage.[^aac-complex-intro]

## Detailed explanation

In electrical engineering, `j` denotes the imaginary unit satisfying `j² = -1`; the letter `j` is used to avoid confusion with the common symbol for current `i`. In the expression `a + jb`, the numbers `a` and `b` specify the coordinates of the complex number: `a` is the real part and `b` is the imaginary part. This is a mathematical representation, not an assertion of two physically independent types of voltage.[^aac-complex-intro]

For single-frequency sinusoidal AC, a phasor preserves two essential characteristics: magnitude and phase relative to a reference signal. For instance, `3 + j4` corresponds to a point with coordinates `3` and `4`; its magnitude is `5` and its angle is approximately `53.13°`. The same quantity in polar form is `5∠53.13°`. Both notations describe the same complex quantity, merely in different coordinates.[^aac-complex-intro]

In the time domain, physical voltage remains a real sine wave. Phasor notation is a compact computational tool: after solving, the complex coordinates are interpreted as amplitude and phase relationship, and the time-domain waveform can be reconstructed if needed. The quantity `j` here is not an "imaginary" component of a multimeter measurement.[^aac-complex-intro]

**Common mistakes:**

- Treating `j` as a physical variable or imagining the measured voltage as unreal.
- Confusing `b` with magnitude: in `a + jb`, it is a coordinate; magnitude is determined from both coordinates.
- Using a phasor without a shared frequency and reference angle.[^aac-complex-intro]

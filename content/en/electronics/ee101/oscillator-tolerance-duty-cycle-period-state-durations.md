---
id: emb-elee-0244
title: "A 10 MHz oscillator with ±50 ppm tolerance and a 50% duty cycle. What are the period, the state durations and the frequency error?"
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
  - source_id: ti-swra372
    title: "TI SWRA372C: AN100 Crystal Selection Guide"
    url: https://www.ti.com/lit/an/swra372c/swra372c.pdf
  - source_id: ti-sdaa032
    title: "TI SDAA032: Seamless PWM Duty Cycle Updates Without Intermediate Artifacts"
    url: https://www.ti.com/lit/an/sdaa032/sdaa032.pdf
---

## Short answer

The period is `T = 1/f = 100 ns`. At a nominal 50% duty cycle, the HIGH and LOW states each last 50 ns, since `D = 100*High/(High + Low)`.[^ti-sdaa032] A ±50 ppm tolerance defines the relative frequency error, giving an absolute deviation of `Δf = f*ppm*10^-6 = 10^7*50*10^-6 = ±500 Hz`.[^ti-swra372]

## Detailed explanation

The period is the inverse of frequency: `T = 1/f = 1/(10*10^6 Hz) = 100 ns`. This is the nominal value. A tolerance of ±50 ppm describes the relative frequency error: ppm means parts per million, so `50 ppm = 50*10^-6`. For 10 MHz, the deviation equals `10*10^6*50*10^-6 = 500 Hz`, which means the frequency can range from 9.9995 MHz to 10.0005 MHz.[^ti-swra372]

The period depends inversely on frequency, so its bounds are nearly symmetrical: at 10.0005 MHz, `T = 99.995 ns`, and at 9.9995 MHz, `T = 100.005 ns`. Thus, the period deviates by approximately ±5 ps, whereas a frequency error of ±500 Hz and a period variation are different quantities that are not directly compared.

State durations depend on the duty cycle. If it is exactly 50 %, each state lasts `T/2 = 50 ns`. With ppm, `T/2` lies between 49.9975 ns and 50.0025 ns, which is ±2.5 ps. Important: ppm applies to frequency, not to the ratio of states. If both states scale identically, `D` does not change; therefore, the actual duty cycle is determined by a separate datasheet parameter, not by the frequency tolerance.

**Common mistakes:**

- Confusing ppm with percentages: 50 ppm equals 0.005 %, not 50 %;
- Assuming that ±500 Hz implies ±500 Hz on the period; the period changes by only ±5 ps;
- Assuming a 50 % duty cycle is guaranteed for any oscillator.

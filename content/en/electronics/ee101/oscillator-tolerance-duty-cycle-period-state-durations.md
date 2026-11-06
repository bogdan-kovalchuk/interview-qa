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

TODO

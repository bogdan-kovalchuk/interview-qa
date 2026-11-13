---
id: emb-elee-0243
title: "Which parameters characterize a clock signal?"
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
  - source_id: ti-snaa285
    title: "TI SNAA285: Time-Domain Jitter Measurement Considerations for Low-Noise Oscillators"
    url: https://www.ti.com/lit/an/snaa285/snaa285.pdf
  - source_id: ti-sdaa032
    title: "TI SDAA032: Seamless PWM Duty Cycle Updates Without Intermediate Artifacts"
    url: https://www.ti.com/lit/an/sdaa032/sdaa032.pdf
---

## Short answer

A clock signal is characterized by its frequency `f`, period `T = 1/f`, and duty cycle `D = t_HIGH/T` (as a percentage, `D = 100*t_HIGH/T`, or as expressed by TI, `D = 100*High/(High + Low)`).[^ti-sdaa032] Other critical parameters include logic voltage levels, rise and fall edge times, and jitter (the deviation of cycle duration from an ideal period).[^ti-snaa285]

## Detailed explanation

A clock signal is described by frequency and timing parameters. Frequency `f` is measured in hertz, and period `T = 1/f` is the duration of one complete cycle. The duty cycle indicates what fraction of the period the signal remains in state 1: `D = t_HIGH/T`, or as a percentage, `D = 100*t_HIGH/T`. In a TI document on PWM, this is written as `D = 100*High/(High + Low)`, where the sum of High and Low yields the period.[^ti-sdaa032]

**Example:** At `f = 50 MHz`, we have `T = 1/(50*10^6) = 20 ns`. If `t_HIGH = 9 ns`, then `t_LOW = 11 ns` and `D = 100*9/(9 + 11) = 45 %`. Such a signal is asymmetrical, and this matters for circuits that depend on the duration of the HIGH state, rather than just the frequency.

Logic levels define which voltages the downstream input interprets as 1 and 0. Rise and fall edge times determine how long the signal takes to transition between these levels, affecting how quickly and cleanly the circuit switches.

Jitter is the deviation from ideal timing. According to JEDEC JESD65B, period jitter is the deviation of cycle duration from an ideal period over a random sample of cycles, while cycle-to-cycle jitter is the variation in duration between adjacent cycles.[^ti-snaa285] Period jitter is primarily used to ensure setup and hold times for logic in CPUs and FPGAs. It must be measured on a sample of 1,000 to 10,000 cycles.[^ti-snaa285]

**Common mistakes:**

- Assuming a 50 % duty cycle by default without checking the datasheet;
- Confusing jitter with frequency error: jitter describes deviations of individual cycles, whereas a tolerance in ppm shifts the entire frequency;
- Measuring jitter over a small number of cycles, whereas a reliable result requires many cycles.

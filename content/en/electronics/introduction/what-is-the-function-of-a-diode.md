---
id: emb-elintro-0006
title: What is the function of a diode?
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: vishay-diode
    title: "Vishay 1N4001-1N4007 rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---

## Short answer

A rectifier diode conducts mainly from anode to cathode under forward bias and blocks most current under reverse bias within its ratings. Real diodes have forward voltage and reverse leakage; `V_RRM` is a maximum repetitive peak reverse-voltage rating, not a zero-current threshold. [^vishay-diode]

## Detailed explanation

Forward bias means the anode is sufficiently positive relative to the cathode for the intended current. Forward current is strongly nonlinear with voltage; a diode is not a fixed resistor or a perfect switch. Its forward drop depends on current, temperature and device technology.

Reverse bias greatly reduces conduction for a normal rectifier, but does not eliminate it. The Vishay 1N4001-1N4007 datasheet specifies maximum reverse leakage at rated blocking voltage of 5 µA at 25 °C and 50 µA at 125 °C. The rating and temperature belong to this family; they are not universal diode values. [^vishay-diode]

An ideal-diode circuit exercise may approximate forward conduction as a short and reverse conduction as an open. Label that approximation explicitly. For hardware, select forward-current, reverse-voltage and thermal ratings and account for transient/recovery behavior. Breakdown should not be treated as normal operation for a rectifier simply because some other diode types intentionally operate there.

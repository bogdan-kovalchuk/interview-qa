---
id: emb-elintro-0170
title: "What is a diode's reverse leakage current?"
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
  - source_id: vishay-1n400x
    title: "Vishay: 1N4001–1N4007 datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---


## Short answer

Under reverse bias, a real diode conducts a small reverse leakage current, although an ideal model would consider it zero.[^aac-semiconductors] Its magnitude depends on reverse voltage, temperature, and the specific component, so you should verify it in the datasheet.

## Detailed explanation

Reverse leakage current is a small current that flows through a real diode under reverse bias, when the cathode is at a higher potential than the anode. The ideal diode model treats this current as zero, but in a real semiconductor, thermally generated carriers and other mechanisms cause a small current.[^aac-semiconductors]

It should not be confused with current in the breakdown regime. Below the maximum reverse voltage rating, leakage is typically small; when approaching or exceeding the rating, the behavior changes and current can rise sharply. Datasheet values must always be read alongside test conditions: the manufacturer specifies the applied reverse voltage and temperature, rather than a single universal figure for all operating conditions.[^aac-semiconductors]

Temperature has practical significance: in specifications, leakage current often increases noticeably with heating. For example, in the Vishay datasheet for the 1N4001–1N4007 family, maximum DC reverse current is listed as 5 μA at 25 °C and 50 μA at 125 °C at the rated DC blocking voltage.[^vishay-1n400x] These are specific conditions for a specific series, rather than a universal multiplier rule for any diode.

In high-impedance sensor nodes, sample-and-hold circuits, and precision measurements, even a small leakage can introduce noticeable error or slowly discharge a capacitor. A common mistake is treating a reverse-biased diode as a completely open switch; to evaluate leakage, you must check the temperature characteristic and datasheet conditions, as well as account for PCB and test-instrument leakages.[^aac-semiconductors] [^vishay-1n400x]

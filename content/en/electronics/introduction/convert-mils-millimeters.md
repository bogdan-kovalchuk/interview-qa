---
id: emb-elintro-0292
title: "How do you convert mils to millimeters?"
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
  - source_id: nist-inch
    title: "NIST: SI Units – Length"
    url: https://www.nist.gov/pml/owm/si-units-length
---

## Short answer

One mil equals 0.001 inch, and the international inch is exactly 25.4 mm, making 1 mil equal to 0.0254 mm.[^nist-inch] To convert mils to millimeters, multiply the value in mils by 0.0254; for example, 25 mil equals 0.635 mm.

## Detailed explanation

One mil equals one thousandth of an international inch, which is exactly 0.0254 mm; to convert mils to millimeters, multiply the value in mils by 0.0254.[^nist-inch] Here, mil is a unit of length, not millimeter and not milliliter.

The international inch is defined exactly as 25.4 mm. Since one mil is 0.001 inch, the calculation yields 0.001 × 25.4 mm = 0.0254 mm. The inverse conversion divides the millimeter value by 0.0254. In electronics, mils are commonly encountered in PCB trace widths and pin pitches, whereas mechanical drawings may specify the same dimensions in millimeters.[^nist-inch]

Example: 25 mil × 0.0254 mm/mil = 0.635 mm. Therefore, a trace with a width of 25 mil has a width of 0.635 mm. This is an exact unit conversion; manufacturing tolerances are evaluated separately.[^nist-inch]

**Common mistakes:**

- Confusing mil with millimeter; one mil equals only 0.0254 mm.
- Using a factor of 25.4 instead of 0.0254 when multiplying mils.
- Mistaking the abbreviation mil for a millimeter mark in drawings or datasheets.

Before calculating, verify the source units. For example, 10 mil is 0.254 mm, whereas 10 mm is approximately 393.7 mil. This sanity check prevents thousand-fold errors caused by confusing mils with inches.[^nist-inch]

---
id: emb-elintro-0026
title: "How do you convert 3.0 × 10⁴ W to kilowatts?"
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
  - source_id: nist-si-prefixes
    title: "NIST: SP 330, Section 3 – Decimal multiples and sub-multiples of SI units"
    url: https://www.nist.gov/pml/special-publication-330/sp-330-section-3
---

## Short answer

Since the prefix kilo means 10³, 3.0 × 10⁴ W equals 30 kW. This is also 0.03 MW, because mega means 10⁶.[^nist-si-prefixes]

## Detailed explanation

To convert watts to kilowatts, divide the value in watts by 1000: the prefix kilo means a multiplier of 10³. Here `3.0 × 10⁴ W` is `30 000 W`, so `30 000 / 1000 = 30 kW`.[^nist-si-prefixes]

The coefficient 3.0 has two significant figures, so the notation `30 kW` preserves the precision of the initial value. Do not interpret kilo as 1024: SI prefixes are decimal, whereas separate prefixes like kibi are used for binary multipliers.[^nist-si-prefixes]

The same conversion can be performed by factoring powers of ten: `3.0 × 10⁴ W = 3.0 × 10 × 10³ W`. Since `10³ W` constitutes one kilowatt, the coefficient in front of it equals 30. This approach helps avoid a three-order-of-magnitude error when converting from a base unit to a prefixed unit.[^nist-si-prefixes]

The unit W does not alter the physical quantity: both watts and kilowatts measure power. Only the scale of representation changes, so the value must be divided by the number of watts in one kilowatt, rather than multiplied by 1000.[^nist-si-prefixes]

**Order-of-magnitude check:** `30 kW = 30 000 W`, so the initial watts and the resulting kilowatts describe the same power.

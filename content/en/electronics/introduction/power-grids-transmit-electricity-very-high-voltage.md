---
id: emb-elintro-0152
title: "Why do power grids transmit electricity at very high voltage (35–500 kV)?"
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
  - source_id: openstax-transformers
    title: "OpenStax University Physics Volume 2, 15.6 Transformers"
    url: https://openstax.org/books/university-physics-volume-2/pages/15-6-transformers
---

## Short answer

For the same transmitted power, increasing the voltage reduces current in the line, while losses in its resistance depend on the square of the current. Therefore, high-voltage transmission typically reduces resistive losses over a given distance; near consumers, transformers step down the voltage to a usable level. Specific voltage levels depend on the power system, distance, power rating, and line construction.[^openstax-transformers]

## Detailed explanation

Power grids transmit the same power at high voltage to reduce current in the conductors and, accordingly, resistive losses. For active power in a simple single-phase model, `P = V*I`; therefore, if power is constant, increasing voltage yields a smaller current. Line heating is determined by `P_loss = I^2*R`, where `R` is conductor resistance. It is the square of current that explains why reducing it substantially cuts losses.[^openstax-transformers]

In a three-phase grid, the exact relationship between line voltage, current, and active power also depends on the power factor. The conclusion that higher voltage reduces current for a given transmitted power still holds, but the practical choice of voltage accounts for insulation, corona, reactive effects, equipment cost, distance, and operating rules. High voltage does not imply zero losses or an automatically optimal choice for every line.[^openstax-transformers]

Example: to transmit 1 MW in a simplified model at 10 kV, current is `I = P/V = 100 A`, while at 100 kV it is `10 A`. For the same line resistance, the second case yields one hundred times lower `I^2*R` losses: the current decreased tenfold, and losses depend on its square. This comparison illustrates the principle rather than specifying ratings of a specific grid.[^openstax-transformers]

Near the consumer, transformers step down the voltage to the level required for distribution and utilization. This adds conversion stages and their own losses, but allows efficient transmission to be combined with a practical load voltage.[^openstax-transformers]

**Common mistakes:**
- explaining loss reduction merely as "electricity flowing better";
- forgetting that resistance losses are proportional to the square of current;
- presenting the voltage range as a universal rule for all countries and lines.

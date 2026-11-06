---
id: emb-eldig-0026
title: "What happens during bit-width overflow in unsigned n-bit binary addition?"
track: electronics
section: digital-logic
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
  - source_id: harris-harris-ddca
    title: "David Money Harris, Sarah L. Harris. Digital Design and Computer Architecture. Morgan Kaufmann"
    url: https://www.elsevier.com/books/digital-design-and-computer-architecture/harris/978-0-12-394424-5
  - source_id: patterson-hennessy-cod
    title: "David A. Patterson, John L. Hennessy. Computer Organization and Design: The Hardware/Software Interface. Morgan Kaufmann"
    url: https://www.elsevier.com/books/computer-organization-and-design-arm-edition/patterson/978-0-12-801733-3
---

## Short answer

When addition produces a sum exceeding the maximum representable value `2^n - 1`, unsigned overflow occurs. For example, adding 1 to the 8-bit maximum of 255 (binary `11111111`) generates a carry into the ninth bit, wrapping the 8-bit register result to 0. The carry-out bit is captured in a processor status flag or discarded, corrupting the direct register result.[^harris-harris-ddca] [^patterson-hennessy-cod]

## Detailed explanation

TODO

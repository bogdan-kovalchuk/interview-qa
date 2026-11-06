---
id: emb-eldig-0025
title: "What rules govern single-bit binary addition and carry generation?"
track: electronics
section: digital-logic
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
  - source_id: floyd-digital
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
  - source_id: harris-harris-ddca
    title: "David Money Harris, Sarah L. Harris. Digital Design and Computer Architecture. Morgan Kaufmann"
    url: https://www.elsevier.com/books/digital-design-and-computer-architecture/harris/978-0-12-394424-5
---

## Short answer

Adding zero gives `0 + 0 = 0` and `1 + 0 = 1` with no carry. Adding two ones gives `1 + 1 = 0` with a carry of 1 to the next bit, because the sum equals binary `10` (decimal 2). Adding three ones gives `1 + 1 + 1 = 1` with a carry-out of 1 (binary `11`, decimal 3).[^floyd-digital] [^harris-harris-ddca]

## Detailed explanation

TODO

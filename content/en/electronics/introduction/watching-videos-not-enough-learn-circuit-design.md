---
id: emb-elintro-0308
title: "Why is watching videos not enough to learn circuit design?"
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
  - source_id: cmu-retrieval-practice
    title: "Carnegie Mellon University Eberly Center: Retrieval Practice"
    url: https://www.cmu.edu/teaching/resources/instructionalstrategies/activelearningstrategies/retrievalpractice/index.html
---

## Short answer

Watching alone is insufficient to verify whether you can apply an idea: solve a problem or predict a circuit outcome, and then check it against calculation, measurement, or simulation. Active retrieval followed by feedback helps reveal misunderstandings and consolidate the material.[^cmu-retrieval-practice]

## Detailed explanation

A video can explain a principle and show an example, but on its own does not verify whether the viewer can reproduce the reasoning or apply it in a different circuit. While watching, it is easy to recognize familiar steps without realizing that, without prompts, choosing the necessary law or predicting the outcome is difficult.

To test understanding, after an explanation it is worth covering the solution and stating independently what quantities are known, what rules are required, and what will happen in the circuit. Next, one can perform a calculation, simulate the circuit, or assemble it on a safe low-voltage platform. A hands-on task forces retrieving the concept and turning it into a sequence of actions; in education, active retrieval, practice problems, and feedback on correctness are valuable learning practices.[^cmu-retrieval-practice]

Comparing a prediction with the actual result provides an additional signal. If the measurement differs, one must verify component polarity, connections, component values, instrument settings, and the assumptions made. Simulation helps vary parameters rapidly, but it relies on component models and does not automatically replicate every parasitic characteristic of a real breadboard. A physical experiment, on the other hand, requires a properly assembled circuit and safe power limits.

Thus, videos are best used as an introduction or explanation, followed by independent recall, problem solving, and verification. It is not necessary to build a complex device every time: predicting current direction, performing a calculation, and comparing it against a simulation is sufficient at first. Watching remains helpful, but active work reveals what is already understood and what requires further review.[^cmu-retrieval-practice]

**Common mistake:**

- Mistaking familiarity with an example for proof of understanding. Try solving a similar problem with different components or values without video prompts, and then verify your reasoning against a reliable solution or measurement.

---
id: emb-elintro-0077
title: "What is the key difference between `DC` and `AC`?"
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
  - source_id: aac-dc-ac-direction
    title: "All About Circuits: Voltage and Current"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-1/voltage-current/
---
## Short answer

`DC` means current flowing in one direction; its magnitude may vary. `AC` periodically reverses the direction of current (or the polarity of voltage). A battery typically provides `DC`, while household mains provides `AC`.[^aac-dc-ac-direction]

## Detailed explanation

`DC` (direct current) is current whose direction does not change; `AC` (alternating current) periodically reverses direction. You should distinguish them by direction, not by whether the waveform is a perfectly flat line.[^aac-dc-ac-direction]

In a battery circuit, the polarity of the source is typically constant, so conventional current through the load flows in a single unchanging direction. This does not mean its magnitude must be constant: for example, the voltage of a pulsating rectifier may vary over time, even though the current does not reverse. Such a waveform should not be confused with pure alternating current.[^aac-dc-ac-direction]

In conventional sinusoidal `AC`, the voltage changes sign every half-period, and current in a simple resistive circuit changes direction along with it. Frequency describes the number of complete cycles per second, and amplitude describes the maximum deviation from zero. A real AC supply may have a distorted waveform, but reversal remains the key defining feature.[^aac-dc-ac-direction]

**Example:** a battery powering a lamp provides unidirectional current. A mains source causes the current in a resistive load to move in one direction and then in the opposite direction. If the voltage pulsates after a rectifier, its direction in the load can still remain one-way.[^aac-dc-ac-direction]

**Common mistake:** calling any current with a varying magnitude `AC`. Check the sign of the current or the polarity of the voltage over time; a change in magnitude alone does not mean a reversal of direction.[^aac-dc-ac-direction]

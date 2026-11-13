---
id: emb-elee-0085
title: "Why can the ground clips of two probes on an ordinary oscilloscope not be attached to different circuit nodes?"
track: electronics
section: ee101
sources:
  - source_id: tek-probing
    title: "Tektronix: Probing Techniques for Accurate Voltage Measurements on Power Supplies with Oscilloscopes"
    url: https://www.tek.com/en/documents/application-note/probing-techniques-accurate-voltage-measurements-power-converters-oscillos
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

In a standard earth-grounded oscilloscope, the channel ground clips are connected to each other and to protective earth (PE), so attaching them to different nodes can cause a short circuit.[^tek-probing] To measure voltage differences, connect both clips to the circuit's common ground and subtract channels, or use an appropriate differential probe.[^tek-probing]

## Detailed explanation

The ground clips of standard oscilloscope channels are often electrically connected to each other and to protective earth (PE), so attaching them to different nodes can short those nodes together through the oscilloscope.[^tek-probing]

In a standard passive probe, the ground clip is not a separate isolated input: it is connected to the outer conductor of the BNC connector and the chassis of the instrument. When attached to a node, that node is effectively tied to earth ground. A second clip placed at a different potential creates a low-resistance path between the nodes through the common connection of the channels, and the resulting current can damage the circuit or the instrument. This can happen even when the channels appear independent on the screen.[^tek-probing]

To measure voltage between two ungrounded points, a differential probe with an appropriate common-mode and differential voltage range is used. Sometimes two standard probes are used: both clips are connected to the circuit's common ground, and the oscilloscope displays the difference between CH1 and CH2. This method is only quasi-differential: probe and channel mismatch degrades common-mode rejection, and each input must still stay within its rated voltage limits.[^tek-probing]

**Common mistakes:**
- Assuming that the ground symbol on the probe indicates an isolated measurement input.
- Disconnecting the oscilloscope's protective earth ground to "float" with the circuit; this creates an electric shock hazard.

For example, if two clips are placed on opposite sides of a resistor in an ungrounded power branch, the clips can connect those points to PE and to each other, effectively bypassing the resistor. Before connecting, verify whether the oscilloscope is a standard grounded instrument, and choose a differential probe or a safe measurement referenced to the circuit's common ground.[^tek-probing]
